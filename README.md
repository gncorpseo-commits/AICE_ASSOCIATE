# 🎯 AICE Associate 합격 프로젝트

## 📋 프로젝트 개요

| 항목 | 내용 |
|------|------|
| **목표** | AICE Associate 자격증 취득 |
| **학습 기간** | 5주 (하루 90분) |
| **총 학습 시간** | 약 45시간 |
| **합격 기준** | 80점 이상 (2025년 기준) |
| **모의고사** | 30회 (450문항) |

---

## 📁 프로젝트 구조

```
AICE_Associate/
│
├── README.md                       # 학습 가이드 (현재 파일)
├── requirements.txt                # 필요 라이브러리
│
├── basics/                         # 기초 학습
│   ├── pandas_basics.ipynb         # pandas 필수 패턴
│   └── preprocessing.ipynb         # 전처리 기초
│
├── templates/                      # 시험용 템플릿
│   ├── ml_pipeline.py              # ML 파이프라인 템플릿
│   └── quick_reference.md          # 빠른 참조 치트시트
│
└── mock_exams/                     # 모의고사 30회
    ├── level_1_basic/              # 🟢 기초 (1-10회)
    ├── level_2_intermediate/       # 🟡 중급 (11-20회)
    ├── level_3_advanced/           # 🔴 실전 (21-30회)
    └── data/                       # 30개 데이터셋
```

---

## 📅 5주 학습 로드맵

### Week 1-2: 기초 다지기 🟢
```
📁 basics/ + mock_exams/level_1_basic/

학습 내용:
• pandas 필수 패턴 (read, info, describe, isna)
• 전처리 (결측치, 인코딩, 파생변수)
• 시각화 (histplot, heatmap)

모의고사:
• mock_01 ~ mock_10 (하루 1회)
• 시간 제한 없이 천천히
• 패턴 익히기에 집중
```

### Week 3-4: 모델링 마스터 🟡
```
📁 mock_exams/level_2_intermediate/

학습 내용:
• 회귀: LinearRegression, RandomForestRegressor
• 분류: LogisticRegression, RandomForestClassifier
• 평가: RMSE, R², Accuracy, F1

모의고사:
• mock_11 ~ mock_20 (하루 1회)
• 90분 시간 제한 시작
• 틀린 문제 복습
```

### Week 5: 실전 연습 🔴
```
📁 mock_exams/level_3_advanced/

학습 내용:
• 실제 시험과 동일 조건
• 시간 관리 연습
• 변수명/해석 문장 체크

모의고사:
• mock_21 ~ mock_30 (하루 1-2회)
• 80점 이상 목표
• 최종 점검
```

---

## 📊 모의고사 구성 (15문항 × 30회 = 450문항)

### 🟢 Level 1: 기초 (1-10회)

| 회차 | 시나리오 | 유형 | 파일명 |
|------|----------|------|--------|
| 01 | 배달 소요시간 예측 | 회귀 | mock_01_delivery.ipynb |
| 02 | 월별 매출 예측 | 회귀 | mock_02_sales.ipynb |
| 03 | 기온 예측 | 회귀 | mock_03_temperature.ipynb |
| 04 | 주택 가격 예측 | 회귀 | mock_04_housing.ipynb |
| 05 | 교통량 예측 | 회귀 | mock_05_traffic.ipynb |
| 06 | 고객 이탈 예측 | 분류 | mock_06_churn.ipynb |
| 07 | 스팸 메일 분류 | 분류 | mock_07_spam.ipynb |
| 08 | 대출 승인 예측 | 분류 | mock_08_loan.ipynb |
| 09 | 질병 유무 예측 | 분류 | mock_09_disease.ipynb |
| 10 | 고객 만족도 분류 | 분류 | mock_10_satisfaction.ipynb |

### 🟡 Level 2: 중급 (11-20회)

| 회차 | 시나리오 | 유형 | 파일명 |
|------|----------|------|--------|
| 11 | 택시 도착시간 예측 | 회귀 | mock_11_taxi.ipynb |
| 12 | 상품 수요 예측 | 회귀 | mock_12_demand.ipynb |
| 13 | 에너지 소비 예측 | 회귀 | mock_13_energy.ipynb |
| 14 | 재고 수준 예측 | 회귀 | mock_14_inventory.ipynb |
| 15 | 대기시간 예측 | 회귀 | mock_15_waiting.ipynb |
| 16 | 금융 사기 탐지 | 분류 | mock_16_fraud.ipynb |
| 17 | 구매 전환 예측 | 분류 | mock_17_conversion.ipynb |
| 18 | 리뷰 감성 분류 | 분류 | mock_18_sentiment.ipynb |
| 19 | 신용 위험 등급 | 분류 | mock_19_credit.ipynb |
| 20 | 광고 클릭 예측 | 분류 | mock_20_click.ipynb |

### 🔴 Level 3: 실전 (21-30회)

| 회차 | 시나리오 | 유형 | 파일명 |
|------|----------|------|--------|
| 21 | 내비게이션 도착시간 ⭐ | 회귀 | mock_21_navigation.ipynb |
| 22 | 통신사 고객 해지 ⭐ | 분류 | mock_22_telecom.ipynb |
| 23 | 중고차 가격 예측 | 회귀 | mock_23_usedcar.ipynb |
| 24 | 제품 품질 예측 | 회귀 | mock_24_quality.ipynb |
| 25 | 구독 서비스 유지 | 분류 | mock_25_subscription.ipynb |
| 26 | 물류 배송시간 | 회귀 | mock_26_logistics.ipynb |
| 27 | 마케팅 캠페인 반응 | 분류 | mock_27_marketing.ipynb |
| 28 | 공장 생산량 예측 | 회귀 | mock_28_production.ipynb |
| 29 | 🏆 최종 모의 (회귀) | 회귀 | mock_29_final_reg.ipynb |
| 30 | 🏆 최종 모의 (분류) | 분류 | mock_30_final_clf.ipynb |

---

## ⚠️ 2025년 AICE Associate 변경사항

| 항목 | 기존 | 2025년 |
|------|------|--------|
| 문항 수 | 14문항 | **15문항** |
| 합격 기준 | 60점 | **80점** |
| 응시료 | 5만원대 | **80,000원** |
| 오픈북 | 자유 검색 | **7개 공식 문서만** |

### 📚 허용되는 사이트 (2025년 2회차~)
1. numpy.org
2. pandas.pydata.org
3. matplotlib.org
4. seaborn.pydata.org
5. tensorflow.org
6. scikit-learn.org
7. xgboost.readthedocs.io

---

## 🚀 시작하기

### 1. 환경 설정
```bash
pip install -r requirements.txt
```

### 2. Jupyter Notebook 실행
```bash
jupyter notebook
```

### 3. 학습 순서
1. `basics/` 폴더의 기초 노트북 학습
2. `templates/` 폴더의 템플릿 숙지
3. `mock_exams/level_1_basic/` 부터 순차적으로 풀이

---

## 📊 예상 점수 향상

| 단계 | 완료 후 예상 점수 |
|------|------------------|
| Level 1 완료 (10회) | 60-70점 |
| Level 2 완료 (20회) | 75-85점 |
| Level 3 완료 (30회) | **85-95점** ✅ |

---

## 💡 합격 팁

### ⭕ 해야 할 것
- 문제 지시사항 꼼꼼히 읽기
- 변수명 정확히 사용
- 간단한 모델 하나로 완주
- 결과 해석 문장 필수 작성
- 모든 셀 실행 후 제출

### ❌ 하지 말 것
- 복잡한 모델 여러 개 시도
- 하이퍼파라미터 튜닝에 시간 낭비
- 변수명 임의 변경
- 해석 없이 숫자만 출력
- 셀 실행 안 하고 제출

---

## 📞 시험 정보

- **공식 사이트**: https://aice.study/
- **시험 일정**: 연 6회 (2026년 기준)
- **결과 발표**: 시험 후 약 2주

---

**Good Luck! 🍀**
