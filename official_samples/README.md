# AICE Associate 공식 샘플문항

KT AICE Associate 실기시험과 **같은 형식**의 공식 샘플입니다.

기존 `mock_exams/` 30회는 파이프라인 연습용입니다. **실제 시험 화면(빈칸 채우기, 오류 정정, Keras 토폴로지)** 은 이 폴더가 더 가깝습니다.

| 유형 | 시나리오 | 데이터 | 타겟 | 문항 |
|------|----------|--------|------|------|
| [회귀](regression/) | 내비게이션 ETA | `signal_data.csv` (10,000행) | `Time_Driving` | 14문항 / 100점 |
| [분류](classification/) | 와인 품질등급 | `wine_quality_data.csv` (90,784행) | `Grade` (Pass/Fail) | 14문항 / 100점 |

## 시험과 동일한 구성

| 영역 | 배점 | 하는 일 |
|------|------|---------|
| 데이터 분석 | 20점 | import, CSV 로드, countplot / boxplot / jointplot |
| 데이터 전처리 | 30점 | 이상치, 결측치, 원-핫 인코딩, train/valid 분리, 스케일링 |
| AI 모델링 | 50점 | DecisionTree + RandomForest, 변수중요도, 지표 비교, Keras DNN |

문항 유형:

1. **코드 작성** — `#여기에 답안코드를 작성하고 실행하세요`
2. **빈칸 채우기** — `<#3-1>` 자리를 채운 뒤, 답안 셀에 단어만 적기
3. **오류 정정** — 일부러 깨진 코드를 고치기
4. **단답** — 그래프/숫자 결과를 셀에 적기 (실행 불필요)

## 푸는 순서 (추천)

1. `regression/problem.ipynb` 90분
2. `classification/problem.ipynb` 90분
3. 각 폴더의 `solution.ipynb` + `answer_key.md`로 채점
4. 틀린 패턴만 `templates/quick_reference.md`의 **공식 샘플 패턴** 섹션으로 복습

## 실행 방법

### Windows (추천)

프로젝트 루트의 `start_study.bat` 를 실행하세요. Python 설치부터 Jupyter까지 한 번에 진행합니다.

```powershell
cd C:\project\GN_Build_Up\AICE_Associate_samples
git pull
.\start_study.bat
```

브라우저가 열리면 `regression/problem.ipynb` 부터 풉니다.

### Jupyter를 직접 켤 때

노트북과 CSV는 **같은 폴더**에서 열어야 합니다.

```bash
# 회귀
jupyter notebook official_samples/regression/problem.ipynb

# 분류
jupyter notebook official_samples/classification/problem.ipynb
```

Colab을 쓰면 CSV를 함께 업로드하거나, 같은 폴더의 raw URL로 `pd.read_csv` 하세요.

## 주의

- 분류 Q10 `GridSearchCV`(RandomForest, `n_estimators` 최대 500, cv=5)는 데이터가 커서 **수 분** 걸릴 수 있습니다. 시험에서도 돌려 놓고 다른 문항을 이어 가세요.
- 분류 샘플 원본은 해설지라서 오류 정정 문항의 원본 버그 코드가 이미 수정되어 있었습니다. 문제 노트북의 7-3 / 9-1 / 11-1 / 12-1 오류는 **회귀 샘플과 같은 시험 유형**으로 재구성했습니다. 단답(42262, 237, 500, `FE_points_winery`)은 공식 해설 값입니다.
- 변수명(`df`, `data`, `X_train`, `y_valid`, `gs_rf`, `estop`, `history` 등)은 문제 지시 그대로 쓰세요. 채점이 변수명에 묶여 있습니다.
