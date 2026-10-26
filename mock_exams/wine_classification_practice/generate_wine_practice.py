#!/usr/bin/env python3
"""Generate 3 wine-quality classification practice exam notebooks (problem + solution)."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_SRC = Path(__file__).resolve().parents[2] / "official_samples" / "classification" / "wine_quality_data.csv"
TOPO_SRC = Path(__file__).resolve().parents[2] / "official_samples" / "classification" / "Topology.png"


def md(src: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": [line + "\n" for line in src.split("\n")]}


def code(src: str) -> dict:
    lines = [line + "\n" for line in src.split("\n")]
    if lines:
        lines[-1] = lines[-1].rstrip("\n")
        if not lines[-1].endswith("\n") and src.endswith("\n"):
            lines[-1] += "\n"
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line if line.endswith("\n") else line + "\n" for line in src.split("\n")[:-1]]
        + ([src.split("\n")[-1] + ("\n" if src.endswith("\n") or True else "")] if src else []),
    }


def code_clean(src: str) -> dict:
    """Code cell with normalized trailing newline."""
    if not src.endswith("\n"):
        src += "\n"
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [ln + "\n" for ln in src.split("\n")[:-1]] + ([src.split("\n")[-1] + "\n"] if src.split("\n")[-1] else []),
    }


def notebook(cells: list) -> dict:
    return {
        "nbformat": 4,
        "nbformat_minor": 5,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "pygments_lexer": "ipython3"},
        },
        "cells": cells,
    }


COMMON_IMPORT = """import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings('ignore')

candidates = [
    'NanumGothic', 'NanumGothicCoding', 'NanumBarunGothic',
    'Malgun Gothic', 'AppleGothic', 'Noto Sans CJK KR'
]
available = {f.name for f in fm.fontManager.ttflist}
for name in candidates:
    if name in available:
        plt.rc('font', family=name)
        break
plt.rcParams['axes.unicode_minus'] = False
"""

HEADER_NOTICE = """#### **<span style="color:red">[유의사항]</span>**
- <span style="color:darkgreen">각 문항의 답안은 반드시 *'#여기에 답안코드를 작성하고 실행하세요' , ‘#여기에 답안을 입력하세요’* 등이 표시된 셀(cell)에 입력해야 합니다</span>
- <span style="color:darkgreen">제공된 시험문항 셀을 삭제하거나 답안 위치가 아닌 다른 셀에 답안코드를 작성 시 채점되지 않습니다</span>
- 답안 작성 전에 문항에 제시된 가이드를 확인하세요
- 문항에 변수명이 제시된 경우 반드시 해당 변수명을 사용하세요
- 오픈북은 허용된 사이트만 참고 가능합니다 (numpy / pandas / matplotlib / seaborn / scikit-learn / tensorflow / xgboost)
---"""

COLUMNS = """**[ 데이터 컬럼 설명 (데이터 파일명: wine_quality_data.csv) ]**

- Grade             : 와인품질등급(Pass, Fail)
- E_title           : 와인이름
- E_country         : 생산국가
- E_province        : 생산지 세부주소 ①
- E_region_1        : 생산지 세부주소 ②
- E_region_2        : 생산지 세부주소 ③
- E_winery          : 와이너리(와인 생산 농장명)
- E_FE_vintage      : 포도수확연도
- E_wine_variety    : 포도품종
- E_FE_wine_kind    : 와인종류
- FE_continent      : 생산대륙(신대륙/구대륙)
- E_price           : 가격
- FE_points_location : 와인 생산지 평점
- FE_points_variety  : 포도 품종 평점
- FE_points_winery   : 와이너리 평점"""

SCENARIO = """### **와인 데이터를 활용한 <span style="color:darkgreen">와인 품질</span> 예측 — 모의고사 {set_no}**
---

- 도메인 : 품질 관리(QC)
- 목  표 : 와인의 품질을 예측하는 인공지능모델 개발
- 공식 분류 샘플과 **동일 데이터(`wine_quality_data.csv`)** 를 사용합니다.
- 문항 유형(빈칸 / 코드 작성 / 오류 정정 / 단답)은 공식과 유사하되, **pandas·seaborn·sklearn API를 더 다양하게** 연습하도록 구성했습니다.
- 난이도: 공식과 동일 ~ 약간 어렵게 / GridSearch는 연습용으로 파라미터 후보를 소폭 축소했습니다.

---"""


def blank_answers(problem: bool, answers: dict[str, str], keys: list[str]) -> list:
    cells = []
    for k in keys:
        if problem:
            cells.append(code_clean(f"# ({k}) 여기에 답안을 입력하세요(실행 불필요)\n"))
        else:
            cells.append(code_clean(f"# ({k}) 여기에 답안을 입력하세요(실행 불필요)\n\n{answers[k]}\n"))
    return cells


def write_nb(path: Path, cells: list) -> None:
    path.write_text(json.dumps(notebook(cells), ensure_ascii=False, indent=1), encoding="utf-8")
    print("wrote", path)


# ---------------------------------------------------------------------------
# SET 1 — heatmap / violin / fillna / isin / MinMax / LR+RF / f1 / DNN
# ---------------------------------------------------------------------------

def build_set1(problem: bool) -> list:
    a = {
        "3-1": "heatmap",
        "3-2": "annot",
        "3-3": "corr",
        "5-1": "fillna",
        "5-2": "median",
        "6-1": "isna",
        "6-2": "dropna",
        "7-1": "isin",
        "7-2": "value_counts",
        "7-4": "46402",
        "9-2": "실행 결과의 round(np.max(X_valid)) 값 (환경에 따라 상이할 수 있음)",
        "10-3": "실행 후 gs_rf.best_params_['n_estimators'] 값",
        "11-2": "FE_points_winery",
        "12-2": "RandomForest",
        "13-1": "Dense(128, activation='relu'), Dropout(0.3), Dense(64, activation='relu'), Dense(32, activation='relu'), Dense(2, activation='sigmoid')",
        "13-2": "patience",
    }

    cells = [
        md("**AICE Associate <font color=red>모의고사</font> — 분류 Set 1**"),
        md(SCENARIO.format(set_no=1)),
        md(HEADER_NOTICE),
        md(COLUMNS),
        md("**배점:** 데이터 분석 20점 · 데이터 전처리 30점 · AI 모델링 50점 (총 14문항 / 100점)\n\n이 노트북과 `wine_quality_data.csv`는 같은 폴더에서 실행하세요."),
        md("## <font color=blue>**<데이터 분석 (20점)>**</font>"),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code_clean(COMMON_IMPORT),
        md("### **1. pandas 라이브러리를 별칭(alias) pd 로 불러오세요.**\n---"),
        code_clean(
            "# (1) 여기에 답안코드를 작성하고 실행하세요\n"
            + ("" if problem else "\nimport pandas as pd\n")
        ),
        md(
            "### **2. wine_quality_data.csv 를 읽어 data 에 할당하고, 행·열 개수(shape)와 컬럼별 결측치 합계를 출력하세요.**\n"
            "* **\n- 데이터프레임 변수명 : data\n- 파일명 : wine_quality_data.csv\n---"
        ),
        code_clean(
            "# (2) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\ndata = pd.read_csv('./wine_quality_data.csv')\nprint(data.shape)\nprint(data.isna().sum())\n"
            )
        ),
        md("### **3. 수치형 컬럼 상관관계를 히트맵으로 시각화하려 합니다.**"),
        md(
            "* **\n"
            "- 대상 : data 에서 수치형 열만 선택\n"
            "- 상관계수 행렬을 구한 뒤 seaborn 히트맵으로 그리세요\n"
            "- 히트맵에 상관계수 숫자를 표시하는 옵션을 켜세요\n"
            "- <font color=blue>아래 코드의 빈칸을 채우고 실행하세요 (#3-1, #3-2, #3-3)</font>\n---"
        ),
        code_clean(
            "# (코드 셀) 코드의 빈칸을 채우고 실행하세요\n\n"
            + (
                "num = data.select_dtypes(include='number')\n"
                "sns.<#3-1>(num.<#3-3>(), <#3-2>=True, cmap='coolwarm')\n"
                "plt.title('Numeric Correlation')\n"
                "plt.show()\n"
                if problem
                else "num = data.select_dtypes(include='number')\n"
                "sns.heatmap(num.corr(), annot=True, cmap='coolwarm')\n"
                "plt.title('Numeric Correlation')\n"
                "plt.show()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["3-1", "3-2", "3-3"])
    cells += [
        md(
            "### **4. Grade 별 E_price 분포를 violinplot 으로 그리세요.**\n"
            "* **\n- seaborn violinplot / x='Grade', y='E_price'\n---"
        ),
        code_clean(
            "# (4) 여기에 답안코드를 작성하고 실행하세요\n"
            + ("" if problem else "\nsns.violinplot(data=data, x='Grade', y='E_price')\nplt.show()\n")
        ),
        md("## <font color=blue>**<데이터 전처리 (30점)>**</font>"),
        md(
            "### **5. E_price 결측치를 중앙값으로 채운 뒤 data_temp 에 저장하고, E_title 컬럼을 삭제하세요.**\n"
            "* **\n- <font color=blue>빈칸 (#5-1, #5-2)</font>\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "data_temp = data.copy()\n"
                "data_temp['E_price'] = data_temp['E_price'].<#5-1>(data_temp['E_price'].<#5-2>())\n"
                "data_temp = data_temp.drop(columns=['E_title'])\n"
                "data_temp.reset_index(drop=True, inplace=True)\n"
                if problem
                else "data_temp = data.copy()\n"
                "data_temp['E_price'] = data_temp['E_price'].fillna(data_temp['E_price'].median())\n"
                "data_temp = data_temp.drop(columns=['E_title'])\n"
                "data_temp.reset_index(drop=True, inplace=True)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["5-1", "5-2"])
    cells += [
        md(
            "### **6. data_temp 의 남은 결측 행을 제거하고 data_na 에 저장하세요.**\n"
            "* **\n- 결측 확인 후 행 삭제 / 빈칸 (#6-1, #6-2)\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "print(data_temp.<#6-1>().sum())\n"
                "data_na = data_temp.<#6-2>()\n"
                "print(data_na.<#6-1>().sum())\n"
                if problem
                else "print(data_temp.isna().sum())\n"
                "data_na = data_temp.dropna()\n"
                "print(data_na.isna().sum())\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["6-1", "6-2"])
    cells += [
        md(
            "### **7. 와인종류 치환 후 원-핫 인코딩**\n"
            "* **\n"
            "- (7-1)(7-2) isin / value_counts 빈칸 (공식과 동일 치환 규칙)\n"
            "- (7-3) 오류 정정: drop axis, get_dummies\n"
            "- (7-4) red 개수 단답\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "data_na.loc[data_na['E_FE_wine_kind'].<#7-1>(['white|rose|sparkling','red|white|sparkling', 'red|white|rose|sparkling',\n"
                "                                                                               'red|sparkling']), ['E_FE_wine_kind']] = 'sparkling'\n"
                "data_na.loc[data_na['E_FE_wine_kind'].<#7-1>(['white|sparkling']), ['E_FE_wine_kind']] = 'white'\n"
                "data_na.loc[data_na['E_FE_wine_kind'].<#7-1>(['red|rose', 'red|white', 'red|rose|sparkling']), ['E_FE_wine_kind']] = 'red'\n\n"
                "print(data_na['E_FE_wine_kind'].<#7-2>())\n"
                if problem
                else "data_na.loc[data_na['E_FE_wine_kind'].isin(['white|rose|sparkling','red|white|sparkling', 'red|white|rose|sparkling',\n"
                "                                                                               'red|sparkling']), ['E_FE_wine_kind']] = 'sparkling'\n"
                "data_na.loc[data_na['E_FE_wine_kind'].isin(['white|sparkling']), ['E_FE_wine_kind']] = 'white'\n"
                "data_na.loc[data_na['E_FE_wine_kind'].isin(['red|rose', 'red|white', 'red|rose|sparkling']), ['E_FE_wine_kind']] = 'red'\n\n"
                "print(data_na['E_FE_wine_kind'].value_counts())\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["7-1", "7-2"])
    cells += [
        code_clean(
            "# (7-3) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "data_na = data_na.drop( ['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety'], axis=0)\n"
                "data_preset = pd.get_dummy(data = data_na, column = ['E_country', 'E_FE_wine_kind'], drop_first=True)\n"
                "data_preset.info()\n"
                if problem
                else "data_na = data_na.drop(['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety'], axis=1)\n"
                "data_preset = pd.get_dummies(data=data_na, columns=['E_country', 'E_FE_wine_kind'], drop_first=True)\n"
                "data_preset.info()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["7-4"])
    cells += [
        md(
            "### **8. Grade 를 y, 나머지를 X 로 두고 train_test_split (70:30, stratify, random_state=7)**\n---"
        ),
        code_clean(
            "# (8) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.model_selection import train_test_split\n\n"
                "y = data_preset['Grade']\n"
                "X = data_preset.drop(columns=['Grade'])\n"
                "X_train, X_valid, y_train, y_valid = train_test_split(\n"
                "    X, y, test_size=0.3, random_state=7, stratify=y)\n"
            )
        ),
        md(
            "### **9. MinMaxScaler 오류 정정**\n"
            "* **\n- (9-1) 오류 정정: train fit_transform / valid transform\n- (9-2) 스케일된 검증셋 최댓값을 반올림한 값\n---"
        ),
        code_clean(
            "# (9-1) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "from sklearn.preprocessing import MinMaxScaler\n\n"
                "mm = MinMaxScaler()\n"
                "X_train = mm.transform(X_train)\n"
                "X_valid = mm.transform(X_train)\n"
                "round(np.max(X_valid))\n"
                if problem
                else "from sklearn.preprocessing import MinMaxScaler\n\n"
                "mm = MinMaxScaler()\n"
                "X_train = mm.fit_transform(X_train)\n"
                "X_valid = mm.transform(X_valid)\n"
                "round(np.max(X_valid))\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["9-2"])
    cells += [
        md("## <font color=blue>**<AI 모델링(50점)>**</font>"),
        md(
            "### **10. LogisticRegression 과 RandomForestClassifier 를 GridSearchCV 로 학습**\n"
            "* **\n"
            "- (10-1) LogisticRegression: C 후보 [0.1, 1, 10], cv=3, scoring='accuracy', n_jobs=-1, max_iter=500 → gs_lr, fit\n"
            "- (10-2) RandomForestClassifier: n_estimators [100, 200], max_depth [5, 10], cv=3, random_state=7 → gs_rf, fit\n"
            "- (10-3) RandomForest 최적 n_estimators\n---"
        ),
        code_clean(
            "# (10-1) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.linear_model import LogisticRegression\n"
                "from sklearn.model_selection import GridSearchCV\n\n"
                "gs_lr = GridSearchCV(\n"
                "    LogisticRegression(max_iter=500),\n"
                "    param_grid={'C': [0.1, 1, 10]},\n"
                "    cv=3, scoring='accuracy', n_jobs=-1)\n"
                "gs_lr.fit(X_train, y_train)\n"
            )
        ),
        code_clean(
            "# (10-2) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.ensemble import RandomForestClassifier\n\n"
                "gs_rf = GridSearchCV(\n"
                "    RandomForestClassifier(random_state=7),\n"
                "    param_grid={'n_estimators': [100, 200], 'max_depth': [5, 10]},\n"
                "    cv=3, scoring='accuracy', n_jobs=-1)\n"
                "gs_rf.fit(X_train, y_train)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["10-3"])
    cells += [
        md(
            "### **11. RandomForest 변수중요도 (오류 정정)**\n"
            "* **\n- (11-1) best_estimator_.feature_importances_ / sort_values\n- (11-2) 상위 1개 변수명\n---"
        ),
        code_clean(
            "# (11-1) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "fi = pd.DataFrame({'feature': X.columns, 'importance': gs_rf.importances})\n"
                "fi = fi.sort_index('importance', ascending=False)[:10]\n"
                "sns.barplot(x='importance', y='feature', data=fi)\n"
                "plt.show()\n"
                if problem
                else "fi = pd.DataFrame({\n"
                "    'feature': X.columns,\n"
                "    'importance': gs_rf.best_estimator_.feature_importances_})\n"
                "fi = fi.sort_values('importance', ascending=False)[:10]\n"
                "sns.barplot(x='importance', y='feature', data=fi)\n"
                "plt.show()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["11-2"])
    cells += [
        md(
            "### **12. f1_score 로 성능 비교 (오류 정정)**\n"
            "* **\n- (12-1) best_estimator_ predict + f1_score(average='weighted')\n- (12-2) 더 우수한 모델 이름\n---"
        ),
        code_clean(
            "# (12-1) 아래 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "from sklearn_metrics import f1\n\n"
                "y_pred_lr = gs_lr.predict(X_valid)\n"
                "y_pred_rf = gs_rf.predict(X_train)\n\n"
                "lr_f1 = f1(y_valid, y_pred_rf, average='weighted')\n"
                "rf_f1 = f1(y_valid, y_pred_rf, average='weighted')\n"
                "print(lr_f1, rf_f1)\n"
                if problem
                else "from sklearn.metrics import f1_score\n\n"
                "y_pred_lr = gs_lr.best_estimator_.predict(X_valid)\n"
                "y_pred_rf = gs_rf.best_estimator_.predict(X_valid)\n\n"
                "lr_f1 = f1_score(y_valid, y_pred_lr, average='weighted')\n"
                "rf_f1 = f1_score(y_valid, y_pred_rf, average='weighted')\n"
                "print(lr_f1, rf_f1)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["12-2"])
    cells += [
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code_clean(
            "import tensorflow as tf\n"
            "from tensorflow.keras.models import Sequential\n"
            "from tensorflow.keras.layers import Dense, Dropout\n"
            "from tensorflow.keras.callbacks import EarlyStopping\n"
            "from tensorflow.keras.utils import to_categorical\n"
            "tf.random.set_seed(1)\n"
        ),
        md(
            "### **13. DNN 모델링 (공식 Topology 와 동일 계열)**\n"
            "* **\n- Dense 128-relu → Dropout 0.3 → Dense 64-relu → Dense 32-relu → Dense 2-sigmoid\n"
            "- EarlyStopping monitor=val_loss, patience=14\n"
            "- <font color=blue>빈칸 #13-1, #13-2</font>\n---"
        ),
        md("![DNN Topology](Topology.png)"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "from sklearn.preprocessing import LabelEncoder\n\n"
                "model = Sequential([\n"
                "    <#13-1>\n"
                "])\n\n"
                "estop = EarlyStopping(monitor='val_loss', <#13-2>=14, restore_best_weights=True)\n"
                "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n\n"
                "le = LabelEncoder()\n"
                "y_train_enc = le.fit_transform(y_train)\n"
                "y_valid_enc = le.transform(y_valid)\n"
                "y_train_oh = to_categorical(y_train_enc)\n"
                "y_valid_oh = to_categorical(y_valid_enc)\n\n"
                "history = model.fit(X_train, y_train_oh, epochs=50, batch_size=128,\n"
                "                    validation_data=(X_valid, y_valid_oh), callbacks=[estop])\n"
                if problem
                else "from sklearn.preprocessing import LabelEncoder\n\n"
                "model = Sequential([\n"
                "    Dense(128, activation='relu'),\n"
                "    Dropout(0.3),\n"
                "    Dense(64, activation='relu'),\n"
                "    Dense(32, activation='relu'),\n"
                "    Dense(2, activation='sigmoid'),\n"
                "])\n\n"
                "estop = EarlyStopping(monitor='val_loss', patience=14, restore_best_weights=True)\n"
                "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n\n"
                "le = LabelEncoder()\n"
                "y_train_enc = le.fit_transform(y_train)\n"
                "y_valid_enc = le.transform(y_valid)\n"
                "y_train_oh = to_categorical(y_train_enc)\n"
                "y_valid_oh = to_categorical(y_valid_enc)\n\n"
                "history = model.fit(X_train, y_train_oh, epochs=50, batch_size=128,\n"
                "                    validation_data=(X_valid, y_valid_oh), callbacks=[estop])\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["13-1", "13-2"])
    cells += [
        md(
            "### **14. history 의 accuracy / val_accuracy 를 한 그래프에 그리세요.**\n"
            "* **\n- legend: acc, val_acc / title: Model Accuracy / xlabel Epochs, ylabel Accuracy\n---"
        ),
        code_clean(
            "# (14) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nplt.plot(history.history['accuracy'], label='acc')\n"
                "plt.plot(history.history['val_accuracy'], label='val_acc')\n"
                "plt.title('Model Accuracy')\n"
                "plt.xlabel('Epochs')\n"
                "plt.ylabel('Accuracy')\n"
                "plt.legend()\n"
                "plt.show()\n"
            )
        ),
        md("### **모든 문항이 완료되었습니다. 수고하셨습니다.**\n해설은 `set01_solution.ipynb` / `answer_key_set01.md` 를 참고하세요."),
    ]
    return cells


# ---------------------------------------------------------------------------
# SET 2 — describe / hist+count subplots / IQR / crosstab / StandardScaler / DT+RF / confusion_matrix
# ---------------------------------------------------------------------------

def build_set2_v2(problem: bool) -> list:
    a = {
        "3-1": "subplots",
        "3-2": "axes",
        "3-3": "set_xlabel",
        "5-1": "drop",
        "5-2": "index",
        "6-1": "isnull",
        "6-2": "dropna",
        "7-1": "where",
        "7-2": "nunique",
        "7-4": "23489",
        "9-2": "실행 결과",
        "10-3": "실행 후 best max_depth",
        "11-2": "FE_points_winery",
        "12-2": "RandomForest",
        "13-2": "patience",
    }
    cells = [
        md("**AICE Associate <font color=red>모의고사</font> — 분류 Set 2**"),
        md(SCENARIO.format(set_no=2)),
        md(HEADER_NOTICE),
        md(COLUMNS),
        md("**배점:** 데이터 분석 20점 · 데이터 전처리 30점 · AI 모델링 50점 (총 14문항 / 100점)"),
        md("## <font color=blue>**<데이터 분석 (20점)>**</font>"),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code_clean(COMMON_IMPORT),
        md("### **1. scikit-learn 을 별칭 sk 로 import 하세요.**\n---"),
        code_clean("# (1) 여기에 답안코드를 작성하고 실행하세요\n" + ("" if problem else "\nimport sklearn as sk\n")),
        md(
            "### **2. pandas 로 CSV 를 읽어 data 에 넣고, 수치형/비수치형 describe 를 각각 출력하세요.**\n---"
        ),
        code_clean(
            "# (2) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nimport pandas as pd\n"
                "data = pd.read_csv('./wine_quality_data.csv')\n"
                "display(data.describe(include='number'))\n"
                "display(data.describe(exclude='number'))\n"
            )
        ),
        md("### **3. FE_continent countplot + FE_points_location histplot (subplots)**"),
        md("* **\n- 빈칸: subplots / axes / set_xlabel\n---"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "fig, axes = plt.<#3-1>(nrows=1, ncols=2, figsize=(15, 6))\n"
                "sns.countplot(data=data, x='FE_continent', ax=<#3-2>[0])\n"
                "sns.histplot(data=data, x='FE_points_location', hue='Grade', ax=<#3-2>[1])\n"
                "<#3-2>[0].<#3-3>('Continent')\n"
                "<#3-2>[1].set_title('Location Score')\n"
                "plt.show()\n"
                if problem
                else "fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))\n"
                "sns.countplot(data=data, x='FE_continent', ax=axes[0])\n"
                "sns.histplot(data=data, x='FE_points_location', hue='Grade', ax=axes[1])\n"
                "axes[0].set_xlabel('Continent')\n"
                "axes[1].set_title('Location Score')\n"
                "plt.show()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["3-1", "3-2", "3-3"])
    cells += [
        md("### **4. Grade × FE_continent crosstab 을 heatmap 으로 그리세요.**\n---"),
        code_clean(
            "# (4) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nct = pd.crosstab(data['Grade'], data['FE_continent'])\n"
                "sns.heatmap(ct, annot=True, fmt='d')\n"
                "plt.show()\n"
            )
        ),
        md("## <font color=blue>**<데이터 전처리 (30점)>**</font>"),
        md("### **5. FE_points_variety IQR 이상치 제거 + E_title 삭제 → data_temp**\n---"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "q1 = data['FE_points_variety'].quantile(0.25)\n"
                "q3 = data['FE_points_variety'].quantile(0.75)\n"
                "iqr = q3 - q1\n"
                "lower_fence = q1 - 1.5 * iqr\n"
                "upper_fence = q3 + 1.5 * iqr\n"
                "data_temp = data.<#5-1>( data[(data['FE_points_variety'] > upper_fence) | (data['FE_points_variety'] < lower_fence)].<#5-2>, axis=0)\n"
                "data_temp = data_temp.<#5-1>( columns=['E_title'], axis=1)\n"
                "data_temp.reset_index(drop=True, inplace=True)\n"
                if problem
                else "q1 = data['FE_points_variety'].quantile(0.25)\n"
                "q3 = data['FE_points_variety'].quantile(0.75)\n"
                "iqr = q3 - q1\n"
                "lower_fence = q1 - 1.5 * iqr\n"
                "upper_fence = q3 + 1.5 * iqr\n"
                "data_temp = data.drop(data[(data['FE_points_variety'] > upper_fence) | (data['FE_points_variety'] < lower_fence)].index)\n"
                "data_temp = data_temp.drop(columns=['E_title'])\n"
                "data_temp.reset_index(drop=True, inplace=True)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["5-1", "5-2"])
    cells += [
        md("### **6. 결측 행 제거 → data_na**\n---"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "print(data_temp.<#6-1>().sum())\n"
                "data_na = data_temp.<#6-2>()\n"
                "print(data_na.<#6-1>().sum())\n"
                if problem
                else "print(data_temp.isnull().sum())\n"
                "data_na = data_temp.dropna()\n"
                "print(data_na.isnull().sum())\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["6-1", "6-2"])
    cells += [
        md(
            "### **7. E_country 를 US / Other 로 단순화 후 원핫**\n"
            "* **\n- (7-1) where 빈칸 (7-2) nunique (7-3) 오류정정 (7-4) US 건수\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "data_na['E_country'] = data_na['E_country'].<#7-1>(data_na['E_country'] == 'US', other='Other')\n"
                "print(data_na['E_country'].<#7-2>())\n"
                "print(data_na['E_country'].value_counts())\n"
                if problem
                else "data_na['E_country'] = data_na['E_country'].where(data_na['E_country'] == 'US', other='Other')\n"
                "print(data_na['E_country'].nunique())\n"
                "print(data_na['E_country'].value_counts())\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["7-1", "7-2"])
    cells += [
        code_clean(
            "# (7-3) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "data_na = data_na.drop(['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety', 'E_FE_wine_kind'], axis=0)\n"
                "data_preset = pd.get_dummies(data=data_na, column=['E_country'], drop_first=True)\n"
                "data_preset.info()\n"
                if problem
                else "data_na = data_na.drop(['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety', 'E_FE_wine_kind'], axis=1)\n"
                "data_preset = pd.get_dummies(data=data_na, columns=['E_country'], drop_first=True)\n"
                "data_preset.info()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["7-4"])
    cells += [
        md("### **8. train_test_split 70:30, stratify, random_state=7**\n---"),
        code_clean(
            "# (8) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.model_selection import train_test_split\n"
                "y = data_preset['Grade']\n"
                "X = data_preset.drop(columns=['Grade'])\n"
                "X_train, X_valid, y_train, y_valid = train_test_split(\n"
                "    X, y, test_size=0.3, random_state=7, stratify=y)\n"
            )
        ),
        md("### **9. StandardScaler 오류 정정**\n---"),
        code_clean(
            "# (9-1) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "from sklearn.preprocessing import StandardScaler\n"
                "ss = StandardScaler()\n"
                "X_train = ss.transform(X_train)\n"
                "X_valid = ss.transform(X_train)\n"
                "round(np.max(X_valid))\n"
                if problem
                else "from sklearn.preprocessing import StandardScaler\n"
                "ss = StandardScaler()\n"
                "X_train = ss.fit_transform(X_train)\n"
                "X_valid = ss.transform(X_valid)\n"
                "round(np.max(X_valid))\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["9-2"])
    cells += [
        md("## <font color=blue>**<AI 모델링(50점)>**</font>"),
        md(
            "### **10. DecisionTreeClassifier + RandomForestClassifier GridSearchCV (cv=3)**\n"
            "* **\n- DT: max_depth [3,5,7], min_samples_split [2,5] → gs_dt\n"
            "- RF: n_estimators [100,200], max_depth [5,10] → gs_rf\n"
            "- (10-3) RF 최적 max_depth\n---"
        ),
        code_clean(
            "# (10-1) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.tree import DecisionTreeClassifier\n"
                "from sklearn.model_selection import GridSearchCV\n"
                "gs_dt = GridSearchCV(\n"
                "    DecisionTreeClassifier(random_state=7),\n"
                "    {'max_depth': [3, 5, 7], 'min_samples_split': [2, 5]},\n"
                "    cv=3, scoring='accuracy', n_jobs=-1)\n"
                "gs_dt.fit(X_train, y_train)\n"
            )
        ),
        code_clean(
            "# (10-2) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.ensemble import RandomForestClassifier\n"
                "gs_rf = GridSearchCV(\n"
                "    RandomForestClassifier(random_state=7),\n"
                "    {'n_estimators': [100, 200], 'max_depth': [5, 10]},\n"
                "    cv=3, scoring='accuracy', n_jobs=-1)\n"
                "gs_rf.fit(X_train, y_train)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["10-3"])
    cells += [
        md("### **11. 변수중요도 오류 정정**\n---"),
        code_clean(
            "# (11-1) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "fi = pd.DataFrame({'feature': X.columns, 'importance': gs_rf.feature_importances_})\n"
                "fi = fi.sort_values('importance', ascending=True)[:10]\n"
                "sns.barplot(x='importance', y='feature', data=fi)\n"
                "plt.show()\n"
                if problem
                else "fi = pd.DataFrame({\n"
                "    'feature': X.columns,\n"
                "    'importance': gs_rf.best_estimator_.feature_importances_})\n"
                "fi = fi.sort_values('importance', ascending=False)[:10]\n"
                "sns.barplot(x='importance', y='feature', data=fi)\n"
                "plt.show()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["11-2"])
    cells += [
        md("### **12. confusion_matrix / accuracy_score 오류 정정**\n---"),
        code_clean(
            "# (12-1) 아래 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "from sklearn.metrics import confusion_matrix, accuracy_score\n\n"
                "y_pred_dt = gs_dt.predict(X_valid)\n"
                "y_pred_rf = gs_rf.predict(X_valid)\n"
                "print(confusion_matrix(y_valid, y_pred_dt))\n"
                "dt_acc = accuracy_score(y_valid, y_pred_rf)\n"
                "rf_acc = accuracy_score(y_valid, y_pred_rf)\n"
                "print(dt_acc, rf_acc)\n"
                if problem
                else "from sklearn.metrics import confusion_matrix, accuracy_score\n\n"
                "y_pred_dt = gs_dt.best_estimator_.predict(X_valid)\n"
                "y_pred_rf = gs_rf.best_estimator_.predict(X_valid)\n"
                "print(confusion_matrix(y_valid, y_pred_dt))\n"
                "dt_acc = accuracy_score(y_valid, y_pred_dt)\n"
                "rf_acc = accuracy_score(y_valid, y_pred_rf)\n"
                "print(dt_acc, rf_acc)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["12-2"])
    cells += [
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code_clean(
            "import tensorflow as tf\n"
            "from tensorflow.keras.models import Sequential\n"
            "from tensorflow.keras.layers import Dense, Dropout\n"
            "from tensorflow.keras.callbacks import EarlyStopping\n"
            "from tensorflow.keras.utils import to_categorical\n"
            "tf.random.set_seed(1)\n"
        ),
        md("### **13. DNN (공식과 동일 토폴로지 계열) — patience 빈칸**\n---"),
        md("![DNN Topology](Topology.png)"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "from sklearn.preprocessing import LabelEncoder\n"
                "model = Sequential([\n"
                "    Dense(128, activation='relu'), Dropout(0.3),\n"
                "    Dense(64, activation='relu'), Dense(32, activation='relu'),\n"
                "    Dense(2, activation='sigmoid')\n"
                "])\n"
                "estop = EarlyStopping(monitor='val_loss', <#13-2>=14, restore_best_weights=True)\n"
                "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n"
                "le = LabelEncoder()\n"
                "y_train_oh = to_categorical(le.fit_transform(y_train))\n"
                "y_valid_oh = to_categorical(le.transform(y_valid))\n"
                "history = model.fit(X_train, y_train_oh, epochs=50, batch_size=128,\n"
                "                    validation_data=(X_valid, y_valid_oh), callbacks=[estop])\n"
                if problem
                else "from sklearn.preprocessing import LabelEncoder\n"
                "model = Sequential([\n"
                "    Dense(128, activation='relu'), Dropout(0.3),\n"
                "    Dense(64, activation='relu'), Dense(32, activation='relu'),\n"
                "    Dense(2, activation='sigmoid')\n"
                "])\n"
                "estop = EarlyStopping(monitor='val_loss', patience=14, restore_best_weights=True)\n"
                "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n"
                "le = LabelEncoder()\n"
                "y_train_oh = to_categorical(le.fit_transform(y_train))\n"
                "y_valid_oh = to_categorical(le.transform(y_valid))\n"
                "history = model.fit(X_train, y_train_oh, epochs=50, batch_size=128,\n"
                "                    validation_data=(X_valid, y_valid_oh), callbacks=[estop])\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["13-2"])
    cells += [
        md("### **14. Model Accuracy 곡선 (acc / val_acc)**\n---"),
        code_clean(
            "# (14) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nplt.plot(history.history['accuracy'], label='acc')\n"
                "plt.plot(history.history['val_accuracy'], label='val_acc')\n"
                "plt.title('Model Accuracy')\n"
                "plt.xlabel('Epochs')\n"
                "plt.ylabel('Accuracy')\n"
                "plt.legend()\n"
                "plt.show()\n"
            )
        ),
        md("### **모든 문항이 완료되었습니다. 수고하셨습니다.**"),
    ]
    return cells


# ---------------------------------------------------------------------------
# SET 3 — groupby / box+bar subplots / query / map / RobustScaler / RF+GB / classification_report
# ---------------------------------------------------------------------------

def build_set3(problem: bool) -> list:
    a = {
        "3-1": "subplots",
        "3-2": "axes",
        "3-3": "set_title",
        "5-1": "query",
        "5-2": "copy",
        "6-1": "isna",
        "6-2": "dropna",
        "7-1": "map",
        "7-2": "value_counts",
        "7-4": "29211",
        "9-2": "실행 결과",
        "10-3": "실행 후 best n_estimators",
        "11-2": "FE_points_winery",
        "12-2": "RandomForest",
        "13-2": "patience",
    }
    cells = [
        md("**AICE Associate <font color=red>모의고사</font> — 분류 Set 3 (약간 어렵게)**"),
        md(SCENARIO.format(set_no=3)),
        md(HEADER_NOTICE),
        md(COLUMNS),
        md("**배점:** 데이터 분석 20점 · 데이터 전처리 30점 · AI 모델링 50점 (총 14문항 / 100점)"),
        md("## <font color=blue>**<데이터 분석 (20점)>**</font>"),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code_clean(COMMON_IMPORT),
        md("### **1. pandas 를 pd 로, seaborn 이 이미 sns 라면 numpy 만 np 로 확인 import 하세요. (pandas import)**\n---"),
        code_clean("# (1) 여기에 답안코드를 작성하고 실행하세요\n" + ("" if problem else "\nimport pandas as pd\n")),
        md(
            "### **2. 데이터 로드 후 Grade 별 FE_points_winery 평균을 groupby 로 구해 출력하세요.**\n---"
        ),
        code_clean(
            "# (2) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\ndata = pd.read_csv('./wine_quality_data.csv')\n"
                "print(data.groupby('Grade')['FE_points_winery'].mean())\n"
            )
        ),
        md("### **3. boxplot + barplot(추정) subplots**"),
        md(
            "* **\n- 왼쪽: Grade vs FE_points_winery boxplot\n"
            "- 오른쪽: Grade 별 E_price 평균 barplot (estimator='mean')\n"
            "- 제목 Wine Box / Price Bar (#3-3 set_title)\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "fig, axes = plt.<#3-1>(1, 2, figsize=(15, 6))\n"
                "sns.boxplot(data=data, x='Grade', y='FE_points_winery', ax=<#3-2>[0])\n"
                "sns.barplot(data=data, x='Grade', y='E_price', estimator='mean', ax=<#3-2>[1])\n"
                "<#3-2>[0].<#3-3>('Wine Box')\n"
                "<#3-2>[1].<#3-3>('Price Bar')\n"
                "plt.show()\n"
                if problem
                else "fig, axes = plt.subplots(1, 2, figsize=(15, 6))\n"
                "sns.boxplot(data=data, x='Grade', y='FE_points_winery', ax=axes[0])\n"
                "sns.barplot(data=data, x='Grade', y='E_price', estimator='mean', ax=axes[1])\n"
                "axes[0].set_title('Wine Box')\n"
                "axes[1].set_title('Price Bar')\n"
                "plt.show()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["3-1", "3-2", "3-3"])
    cells += [
        md(
            "### **4. E_FE_vintage 와 FE_points_winery 의 관계를 scatterplot 으로, hue='Grade' 로 그리세요.**\n---"
        ),
        code_clean(
            "# (4) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nsns.scatterplot(data=data.sample(3000, random_state=7), x='E_FE_vintage', y='FE_points_winery', hue='Grade', alpha=0.5)\n"
                "plt.show()\n"
            )
        ),
        md("## <font color=blue>**<데이터 전처리 (30점)>**</font>"),
        md(
            "### **5. E_price 가 결측이 아닌 행만 남기고, FE_points_winery>=80 인 행만 query 로 필터 → data_temp**\n"
            "* **\n- E_title 삭제\n- 빈칸: query / copy (연습용)\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "data_temp = data.dropna(subset=['E_price']).<#5-1>('FE_points_winery >= 80').<#5-2>()\n"
                "data_temp = data_temp.drop(columns=['E_title'])\n"
                "data_temp.reset_index(drop=True, inplace=True)\n"
                if problem
                else "data_temp = data.dropna(subset=['E_price']).query('FE_points_winery >= 80').copy()\n"
                "data_temp = data_temp.drop(columns=['E_title'])\n"
                "data_temp.reset_index(drop=True, inplace=True)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["5-1", "5-2"])
    cells += [
        md("### **6. 남은 결측 제거 → data_na**\n---"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "print(data_temp.<#6-1>().sum())\n"
                "data_na = data_temp.<#6-2>()\n"
                "print(data_na.<#6-1>().sum())\n"
                if problem
                else "print(data_temp.isna().sum())\n"
                "data_na = data_temp.dropna()\n"
                "print(data_na.isna().sum())\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["6-1", "6-2"])
    cells += [
        md(
            "### **7. Grade 를 map 으로 Fail→0, Pass→1 변환 후 원핫**\n"
            "* **\n- (7-1) map (7-2) value_counts (7-3) 오류정정 (7-4) Pass(=1) 개수\n---"
        ),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "data_na['Grade'] = data_na['Grade'].<#7-1>({'Fail': 0, 'Pass': 1})\n"
                "print(data_na['Grade'].<#7-2>())\n"
                if problem
                else "data_na['Grade'] = data_na['Grade'].map({'Fail': 0, 'Pass': 1})\n"
                "print(data_na['Grade'].value_counts())\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["7-1", "7-2"])
    cells += [
        code_clean(
            "# (7-3) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "data_na = data_na.drop(['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety'], axis=0)\n"
                "data_preset = pd.get_dummies(data=data_na, columns=['E_country', 'E_FE_wine_kind'], drop_first=False)\n"
                "# drop_first 는 True 가 모범이지만, 오류는 axis / 함수명에 있습니다.\n"
                "data_preset.info()\n"
                if problem
                else "data_na = data_na.drop(['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety'], axis=1)\n"
                "data_preset = pd.get_dummies(data=data_na, columns=['E_country', 'E_FE_wine_kind'], drop_first=True)\n"
                "data_preset.info()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["7-4"])
    cells += [
        md("### **8. train_test_split (test_size=0.3, random_state=7, stratify=y)**\n---"),
        code_clean(
            "# (8) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.model_selection import train_test_split\n"
                "y = data_preset['Grade']\n"
                "X = data_preset.drop(columns=['Grade'])\n"
                "X_train, X_valid, y_train, y_valid = train_test_split(\n"
                "    X, y, test_size=0.3, random_state=7, stratify=y)\n"
            )
        ),
        md("### **9. RobustScaler 오류 정정**\n---"),
        code_clean(
            "# (9-1) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "from sklearn.preprocessing import RobustScaler\n"
                "rs = RobustScaler()\n"
                "X_valid = rs.fit_transform(X_valid)\n"
                "X_train = rs.transform(X_train)\n"
                "round(np.max(X_valid))\n"
                if problem
                else "from sklearn.preprocessing import RobustScaler\n"
                "rs = RobustScaler()\n"
                "X_train = rs.fit_transform(X_train)\n"
                "X_valid = rs.transform(X_valid)\n"
                "round(np.max(X_valid))\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["9-2"])
    cells += [
        md("## <font color=blue>**<AI 모델링(50점)>**</font>"),
        md(
            "### **10. RandomForest + GradientBoosting GridSearchCV (cv=3)**\n"
            "* **\n- RF → gs_rf / GB → gs_gb\n- (10-3) RF 최적 n_estimators\n---"
        ),
        code_clean(
            "# (10-1) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.ensemble import RandomForestClassifier\n"
                "from sklearn.model_selection import GridSearchCV\n"
                "gs_rf = GridSearchCV(\n"
                "    RandomForestClassifier(random_state=7),\n"
                "    {'n_estimators': [100, 200], 'max_depth': [5, 10]},\n"
                "    cv=3, scoring='accuracy', n_jobs=-1)\n"
                "gs_rf.fit(X_train, y_train)\n"
            )
        ),
        code_clean(
            "# (10-2) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nfrom sklearn.ensemble import GradientBoostingClassifier\n"
                "gs_gb = GridSearchCV(\n"
                "    GradientBoostingClassifier(random_state=7),\n"
                "    {'n_estimators': [50, 100], 'max_depth': [2, 3]},\n"
                "    cv=3, scoring='accuracy', n_jobs=-1)\n"
                "gs_gb.fit(X_train, y_train)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["10-3"])
    cells += [
        md("### **11. RF 변수중요도 오류 정정**\n---"),
        code_clean(
            "# (11-1) 여기에 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "fi = pd.DataFrame({'feature': X.columns, 'importance': gs_rf.best_estimator_.feature_importance})\n"
                "fi = fi.sort_values('importance', ascending=False).head(10)\n"
                "sns.barplot(data=fi, x='importance', y='feature')\n"
                "plt.show()\n"
                if problem
                else "fi = pd.DataFrame({\n"
                "    'feature': X.columns,\n"
                "    'importance': gs_rf.best_estimator_.feature_importances_})\n"
                "fi = fi.sort_values('importance', ascending=False).head(10)\n"
                "sns.barplot(data=fi, x='importance', y='feature')\n"
                "plt.show()\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["11-2"])
    cells += [
        md("### **12. classification_report 오류 정정**\n---"),
        code_clean(
            "# (12-1) 아래 코드의 오류를 정정하고 실행하세요\n\n"
            + (
                "from sklearn.metrics import classification_report, accuracy_score\n\n"
                "y_pred_rf = gs_rf.predict(X_valid)\n"
                "y_pred_gb = gs_gb.predict(X_valid)\n"
                "print(classification_report(y_valid, y_pred_rf))\n"
                "rf_acc = accuracy_score(y_valid, y_pred_gb)\n"
                "gb_acc = accuracy_score(y_valid, y_pred_gb)\n"
                "print(rf_acc, gb_acc)\n"
                if problem
                else "from sklearn.metrics import classification_report, accuracy_score\n\n"
                "y_pred_rf = gs_rf.best_estimator_.predict(X_valid)\n"
                "y_pred_gb = gs_gb.best_estimator_.predict(X_valid)\n"
                "print(classification_report(y_valid, y_pred_rf))\n"
                "rf_acc = accuracy_score(y_valid, y_pred_rf)\n"
                "gb_acc = accuracy_score(y_valid, y_pred_gb)\n"
                "print(rf_acc, gb_acc)\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["12-2"])
    cells += [
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code_clean(
            "import tensorflow as tf\n"
            "from tensorflow.keras.models import Sequential\n"
            "from tensorflow.keras.layers import Dense, Dropout\n"
            "from tensorflow.keras.callbacks import EarlyStopping\n"
            "from tensorflow.keras.utils import to_categorical\n"
            "tf.random.set_seed(1)\n"
        ),
        md(
            "### **13. DNN — Grade 가 이미 0/1 이므로 LabelEncoder 없이 to_categorical 만 사용해도 됩니다.**\n"
            "* **\n- patience 빈칸 (#13-2)\n---"
        ),
        md("![DNN Topology](Topology.png)"),
        code_clean(
            "# (코드 셀)\n\n"
            + (
                "model = Sequential([\n"
                "    Dense(128, activation='relu'), Dropout(0.3),\n"
                "    Dense(64, activation='relu'), Dense(32, activation='relu'),\n"
                "    Dense(2, activation='sigmoid')\n"
                "])\n"
                "estop = EarlyStopping(monitor='val_loss', <#13-2>=14, restore_best_weights=True)\n"
                "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n"
                "y_train_oh = to_categorical(y_train)\n"
                "y_valid_oh = to_categorical(y_valid)\n"
                "history = model.fit(X_train, y_train_oh, epochs=50, batch_size=128,\n"
                "                    validation_data=(X_valid, y_valid_oh), callbacks=[estop])\n"
                if problem
                else "model = Sequential([\n"
                "    Dense(128, activation='relu'), Dropout(0.3),\n"
                "    Dense(64, activation='relu'), Dense(32, activation='relu'),\n"
                "    Dense(2, activation='sigmoid')\n"
                "])\n"
                "estop = EarlyStopping(monitor='val_loss', patience=14, restore_best_weights=True)\n"
                "model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n"
                "y_train_oh = to_categorical(y_train)\n"
                "y_valid_oh = to_categorical(y_valid)\n"
                "history = model.fit(X_train, y_train_oh, epochs=50, batch_size=128,\n"
                "                    validation_data=(X_valid, y_valid_oh), callbacks=[estop])\n"
            )
        ),
    ]
    cells += blank_answers(problem, a, ["13-2"])
    cells += [
        md("### **14. Accuracy 학습 곡선**\n---"),
        code_clean(
            "# (14) 여기에 답안코드를 작성하고 실행하세요\n"
            + (
                ""
                if problem
                else "\nplt.plot(history.history['accuracy'], label='acc')\n"
                "plt.plot(history.history['val_accuracy'], label='val_acc')\n"
                "plt.title('Model Accuracy')\n"
                "plt.xlabel('Epochs')\n"
                "plt.ylabel('Accuracy')\n"
                "plt.legend()\n"
                "plt.show()\n"
            )
        ),
        md("### **모든 문항이 완료되었습니다. 수고하셨습니다.**"),
    ]
    return cells


ANSWER_KEYS = {
    1: """# Set 1 정답 요약

| 번호 | 정답 |
|------|------|
| 1 | `import pandas as pd` |
| 2 | `read_csv` + `shape` + `isna().sum()` |
| 3-1/2/3 | `heatmap` / `annot` / `corr` |
| 4 | `sns.violinplot(..., x='Grade', y='E_price')` |
| 5-1/2 | `fillna` / `median` |
| 6-1/2 | `isna` / `dropna` |
| 7-1/2 | `isin` / `value_counts` |
| 7-3 | `axis=1`, `get_dummies`, `columns=` |
| 7-4 | `46402` (fillna+dropna 후 치환 기준 red; 공식 IQR 경로와 다름) |
| 8 | `train_test_split(..., test_size=0.3, random_state=7, stratify=y)` |
| 9-1 | `fit_transform(X_train)`, `transform(X_valid)` |
| 10 | `GridSearchCV` + LR / RF |
| 11-1 | `best_estimator_.feature_importances_`, `sort_values` |
| 11-2 | 보통 `FE_points_winery` |
| 12-1 | `f1_score` + `best_estimator_.predict(X_valid)` |
| 12-2 | `RandomForest` |
| 13-2 | `patience` |
| 14 | `history.history['accuracy']` / `val_accuracy` |
""",
    2: """# Set 2 정답 요약

| 번호 | 정답 |
|------|------|
| 1 | `import sklearn as sk` |
| 2 | `describe(include='number')` / `exclude='number'` |
| 3-1/2/3 | `subplots` / `axes` / `set_xlabel` |
| 4 | `pd.crosstab` + `sns.heatmap` |
| 5-1/2 | `drop` / `index` |
| 6-1/2 | `isnull` / `dropna` |
| 7-1/2 | `where` / `nunique` |
| 7-3 | `axis=1`, `columns=` |
| 7-4 | `23489` (US 건수, IQR+dropna 후) |
| 9-1 | StandardScaler `fit_transform` / `transform` |
| 10 | DT + RF GridSearchCV |
| 11 | `best_estimator_.feature_importances_`, 내림차순 |
| 12 | `confusion_matrix` + `accuracy_score` on **valid** preds |
| 13-2 | `patience` |
""",
    3: """# Set 3 정답 요약

| 번호 | 정답 |
|------|------|
| 1 | `import pandas as pd` |
| 2 | `groupby('Grade')['FE_points_winery'].mean()` |
| 3-1/2/3 | `subplots` / `axes` / `set_title` |
| 4 | `sns.scatterplot(..., hue='Grade')` |
| 5-1/2 | `query` / `copy` |
| 6-1/2 | `isna` / `dropna` |
| 7-1/2 | `map` / `value_counts` |
| 7-3 | `drop(..., axis=1)` |
| 7-4 | `29211` (Pass→1 개수) |
| 9-1 | RobustScaler: train에 fit, valid에 transform |
| 10 | RF + GradientBoosting GridSearchCV |
| 11 | `feature_importances_` (복수형) |
| 12 | `classification_report` + 올바른 predict 대상 |
| 13-2 | `patience` |
""",
}


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    def ensure_link(src: Path, dest: Path) -> None:
        if dest.exists() or dest.is_symlink():
            return
        try:
            dest.symlink_to(src)
            print("linked", dest.name)
        except OSError:
            shutil.copy2(src, dest)
            print("copied", dest.name)

    if DATA_SRC.exists():
        ensure_link(Path("../../official_samples/classification/wine_quality_data.csv"), ROOT / "wine_quality_data.csv")
    if TOPO_SRC.exists():
        ensure_link(Path("../../official_samples/classification/Topology.png"), ROOT / "Topology.png")

    builders = {1: build_set1, 2: build_set2_v2, 3: build_set3}
    for n, builder in builders.items():
        write_nb(ROOT / f"set{n:02d}_problem.ipynb", builder(True))
        write_nb(ROOT / f"set{n:02d}_solution.ipynb", builder(False))
        (ROOT / f"answer_key_set{n:02d}.md").write_text(ANSWER_KEYS[n], encoding="utf-8")

    readme = """# 와인 품질 분류 모의고사 (공식 샘플 기반)

공식 분류 샘플과 **동일 데이터** `wine_quality_data.csv` 를 사용합니다.

| 세트 | 파일 | 특징 |
|------|------|------|
| 1 | `set01_problem.ipynb` / `set01_solution.ipynb` | heatmap, violin, fillna/median, MinMax, LR+RF, f1 |
| 2 | `set02_*` | describe, crosstab heatmap, IQR, where, StandardScaler, DT+RF, confusion_matrix |
| 3 | `set03_*` | groupby, barplot, query, map(0/1), RobustScaler, RF+GB, classification_report |

- 오류 정정형 문항: 각 세트 Q7-3, Q9-1, Q11-1, Q12-1 포함
- GridSearch는 연습용으로 cv=3·후보 축소 (공식보다 가볍게)
- DNN Topology 이미지는 공식 `Topology.png` 복사본 사용

정답 요약: `answer_key_set0N.md`
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
