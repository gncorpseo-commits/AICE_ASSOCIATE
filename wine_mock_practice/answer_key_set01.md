# Set 1 정답 요약

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
