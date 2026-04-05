"""
===============================================================================
AICE Associate 표준 ML 파이프라인 템플릿
===============================================================================

이 템플릿은 AICE Associate 시험에서 사용하는 
머신러닝 파이프라인의 표준 구조입니다.

시험에서 이 순서대로 진행하면 안정적으로 문제를 풀 수 있습니다.

사용법:
1. 이 파일을 복사하여 사용
2. 주석의 지시에 따라 코드 수정
3. 변수명은 문제에서 지시한 대로 변경

===============================================================================
"""

# ============================================================================
# 1. 라이브러리 Import
# ============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# sklearn - 모델링
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

# sklearn - 회귀 모델
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# sklearn - 분류 모델
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# sklearn - 평가 지표
from sklearn.metrics import mean_squared_error, r2_score  # 회귀용
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix  # 분류용

# 시각화 한글 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

print("라이브러리 import 완료!")


# ============================================================================
# 2. 데이터 로딩
# ============================================================================
# ⚠️ 파일명을 문제에서 지시한 파일명으로 변경하세요
df = pd.read_csv('data.csv')

# 데이터 미리보기
print("=== 데이터 미리보기 ===")
df.head()


# ============================================================================
# 3. 데이터 탐색 (EDA)
# ============================================================================
# 3-1. 데이터 크기 확인
print(f"데이터 shape: {df.shape}")
print(f"행 개수: {df.shape[0]}, 열 개수: {df.shape[1]}")

# 3-2. 데이터 정보 확인
print("\n=== 데이터 정보 ===")
print(df.info())

# 3-3. 기초 통계량
print("\n=== 기초 통계량 ===")
df.describe()


# ============================================================================
# 4. 결측치 확인 및 처리
# ============================================================================
# 4-1. 결측치 확인
print("=== 결측치 확인 ===")
print(df.isna().sum())
print(f"\n총 결측치 개수: {df.isna().sum().sum()}")

# 4-2. 결측치 처리
# ⚠️ 변수명을 문제에서 지시한 이름으로 변경하세요 (예: df_clean)
df_clean = df.copy()

# 수치형 컬럼: 평균값으로 대체
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df_clean[col].isna().sum() > 0:
        df_clean[col].fillna(df_clean[col].mean(), inplace=True)
        print(f"  - {col}: 평균값으로 대체")

# 범주형 컬럼: 최빈값으로 대체
categorical_cols = df_clean.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df_clean[col].isna().sum() > 0:
        df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
        print(f"  - {col}: 최빈값으로 대체")

# 결측치 처리 확인
print("\n결측치 처리 후:")
print(df_clean.isna().sum())


# ============================================================================
# 5. 데이터 시각화
# ============================================================================
# 5-1. 타겟 변수 분포 (히스토그램)
# ⚠️ 'target' 부분을 실제 타겟 컬럼명으로 변경하세요
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['target'], kde=True, bins=30)
plt.title('타겟 변수 분포')
plt.xlabel('값')
plt.ylabel('빈도')
plt.show()

# 5-2. 상관관계 히트맵
plt.figure(figsize=(12, 8))
numeric_df = df_clean.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('상관관계 히트맵')
plt.tight_layout()
plt.show()


# ============================================================================
# 6. 파생변수 생성 (Feature Engineering)
# ============================================================================
# 예시 1: 거리 계산 (좌표가 있는 경우)
# df_clean['distance'] = np.sqrt(
#     (df_clean['lat2'] - df_clean['lat1'])**2 +
#     (df_clean['lng2'] - df_clean['lng1'])**2
# )

# 예시 2: 시간대 추출 (시간 데이터가 있는 경우)
# df_clean['hour'] = pd.to_datetime(df_clean['datetime']).dt.hour

# 예시 3: 요일 추출
# df_clean['dayofweek'] = pd.to_datetime(df_clean['datetime']).dt.dayofweek

print("파생변수 생성 완료")
df_clean.head()


# ============================================================================
# 7. 범주형 변수 인코딩
# ============================================================================
# 방법 1: One-Hot Encoding (권장)
# ⚠️ columns 리스트에 범주형 컬럼명을 넣으세요
df_encoded = pd.get_dummies(df_clean, columns=['category_col1', 'category_col2'])

# 방법 2: Label Encoding (순서가 있는 범주형)
# le = LabelEncoder()
# df_encoded['category_encoded'] = le.fit_transform(df_clean['category_col'])

print(f"인코딩 후 shape: {df_encoded.shape}")
df_encoded.head()


# ============================================================================
# 8. 피처(X)와 타겟(y) 분리
# ============================================================================
# ⚠️ 'target'과 'id' 부분을 실제 컬럼명으로 변경하세요
# ⚠️ 변수명 X, y는 문제 지시에 따라 변경 가능

# 제외할 컬럼 (타겟 + ID 등)
drop_cols = ['target', 'id']

X = df_encoded.drop(drop_cols, axis=1)
y = df_encoded['target']

print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
print(f"\n피처 목록: {list(X.columns)}")


# ============================================================================
# 9. 데이터 분할 (Train/Test Split)
# ============================================================================
# ⚠️ test_size, random_state는 문제 지시에 따라 변경하세요

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # 보통 0.2 또는 0.3
    random_state=42     # 보통 42
)

# ⚠️ 분류 문제이고 클래스 불균형이 심하면 stratify=y 옵션을 고려하세요
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42, stratify=y
# )

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")


# ============================================================================
# 10. 모델 학습
# ============================================================================
# ⚠️ 문제 유형에 따라 모델 선택

# -------------------- 회귀 문제 --------------------
# 방법 1: LinearRegression (간단, 안정적)
model = LinearRegression()

# 방법 2: RandomForestRegressor (성능 우수)
# model = RandomForestRegressor(random_state=42, n_estimators=100)

# -------------------- 분류 문제 --------------------
# 방법 1: LogisticRegression (간단, 안정적)
# model = LogisticRegression(random_state=42, max_iter=1000)

# 방법 2: RandomForestClassifier (성능 우수)
# model = RandomForestClassifier(random_state=42, n_estimators=100)

# ⚠️ 클래스 불균형 시 class_weight='balanced' 고려
# model = LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced')
# model = RandomForestClassifier(random_state=42, n_estimators=100, class_weight='balanced')

# 모델 학습
model.fit(X_train, y_train)
print(f"모델 학습 완료: {type(model).__name__}")


# ============================================================================
# 11. 예측 수행
# ============================================================================
y_pred = model.predict(X_test)

print("예측 완료!")
print(f"예측값 샘플: {y_pred[:5]}")


# ============================================================================
# 12. 모델 평가
# ============================================================================
# -------------------- 회귀 문제 평가 --------------------
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("=== 회귀 모델 평가 결과 ===")
print(f"RMSE: {rmse:.4f}")
print(f"R² Score: {r2:.4f}")

# -------------------- 분류 문제 평가 --------------------
# accuracy = accuracy_score(y_test, y_pred)
# f1 = f1_score(y_test, y_pred, average='weighted')  # 다중분류시 'weighted'
# 
# print("=== 분류 모델 평가 결과 ===")
# print(f"Accuracy: {accuracy:.4f}")
# print(f"F1 Score: {f1:.4f}")

# ⚠️ 지표 변경 요구 시 (예: Precision/Recall)
# from sklearn.metrics import precision_score, recall_score
# precision = precision_score(y_test, y_pred, average='weighted')
# recall = recall_score(y_test, y_pred, average='weighted')
# print(f"Precision: {precision:.4f}")
# print(f"Recall: {recall:.4f}")


# ============================================================================
# 13. 결과 시각화
# ============================================================================
# -------------------- 회귀: 실제값 vs 예측값 --------------------
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('실제값')
plt.ylabel('예측값')
plt.title('실제값 vs 예측값')
plt.show()

# -------------------- 분류: 혼동 행렬 --------------------
# from sklearn.metrics import ConfusionMatrixDisplay
# ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
# plt.title('혼동 행렬')
# plt.show()


# ============================================================================
# 14. 결과 해석 (⭐ 매우 중요!)
# ============================================================================
print("""
===============================================================================
                         [모델 성능 해석]
===============================================================================

1. RMSE (Root Mean Squared Error): {:.2f}
   - 예측값과 실제값의 평균 오차가 약 {:.0f} 수준입니다.
   - 이는 [도메인 맥락에서의 해석]을 의미합니다.

2. R² Score: {:.4f}
   - 모델이 타겟 변수 변동의 약 {:.1f}%를 설명할 수 있습니다.
   - 이는 [좋은/보통/개선필요한] 수준의 설명력입니다.

3. 비즈니스 적용 방안:
   - 본 모델을 활용하여 [구체적인 활용 방안]을 수행할 수 있습니다.
   - 추가적으로 [개선 방향]을 고려하면 예측 정확도를 높일 수 있습니다.

===============================================================================
""".format(rmse, rmse, r2, r2*100))


# ============================================================================
# 15. (선택) 피처 중요도 확인 (RandomForest 사용 시)
# ============================================================================
# if hasattr(model, 'feature_importances_'):
#     feature_importance = pd.DataFrame({
#         'feature': X.columns,
#         'importance': model.feature_importances_
#     }).sort_values('importance', ascending=False)
#     
#     plt.figure(figsize=(10, 6))
#     sns.barplot(data=feature_importance.head(10), x='importance', y='feature')
#     plt.title('Top 10 Feature Importance')
#     plt.show()
