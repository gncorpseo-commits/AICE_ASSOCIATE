# 회귀 샘플 정답 (내비게이션 ETA)

공식 해설 기준. 빈칸/단답만 정리했습니다. 전체 코드는 `solution.ipynb`를 보세요.

| 번호 | 유형 | 정답 |
|------|------|------|
| 1 | 코드 | `import pandas as pd` |
| 2 | 코드 | `df = pd.read_csv('./signal_data.csv')` 후 `df.head(4)` |
| 3-1 | 코드 | `sns.countplot(data=df, x='Address1')` |
| 3-2 | 단답 | `경기도` |
| 4 | 코드 | `sns.jointplot(data=df, x='Time_Driving', y='Speed_Per_Hour')` |
| 5 | 코드 | `df_temp = df[df.Speed_Per_Hour < 300]` 후 `RID` 삭제 |
| 6-1 | 오류 정정 | `df_temp.dropna()` / `isnull().sum()` |
| 6-2 | 단답 | `2` |
| 7-1 | 빈칸 | `get_dummies` |
| 7-2 | 빈칸 | `columns` |
| 8 | 코드 | `test_size=0.2`, `random_state=42`, 타겟 `Time_Driving` |
| 9-1 | 오류 정정 | `rs.fit_transform(X_train)` / `rs.transform(X_valid)` |
| 9-2 | 단답 | `6` |
| 10-1 | 코드 | `DecisionTreeRegressor(max_depth=5, min_samples_split=3, random_state=120)` |
| 10-2 | 코드 | `RandomForestRegressor` 동일 하이퍼파라미터 → `rf` |
| 11-1 | 오류 정정 | `rf.feature_importances_` + `sort_values` |
| 11-2 | 단답 | `Speed_Per_Hour` |
| 12-1 | 오류 정정 | `predict(X_valid)` + `mean_absolute_error` |
| 12-2 | 단답 | `RandomForest` (대소문자/띄어쓰기 변형 인정) |
| 13 | 코드 | Dense 64-selu → Dropout 0.1 → 32 → 16 → 1-linear, `patience=9` |
| 14-1 | 빈칸 | `history.history` |
| 14-2 | 빈칸 | `legend` |

### 자주 틀리는 포인트

- Q5는 `>= 300` 삭제 → 조건은 **`Speed_Per_Hour < 300`**
- Q6 버그: `drop()` / `isnull().total()` → `dropna()` / `isnull().sum()`
- Q9 버그: train에 `fit` 없이 `transform`, valid에 **train을 다시 transform**
- Q11 버그: `rf.importances`, `sort_index` → `feature_importances_`, `sort_values`
- Q12는 MAE가 **작을수록** 좋음 → RandomForest
- Q13 입력 차원은 `X.shape[1]` (공식 해설 그대로)
- Q13 출력층은 회귀라 `Dense(1, activation='linear')`, loss `mean_squared_error`
