#!/usr/bin/env python3
"""Generate AICE Associate official sample problem/solution notebooks."""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
NB_META = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {"name": "python", "version": "3.8.0"},
}


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


def save(path: Path, cells):
    nb = {"nbformat": 4, "nbformat_minor": 4, "metadata": NB_META, "cells": cells}
    path.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {path} ({len(cells)} cells)")


NOTICE = """#### **<span style="color:red">[유의사항]</span>**
- <span style="color:darkgreen">각 문항의 답안은 반드시 *'#여기에 답안코드를 작성하고 실행하세요' , ‘#여기에 답안을 입력하세요’* 등이 표시된 셀(cell)에 입력해야 합니다</span>
- <span style="color:darkgreen">제공된 시험문항 셀을 삭제하거나 답안 위치가 아닌 다른 셀에 답안코드를 작성 시 채점되지 않습니다</span>
- 답안 작성 전에 문항에 제시된 가이드를 확인하세요
- 문항에 변수명이 제시된 경우 반드시 해당 변수명을 사용하세요
- 시험 중에는 상단의 '임시저장' 버튼을 수시로 클릭해 저장해주시고, 답안 제출시에는 '최종제출' 버튼을 클릭해주시기 바랍니다
- 오픈북은 허용된 사이트만 참고 가능합니다 (numpy / pandas / matplotlib / seaborn / scikit-learn / tensorflow / xgboost)
---"""

FONT_HELPER = """import numpy as np
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
plt.rcParams['axes.unicode_minus'] = False"""

TF_HELPER = """import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical

tf.random.set_seed(1)"""


def blank(label: str) -> str:
    return f"# ({label}) 여기에 답안을 입력하세요(실행 불필요)\n"


def write_code(label: str) -> str:
    return f"# ({label}) 여기에 답안코드를 작성하고 실행하세요\n"


def fix_code(label: str) -> str:
    return f"# ({label}) 여기에 코드의 오류를 정정하고 실행하세요\n"


def fill_code() -> str:
    return "# (코드 셀) 코드의 빈칸을 채우고 실행하세요\n"


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------

CLF_Q3_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

fig, axes = plt.<#3-1>(nrows=1, ncols=2, figsize=(15, 6))

sns.countplot(data=data, x='E_FE_wine_kind', ax=<#3-2>[0])
sns.histplot(data=data, x='FE_points_winery', hue='Grade', ax=<#3-2>[1])

plt.setp(<#3-2>[0].get_xticklabels(), rotation=45, ha='right')

<#3-2>[0].<#3-3>('Wine Count')
<#3-2>[1].<#3-3>('Winery Score')

plt.show()"""

CLF_Q3_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

sns.countplot(data=data, x='E_FE_wine_kind', ax=axes[0])
sns.histplot(data=data, x='FE_points_winery', hue='Grade', ax=axes[1])

plt.setp(axes[0].get_xticklabels(), rotation=45, ha='right')

axes[0].set_title('Wine Count')
axes[1].set_title('Winery Score')

plt.show()"""

CLF_Q5_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

q1 = data['FE_points_winery'].quantile(0.25)
q3 = data['FE_points_winery'].quantile(0.75)
iqr = q3 - q1

lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

data_temp = data.<#5-1>( data[(data['FE_points_winery'] > upper_fence) | (data['FE_points_winery'] < lower_fence)].<#5-2>)
data_temp = data_temp.<#5-1>( columns=['E_title'])
data_temp.reset_index(drop=True, inplace=True)"""

CLF_Q5_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

q1 = data['FE_points_winery'].quantile(0.25)
q3 = data['FE_points_winery'].quantile(0.75)
iqr = q3 - q1

lower_fence = q1 - 1.5 * iqr
upper_fence = q3 + 1.5 * iqr

# pandas 2.x: drop(index=...) 와 drop(columns=...) 를 함께 쓰지 않습니다.
# 시험 빈칸 답은 그대로 drop / index 입니다.
data_temp = data.drop(data[(data['FE_points_winery'] > upper_fence) | (data['FE_points_winery'] < lower_fence)].index)
data_temp = data_temp.drop(columns=['E_title'])
data_temp.reset_index(drop=True, inplace=True)"""

CLF_Q6_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

print( '결측치 처리 전\\n', data_temp.<#6-1>().sum() )
data_na = data_temp.<#6-2>()
print( '결측치 처리 후\\n', data_na.<#6-1>().sum() )"""

CLF_Q6_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

print( '결측치 처리 전\\n', data_temp.isnull().sum() )
data_na = data_temp.dropna()
print( '결측치 처리 후\\n', data_na.isnull().sum() )"""

CLF_Q7_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

data_na.loc[data_na['E_FE_wine_kind'].<#7-1>(['white|rose|sparkling','red|white|sparkling', 'red|white|rose|sparkling',
                                                                               'red|sparkling']), ['E_FE_wine_kind']] = 'sparkling'
data_na.loc[data_na['E_FE_wine_kind'].<#7-1>(['white|sparkling']), ['E_FE_wine_kind']] = 'white'
data_na.loc[data_na['E_FE_wine_kind'].<#7-1>(['red|rose', 'red|white', 'red|rose|sparkling']), ['E_FE_wine_kind']] = 'red'

print(data_na['E_FE_wine_kind'].<#7-2>())"""

CLF_Q7_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

data_na.loc[data_na['E_FE_wine_kind'].isin(['white|rose|sparkling','red|white|sparkling', 'red|white|rose|sparkling',
                                                                               'red|sparkling']), ['E_FE_wine_kind']] = 'sparkling'
data_na.loc[data_na['E_FE_wine_kind'].isin(['white|sparkling']), ['E_FE_wine_kind']] = 'white'
data_na.loc[data_na['E_FE_wine_kind'].isin(['red|rose', 'red|white', 'red|rose|sparkling']), ['E_FE_wine_kind']] = 'red'

print(data_na['E_FE_wine_kind'].value_counts())"""

CLF_Q73_BUG = """# (7-3) 여기에 코드의 오류를 정정하고 실행하세요

data_na = data_na.drop( ['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety'], axis=0)
data_preset = pd.get_dummy(data = data_na, column = ['E_country', 'E_FE_wine_kind'], drop_first=True)
data_preset.info()"""

CLF_Q73_SOL = """# (7-3) 여기에 코드의 오류를 정정하고 실행하세요

data_na = data_na.drop( ['E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety'], axis=1)
data_preset = pd.get_dummies(data = data_na, columns = ['E_country', 'E_FE_wine_kind'], drop_first=True)
data_preset.info()"""

CLF_Q9_BUG = """# (9-1) 여기에 코드의 오류를 정정하고 실행하세요

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X_train = ss.transform(X_train)
X_valid = ss.transform(X_train)
round(np.max(X_valid))"""

CLF_Q9_SOL = """# (9-1) 여기에 코드의 오류를 정정하고 실행하세요

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_valid = ss.transform(X_valid)
round(np.max(X_valid))"""

CLF_Q11_BUG = """# (11-1) 여기에 코드의 오류를 정정하고 실행하세요

fi = pd.DataFrame({'feature': X.columns, 'importance': gs_rf.importances})
fi = fi.sort_index('importance', ascending=False)[:10]
sns.barplot(x='importance', y='feature', data=fi, palette='viridis')"""

CLF_Q11_SOL = """# (11-1) 여기에 코드의 오류를 정정하고 실행하세요

fi = pd.DataFrame({'feature': X.columns, 'importance': gs_rf.best_estimator_.feature_importances_})
fi = fi.sort_values('importance', ascending=False)[:10]
sns.barplot(x='importance', y='feature', data=fi, palette='viridis')"""

CLF_Q12_BUG = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

from sklearn_metrics import accuracy

y_pred_dt = gs_dt.predict(X_valid)
y_pred_rf = gs_rf.predict(X_train)

dt_acc = accuracy(y_valid, y_pred_rf)
rf_acc = accuracy(y_valid, y_pred_rf)

info(dt_acc, rf_acc)"""

CLF_Q12_SOL = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

from sklearn.metrics import accuracy_score

y_pred_dt = gs_dt.best_estimator_.predict(X_valid)
y_pred_rf = gs_rf.best_estimator_.predict(X_valid)

dt_acc = accuracy_score(y_valid, y_pred_dt)
rf_acc = accuracy_score(y_valid, y_pred_rf)

print(dt_acc, rf_acc)"""

CLF_Q13_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

from sklearn.preprocessing import LabelEncoder

model = Sequential([
    <#13-1>
])

estop = EarlyStopping(monitor='val_loss', <#13-2>=14, restore_best_weights=True)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_valid = le.transform(y_valid)

y_train= to_categorical(y_train)
y_valid = to_categorical(y_valid)

history = model.fit(X_train, y_train,
                     epochs=50,
                     batch_size=128,
                     validation_data=(X_valid, y_valid),
                     callbacks=[estop])"""

CLF_Q13_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

from sklearn.preprocessing import LabelEncoder

model = Sequential([
    Dense(128, activation='relu', input_dim=X_train.shape[1]),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dense(32, activation='relu'),
    Dense(2, activation='sigmoid')
])

estop = EarlyStopping(monitor='val_loss', patience=14, restore_best_weights=True)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

le = LabelEncoder()
y_train = le.fit_transform(y_train)
y_valid = le.transform(y_valid)

y_train= to_categorical(y_train)
y_valid = to_categorical(y_valid)

history = model.fit(X_train, y_train,
                     epochs=50,
                     batch_size=128,
                     validation_data=(X_valid, y_valid),
                     callbacks=[estop])"""

CLF_Q10_1 = """# (10-1) 여기에 답안코드를 작성하고 실행하세요

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

dt = DecisionTreeClassifier(random_state=7)

param_grid_dt = {
    "max_depth": [3, 5, 7, 10],
    "min_samples_split": [2, 3, 5, 10]
}

gs_dt = GridSearchCV(
    estimator=dt,
    param_grid=param_grid_dt,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

gs_dt.fit(X_train, y_train)"""

CLF_Q10_2 = """# (10-2) 여기에 답안코드를 작성하고 실행하세요

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=7)

param_grid_rf = {
    "n_estimators": [100, 200, 500],
    "max_depth": [5, 10, 20],
    "min_samples_split": [2, 5, 10]
}

gs_rf = GridSearchCV(
    estimator=rf,
    param_grid=param_grid_rf,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

gs_rf.fit(X_train, y_train)"""

CLF_Q14_SOL = """# (14) 여기에 답안코드를 작성하고 실행하세요

plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(['acc', 'val_acc'])
plt.show()"""


def clf_common_intro():
    return [
        md("**AICE Associate <font color=red>공식 샘플문항</font> — 분류**"),
        md("""### **와인 데이터를 활용한 <span style="color:darkgreen">와인 품질</span> 예측**
---

- 도메인 : 품질 관리(QC)
- 목  표 : 와인의 품질을 예측하는 인공지능모델 개발
- 와인 도매업체인 C사에서 수입하는 와인 품질이 경쟁사 와인 품질 대비 떨어진다는 평가를 받으며 매출이 감소하고 있다.
- 계속되는 매출 부진을 만회하기 위해, C사 품질관리팀장은 수십년간 축적된 공신력 있는 와인평론가의 와인 평가 데이터를 활용해서 '와인품질등급'을 예측하는 인공지능 모델을 도입하려고 한다.
- C사는 브랜드파워가 있기 때문에, 인공지능을 활용해서 '와인품질등급'의 정확도가 개선되어 고품질의 와인만 선별하여 수입하면 매출이 빠르게 회복될 것으로 기대하고 있다.

---"""),
        md(NOTICE),
        md("""**[ 데이터 컬럼 설명 (데이터 파일명: wine_quality_data.csv) ]**

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
- FE_points_winery   : 와이너리 평점
"""),
        md("""**배점:** 데이터 분석 20점 · 데이터 전처리 30점 · AI 모델링 50점 (총 14문항 / 100점)

이 노트북과 `wine_quality_data.csv`는 같은 폴더에서 실행하세요.
GridSearchCV(Q10)는 데이터가 약 9만 행이라 수 분이 걸릴 수 있습니다."""),
    ]


def build_clf(solution: bool):
    cells = clf_common_intro()
    if not solution:
        cells.append(md("""> 분류 샘플 원본은 **해설지**로 제공되어, 오류 정정 문항(7-3, 9-1, 11-1, 12-1)의 원본 오류 코드가 이미 수정된 상태였습니다.
> 문제 노트북의 해당 오류 코드는 **회귀 공식 샘플과 같은 시험 유형**으로 재구성했습니다. 정답은 `solution.ipynb` / `answer_key.md`를 참고하세요."""))

    cells += [
        md("## <font color=blue>**<데이터 분석 (20점)>**</font>"),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code(FONT_HELPER),
        md("""### **1. scikit-learn은 머신러닝에 널리 사용되는 파이썬 라이브러리입니다.**
### **scikit-learn을 사용할 수 있게 별칭(alias)을 sk로 해서 불러오세요.**
---"""),
        code(write_code("1") + ("\nimport sklearn as sk" if solution else "")),
        md("""### **2. AI 모델링을 위해 분석 및 처리할 데이터 파일을 읽어오려고 합니다.**
### **pandas로 데이터 파일을 읽어온 뒤, 데이터프레임 변수명 data 에 할당하고 첫 4개 행을 출력하세요.**

* **
- 데이터프레임 변수명 : data
- 데이터 파일명 : wine_quality_data.csv
    - csv 파일은 본 문제/답안지와 동일한 경로에 있습니다
---"""),
        code(
            write_code("2")
            + (
                "\nimport pandas as pd\n\ndata = pd.read_csv('./wine_quality_data.csv')\ndata.head(4)"
                if solution
                else ""
            )
        ),
        md("### **3. 시각화를 통해 와인종류(E_FE_wine_kind)와 와이너리 평점(FE_points_winery)의 분포를 파악하려 합니다.**"),
        md("""* **
- 대상 데이터프레임 : data
- 와인종류(E_FE_wine_kind)의 분포를 보여주는 countplot 그래프를 그리세요
- 와인등급(Grade) 별 와이너리 평점(FE_points_winery)의 분포를 보여주는 histplot 그래프를 그리세요
- subplots를 활용하여 두 그래프를 가로 방향으로 나란히 그리세요
- 두 그래프의 제목을 각각 'Wine Count'와 'Winery Score'로 설정하세요<br><br>
- <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
- <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#3-1, #3-2, #3-3)</font>
-----"""),
        code(CLF_Q3_SOL if solution else CLF_Q3_BLANK),
        code(blank("3-1") + ("\nsubplots" if solution else "")),
        code(blank("3-2") + ("\naxes" if solution else "")),
        code(blank("3-3") + ("\nset_title" if solution else "")),
        md("""### **4. 그래프를 통해 와인품질등급(Grade) 별 와이너리 평점(FE_points_winery) 컬럼의 분포를 확인하려 합니다.**
### **아래 가이드에 따라 boxplot으로 시각화하세요.**"""),
        md("""* **
- 대상 데이터프레임 : data
- seaborn의 boxplot으로 와이너리 평점(FE_points_winery) 컬럼의 분포를 그래프로 그리세요
- X축에는 와인품질등급(Grade)을, Y축에는 와이너리 평점(FE_points_winery)을 표시하세요
---"""),
        code(
            write_code("4")
            + ("\nsns.boxplot(data=data, x='Grade', y='FE_points_winery')" if solution else "")
        ),
        md("## <font color=blue>**<데이터 전처리 (30점)>**</font>"),
        md("""### **5. boxplot으로 확인한 결과, 와이너리 평점(FE_points_winery) 컬럼에서 이상치가 발견되었습니다. AI모델링할때 부정적 영향이 없도록 아래 가이드에 따라 이상치를 처리하세요.**
* **
- 대상 데이터프레임 : data
- 와이너리 평점이 upperfence 값보다 큰 이상치가 있는 행(row)을 삭제하세요
- 와이너리 평점이 lowerfence 값보다 작은 이상치가 있는 행(row)을 삭제하세요
- AI모델링에 불필요한 와인이름(E_title) 컬럼을 삭제하세요
- 전처리를 적용한 데이터프레임은 data_temp라는 변수명으로 저장하세요<br><br>
- <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
- <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#5-1, #5-2)</font>
---"""),
        code(CLF_Q5_SOL if solution else CLF_Q5_BLANK),
        code(blank("5-1") + ("\ndrop" if solution else "")),
        code(blank("5-2") + ("\nindex" if solution else "")),
        md("""### **6. 데이터에 결측치가 있을 경우 AI모델링의 성능이 저하될 수 있습니다. AI모델링할때 부정적 영향이 없도록 아래 가이드에 따라 결측치를 처리하세요.**
* **
- 대상 데이터프레임 : data_temp
- 결측치 개수를 확인한 후에 결측치가 있는 행을 모두 삭제하세요
- 전처리가 반영된 데이터프레임은 변수명 data_na에 저장하세요
- 결측치가 사라졌는지 확인하세요
- <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
- <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#6-1, #6-2)</font>
---"""),
        code(CLF_Q6_SOL if solution else CLF_Q6_BLANK),
        code(blank("6-1") + ("\nisnull" if solution else "")),
        code(blank("6-2") + ("\ndropna" if solution else "")),
        md("""### **7. 원-핫 인코딩(One-Hot Encoding)은 범주형 데이터를 1과 0의 이진형 벡터로 변환하기 위해 사용하는 방법입니다.**
### **아래 가이드에 따라 범주형 데이터를 이진형 벡터로 변환하는 코드를 완성하세요.**
* **
- **(7-1) 아래 가이드에 따라 데이터를 처리하는 코드를 작성하고 실행하세요**
    - 대상 데이터프레임 : data_na
    - 와인종류(E_FE_wine_kind) 컬럼의 값들을 아래 기준에 따라 치환하세요
        - 'white|rose|sparkling','red|white|sparkling', 'red|white|rose|sparkling', 'red|sparkling' > 4가지 값을 'sparkling' 으로 치환
        - 'white|sparkling' > 1가지 값을 'white' 로 치환
        - 'red|rose', 'red|white', 'red|rose|sparkling' > 3가지 값을 'red' 로 치환
    - 치환 후 와인종류(E_FE_wine_kind)의 카테고리 별 개수를 출력하세요
    - <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
    - <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#7-1, #7-2)</font><br><br>
- **(7-3) 아래 가이드에 따라 결측치를 처리하고 검증하는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
    - 대상 데이터프레임 : data_na
    - 불필요한 컬럼 5개('E_province', 'E_region_1', 'E_region_2', 'E_winery', 'E_wine_variety')를 삭제하세요
    - 원-핫 인코딩 대상 컬럼은 'E_country', 'E_FE_wine_kind' 2개 입니다
    - 원-핫인코딩이 반영된 결과를 데이터프레임 변수명 data_preset에 저장하세요
    - 원-핫인코딩한 결과, 인코딩 대상 컬럼이 변환되었는지 info 함수로 검증하세요<br><br>
- **(7-4) data_na의 와인종류(E_FE_wine_kind) 중 'red'의 개수를 작성하세요**<br><br>
---"""),
        code(CLF_Q7_SOL if solution else CLF_Q7_BLANK),
        code(blank("7-1") + ("\nisin" if solution else "")),
        code(blank("7-2") + ("\nvalue_counts" if solution else "")),
        code(CLF_Q73_SOL if solution else CLF_Q73_BUG),
        code(blank("7-4") + ("\n42262" if solution else "")),
        md("""### **8. 모델링후에 모델의 성능을 평가할 수 있도록 훈련과 검증 각각에 사용할 데이터셋을 분리하려고 합니다.**
### **와인품질등급(Grade) 컬럼을 레이블값 y로, 나머지 컬럼을 피처값 X로 할당한 후 훈련데이터셋과 검증데이터셋으로 분리하세요.**
* **
- 대상 데이터프레임 : data_preset
- 훈련과 검증데이터셋 분리
  - 훈련데이터셋 레이블 : y_train, 훈련데이터셋 피처: X_train
  - 검증데이터셋 레이블 : y_valid, 검증데이터셋 피처: X_valid
  - 훈련데이터셋과 검증데이터셋 비율은 70:30으로 설정하세요
  - 훈련데이터셋과 검증데이터셋의 와인등급 비율을 동일하게 하는 옵션을 설정하세요.
  - 난수 시드는 7로 설정하세요
  - scikit-learn의 train_test_split 함수를 활용하세요
---"""),
        code(
            write_code("8")
            + (
                """
from sklearn.model_selection import train_test_split

X = data_preset.drop('Grade', axis=1)
y = data_preset['Grade']

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.3, random_state=7, stratify=y)"""
                if solution
                else ""
            )
        ),
        md("""### **9. 스케일링을 통해 데이터 이상치의 영향도를 낮추려고 합니다.**

* **
- **(9-1) 아래 가이드에 따라 스케일링 처리하는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
    - sklearn.preprocessing에서 StandardScaler 함수를 import하세요
    - StandardScaler 함수를 ss 변수에 지정하세요
    - 훈련데이터에 대해 StandardScaler를 학습시키고 변환을 적용하세요
    - 검증데이터에 학습된 스케일링 기준을 그대로 적용하세요
    - 스케일링된 검증데이터의 가장 큰 값을 찾고, 이를 반올림하세요<br><br>
- **(9-2) StandardScaler 적용 후 검증데이터의 최댓값을 반올림한 결과는 무엇입니까?**
----"""),
        code(CLF_Q9_SOL if solution else CLF_Q9_BUG),
        code(blank("9-2") + ("\n237" if solution else "")),
        md("## <font color=blue>**<AI 모델링(50점)>**</font>"),
        md("""### **10. 와인품질등급(Grade)을 예측하는 머신러닝 모델을 만들려고 합니다.**
### **DecisionTree와 RandomForest는 여러 규칙을 순차적으로 적용하면서 독립변수 공간을 분할하는 모형으로서, 분류와 회귀 분석에 모두 사용될 수 있습니다.**

* **
- **(10-1) DecisionTree 모델의 하이퍼파라미터를 아래와 같이 구성하고, 변수에 저장하세요**
  - Cross Validation 방법론 중 GridSearchCV 사용하여 총 5회의 Cross Validation 수행
  - 트리의 최대 깊이 후보 : [3, 5, 7, 10]
  - 노드를 분할하기 위한 최소한의 샘플 데이터수(min_samples_split) 후보 : [2, 3, 5, 10]
  - GridSearchCV의 scoring 파라미터는 'accuracy', n_jobs 파라미터는 -1 로 설정
  - DecisionTree 모델의 난수 시드 : 7
  - Decision Tree 모델을 gs_dt 변수에 저장하세요
  - 앞서 분리한 훈련데이터셋으로 fit 함수를 사용해 학습시키세요<br><br>
- **(10-2) RandomForest 모델의 하이퍼파라미터를 아래와 같이 설정하고, 변수에 저장하세요**
  - Cross Validation 방법론 중 GridSearchCV 사용하여 총 5회의 Cross Validation 수행
  - 분류기 개수 후보 : [100, 200, 500]
  - 트리의 최대 깊이 후보 : [5, 10, 20]
  - 노드를 분할하기 위한 최소한의 샘플 데이터수(min_samples_split) 후보 : [2, 5, 10]
  - GridSearchCV의 scoring 파라미터는 'accuracy', n_jobs 파라미터는 -1 로 설정
  - RandomForest 모델의 난수 시드 : 7
  - Random Forest 모델을 gs_rf 변수에 저장하세요
  - 앞서 분리한 훈련데이터셋으로 fit 함수를 사용해 학습시키세요<br><br>
- **(10-3) Grid Search를 통해 찾아낸 RandomForest의 최적화된 분류기 개수는 몇 개 인가요?**<br><br>
---"""),
        code(CLF_Q10_1 if solution else write_code("10-1")),
        code(CLF_Q10_2 if solution else write_code("10-2")),
        code(blank("10-3") + ("\n500" if solution else "")),
        md("""### **11. 모델의 해석력과 개선 방향을 이해하기 위해 RandomForest 모델의 변수중요도를 파악하려고 합니다.**

* **
- **(11-1) 아래 가이드에 따라 모델의 변수중요도 파악하는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
    - Grid Search를 통해 찾은 최적화된 파라미터가 적용된 gs_rf의 best_estimator를 사용하세요
    - 변수중요도 점수와 변수 이름을 매핑하여 DataFrame을 만드세요
    - 변수중요도 점수를 기준으로 내림차순 정렬하고 Top 10 개만 선정하세요
    - 변수중요도 점수를 막대 그래프로 시각화하세요<br><br>
- **(11-2) 출력된 그래프에서 가장 높은 중요도를 보이는 변수명을 쓰세요**
---"""),
        code(CLF_Q11_SOL if solution else CLF_Q11_BUG),
        code(blank("11-2") + ("\nFE_points_winery" if solution else "")),
        md("""### **12. 앞서 학습시킨 DecisionTree와 RandomForest 모델의 성능을 평가하려고 합니다.**

* **
- **(12-1) 아래 가이드에 따라 각 모델의 Accuracy를 산출하려는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
  - Grid Search를 통해 찾은 최적화된 파라미터가 적용된 gs_dt와 gs_rf의 best_estimator를 사용하세요
  - 성능 평가는 검증데이터셋을 활용하세요
  - 앞서 만든 DecisionTree 모델로 y값을 예측하고, 그 결과를 y_pred_dt 변수에 저장하세요
  - 검증 정답(y_valid)과 예측값(y_pred_dt)의 Accuracy를 구하고 dt_acc 변수에 저장하세요
  - 앞서 만든 RandomForest 모델로 y값을 예측하고, 그 결과를 y_pred_rf에 저장하세요
  - 검증 정답(y_valid)과 예측값(y_pred_rf)의 Accuracy를 구하고 rf_acc 변수에 저장하세요
  - 2개 모델의 Accuracy값을 출력하세요<br><br>
- **(12-2) 두 모델의 Accuracy 결과를 비교했을 때, 성능이 더 우수한 모델은 무엇인가요?**
---"""),
        code(CLF_Q12_SOL if solution else CLF_Q12_BUG),
        code(blank("12-2") + ("\nRandomForest" if solution else "")),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code(TF_HELPER),
        md("""### **13. 와인품질등급(Grade)을 예측하는 딥러닝 모델을 만들려고 합니다.**
### **아래 토폴로지 다이어그램과 가이드를 참고해서 모델링하고 학습을 수행하세요.**
* **
- tensorflow framework를 사용하고 하단의 토폴로지 그림과 동일한 딥러닝 모델을 구현하세요
- 히든 레이어의 activation 함수는 'relu'를, 마지막 아웃풋 레이어의 activation 함수는 'sigmoid'를 사용하세요
- EarlyStopping 함수를 사용해서 14번의 epoch 동안 모니터링 지표(val_loss)가 향상되지 않을 경우 훈련을 중지하도록 설정하고 estop 변수에 저장하세요
- optimizer는 adam, metrics는 accuracy, loss는 binary_crossentropy로 지정해서 모델을 컴파일하세요
- 다음 조건에 따라 모델을 학습하고 학습정보는 history 변수에 저장하세요
    - batch_size : 128
    - epoch : 50
- 안내된 내용 외 별도의 파라미터를 입력하지 마세요
- <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
- <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#13-1, #13-2)</font>
---"""),
        md("![DNN Topology](Topology.png)"),
        code(CLF_Q13_SOL if solution else CLF_Q13_BLANK),
        code(
            blank("13-1")
            + (
                "\nDense(128, activation='relu', input_dim=X_train.shape[1]),\nDropout(0.3),\nDense(64, activation='relu'),\nDense(32, activation='relu'),\nDense(2, activation='sigmoid')"
                if solution
                else ""
            )
        ),
        code(blank("13-2") + ("\npatience" if solution else "")),
        md("""### **14. 앞서 만든 딥러닝 모델의 일반화 성능(Generalization Performance)을 평가하려고 합니다. matplotlib 라이브러리 활용해서, 학습 Accuracy와 검증 Accuracy의 변화를 그래프로 시각화하세요.**
* **
- 아래 가이드에 따라 Accuracy 변화를 시각화하는 코드를 완성하세요
    - 1개의 그래프에 학습 Accuracy과 검증 Accuracy 2가지를 모두 표시하세요
    - 위 2가지 각각의 범례를 'acc', 'val_acc'로 표시하세요
    - 그래프의 타이틀은 'Model Accuracy'로 표시하세요
    - X축에는 'Epochs'라고 표시하고 Y축에는 'Accuracy'라고 표시하세요<br><br>
---"""),
        code(CLF_Q14_SOL if solution else write_code("14")),
        md("""### **모든 문항이 완료되었습니다. 수고하셨습니다.**
채점 후에는 `answer_key.md`와 `solution.ipynb`로 대조하세요."""),
    ]
    return cells


# ---------------------------------------------------------------------------
# Regression
# ---------------------------------------------------------------------------

REG_Q7_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

df_na.drop( ['Time_Departure', 'Time_Arrival'] , axis=1, inplace=True)
df_preset = pd. <#7-1> (data=df_na, <#7-2>=['Address1', 'Address2'] )
df_preset.info()"""

REG_Q7_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

df_na.drop( ['Time_Departure', 'Time_Arrival'] , axis=1, inplace=True)
df_preset = pd.get_dummies(data=df_na, columns=['Address1', 'Address2'] )
df_preset.info()"""

REG_Q6_BUG = """# (6-1) 여기에 코드의 오류를 정정하고 실행하세요

print( '결측치 처리전\\n', df_temp.isnull().sum() )
df_na = df_temp.drop()
print( '\\n결측치 처리후\\n', df_na.isnull().total() )"""

REG_Q6_SOL = """# (6-1) 여기에 코드의 오류를 정정하고 실행하세요

print( '결측치 처리전\\n', df_temp.isnull().sum() )
df_na = df_temp.dropna()
print( '\\n결측치 처리후\\n', df_na.isnull().sum() )"""

REG_Q9_BUG = """# (9-1) 여기에 코드의 오류를 정정하고 실행하세요

from sklearn.preprocessing import RobustScaler
rs = RobustScaler()
X_train = rs.transform(X_train)
X_valid = rs.transform(X_train)
round(np.max(X_valid))"""

REG_Q9_SOL = """# (9-1) 여기에 코드의 오류를 정정하고 실행하세요

from sklearn.preprocessing import RobustScaler
rs = RobustScaler()
X_train = rs.fit_transform(X_train)
X_valid = rs.transform(X_valid)
round( np.max(X_valid) )"""

REG_Q11_BUG = """# (11-1) 여기에 코드의 오류를 정정하고 실행하세요

fi = pd.DataFrame({'feature': X.columns, 'importance': rf.importances})
fi = fi.sort_index('importance', ascending=False)[:10]
sns.barplot(x='importance', y='feature', data=fi, palette='viridis')"""

REG_Q11_SOL = """# (11-1) 여기에 코드의 오류를 정정하고 실행하세요

fi = pd.DataFrame({'feature': X.columns, 'importance': rf.feature_importances_})
fi = fi.sort_values('importance', ascending=False)[:10]
sns.barplot(x='importance', y='feature', data=fi, palette='viridis')"""

REG_Q12_BUG = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

y_pred_dt = dt.predict(X_valid)
y_pred_rf = rf.predict(X_train)

from sklearn_metrics import mean.absolute

dt_mae = mean.absolute(y_valid, y_pred_rf)
rf_mae = mean.absolute(y_valid, y_pred_rf)
info(dt_mae, rf_mae)"""

REG_Q12_SOL = """# (12-1) 아래 코드의 오류를 정정하고 실행하세요

y_pred_dt = dt.predict(X_valid)
y_pred_rf = rf.predict(X_valid)

from sklearn.metrics import mean_absolute_error

dt_mae = mean_absolute_error(y_valid, y_pred_dt)
rf_mae = mean_absolute_error(y_valid, y_pred_rf)
print(dt_mae, rf_mae)"""

REG_Q13_SOL = """# (13) 여기에 답안코드를 작성하고 실행하세요

model = Sequential()
model.add(Dense(64, activation='selu', input_dim=X.shape[1]))
model.add(Dropout(0.1))
model.add(Dense(32, activation='selu'))
model.add(Dense(16, activation='selu'))
model.add(Dense(1, activation='linear'))

estop = EarlyStopping(monitor='val_loss', patience=9)
model.compile(optimizer='adam', loss='mean_squared_error', metrics = ['mse'])

history = model.fit(X_train, y_train, batch_size=128, epochs=50,
                    validation_data=(X_valid, y_valid), callbacks=[estop])"""

REG_Q14_BLANK = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

plt.plot(<#14-1>["mse"])
plt.plot(<#14-1>["val_mse"])
plt.title("Model MSE")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.<#14-2>(['mse', 'val_mse'])
plt.show()"""

REG_Q14_SOL = """# (코드 셀) 코드의 빈칸을 채우고 실행하세요

plt.plot(history.history["mse"])
plt.plot(history.history["val_mse"])
plt.title("Model MSE")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.legend(['mse', 'val_mse'])
plt.show()"""


def reg_common_intro():
    return [
        md("**AICE Associate <font color=red>공식 샘플문항</font> — 회귀**"),
        md("""### **내비게이션 주행데이터를 이용한 목적지 <span style="color:darkgreen">예상 도착시각</span> 개선**
---

- 도메인 : 운송
- 목  표 : 자동차 내비게이션의 목적지 도착시간을 예측하는 인공지능모델 개발
- A사의 자동차 내비게이션이 경쟁사 상품에 비해 목적지 예상 도착시간(ETA : Estimated Time of Arrival)의 정확도가 떨어진다는 평가를 받으면서 판매량이 줄어들고 있다.
- 계속되는 판매량 부진을 만회하기 위해, A사 서비스개발팀장은 내비게이션 서비스를 하며 축적한 이용자의 주행데이터를 활용해서 '목적지 예상도착 시간'을 예측하는 인공지능 모델을 도입하려고 한다.
- A사는 브랜드파워가 있기 때문에, 인공지능을 활용해서 '목적지 예상 도착시간'의 정확도가 개선되면 자사 내비게이션의 판매량이 빠르게 회복될 것으로 기대하고 있다.

---"""),
        md(NOTICE),
        md("""**[ 데이터 컬럼 설명 (데이터 파일명: signal_data.csv) ]**

- RID                 : 경로ID
- Time_Departure      : 출발시각
- Time_Arrival        : 도착시각
- Distance            : 이동 거리, 단위 (m)
- Time_Driving        : 실주행시간(초)
- Speed_Per_Hour      : 평균시속
- Address1            : 주소1
- Address2            : 주소2
- Weekday             : Time_Departure(출발시각)의 요일
- Hour                : Time_Departure(출발시각)의 시각
- Day                 : Time_Departure(출발시각)의 날짜
- Signaltype          : 경로의 신호등 갯수
"""),
        md("""**배점:** 데이터 분석 20점 · 데이터 전처리 30점 · AI 모델링 50점 (총 14문항 / 100점)

이 노트북과 `signal_data.csv`는 같은 폴더에서 실행하세요."""),
    ]


def build_reg(solution: bool):
    cells = reg_common_intro()
    cells += [
        md("## <font color=blue>**<데이터 분석 (20점)>**</font>"),
        md("""### **1. pandas는 데이터 분석에 널리 사용되는 파이썬 라이브러리입니다.**
### **pandas를 사용할 수 있게 별칭(alias)을 pd로 해서 불러오세요.**
---"""),
        code(write_code("1") + ("\nimport pandas as pd" if solution else "")),
        md("""### **2. AI 모델링을 위해 분석 및 처리할 데이터 파일을 읽어오려고 합니다.**
### **pandas로 데이터 파일을 읽어온 뒤, 데이터프레임 변수명 df에 할당하고 첫 4개 행을 출력하세요.**

* **
- 데이터프레임 변수명 : df
- 데이터 파일명 : signal_data.csv
    - csv 파일은 본 문제/답안지와 동일한 경로에 있습니다
---"""),
        code(
            write_code("2")
            + ("\ndf = pd.read_csv('./signal_data.csv')\ndf.head(4)" if solution else "")
        ),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code(FONT_HELPER),
        md("### **3. 시각화를 통해 네비게이션 목적지 주소1(Address1)의 분포를 파악하려 합니다.**"),
        md("""* **
- **(3-1) 아래 가이드에 따라 seaborn 라이브러리를 활용해서 시각화하세요**
    - 대상 데이터프레임 : df
    - 목적지 주소1의 분포를 보여주는 countplot 그래프를 그리세요<br><br>
- **(3-2) 출력된 그래프에서 내비게이션 이용자들이 가장 많이 찾는 목적지 주소1은 어디인가요?**
-----"""),
        code(write_code("3-1") + ("\nsns.countplot(data=df, x='Address1')" if solution else "")),
        code(blank("3-2") + ("\n경기도" if solution else "")),
        md("""### **4. 그래프를 통해 실주행시간(Time_Driving)과 평균시속(Speed_Per_Hour) 컬럼의 분포와 관계를 확인하려 합니다.**
### **아래 가이드에 따라 jointplot으로 시각화하세요.**"""),
        md("""* **
- 대상 데이터프레임 : df
- seaborn의 jointplot으로 두 컬럼 간의 관계를 그래프로 그리세요
- X축에는 실주행시간(Time_Driving)을, Y축에는 평균시속(Speed_Per_Hour)을 표시하세요
---"""),
        code(
            write_code("4")
            + ("\nsns.jointplot(data=df, x='Time_Driving', y='Speed_Per_Hour')" if solution else "")
        ),
        md("## <font color=blue>**<데이터 전처리 (30점)>**</font>"),
        md("""### **5. jointplot으로 확인한 결과, 평균시속(Speed_Per_Hour) 컬럼에서 이상치가 발견되었습니다. AI모델링할때 부정적 영향이 없도록 아래 가이드에 따라 이상치를 처리하세요.**
* **
- 대상 데이터프레임 : df
- 평균시속이 300보다 크거나 같은 이상치가 있는 행(row)을 삭제하세요
- AI모델링에 불필요한 경로ID(RID) 컬럼을 삭제하세요
- 전처리를 적용한 데이터프레임은 df_temp라는 변수명으로 저장하세요
---"""),
        code(
            write_code("5")
            + (
                "\ndf_temp = df[df.Speed_Per_Hour < 300]\ndf_temp.drop('RID', axis=1, inplace=True)"
                if solution
                else ""
            )
        ),
        md("""### **6. 데이터에 결측치가 있을 경우 AI모델링의 성능이 저하될 수 있습니다. 아래 가이드에 따라 결측치를 확인하고 처리하세요.**
* **
- **(6-1) 아래 가이드에 따라 결측치를 처리하고 검증하는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
    - 대상 데이터프레임 : df_temp
    - 결측치 개수를 확인한 후에 결측치가 있는 행을 모두 삭제하세요
    - 전처리가 반영된 데이터프레임은 변수명 df_na에 저장하세요
    - 결측치가 사라졌는지 확인하세요<br><br>
- **(6-2) df_temp의 결측치 개수는 총 몇 개인가요?**
---"""),
        code(REG_Q6_SOL if solution else REG_Q6_BUG),
        code(blank("6-2") + ("\n2" if solution else "")),
        md("""### **7. 원-핫 인코딩(One-Hot Encoding)은 범주형 데이터를 1과 0의 이진형 벡터로 변환하기 위해 사용하는 방법입니다.**
### **아래 가이드에 따라 범주형 데이터를 이진형 벡터로 변환하는 코드를 완성하세요.**
* **
- 대상 데이터프레임 : df_na
- 원-핫 인코딩 대상 : object형(문자형) 컬럼 전체
- 원-핫인코딩이 반영된 결과를 데이터프레임 변수명 df_preset에 저장하세요
- 원-핫인코딩한 결과, object형(문자형) 컬럼이 변환되었는지 info 함수로 검증하세요<br><br>
- <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
- <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#7-1, #7-2)</font>
---"""),
        code(REG_Q7_SOL if solution else REG_Q7_BLANK),
        code(blank("7-1") + ("\nget_dummies" if solution else "")),
        code(blank("7-2") + ("\ncolumns" if solution else "")),
        md("""### **8. 모델링후에 모델의 성능을 평가할 수 있도록 훈련과 검증 각각에 사용할 데이터셋을 분리하려고 합니다.**
### **실주행시간(Time_Driving) 컬럼을 레이블값 y로, 나머지 컬럼을 피처값 X로 할당한 후 훈련데이터셋과 검증데이터셋으로 분리하세요.**
* **
- 대상 데이터프레임 : df_preset
- 훈련과 검증데이터셋 분리
  - 훈련데이터셋 레이블 : y_train, 훈련데이터셋 피처: X_train
  - 검증데이터셋 레이블 : y_valid, 검증데이터셋 피처: X_valid
  - 훈련데이터셋과 검증데이터셋 비율은 80:20으로 설정하세요
  - 난수 시드는 42로 설정하세요
  - scikit-learn의 train_test_split 함수를 활용하세요
---"""),
        code(
            write_code("8")
            + (
                """
X = df_preset.drop('Time_Driving', axis=1)
y = df_preset['Time_Driving']

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)"""
                if solution
                else ""
            )
        ),
        md("""### **9. 스케일링을 통해 데이터 이상치의 영향도를 낮추려고 합니다.**

* **
- **(9-1) 아래 가이드에 따라 스케일링 처리하는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
    - sklearn.preprocessing에서 RobustScaler 함수를 import하세요
    - RobustScaler 함수를 rs 변수에 지정하세요
    - 훈련데이터에 대해 RobustScaler를 학습시키고 변환을 적용하세요
    - 검증데이터에 학습된 스케일링 기준을 그대로 적용하세요
    - 스케일링된 검증데이터의 가장 큰 값을 찾고, 이를 반올림하세요<br><br>
- **(9-2) RobustScaler 적용 후 검증데이터의 최댓값을 반올림한 결과는 무엇입니까?**
----"""),
        code(REG_Q9_SOL if solution else REG_Q9_BUG),
        code(blank("9-2") + ("\n6" if solution else "")),
        md("## <font color=blue>**<AI 모델링(50점)>**</font>"),
        md("""### **10. 실주행시간(Time_Driving)을 예측하는 머신러닝 모델을 만들려고 합니다.**
### **DecisionTree와 RandomForest는 여러 규칙을 순차적으로 적용하면서 독립변수 공간을 분할하는 모형으로서, 분류와 회귀 분석에 모두 사용될 수 있습니다.**

* **
- **(10-1) DecisionTree 모델의 하이퍼파라미터를 아래와 같이 구성하고, 변수에 저장하세요**
  - 트리의 최대 깊이 : 5
  - 노드를 분할하기 위한 최소한의 샘플 데이터수(min_samples_split) : 3
  - 난수 시드 : 120
  - Decision Tree 모델을 dt 변수에 저장하세요
  - 앞서 분리한 훈련데이터셋으로 fit 함수를 사용해 학습시키세요<br><br>
- **(10-2) RandomForest 모델의 하이퍼파라미터를 아래와 같이 설정하고, 변수에 저장하세요**
  - 트리의 최대 깊이 : 5
  - 노드를 분할하기 위한 최소한의 샘플 데이터수(min_samples_split) : 3
  - 난수 시드 : 120
  - Random Forest 모델을 rf 변수에 저장하세요
  - 앞서 분리한 훈련데이터셋으로 fit 함수를 사용해 학습시키세요
---"""),
        code(
            write_code("10-1")
            + (
                """
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(max_depth=5,   min_samples_split=3, random_state=120)
dt.fit(X_train, y_train)"""
                if solution
                else ""
            )
        ),
        code(
            write_code("10-2")
            + (
                """
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(max_depth=5,   min_samples_split=3, random_state=120)
rf.fit(X_train, y_train)"""
                if solution
                else ""
            )
        ),
        md("""### **11. 모델의 해석력과 개선 방향을 이해하기 위해 RandomForest 모델의 변수중요도를 파악하려고 합니다.**

* **
- **(11-1) 아래 가이드에 따라 모델의 변수중요도 파악하는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
    - 변수중요도 점수와 변수 이름을 매핑하여 DataFrame을 만드세요
    - 변수중요도 점수를 기준으로 내림차순 정렬하고 top 10개만 선정하세요.
    - 변수중요도 점수를 막대 그래프로 시각화하세요<br><br>
- **(11-2) 출력된 그래프에서 가장 높은 중요도를 보이는 변수명을 쓰세요**
---"""),
        code(REG_Q11_SOL if solution else REG_Q11_BUG),
        code(blank("11-2") + ("\nSpeed_Per_Hour" if solution else "")),
        md("""### **12. 앞서 학습시킨 DecisionTree와 RandomForest 모델의 성능을 평가하려고 합니다.**

* **
- **(12-1) 아래 가이드에 따라 각 모델의 MAE를 산출하려는데 에러가 나고 있습니다. 코드의 오류를 정정하세요**
  - 성능 평가는 검증데이터셋을 활용하세요
  - 앞서 만든 DecisionTree 모델로 y값을 예측하고, 그 결과를 y_pred_dt 변수에 저장하세요
  - 검증 정답(y_valid)과 예측값(y_pred_dt)의 MAE를 구하고 dt_mae 변수에 저장하세요
  - 앞서 만든 RandomForest 모델로 y값을 예측하고, 그 결과를 y_pred_rf에 저장하세요
  - 검증 정답(y_valid)과 예측값(y_pred_rf)의 MAE를 구하고 rf_mae 변수에 저장하세요
  - 2개 모델의 MAE값을 출력하세요<br><br>
- **(12-2) 두 모델의 MAE 결과를 비교했을 때, 성능이 더 우수한 모델은 무엇인가요?**
---"""),
        code(REG_Q12_SOL if solution else REG_Q12_BUG),
        code(blank("12-2") + ("\nRandomForest" if solution else "")),
        md("> **<span style=\"color:red\">다음 문항을 풀기 전에 </span>아래 코드를 실행하세요.**"),
        code(TF_HELPER),
        md("""### **13. 실주행시간(Time_Driving)을 예측하는 딥러닝 모델을 만들려고 합니다.**
### **아래 토폴로지 다이어그램과 가이드를 참고해서 모델링하고 학습을 수행하세요.**
* **
- tensorflow framework를 사용하고 하단의 토폴로지 그림과 동일한 딥러닝 모델을 구현하세요
- 히든 레이어의 activation 함수는 'selu'를, 마지막 아웃풋 레이어의 activation 함수는 'linear'를 사용하세요
- EarlyStopping 함수를 사용해서 9번의 epoch 동안 모니터링 지표(val_loss)가 향상되지 않을 경우 훈련을 중지하도록 설정하고 estop 변수에 저장하세요
- optimizer는 adam, metrics는 mse, loss는 mean_squared_error로 지정해서 모델을 컴파일하세요
- 다음 조건에 따라 모델을 학습하고 학습정보는 history 변수에 저장하세요
    - batch_size : 128
    - epoch : 50
- 안내된 내용 외 별도의 파라미터를 입력하지 마세요
---"""),
        md("![DNN Topology](topology.png)"),
        code(REG_Q13_SOL if solution else write_code("13")),
        md("""### **14. 앞서 만든 딥러닝 모델의 일반화 성능(Generalization Performance)을 평가하려고 합니다. matplotlib 라이브러리 활용해서, 학습 MSE와 검증 MSE의 변화를 그래프로 시각화하세요.**
* **
- 아래 가이드에 따라 MSE 변화를 시각화하는 코드를 완성하세요
    - 1개의 그래프에 학습 MSE과 검증 MSE 2가지를 모두 표시하세요
    - 위 2가지 각각의 범례를 'mse', 'val_mse'로 표시하세요
    - 그래프의 타이틀은 'Model MSE'로 표시하세요
    - X축에는 'Epochs'라고 표시하고 Y축에는 'MSE'라고 표시하세요<br><br>
- <font color=blue>아래 코드 셀(cell)에 있는 코드의 빈칸을 채우고 실행하세요</font>
- <font color=blue>빈칸에 들어갈 내용은 각 답안 셀(cell)에 입력하세요 (#14-1, #14-2)</font>
---"""),
        code(REG_Q14_SOL if solution else REG_Q14_BLANK),
        code(blank("14-1") + ("\nhistory.history" if solution else "")),
        code(blank("14-2") + ("\nlegend" if solution else "")),
        md("""### **모든 문항이 완료되었습니다. 수고하셨습니다.**
채점 후에는 `answer_key.md`와 `solution.ipynb`로 대조하세요."""),
    ]
    return cells


def main():
    save(BASE / "classification" / "problem.ipynb", build_clf(False))
    save(BASE / "classification" / "solution.ipynb", build_clf(True))
    save(BASE / "regression" / "problem.ipynb", build_reg(False))
    save(BASE / "regression" / "solution.ipynb", build_reg(True))


if __name__ == "__main__":
    main()
