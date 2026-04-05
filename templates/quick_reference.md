# 📋 AICE Associate Quick Reference (치트시트)

## 🔥 시험 중 빠른 참조용

---

## 1. 라이브러리 Import

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, f1_score
```

---

## 2. 데이터 로딩 & 탐색

| 작업 | 코드 |
|------|------|
| CSV 로딩 | `df = pd.read_csv('file.csv')` |
| 미리보기 | `df.head()` |
| 크기 확인 | `df.shape` |
| 정보 확인 | `df.info()` |
| 통계량 | `df.describe()` |
| 컬럼 목록 | `df.columns` |
| 데이터 타입 | `df.dtypes` |

---

## 3. 결측치 처리

| 작업 | 코드 |
|------|------|
| 결측치 확인 | `df.isna().sum()` |
| 총 결측치 | `df.isna().sum().sum()` |
| 평균으로 대체 | `df['col'].fillna(df['col'].mean(), inplace=True)` |
| 중앙값으로 대체 | `df['col'].fillna(df['col'].median(), inplace=True)` |
| 최빈값으로 대체 | `df['col'].fillna(df['col'].mode()[0], inplace=True)` |
| 결측치 삭제 | `df.dropna(inplace=True)` |

---

## 4. 데이터 전처리

### 4-1. 인코딩

```python
# One-Hot Encoding (권장)
df_encoded = pd.get_dummies(df, columns=['col1', 'col2'])

# Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['col_encoded'] = le.fit_transform(df['col'])
```

### 4-2. 스케일링

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# 표준화 (평균=0, 표준편차=1)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 정규화 (0~1 범위)
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
```

### 4-3. 파생변수

```python
# 거리 계산
df['distance'] = np.sqrt((df['x2']-df['x1'])**2 + (df['y2']-df['y1'])**2)

# 시간 추출
df['hour'] = pd.to_datetime(df['datetime']).dt.hour
df['dayofweek'] = pd.to_datetime(df['datetime']).dt.dayofweek

# 비율 계산
df['ratio'] = df['col1'] / df['col2']
```

---

## 5. 시각화

### 5-1. 분포 확인

```python
# 히스토그램
plt.figure(figsize=(10, 6))
sns.histplot(df['col'], kde=True)
plt.title('Distribution')
plt.show()

# 박스플롯
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='value', data=df)
plt.show()
```

### 5-2. 상관관계

```python
# 히트맵
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
```

### 5-3. 산점도

```python
plt.figure(figsize=(10, 6))
plt.scatter(df['x'], df['y'], alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

---

## 6. 모델링

### 6-1. 데이터 분할

```python
X = df.drop(['target', 'id'], axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### 6-2. 회귀 모델

```python
# LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# RandomForestRegressor
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### 6-3. 분류 모델

```python
# LogisticRegression
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

## 7. 평가 지표

### 7-1. 회귀 평가

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
```

### 7-2. 분류 평가

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

acc = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {acc:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
```

---

## 8. 결과 해석 템플릿

### 회귀 해석

```
[모델 성능 해석]

1. RMSE: X.XX
   - 예측값과 실제값의 평균 오차가 약 X 수준입니다.

2. R² Score: 0.XX
   - 모델이 변동의 약 XX%를 설명합니다.

3. 비즈니스 적용:
   - 본 모델을 활용하여 [목적]에 활용할 수 있습니다.
```

### 분류 해석

```
[모델 성능 해석]

1. Accuracy: XX%
   - 전체 데이터 중 XX%를 올바르게 분류했습니다.

2. F1 Score: 0.XX
   - 정밀도와 재현율의 조화평균이 0.XX입니다.

3. 비즈니스 적용:
   - 본 모델을 활용하여 [목적]을 예측할 수 있습니다.
```

---

## 9. 자주 하는 실수 ⚠️

| 실수 | 올바른 방법 |
|------|------------|
| 변수명 다르게 사용 | 문제에서 지시한 변수명 정확히 사용 |
| 셀 실행 안 함 | 모든 셀 실행 후 제출 |
| 해석 누락 | 숫자 + 해석 문장 함께 작성 |
| 복잡한 모델 | 간단한 모델 하나로 완주 |
| import 누락 | 필요한 라이브러리 모두 import |

---

## 10. 변형 대비 필수 패턴

### 10-1. 클래스 불균형 대응
```python
# train_test_split에서 stratify 사용
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 모델에 class_weight 적용 (분류)
model = LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced')
# model = RandomForestClassifier(random_state=42, class_weight='balanced')
```

### 10-2. 평가 지표 변경 대응
```python
from sklearn.metrics import mean_absolute_error, precision_score, recall_score

# 회귀
mae = mean_absolute_error(y_test, y_pred)

# 분류
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
```

### 10-3. 교차검증/하이퍼파라미터 튜닝
```python
from sklearn.model_selection import GridSearchCV

param_grid = {"n_estimators": [100, 200], "max_depth": [None, 5, 10]}
grid = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, scoring="f1_weighted")
grid.fit(X_train, y_train)
best_model = grid.best_estimator_
```

### 10-4. 데이터 누수 방지 체크
```python
# 타겟/ID 유사 컬럼 제거 확인
drop_cols = ['target', 'id']
X = df.drop([c for c in drop_cols if c in df.columns], axis=1)
```

---

## 11. 긴급 코드 (복붙용)

### 전체 파이프라인 (회귀)

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('data.csv')
df.fillna(df.mean(), inplace=True)

X = df.drop(['target'], axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse:.4f}, R²: {r2:.4f}")
```

### 전체 파이프라인 (분류)

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv('data.csv')
df.fillna(df.mode().iloc[0], inplace=True)

X = df.drop(['target'], axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
print(f"Accuracy: {acc:.4f}, F1: {f1:.4f}")
```

---

**Good Luck! 🍀**
