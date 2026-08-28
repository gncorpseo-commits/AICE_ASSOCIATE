# 분류 샘플 정답 (와인 품질)

공식 해설 기준. 빈칸/단답만 정리했습니다. 전체 코드는 `solution.ipynb`를 보세요.

| 번호 | 유형 | 정답 |
|------|------|------|
| 1 | 코드 | `import sklearn as sk` |
| 2 | 코드 | `data = pd.read_csv('./wine_quality_data.csv')` 후 `data.head(4)` |
| 3-1 | 빈칸 | `subplots` |
| 3-2 | 빈칸 | `axes` |
| 3-3 | 빈칸 | `set_title` |
| 4 | 코드 | `sns.boxplot(data=data, x='Grade', y='FE_points_winery')` |
| 5-1 | 빈칸 | `drop` |
| 5-2 | 빈칸 | `index` |
| | 참고 | pandas 2.x에서는 `drop(index=..., axis=0)` 가 에러입니다. 시험 빈칸은 `drop`/`index`이고, 해설 노트북은 `drop(index)` / `drop(columns=)` 로 실행되게 맞춰 두었습니다. |
| 6-1 | 빈칸 | `isnull` |
| 6-2 | 빈칸 | `dropna` |
| 7-1 | 빈칸 | `isin` |
| 7-2 | 빈칸 | `value_counts` |
| 7-3 | 오류 정정 | `drop(..., axis=1)` + `pd.get_dummies(..., columns=...)` |
| 7-4 | 단답 | `42262` (`red` 개수) |
| 8 | 코드 | `train_test_split(..., test_size=0.3, random_state=7, stratify=y)` |
| 9-1 | 오류 정정 | `ss.fit_transform(X_train)` / `ss.transform(X_valid)` |
| 9-2 | 단답 | `237` |
| 10-1 | 코드 | `DecisionTreeClassifier` + `GridSearchCV` → `gs_dt` |
| 10-2 | 코드 | `RandomForestClassifier` + `GridSearchCV` → `gs_rf` |
| 10-3 | 단답 | `500` |
| 11-1 | 오류 정정 | `gs_rf.best_estimator_.feature_importances_` + `sort_values` |
| 11-2 | 단답 | `FE_points_winery` |
| 12-1 | 오류 정정 | `best_estimator_.predict(X_valid)` + `accuracy_score` |
| 12-2 | 단답 | `RandomForest` |
| 13-1 | 빈칸 | `Dense(128, relu)` → `Dropout(0.3)` → `Dense(64)` → `Dense(32)` → `Dense(2, sigmoid)` |
| 13-2 | 빈칸 | `patience` |
| 14 | 코드 | `history.history["accuracy"]` / `val_accuracy`, legend `acc` / `val_acc` |

### 자주 틀리는 포인트

- Q8은 **`stratify=y`** 와 `test_size=0.3`, `random_state=7`
- Q9는 train에만 `fit`, valid에는 `transform`만
- Q10~12는 `gs_rf`가 아니라 **`gs_rf.best_estimator_`**
- Q13 출력층은 클래스 2개라 `Dense(2, activation='sigmoid')` + `binary_crossentropy`
- Q13-2 답은 patience **값(14)이 아니라 파라미터 이름** `patience`
