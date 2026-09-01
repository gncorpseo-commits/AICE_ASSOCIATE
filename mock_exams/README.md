# 모의고사 30회 (공식 샘플 형식)

각 회차는 KT 공식 샘플과 같은 **14문항 / 100점**입니다.

| 영역 | 배점 | 유형 |
|------|------|------|
| 데이터 분석 | 20 | import, CSV, countplot, jointplot/boxplot |
| 데이터 전처리 | 30 | IQR 이상치, 결측(오류 정정), get_dummies(빈칸), split, scaler(오류 정정) |
| AI 모델링 | 50 | DecisionTree + RandomForest, 변수중요도, MAE/Accuracy, Keras + EarlyStopping |

- **문제:** `mock_XX_name.ipynb` (답 비움, 오류 코드 포함)
- **해설:** `mock_XX_name_solution.ipynb`
- **단답 모음:** [`answer_keys.md`](answer_keys.md)

회귀는 변수명 `df` / RobustScaler / MAE, 분류는 변수명 `data` / StandardScaler / Accuracy 입니다. 공식 샘플 두 장과 맞춰 두었습니다.

```bash
python mock_exams/generate_notebooks.py
```
