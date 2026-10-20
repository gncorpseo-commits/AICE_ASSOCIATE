"""
AICE Associate Mock Exam Notebooks Generator
30개의 모의고사 Jupyter Notebook을 생성합니다.
"""

import json
import os

# 노트북 생성 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 모의고사 정보 정의
MOCK_EXAMS = {
    # Level 1 - Basic (회귀 5개 + 분류 5개)
    'level_1_basic': [
        {'num': '01', 'name': 'delivery', 'title': '배달 소요시간 예측', 'type': 'regression', 
         'target': 'delivery_time', 'target_desc': '배달 소요시간 (분)', 'id_col': 'order_id',
         'scenario': '당신은 A 배달회사의 데이터 분석가입니다. 배달 주문 데이터를 분석하여 배달 소요시간을 예측하는 머신러닝 모델을 구축하세요.'},
        
        {'num': '02', 'name': 'sales', 'title': '월별 매출 예측', 'type': 'regression',
         'target': 'monthly_sales', 'target_desc': '월별 매출액', 'id_col': 'store_id',
         'scenario': '당신은 B 유통회사의 데이터 분석가입니다. 매장 데이터를 분석하여 월별 매출을 예측하는 모델을 구축하세요.'},
        
        {'num': '03', 'name': 'temperature', 'title': '기온 예측', 'type': 'regression',
         'target': 'temperature', 'target_desc': '기온 (섭씨)', 'id_col': None,
         'scenario': '당신은 기상청 데이터 분석가입니다. 기상 데이터를 분석하여 기온을 예측하는 모델을 구축하세요.'},
        
        {'num': '04', 'name': 'housing', 'title': '주택 가격 예측', 'type': 'regression',
         'target': 'price', 'target_desc': '주택 가격 (원)', 'id_col': 'house_id',
         'scenario': '당신은 C 부동산 회사의 데이터 분석가입니다. 주택 정보를 분석하여 가격을 예측하는 모델을 구축하세요.'},
        
        {'num': '05', 'name': 'traffic', 'title': '교통량 예측', 'type': 'regression',
         'target': 'traffic_volume', 'target_desc': '교통량', 'id_col': 'record_id',
         'scenario': '당신은 교통관리센터의 데이터 분석가입니다. 도로 데이터를 분석하여 교통량을 예측하는 모델을 구축하세요.'},
        
        {'num': '06', 'name': 'churn', 'title': '고객 이탈 예측', 'type': 'classification',
         'target': 'churn', 'target_desc': '이탈 여부 (0: 유지, 1: 이탈)', 'id_col': 'customer_id',
         'scenario': '당신은 D 서비스 회사의 데이터 분석가입니다. 고객 데이터를 분석하여 이탈 여부를 예측하는 모델을 구축하세요.'},
        
        {'num': '07', 'name': 'spam', 'title': '스팸 메일 분류', 'type': 'classification',
         'target': 'is_spam', 'target_desc': '스팸 여부 (0: 정상, 1: 스팸)', 'id_col': 'email_id',
         'scenario': '당신은 E 이메일 서비스의 데이터 분석가입니다. 이메일 데이터를 분석하여 스팸을 분류하는 모델을 구축하세요.'},
        
        {'num': '08', 'name': 'loan', 'title': '대출 승인 예측', 'type': 'classification',
         'target': 'approved', 'target_desc': '승인 여부 (0: 거절, 1: 승인)', 'id_col': 'applicant_id',
         'scenario': '당신은 F 금융회사의 데이터 분석가입니다. 대출 신청 데이터를 분석하여 승인 여부를 예측하는 모델을 구축하세요.'},
        
        {'num': '09', 'name': 'disease', 'title': '질병 예측', 'type': 'classification',
         'target': 'has_disease', 'target_desc': '질병 유무 (0: 정상, 1: 질병)', 'id_col': 'patient_id',
         'scenario': '당신은 G 병원의 데이터 분석가입니다. 환자 데이터를 분석하여 질병 유무를 예측하는 모델을 구축하세요.'},
        
        {'num': '10', 'name': 'satisfaction', 'title': '고객 만족도 분류', 'type': 'classification',
         'target': 'satisfaction', 'target_desc': '만족도 (Low/Medium/High)', 'id_col': 'customer_id',
         'scenario': '당신은 H 서비스 회사의 데이터 분석가입니다. 고객 피드백 데이터를 분석하여 만족도를 분류하는 모델을 구축하세요.'},
    ],
    
    # Level 2 - Intermediate
    'level_2_intermediate': [
        {'num': '11', 'name': 'taxi', 'title': '택시 이동시간 예측', 'type': 'regression',
         'target': 'trip_duration', 'target_desc': '이동시간 (분)', 'id_col': 'trip_id',
         'scenario': '당신은 택시 서비스 회사의 데이터 분석가입니다. 택시 운행 데이터를 분석하여 이동시간을 예측하는 모델을 구축하세요.'},
        
        {'num': '12', 'name': 'demand', 'title': '상품 수요 예측', 'type': 'regression',
         'target': 'demand', 'target_desc': '수요량', 'id_col': 'product_id',
         'scenario': '당신은 유통회사의 데이터 분석가입니다. 상품 데이터를 분석하여 수요를 예측하는 모델을 구축하세요.'},
        
        {'num': '13', 'name': 'energy', 'title': '에너지 소비 예측', 'type': 'regression',
         'target': 'energy_consumption', 'target_desc': '에너지 소비량', 'id_col': 'building_id',
         'scenario': '당신은 에너지 관리 회사의 데이터 분석가입니다. 건물 데이터를 분석하여 에너지 소비를 예측하는 모델을 구축하세요.'},
        
        {'num': '14', 'name': 'inventory', 'title': '적정 재고 예측', 'type': 'regression',
         'target': 'optimal_stock', 'target_desc': '적정 재고량', 'id_col': 'sku_id',
         'scenario': '당신은 물류회사의 데이터 분석가입니다. 상품 데이터를 분석하여 적정 재고를 예측하는 모델을 구축하세요.'},
        
        {'num': '15', 'name': 'waiting', 'title': '대기시간 예측', 'type': 'regression',
         'target': 'wait_time', 'target_desc': '대기시간 (분)', 'id_col': 'ticket_id',
         'scenario': '당신은 서비스 센터의 데이터 분석가입니다. 대기 데이터를 분석하여 대기시간을 예측하는 모델을 구축하세요.'},
        
        {'num': '16', 'name': 'fraud', 'title': '금융 사기 탐지', 'type': 'classification',
         'target': 'is_fraud', 'target_desc': '사기 여부 (0: 정상, 1: 사기)', 'id_col': 'transaction_id',
         'scenario': '당신은 금융회사의 데이터 분석가입니다. 거래 데이터를 분석하여 사기를 탐지하는 모델을 구축하세요.'},
        
        {'num': '17', 'name': 'conversion', 'title': '구매 전환 예측', 'type': 'classification',
         'target': 'converted', 'target_desc': '전환 여부 (0: 미전환, 1: 전환)', 'id_col': 'visitor_id',
         'scenario': '당신은 이커머스 회사의 데이터 분석가입니다. 방문자 데이터를 분석하여 구매 전환을 예측하는 모델을 구축하세요.'},
        
        {'num': '18', 'name': 'sentiment', 'title': '리뷰 감성 분류', 'type': 'classification',
         'target': 'sentiment', 'target_desc': '감성 (Negative/Neutral/Positive)', 'id_col': 'review_id',
         'scenario': '당신은 리뷰 분석 회사의 데이터 분석가입니다. 리뷰 데이터를 분석하여 감성을 분류하는 모델을 구축하세요.'},
        
        {'num': '19', 'name': 'credit', 'title': '신용 등급 예측', 'type': 'classification',
         'target': 'risk_grade', 'target_desc': '신용 등급 (A/B/C/D)', 'id_col': 'customer_id',
         'scenario': '당신은 신용평가 회사의 데이터 분석가입니다. 고객 데이터를 분석하여 신용 등급을 예측하는 모델을 구축하세요.'},
        
        {'num': '20', 'name': 'click', 'title': '광고 클릭 예측', 'type': 'classification',
         'target': 'clicked', 'target_desc': '클릭 여부 (0: 미클릭, 1: 클릭)', 'id_col': 'impression_id',
         'scenario': '당신은 광고 플랫폼의 데이터 분석가입니다. 광고 노출 데이터를 분석하여 클릭을 예측하는 모델을 구축하세요.'},
    ],
    
    # Level 3 - Advanced
    'level_3_advanced': [
        {'num': '21', 'name': 'navigation', 'title': '내비게이션 도착시간 예측 (실제 기출)', 'type': 'regression',
         'target': 'arrival_time', 'target_desc': '도착시간 (분)', 'id_col': 'route_id',
         'scenario': '당신은 내비게이션 서비스 회사의 데이터 분석가입니다. 경로 데이터를 분석하여 도착시간을 예측하는 머신러닝 모델을 구축하세요. 이 모델은 사용자에게 정확한 도착 예정 시간을 제공하는 데 활용됩니다.'},
        
        {'num': '22', 'name': 'telecom', 'title': '통신사 고객 해지 예측 (실제 기출)', 'type': 'classification',
         'target': 'churn', 'target_desc': '해지 여부 (0: 유지, 1: 해지)', 'id_col': 'customer_id',
         'scenario': '당신은 통신사의 데이터 분석가입니다. 고객 데이터를 분석하여 서비스 해지 여부를 예측하는 모델을 구축하세요. 이 모델은 이탈 위험 고객을 사전에 식별하여 유지 전략을 수립하는 데 활용됩니다.'},
        
        {'num': '23', 'name': 'usedcar', 'title': '중고차 가격 예측', 'type': 'regression',
         'target': 'price', 'target_desc': '가격 (달러)', 'id_col': 'car_id',
         'scenario': '당신은 중고차 거래 플랫폼의 데이터 분석가입니다. 차량 데이터를 분석하여 적정 가격을 예측하는 모델을 구축하세요.'},
        
        {'num': '24', 'name': 'quality', 'title': '제품 품질 예측', 'type': 'regression',
         'target': 'quality_score', 'target_desc': '품질 점수', 'id_col': 'batch_id',
         'scenario': '당신은 제조업체의 데이터 분석가입니다. 생산 데이터를 분석하여 제품 품질을 예측하는 모델을 구축하세요.'},
        
        {'num': '25', 'name': 'subscription', 'title': '구독 서비스 유지 예측', 'type': 'classification',
         'target': 'retained', 'target_desc': '유지 여부 (0: 해지, 1: 유지)', 'id_col': 'user_id',
         'scenario': '당신은 구독 서비스 회사의 데이터 분석가입니다. 사용자 데이터를 분석하여 구독 유지를 예측하는 모델을 구축하세요.'},
        
        {'num': '26', 'name': 'logistics', 'title': '물류 배송시간 예측', 'type': 'regression',
         'target': 'delivery_hours', 'target_desc': '배송시간 (시간)', 'id_col': 'shipment_id',
         'scenario': '당신은 물류회사의 데이터 분석가입니다. 배송 데이터를 분석하여 배송시간을 예측하는 모델을 구축하세요.'},
        
        {'num': '27', 'name': 'marketing', 'title': '마케팅 반응 예측', 'type': 'classification',
         'target': 'responded', 'target_desc': '반응 여부 (0: 무반응, 1: 반응)', 'id_col': 'customer_id',
         'scenario': '당신은 마케팅 회사의 데이터 분석가입니다. 고객 데이터를 분석하여 캠페인 반응을 예측하는 모델을 구축하세요.'},
        
        {'num': '28', 'name': 'production', 'title': '생산량 예측', 'type': 'regression',
         'target': 'production_units', 'target_desc': '생산량 (개)', 'id_col': 'shift_id',
         'scenario': '당신은 제조공장의 데이터 분석가입니다. 생산 데이터를 분석하여 생산량을 예측하는 모델을 구축하세요.'},
        
        {'num': '29', 'name': 'final_reg', 'title': '최종 모의고사 (회귀)', 'type': 'regression',
         'target': 'target', 'target_desc': '타겟 값', 'id_col': 'id',
         'scenario': '이것은 AICE Associate 최종 모의고사입니다. 주어진 데이터를 분석하여 타겟 값을 예측하는 머신러닝 모델을 구축하세요. 실제 시험과 동일한 환경에서 90분 내에 완료하세요.'},
        
        {'num': '30', 'name': 'final_clf', 'title': '최종 모의고사 (분류)', 'type': 'classification',
         'target': 'target', 'target_desc': '타겟 클래스', 'id_col': 'id',
         'scenario': '이것은 AICE Associate 최종 모의고사입니다. 주어진 데이터를 분석하여 타겟 클래스를 예측하는 머신러닝 모델을 구축하세요. 실제 시험과 동일한 환경에서 90분 내에 완료하세요.'},
    ],
}


import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, accuracy_score

NB_META = {
    "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
    "language_info": {"name": "python", "version": "3.8.0"},
}

NOTICE = """#### **<span style="color:red">[유의사항]</span>**
- <span style="color:darkgreen">각 문항의 답안은 반드시 *'#여기에 답안코드를 작성하고 실행하세요' , ‘#여기에 답안을 입력하세요’* 등이 표시된 셀(cell)에 입력해야 합니다</span>
- <span style="color:darkgreen">제공된 시험문항 셀을 삭제하거나 답안 위치가 아닌 다른 셀에 답안코드를 작성 시 채점되지 않습니다</span>
- 답안 작성 전에 문항에 제시된 가이드를 확인하세요
- 문항에 변수명이 제시된 경우 반드시 해당 변수명을 사용하세요
- 오픈북은 허용된 사이트만 참고 가능합니다 (numpy / pandas / matplotlib / seaborn / scikit-learn / tensorflow / xgboost)
---"""

IMPORT_HELPER = """import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['axes.unicode_minus'] = False
try:
    plt.rcParams['font.family'] = 'Malgun Gothic'
except Exception:
    pass
print('imports ok')"""

TF_HELPER = """import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical

tf.random.set_seed(1)"""


def lines(text: str):
    if text == "":
        return []
    if not text.endswith("\n"):
        text += "\n"
    parts = text.split("\n")
    out = []
    for i, part in enumerate(parts):
        if i == len(parts) - 1:
            if part:
                out.append(part)
        else:
            out.append(part + "\n")
    return out


def md(text: str):
    return {"cell_type": "markdown", "metadata": {}, "source": lines(text)}


def code(text: str):
    return {
        "cell_type": "code",
        "metadata": {},
        "source": lines(text),
        "execution_count": None,
        "outputs": [],
    }


def is_cat(s: pd.Series) -> bool:
    return not pd.api.types.is_numeric_dtype(s)


def analyze(exam: dict) -> dict:
    data_file = f"mock_{exam['num']}_{exam['name']}.csv"
    csv_path = os.path.join(BASE_DIR, "data", data_file)
    df = pd.read_csv(csv_path)
    target = exam["target"]
    id_col = exam["id_col"]
    is_reg = exam["type"] == "regression"
    df_name = "df" if is_reg else "data"
    temp_name = "df_temp" if is_reg else "data_temp"
    na_name = "df_na" if is_reg else "data_na"
    preset_name = "df_preset" if is_reg else "data_preset"

    drop = {target}
    if id_col:
        drop.add(id_col)
    cat_cols = [c for c in df.columns if c not in drop and is_cat(df[c])]
    num_cols = [c for c in df.columns if c not in drop and pd.api.types.is_numeric_dtype(df[c])]
    dummy_cols = [c for c in cat_cols if df[c].nunique(dropna=True) <= 20]
    high_card = [c for c in cat_cols if df[c].nunique(dropna=True) > 20]
    if not dummy_cols:
        dummy_cols = [c for c in num_cols if 2 <= df[c].nunique(dropna=True) <= 12][:1]
    plot_cat = dummy_cols[0] if dummy_cols else num_cols[0]
    if len(num_cols) >= 2:
        joint_x, joint_y = num_cols[0], num_cols[1]
    elif num_cols:
        joint_x, joint_y = num_cols[0], target
    else:
        joint_x, joint_y = plot_cat, target
    outlier_col = num_cols[0] if num_cols else (joint_x if joint_x != target else list(df.columns)[0])
    box_y = num_cols[0] if num_cols else joint_x

    top_cat = str(df[plot_cat].value_counts().index[0])

    work = df.copy()
    q1 = work[outlier_col].quantile(0.25)
    q3 = work[outlier_col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    work = work.drop(work[(work[outlier_col] > upper) | (work[outlier_col] < lower)].index)
    if id_col and id_col in work.columns:
        work = work.drop(columns=[id_col])
    for c in high_card:
        if c in work.columns:
            work = work.drop(columns=[c])
    missing = int(work.isnull().sum().sum())
    work = work.dropna()
    if dummy_cols:
        work = pd.get_dummies(work, columns=[c for c in dummy_cols if c in work.columns], drop_first=not is_reg)
    X = work.drop(columns=[target])
    y = work[target]
    X = X.select_dtypes(include=[np.number])
    n_classes = int(y.nunique())
    test_size = 0.2 if is_reg else 0.3
    random_state = 42 if is_reg else 7
    split_kw = dict(test_size=test_size, random_state=random_state)
    if not is_reg:
        split_kw["stratify"] = y
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, **split_kw)
    scaler = RobustScaler() if is_reg else StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_valid_s = scaler.transform(X_valid)
    scaler_max = int(round(float(np.max(X_valid_s))))
    if is_reg:
        dt = DecisionTreeRegressor(max_depth=5, min_samples_split=3, random_state=120)
        rf = RandomForestRegressor(max_depth=5, min_samples_split=3, random_state=120)
        dt.fit(X_train_s, y_train)
        rf.fit(X_train_s, y_train)
        dt_score = mean_absolute_error(y_valid, dt.predict(X_valid_s))
        rf_score = mean_absolute_error(y_valid, rf.predict(X_valid_s))
        better = "RandomForest" if rf_score <= dt_score else "DecisionTree"
    else:
        dt = DecisionTreeClassifier(max_depth=5, min_samples_split=3, random_state=120)
        rf = RandomForestClassifier(max_depth=5, min_samples_split=3, random_state=120)
        dt.fit(X_train_s, y_train)
        rf.fit(X_train_s, y_train)
        dt_score = accuracy_score(y_valid, dt.predict(X_valid_s))
        rf_score = accuracy_score(y_valid, rf.predict(X_valid_s))
        better = "RandomForest" if rf_score >= dt_score else "DecisionTree"
    fi = pd.DataFrame({"feature": X.columns, "importance": rf.feature_importances_}).sort_values(
        "importance", ascending=False
    )
    top_feat = str(fi.iloc[0]["feature"])

    dummy_list = ", ".join([f"'{c}'" for c in dummy_cols]) if dummy_cols else ""
    return {
        "data_file": data_file,
        "data_path": f"../data/{data_file}",
        "is_reg": is_reg,
        "df_name": df_name,
        "temp_name": temp_name,
        "na_name": na_name,
        "preset_name": preset_name,
        "target": target,
        "id_col": id_col,
        "plot_cat": plot_cat,
        "joint_x": joint_x,
        "joint_y": joint_y,
        "outlier_col": outlier_col,
        "box_y": box_y,
        "dummy_cols": dummy_cols,
        "dummy_list": dummy_list,
        "high_card": high_card,
        "top_cat": top_cat,
        "missing": missing,
        "scaler_name": "RobustScaler" if is_reg else "StandardScaler",
        "scaler_var": "rs" if is_reg else "ss",
        "scaler_max": scaler_max,
        "top_feat": top_feat,
        "better": better,
        "test_size": test_size,
        "random_state": random_state,
        "n_classes": n_classes,
        "columns": list(df.columns),
    }


def blank(label: str, ans: str = "", solution: bool = False) -> str:
    body = f"\n{ans}" if solution and ans != "" else ""
    return f"# ({label}) 여기에 답안을 입력하세요(실행 불필요)\n{body}"


def write_code(label: str) -> str:
    return f"# ({label}) 여기에 답안코드를 작성하고 실행하세요\n"


def save_nb(path: Path, cells):
    nb = {"nbformat": 4, "nbformat_minor": 4, "metadata": NB_META, "cells": cells}
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")


def col_desc(meta: dict) -> str:
    rows = [f"- {c}" for c in meta["columns"]]
    return f"**[ 데이터 컬럼 설명 (데이터 파일명: {meta['data_file']}) ]**\n\n" + "\n".join(rows)


def build_cells(exam: dict, meta: dict, solution: bool):
    is_reg = meta["is_reg"]
    df = meta["df_name"]
    temp = meta["temp_name"]
    na = meta["na_name"]
    preset = meta["preset_name"]
    target = meta["target"]
    plot_cat = meta["plot_cat"]
    kind = "회귀" if is_reg else "분류"
    cells = [
        md(f"**AICE Associate <font color=red>모의고사 {exam['num']}</font> — {kind}**"),
        md(f"### **{exam['title']}**\n---\n\n{exam['scenario']}\n\n- 타겟 : `{target}` ({exam['target_desc']})\n\n---"),
        md(NOTICE),
        md(col_desc(meta)),
        md("**배점:** 데이터 분석 20점 · 데이터 전처리 30점 · AI 모델링 50점 (총 14문항 / 100점)\n\nCSV는 `../data/` 에 있습니다. 90분 안에 푸세요."),
        md("## <font color=blue>**<데이터 분석 (20점)>**</font>"),
    ]

    if is_reg:
        cells += [
            md("### **1. pandas는 데이터 분석에 널리 사용되는 파이썬 라이브러리입니다.**\n### **pandas를 사용할 수 있게 별칭(alias)을 pd로 해서 불러오세요.**\n---"),
            code(write_code("1") + ("\nimport pandas as pd" if solution else "")),
            md("### **2. pandas로 데이터 파일을 읽어온 뒤, 데이터프레임 변수명 df에 할당하고 첫 4개 행을 출력하세요.**\n* **\n- 데이터프레임 변수명 : df\n- 데이터 파일명 : `" + meta["data_file"] + "`\n---"),
            code(write_code("2") + (f"\ndf = pd.read_csv('{meta['data_path']}')\ndf.head(4)" if solution else "")),
        ]
    else:
        cells += [
            md("### **1. scikit-learn은 머신러닝에 널리 사용되는 파이썬 라이브러리입니다.**\n### **scikit-learn을 사용할 수 있게 별칭(alias)을 sk로 해서 불러오세요.**\n---"),
            code(write_code("1") + ("\nimport sklearn as sk" if solution else "")),
            md("### **2. pandas로 데이터 파일을 읽어온 뒤, 데이터프레임 변수명 data에 할당하고 첫 4개 행을 출력하세요.**\n* **\n- 데이터프레임 변수명 : data\n- 데이터 파일명 : `" + meta["data_file"] + "`\n---"),
            code(write_code("2") + (f"\nimport pandas as pd\n\ndata = pd.read_csv('{meta['data_path']}')\ndata.head(4)" if solution else "")),
        ]

    cells += [
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code(IMPORT_HELPER),
        md(f"### **3. 시각화를 통해 `{plot_cat}` 의 분포를 파악하려 합니다.**"),
        md(f"* **\n- **(3-1)** seaborn countplot으로 `{plot_cat}` 분포를 그리세요\n- **(3-2)** 그래프에서 가장 많은 값은 무엇입니까?\n-----"),
        code(write_code("3-1") + (f"\nsns.countplot(data={df}, x='{plot_cat}')" if solution else "")),
        code(blank("3-2", meta["top_cat"], solution)),
    ]

    if is_reg:
        cells += [
            md(f"### **4. `{meta['joint_x']}` 와 `{meta['joint_y']}` 의 분포와 관계를 jointplot으로 시각화하세요.**"),
            md(f"* **\n- 대상 데이터프레임 : {df}\n- X축 `{meta['joint_x']}`, Y축 `{meta['joint_y']}`\n---"),
            code(write_code("4") + (f"\nsns.jointplot(data={df}, x='{meta['joint_x']}', y='{meta['joint_y']}')" if solution else "")),
        ]
    else:
        cells += [
            md(f"### **4. `{target}` 별 `{meta['box_y']}` 분포를 boxplot으로 시각화하세요.**"),
            md(f"* **\n- 대상 데이터프레임 : {df}\n- X축 `{target}`, Y축 `{meta['box_y']}`\n---"),
            code(write_code("4") + (f"\nsns.boxplot(data={df}, x='{target}', y='{meta['box_y']}')" if solution else "")),
        ]

    drop_id = ""
    drop_id_sol = ""
    if meta["id_col"]:
        drop_id = f"\n{temp} = {temp}.<#5-1>( columns=['{meta['id_col']}'])"
        drop_id_sol = f"\n{temp} = {temp}.drop(columns=['{meta['id_col']}'])"
    q5_blank = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

q1 = {df}['{meta['outlier_col']}'].quantile(0.25)
q3 = {df}['{meta['outlier_col']}'].quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

{temp} = {df}.<#5-1>( {df}[({df}['{meta['outlier_col']}'] > upper_fence) | ({df}['{meta['outlier_col']}'] < lower_fence)].<#5-2>){drop_id}
{temp}.reset_index(drop=True, inplace=True)"""
    q5_sol = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

q1 = {df}['{meta['outlier_col']}'].quantile(0.25)
q3 = {df}['{meta['outlier_col']}'].quantile(0.75)
iqr = q3 - q1
lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

{temp} = {df}.drop( {df}[({df}['{meta['outlier_col']}'] > upper_fence) | ({df}['{meta['outlier_col']}'] < lower_fence)].index){drop_id_sol}
{temp}.reset_index(drop=True, inplace=True)"""

    q6_bug = f"""# (6-1) 여기에 코드의 오류를 정정하고 실행하세요

print( '결측치 처리전\\n', {temp}.isnull().sum() )
{na} = {temp}.drop()
print( '\\n결측치 처리후\\n', {na}.isnull().total() )"""
    q6_sol = f"""# (6-1) 여기에 코드의 오류를 정정하고 실행하세요

print( '결측치 처리전\\n', {temp}.isnull().sum() )
{na} = {temp}.dropna()
print( '\\n결측치 처리후\\n', {na}.isnull().sum() )"""

    dummy_arg = f"[{meta['dummy_list']}]" if meta["dummy_list"] else None
    extra_drop = ""
    extra_drop_sol = ""
    if meta["high_card"]:
        cols = ", ".join([f"'{c}'" for c in meta["high_card"]])
        extra_drop = f"{na}.drop( [{cols}] , axis=1, inplace=True)\n"
        extra_drop_sol = extra_drop
    if dummy_arg:
        q7_blank = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

{extra_drop}{preset} = pd. <#7-1> (data={na}, <#7-2>={dummy_arg} )
{preset}.info()"""
        q7_sol = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

{extra_drop_sol}{preset} = pd.get_dummies(data={na}, columns={dummy_arg} )
{preset}.info()"""
    else:
        q7_blank = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

{preset} = pd. <#7-1> (data={na} )
{preset}.info()"""
        q7_sol = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

{preset} = pd.get_dummies(data={na} )
{preset}.info()"""

    split_extra = ", stratify=y" if not is_reg else ""
    q8_sol = f"""
X = {preset}.drop('{target}', axis=1)
y = {preset}['{target}']

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size={meta['test_size']}, random_state={meta['random_state']}{split_extra})"""

    svar, sname = meta["scaler_var"], meta["scaler_name"]
    q9_bug = f"""# (9-1) 여기에 코드의 오류를 정정하고 실행하세요

from sklearn.preprocessing import {sname}
{svar} = {sname}()
X_train = {svar}.transform(X_train)
X_valid = {svar}.transform(X_train)
round(np.max(X_valid))"""
    q9_sol = f"""# (9-1) 여기에 코드의 오류를 정정하고 실행하세요

from sklearn.preprocessing import {sname}
{svar} = {sname}()
X_train = {svar}.fit_transform(X_train)
X_valid = {svar}.transform(X_valid)
round(np.max(X_valid))"""

    if is_reg:
        q10_1_sol = """
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(max_depth=5, min_samples_split=3, random_state=120)
dt.fit(X_train, y_train)"""
        q10_2_sol = """
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=5, min_samples_split=3, random_state=120)
rf.fit(X_train, y_train)"""
        metric = "MAE"
        metric_import = "mean_absolute_error"
        q12_bug = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

y_pred_dt = dt.predict(X_valid)
y_pred_rf = rf.predict(X_train)

from sklearn_metrics import mean.absolute

dt_mae = mean.absolute(y_valid, y_pred_rf)
rf_mae = mean.absolute(y_valid, y_pred_rf)
info(dt_mae, rf_mae)"""
        q12_sol = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

y_pred_dt = dt.predict(X_valid)
y_pred_rf = rf.predict(X_valid)

from sklearn.metrics import mean_absolute_error

dt_mae = mean_absolute_error(y_valid, y_pred_dt)
rf_mae = mean_absolute_error(y_valid, y_pred_rf)
print(dt_mae, rf_mae)"""
        better_q = "MAE가 더 작은 모델은 무엇입니까?"
        keras_act, keras_last, keras_loss, keras_metric, patience = "selu", "linear", "mean_squared_error", "mse", 9
        last_units = 1
        hist_key = "mse"
        plot_title = "Model MSE"
        legend = "['mse', 'val_mse']"
    else:
        q10_1_sol = """
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(max_depth=5, min_samples_split=3, random_state=120)
dt.fit(X_train, y_train)"""
        q10_2_sol = """
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(max_depth=5, min_samples_split=3, random_state=120)
rf.fit(X_train, y_train)"""
        metric = "Accuracy"
        q12_bug = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

y_pred_dt = dt.predict(X_valid)
y_pred_rf = rf.predict(X_train)

from sklearn_metrics import accuracy

dt_acc = accuracy(y_valid, y_pred_rf)
rf_acc = accuracy(y_valid, y_pred_rf)
info(dt_acc, rf_acc)"""
        q12_sol = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

y_pred_dt = dt.predict(X_valid)
y_pred_rf = rf.predict(X_valid)

from sklearn.metrics import accuracy_score

dt_acc = accuracy_score(y_valid, y_pred_dt)
rf_acc = accuracy_score(y_valid, y_pred_rf)
print(dt_acc, rf_acc)"""
        better_q = "Accuracy가 더 높은 모델은 무엇입니까?"
        n_classes = meta["n_classes"]
        if n_classes <= 2:
            keras_act, keras_last, keras_loss, keras_metric, patience = "relu", "sigmoid", "binary_crossentropy", "accuracy", 14
            last_units = 2
            hist_key = "accuracy"
        else:
            keras_act, keras_last, keras_loss, keras_metric, patience = "relu", "softmax", "categorical_crossentropy", "accuracy", 14
            last_units = n_classes
            hist_key = "accuracy"
        plot_title = "Model Accuracy"
        legend = "['acc', 'val_acc']"

    q11_bug = """# (11-1) 여기에 코드의 오류를 정정하고 실행하세요

fi = pd.DataFrame({'feature': X.columns, 'importance': rf.importances})
fi = fi.sort_index('importance', ascending=False)[:10]
sns.barplot(x='importance', y='feature', data=fi, palette='viridis')"""
    q11_sol = """# (11-1) 여기에 코드의 오류를 정정하고 실행하세요

fi = pd.DataFrame({'feature': X.columns, 'importance': rf.feature_importances_})
fi = fi.sort_values('importance', ascending=False)[:10]
sns.barplot(x='importance', y='feature', data=fi, palette='viridis')"""

    if is_reg:
        q13_sol = f"""# (13) 여기에 답안코드를 작성하고 실행하세요

model = Sequential()
model.add(Dense(64, activation='{keras_act}', input_dim=X.shape[1]))
model.add(Dropout(0.1))
model.add(Dense(32, activation='{keras_act}'))
model.add(Dense(16, activation='{keras_act}'))
model.add(Dense({last_units}, activation='{keras_last}'))

estop = EarlyStopping(monitor='val_loss', patience={patience})
model.compile(optimizer='adam', loss='{keras_loss}', metrics=['{keras_metric}'])

history = model.fit(X_train, y_train, batch_size=128, epochs=50,
                    validation_data=(X_valid, y_valid), callbacks=[estop])"""
        q13_blank = write_code("13")
        q14_blank = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

plt.plot(<#14-1>["{hist_key}"])
plt.plot(<#14-1>["val_{hist_key}"])
plt.title("{plot_title}")
plt.xlabel("Epoch")
plt.ylabel("{hist_key.upper() if is_reg else 'Accuracy'}")
plt.<#14-2>({legend})
plt.show()"""
        q14_sol = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

plt.plot(history.history["{hist_key}"])
plt.plot(history.history["val_{hist_key}"])
plt.title("{plot_title}")
plt.xlabel("Epoch")
plt.ylabel("{hist_key.upper() if is_reg else 'Accuracy'}")
plt.legend({legend})
plt.show()"""
    else:
        q13_sol = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

from sklearn.preprocessing import LabelEncoder

model = Sequential([
    Dense(128, activation='{keras_act}', input_dim=X_train.shape[1]),
    Dropout(0.3),
    Dense(64, activation='{keras_act}'),
    Dense(32, activation='{keras_act}'),
    Dense({last_units}, activation='{keras_last}')
])

estop = EarlyStopping(monitor='val_loss', patience={patience}, restore_best_weights=True)
model.compile(optimizer='adam', loss='{keras_loss}', metrics=['{keras_metric}'])

le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_valid = le.transform(y_valid)
y_train = to_categorical(y_train)
y_valid = to_categorical(y_valid)

history = model.fit(X_train, y_train, epochs=50, batch_size=128,
                    validation_data=(X_valid, y_valid), callbacks=[estop])"""
        q13_blank = f"""# (코드 셀) 코드의 빈칸을 채우고 실행하세요

from sklearn.preprocessing import LabelEncoder

model = Sequential([
    <#13-1>
])

estop = EarlyStopping(monitor='val_loss', <#13-2>={patience}, restore_best_weights=True)
model.compile(optimizer='adam', loss='{keras_loss}', metrics=['{keras_metric}'])

le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_valid = le.transform(y_valid)
y_train = to_categorical(y_train)
y_valid = to_categorical(y_valid)

history = model.fit(X_train, y_train, epochs=50, batch_size=128,
                    validation_data=(X_valid, y_valid), callbacks=[estop])"""
        q14_blank = write_code("14")
        q14_sol = f"""# (14) 여기에 답안코드를 작성하고 실행하세요

plt.plot(history.history["{hist_key}"])
plt.plot(history.history["val_{hist_key}"])
plt.title("{plot_title}")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend({legend})
plt.show()"""

    strat_txt = "  - 분류이므로 레이블 비율을 유지하는 옵션을 설정하세요.\n" if not is_reg else ""
    cells += [
        md("## <font color=blue>**<데이터 전처리 (30점)>**</font>"),
        md(f"### **5. `{meta['outlier_col']}` 이상치를 IQR 펜스 기준으로 제거하고, 불필요 컬럼을 삭제하세요.**\n* **\n- 대상 : {df}\n- upperfence보다 크거나 lowerfence보다 작은 행을 삭제하세요\n- 전처리 결과는 `{temp}` 에 저장하세요\n- 빈칸 (#5-1, #5-2)을 채우세요\n---"),
        code(q5_sol if solution else q5_blank),
        code(blank("5-1", "drop", solution)),
        code(blank("5-2", "index", solution)),
        md(f"### **6. 결측치를 확인하고 처리하세요.**\n* **\n- **(6-1)** 오류를 정정하세요. `{temp}` 에서 결측 행을 삭제한 뒤 `{na}` 에 저장하세요\n- **(6-2)** `{temp}` 의 결측치 개수는 총 몇 개인가요?\n---"),
        code(q6_sol if solution else q6_bug),
        code(blank("6-2", str(meta["missing"]), solution)),
        md("### **7. 원-핫 인코딩으로 범주형 컬럼을 변환하세요.**\n* **\n- 결과는 `" + preset + "` 에 저장하고 info로 확인하세요\n- 빈칸 (#7-1, #7-2)을 채우세요\n---"),
        code(q7_sol if solution else q7_blank),
        code(blank("7-1", "get_dummies", solution)),
        code(blank("7-2", "columns" if meta["dummy_list"] else "get_dummies", solution)),
        md(f"### **8. `{target}` 을 y로, 나머지를 X로 나눈 뒤 훈련/검증을 분리하세요.**\n* **\n- X_train, X_valid, y_train, y_valid\n- 비율은 훈련 {int((1-meta['test_size'])*100)} : 검증 {int(meta['test_size']*100)}\n- 난수 시드 : {meta['random_state']}\n{strat_txt}---"),
        code(write_code("8") + (q8_sol if solution else "")),
        md(f"### **9. {sname} 로 스케일링하세요.**\n* **\n- **(9-1)** 오류를 정정하세요 (train은 fit_transform, valid는 transform)\n- **(9-2)** 스케일링된 검증데이터 최댓값을 반올림한 결과는?\n----"),
        code(q9_sol if solution else q9_bug),
        code(blank("9-2", str(meta["scaler_max"]), solution)),
        md("## <font color=blue>**<AI 모델링(50점)>**</font>"),
        md("### **10. DecisionTree와 RandomForest 모델을 학습하세요.**\n* **\n- max_depth=5, min_samples_split=3, random_state=120\n- 변수명 dt, rf\n---"),
        code(write_code("10-1") + (q10_1_sol if solution else "")),
        code(write_code("10-2") + (q10_2_sol if solution else "")),
        md("### **11. RandomForest 변수중요도 Top 10을 시각화하세요.**\n* **\n- **(11-1)** 오류를 정정하세요\n- **(11-2)** 가장 중요한 변수명은?\n---"),
        code(q11_sol if solution else q11_bug),
        code(blank("11-2", meta["top_feat"], solution)),
        md(f"### **12. 두 모델의 {metric}를 비교하세요.**\n* **\n- **(12-1)** 오류를 정정하세요 (검증데이터 사용)\n- **(12-2)** {better_q}\n---"),
        code(q12_sol if solution else q12_bug),
        code(blank("12-2", meta["better"], solution)),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code(TF_HELPER),
        md(f"### **13. Keras Sequential로 딥러닝 모델을 만드세요.**\n* **\n- 히든 activation: `{keras_act}`, 출력: `{keras_last}`\n- EarlyStopping patience={patience}, monitor=val_loss, 변수명 estop\n- optimizer=adam, loss=`{keras_loss}`, metrics=`{keras_metric}`\n- batch_size=128, epochs=50, history 변수에 학습 기록 저장\n---"),
        code(q13_sol if solution else q13_blank),
    ]
    if not is_reg:
        cells.append(code(blank("13-1", f"Dense(128, activation='{keras_act}', input_dim=X_train.shape[1]), Dropout(0.3), Dense(64), Dense(32), Dense({last_units}, activation='{keras_last}')", solution)))
        cells.append(code(blank("13-2", "patience", solution)))
    cells += [
        md(f"### **14. 학습/검증 {hist_key} 변화를 그래프로 그리세요.**\n* **\n- 범례 {legend}, 제목 `{plot_title}`\n---"),
        code(q14_sol if solution else q14_blank),
    ]
    if is_reg:
        cells.append(code(blank("14-1", "history.history", solution)))
        cells.append(code(blank("14-2", "legend", solution)))
    cells.append(md("### **모든 문항이 완료되었습니다.**\n채점은 `*_solution.ipynb` 또는 `mock_exams/answer_keys.md` 를 참고하세요."))
    return cells


def generate_all_notebooks():
    print("=" * 60)
    print("Generating official-format mock exams (14 questions)")
    print("=" * 60)
    keys = ["# 모의고사 단답/빈칸 정답 (공식 샘플 형식)\n"]
    for level, exams in MOCK_EXAMS.items():
        level_dir = os.path.join(BASE_DIR, level)
        os.makedirs(level_dir, exist_ok=True)
        print(f"\n[{level}]")
        keys.append(f"\n## {level}\n")
        keys.append("| 회차 | 3-2 | 6-2 결측 | 9-2 scaler max | 11-2 중요변수 | 12-2 우수모델 |\n|------|------|----------|----------------|---------------|---------------|\n")
        for exam in exams:
            meta = analyze(exam)
            base = f"mock_{exam['num']}_{exam['name']}"
            save_nb(Path(level_dir) / f"{base}.ipynb", build_cells(exam, meta, False))
            save_nb(Path(level_dir) / f"{base}_solution.ipynb", build_cells(exam, meta, True))
            print(f"  [OK] {base}.ipynb + _solution.ipynb")
            keys.append(
                f"| {exam['num']} {exam['title']} | {meta['top_cat']} | {meta['missing']} | {meta['scaler_max']} | `{meta['top_feat']}` | {meta['better']} |\n"
            )
    Path(BASE_DIR, "answer_keys.md").write_text("".join(keys), encoding="utf-8")
    print("\nWrote mock_exams/answer_keys.md")
    print("All 30 problem + solution notebooks generated.")


if __name__ == "__main__":
    generate_all_notebooks()
