# 와인 품질 분류 모의고사 (공식 샘플 기반)

공식 분류 샘플과 **동일 데이터** `wine_quality_data.csv` 를 사용합니다.  
데이터/토폴로지 파일은 `official_samples/classification/` 을 가리키는 **심볼릭 링크**입니다. Windows에서 링크가 깨지면 아래를 복사하세요.

```bash
cp ../../official_samples/classification/wine_quality_data.csv .
cp ../../official_samples/classification/Topology.png .
```

| 세트 | 파일 | 특징 |
|------|------|------|
| 1 | `set01_problem.ipynb` / `set01_solution.ipynb` | heatmap, violin, fillna/median, MinMax, LR+RF, f1 |
| 2 | `set02_*` | describe, crosstab heatmap, IQR, where, StandardScaler, DT+RF, confusion_matrix |
| 3 | `set03_*` | groupby, barplot, query, map(0/1), RobustScaler, RF+GB, classification_report |

- 오류 정정형 문항: 각 세트 Q7-3, Q9-1, Q11-1, Q12-1 포함
- GridSearch는 연습용으로 cv=3·후보 축소 (공식보다 가볍게)
- DNN Topology 이미지는 공식 `Topology.png` 복사본 사용

정답 요약: `answer_key_set0N.md`
