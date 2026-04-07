import ast
import base64
import hashlib
import io
import json
import os
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection, preprocessing, metrics, linear_model, ensemble
import xgboost as xgb

try:
    import tensorflow as tf
except Exception:
    tf = None


BASE_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = BASE_DIR / "practice" / "datasets"
DATASET_URL_BASE = "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/"


class RunRequest(BaseModel):
    code: str
    datasetId: str
    questionId: int


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def dataset_path(dataset_id: str) -> Path:
    mapping = {
        "iris": "iris.csv",
        "tips": "tips.csv",
        "titanic": "titanic.csv",
        "penguins": "penguins.csv",
        "flights": "flights.csv",
        "exercise": "exercise.csv",
        "planets": "planets.csv",
        "fmri": "fmri.csv",
        "winequality": "winequality-red.csv",
        "student": "student-performance.csv",
    }
    filename = mapping.get(dataset_id)
    if not filename:
        raise ValueError("Unknown datasetId")
    return DATASETS_DIR / filename


def dataset_url(dataset_id: str) -> str:
    mapping = {
        "iris": "iris.csv",
        "tips": "tips.csv",
        "titanic": "titanic.csv",
        "penguins": "penguins.csv",
        "flights": "flights.csv",
        "exercise": "exercise.csv",
        "planets": "planets.csv",
        "fmri": "fmri.csv",
        "winequality": "winequality-red.csv",
        "student": "student-performance.csv",
    }
    filename = mapping.get(dataset_id)
    if not filename:
        raise ValueError("Unknown datasetId")
    return f"{DATASET_URL_BASE}{filename}"


def exec_with_last_expr(code: str, scope: Dict[str, Any]) -> Tuple[Optional[Any], str]:
    """
    Execute code and return the value of the last expression (if any).
    """
    parsed = ast.parse(code)
    last_value = None
    if parsed.body and isinstance(parsed.body[-1], ast.Expr):
        body = parsed.body[:-1]
        last_expr = parsed.body[-1].value
        exec(compile(ast.Module(body=body, type_ignores=[]), "<string>", "exec"), scope, scope)
        last_value = eval(compile(ast.Expression(body=last_expr), "<string>", "eval"), scope, scope)
    else:
        exec(compile(parsed, "<string>", "exec"), scope, scope)
    return last_value, code


def dataframe_to_html(obj: Any) -> Optional[str]:
    if isinstance(obj, pd.DataFrame):
        return obj.head(20).to_html(index=False)
    if isinstance(obj, pd.Series):
        return obj.head(20).to_frame().to_html(index=True)
    return None


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def result_hash(obj: Any) -> Optional[str]:
    if isinstance(obj, pd.DataFrame):
        payload = obj.head(20).to_json(orient="split")
        return hash_text(payload)
    if isinstance(obj, pd.Series):
        payload = obj.head(20).to_json(orient="split")
        return hash_text(payload)
    if isinstance(obj, np.ndarray):
        payload = json.dumps({"shape": obj.shape, "data": obj.flatten()[:100].tolist()})
        return hash_text(payload)
    if isinstance(obj, (list, tuple)):
        payload = json.dumps({"data": list(obj)[:100]})
        return hash_text(payload)
    if obj is None:
        return None
    return hash_text(str(obj))


def fig_to_base64(fig) -> str:
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode("utf-8")


@app.get("/debug")
def debug_info() -> Dict[str, Any]:
    datasets = {
        "iris": "iris.csv",
        "tips": "tips.csv",
        "titanic": "titanic.csv",
        "penguins": "penguins.csv",
        "flights": "flights.csv",
        "exercise": "exercise.csv",
        "planets": "planets.csv",
        "fmri": "fmri.csv",
        "winequality": "winequality-red.csv",
        "student": "student-performance.csv",
    }
    resolved = {k: str(DATASETS_DIR / v) for k, v in datasets.items()}
    exists = {k: (DATASETS_DIR / v).exists() for k, v in datasets.items()}
    urls = {k: f"{DATASET_URL_BASE}{v}" for k, v in datasets.items()}
    return {
        "base_dir": str(BASE_DIR),
        "datasets_dir": str(DATASETS_DIR),
        "paths": resolved,
        "exists": exists,
        "urls": urls,
    }


@app.post("/run")
def run_code(payload: RunRequest) -> Dict[str, Any]:
    try:
        csv_url = dataset_url(payload.datasetId)

        code = payload.code
        # Basic safety: disallow obvious dangerous imports/keywords.
        blocked = ["import os", "import sys", "import subprocess", "__import__", "open("]
        for keyword in blocked:
            if keyword in code:
                return {"error": f"Blocked keyword: {keyword}"}

        scope: Dict[str, Any] = {
            "pd": pd,
            "np": np,
            "plt": plt,
            "sns": sns,
            "tf": tf,
            "xgb": xgb,
            "model_selection": model_selection,
            "preprocessing": preprocessing,
            "metrics": metrics,
            "linear_model": linear_model,
            "ensemble": ensemble,
            "DATASET_URL": csv_url,
            "DATASET_PATH": csv_url,
        }

        stdout = io.StringIO()
        stderr = io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = stdout, stderr
        try:
            last_value, _ = exec_with_last_expr(code, scope)
        finally:
            sys.stdout, sys.stderr = old_out, old_err

        table_html = None
        image_b64 = None
        result_fp = None
        if "result" in scope:
            table_html = dataframe_to_html(scope["result"])
            result_fp = result_hash(scope["result"])
        elif last_value is not None:
            table_html = dataframe_to_html(last_value)
            result_fp = result_hash(last_value)
        elif "df" in scope:
            table_html = dataframe_to_html(scope["df"])
            result_fp = result_hash(scope["df"])

        fig = plt.gcf()
        if fig and fig.axes:
            image_b64 = fig_to_base64(fig)
        plt.close(fig)

        err_text = stderr.getvalue().strip()
        if err_text:
            return {"error": err_text}

        stdout_text = stdout.getvalue().strip()
        return {
            "stdout": stdout_text,
            "stdout_hash": hash_text(stdout_text) if stdout_text else "",
            "table_html": table_html,
            "image_base64": image_b64,
            "result_hash": result_fp or "",
        }
    except Exception:
        return {"error": traceback.format_exc()}
