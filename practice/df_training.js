const datasets = [
  { id: "iris", source: "Seaborn", name: "Iris", file: "datasets/iris.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "붓꽃 품종 분류 데이터 (샘플)" },
  { id: "tips", source: "Seaborn", name: "Tips", file: "datasets/tips.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "식당 팁/손님 정보 (샘플)" },
  { id: "titanic", source: "Seaborn", name: "Titanic", file: "datasets/titanic.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "타이타닉 생존자 정보 (샘플)" },
  { id: "penguins", source: "Seaborn", name: "Penguins", file: "datasets/penguins.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "펭귄 종별 측정치 (샘플)" },
  { id: "flights", source: "Seaborn", name: "Flights", file: "datasets/flights.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "월별 항공 승객 수 (샘플)" },
  { id: "exercise", source: "Seaborn", name: "Exercise", file: "datasets/exercise.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "운동/심박 데이터 (샘플)" },
  { id: "planets", source: "Seaborn", name: "Planets", file: "datasets/planets.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "외계행성 탐색 정보 (샘플)" },
  { id: "fmri", source: "Seaborn", name: "FMRI", file: "datasets/fmri.csv", url: "https://github.com/mwaskom/seaborn-data", desc: "뇌 스캔 신호 데이터 (샘플)" },
  { id: "winequality", source: "UCI", name: "Wine Quality (Red)", file: "datasets/winequality-red.csv", url: "https://archive.ics.uci.edu/ml/datasets/wine+quality", desc: "와인 화학 성분/품질 (샘플)" },
  { id: "student", source: "UCI", name: "Student Performance", file: "datasets/student-performance.csv", url: "https://archive.ics.uci.edu/ml/datasets/student+performance", desc: "학생 성적/환경 정보 (샘플)" }
];

const DATASET_URLS = {
  iris: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/iris.csv",
  tips: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/tips.csv",
  titanic: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/titanic.csv",
  penguins: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/penguins.csv",
  flights: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/flights.csv",
  exercise: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/exercise.csv",
  planets: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/planets.csv",
  fmri: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/fmri.csv",
  winequality: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/winequality-red.csv",
  student: "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/practice/datasets/student-performance.csv"
};

const glossary = {
  head: { ko: "앞부분 보기", pron: "헤드", en: "head", def: "데이터프레임 상단 N행을 확인하는 함수", usage: "df.head(5)", example: "df.head(3)" },
  info: { ko: "정보 요약", pron: "인포", en: "info", def: "컬럼, 결측치, dtype 요약을 출력", usage: "df.info()", example: "df.info()" },
  describe: { ko: "기초 통계", pron: "디스크라이브", en: "describe", def: "수치형 컬럼의 요약 통계를 계산", usage: "df.describe()", example: "df.describe()" },
  isna: { ko: "결측치 확인", pron: "이즈나", en: "isna", def: "결측치 여부를 True/False로 반환", usage: "df.isna().sum()", example: "df.isna().sum()" },
  fillna: { ko: "결측치 채우기", pron: "필나", en: "fillna", def: "결측치를 지정한 값으로 채움", usage: "df['{{num}}'].fillna(0)", example: "df['{{num}}'].fillna(df['{{num}}'].mean())" },
  dropna: { ko: "결측치 제거", pron: "드롭나", en: "dropna", def: "결측치가 있는 행/열 제거", usage: "df.dropna()", example: "df.dropna(subset=['{{num}}'])" },
  astype: { ko: "형변환", pron: "애즈타입", en: "astype", def: "컬럼의 자료형 변환", usage: "df['{{cat}}'].astype('category')", example: "df['{{cat}}'] = df['{{cat}}'].astype('category')" },
  sort_values: { ko: "정렬", pron: "소트 밸류즈", en: "sort_values", def: "컬럼 기준 정렬", usage: "df.sort_values('{{num}}')", example: "df.sort_values('{{num}}', ascending=False)" },
  query: { ko: "조건 필터", pron: "쿼리", en: "query", def: "문자열 조건으로 필터링", usage: "df.query('{{num}} > {{num}}.mean()')", example: "df.query('{{num}} > {{num}}.mean()')" },
  loc: { ko: "라벨 인덱싱", pron: "록", en: "loc", def: "행/열 라벨 기반 선택", usage: "df.loc[0:3, ['{{cat}}','{{num}}']]", example: "df.loc[0:3, ['{{cat}}','{{num}}']]" },
  iloc: { ko: "정수 인덱싱", pron: "아이록", en: "iloc", def: "정수 위치 기반 선택", usage: "df.iloc[rows, cols]", example: "df.iloc[:5, 0:3]" },
  groupby: { ko: "그룹 집계", pron: "그룹바이", en: "groupby", def: "범주별로 묶어서 집계", usage: "df.groupby('{{cat}}').mean()", example: "df.groupby('{{cat}}')['{{num}}'].mean()" },
  agg: { ko: "집계", pron: "애그", en: "agg", def: "다중 집계 함수 적용", usage: "df.groupby('{{cat}}').agg(['mean','max'])", example: "df.groupby('{{cat}}')['{{num}}'].agg(['mean','median'])" },
  pivot_table: { ko: "피벗 테이블", pron: "피벗 테이블", en: "pivot_table", def: "행/열 기준 교차 집계", usage: "pd.pivot_table(df, values='{{num}}', index='{{cat}}', columns='{{cat2}}')", example: "pd.pivot_table(df, values='{{num}}', index='{{cat}}', columns='{{cat2}}')" },
  merge: { ko: "병합", pron: "머지", en: "merge", def: "공통 키로 데이터프레임 결합", usage: "pd.merge(df1, df2, on='id')", example: "pd.merge(a, b, on='id', how='left')" },
  concat: { ko: "연결", pron: "컨캣", en: "concat", def: "행/열 방향 결합", usage: "pd.concat([a,b])", example: "pd.concat([train, test], axis=0)" },
  value_counts: { ko: "빈도수", pron: "밸류 카운츠", en: "value_counts", def: "범주 빈도 계산", usage: "df['{{cat}}'].value_counts()", example: "df['{{cat}}'].value_counts()" },
  unique: { ko: "고유값", pron: "유니크", en: "unique", def: "고유 값 목록 반환", usage: "df['{{cat}}'].unique()", example: "df['{{cat}}'].unique()" },
  nunique: { ko: "고유값 개수", pron: "뉴-유니크", en: "nunique", def: "고유 값 개수 반환", usage: "df['{{cat}}'].nunique()", example: "df['{{cat}}'].nunique()" },
  cut: { ko: "구간화", pron: "컷", en: "cut", def: "연속형을 구간으로 분할", usage: "pd.cut(df['{{num}}'], bins=3)", example: "pd.cut(df['{{num}}'], bins=3)" },
  qcut: { ko: "분위수 구간화", pron: "큐컷", en: "qcut", def: "동일 개수 기준 구간화", usage: "pd.qcut(df['{{num}}'], q=4)", example: "pd.qcut(df['{{num}}'], q=4)" },
  to_datetime: { ko: "날짜 변환", pron: "투 데이트타임", en: "to_datetime", def: "문자열을 datetime으로 변환", usage: "pd.to_datetime(df['{{cat}}'])", example: "df['{{cat}}'] = pd.to_datetime(df['{{cat}}'])" },
  dt: { ko: "날짜 접근자", pron: "디티", en: "dt", def: "datetime 속성 접근", usage: "df['{{cat}}'].dt.year", example: "df['{{cat}}'].dt.month" },
  apply: { ko: "행/열 함수 적용", pron: "어플라이", en: "apply", def: "함수를 행/열에 적용", usage: "df['{{num}}'].apply(func)", example: "df['{{num}}'].apply(lambda x: x * 2)" },
  map: { ko: "값 매핑", pron: "맵", en: "map", def: "값을 다른 값으로 치환", usage: "df['{{cat}}'].map(dict)", example: "df['{{cat}}'].map({'A':1,'B':0})" },
  replace: { ko: "치환", pron: "리플레이스", en: "replace", def: "특정 값을 다른 값으로 변경", usage: "df['{{cat}}'].replace(old, new)", example: "df['{{cat}}'].replace('A', 'B')" },
  drop_duplicates: { ko: "중복 제거", pron: "드롭 듀플리케이츠", en: "drop_duplicates", def: "중복 행 제거", usage: "df.drop_duplicates()", example: "df.drop_duplicates(subset=['{{cat}}'])" },
  sample: { ko: "무작위 샘플", pron: "샘플", en: "sample", def: "무작위 샘플 추출", usage: "df.sample(n=5)", example: "df.sample(frac=0.1, random_state=42)" },
  get_dummies: { ko: "원-핫 인코딩", pron: "겟 더미즈", en: "get_dummies", def: "범주형 컬럼을 원-핫 인코딩", usage: "pd.get_dummies(df, columns=['{{cat}}'])", example: "pd.get_dummies(df, columns=['{{cat}}'])" },
  train_test_split: { ko: "학습/검증 분리", pron: "트레인 테스트 스플릿", en: "train_test_split", def: "데이터를 학습/검증으로 분리", usage: "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)", example: "train_test_split(X, y, test_size=0.2, random_state=42)" },
  standard_scaler: { ko: "표준화", pron: "스탠다드 스케일러", en: "StandardScaler", def: "평균 0, 표준편차 1로 스케일링", usage: "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)", example: "StandardScaler().fit_transform(X)" },
  minmax_scaler: { ko: "정규화", pron: "민맥스 스케일러", en: "MinMaxScaler", def: "0~1 범위로 스케일링", usage: "from sklearn.preprocessing import MinMaxScaler\nscaler = MinMaxScaler()\nX_scaled = scaler.fit_transform(X)", example: "MinMaxScaler().fit_transform(X)" },
  linear_regression: { ko: "선형회귀", pron: "리니어 리그레션", en: "LinearRegression", def: "회귀 문제를 위한 선형 모델", usage: "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)", example: "LinearRegression().fit(X_train, y_train)" },
  logistic_regression: { ko: "로지스틱 회귀", pron: "로지스틱 리그레션", en: "LogisticRegression", def: "분류 문제를 위한 로지스틱 회귀", usage: "from sklearn.linear_model import LogisticRegression\nmodel = LogisticRegression(max_iter=1000)\nmodel.fit(X_train, y_train)", example: "LogisticRegression(max_iter=1000).fit(X_train, y_train)" },
  eval_regression: { ko: "회귀 평가", pron: "이벨류에이션", en: "RMSE/R2", def: "회귀 성능 지표 계산", usage: "from sklearn.metrics import mean_squared_error, r2_score\nrmse = (mean_squared_error(y_test, y_pred) ** 0.5)\nr2 = r2_score(y_test, y_pred)", example: "rmse = (mean_squared_error(y_test, y_pred) ** 0.5)" },
  eval_regression_full: { ko: "회귀 평가", pron: "이벨류에이션", en: "RMSE/MAE/R2", def: "회귀 성능 지표 계산", usage: "from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score\nrmse = (mean_squared_error(y_test, y_pred) ** 0.5)\nmae = mean_absolute_error(y_test, y_pred)\nr2 = r2_score(y_test, y_pred)", example: "mae = mean_absolute_error(y_test, y_pred)" },
  eval_classification: { ko: "분류 평가", pron: "이벨류에이션", en: "Accuracy/F1", def: "분류 성능 지표 계산", usage: "from sklearn.metrics import accuracy_score, f1_score\nacc = accuracy_score(y_test, y_pred)\nf1 = f1_score(y_test, y_pred, average='weighted')", example: "accuracy_score(y_test, y_pred)" },
  eval_classification_full: { ko: "분류 평가", pron: "이벨류에이션", en: "Accuracy/Precision/Recall/F1", def: "분류 성능 지표 계산", usage: "from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score\nacc = accuracy_score(y_test, y_pred)\nprec = precision_score(y_test, y_pred, average='weighted')\nrec = recall_score(y_test, y_pred, average='weighted')\nf1 = f1_score(y_test, y_pred, average='weighted')", example: "f1 = f1_score(y_test, y_pred, average='weighted')" },
  pipeline_regression: { ko: "회귀 파이프라인", pron: "파이프라인", en: "Pipeline Regression", def: "전처리+모델 학습 파이프라인 구성", usage: "from sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LinearRegression\nX = df.drop(['{{num}}'], axis=1).select_dtypes(include='number')\ny = df['{{num}}']\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)\nmodel = LinearRegression()\nmodel.fit(X_train_scaled, y_train)\ny_pred = model.predict(X_test_scaled)", example: "y_pred = model.predict(X_test_scaled)" },
  pipeline_classification: { ko: "분류 파이프라인", pron: "파이프라인", en: "Pipeline Classification", def: "전처리+모델 학습 파이프라인 구성", usage: "from sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\nX = pd.get_dummies(df.drop(['{{cat}}'], axis=1), drop_first=True)\ny = df['{{cat}}']\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)\nmodel = LogisticRegression(max_iter=1000)\nmodel.fit(X_train_scaled, y_train)\ny_pred = model.predict(X_test_scaled)", example: "y_pred = model.predict(X_test_scaled)" },
  leakage_check: { ko: "데이터 누수 방지", pron: "데이터 누수", en: "Leakage Check", def: "전처리 순서를 올바르게 유지", usage: "from sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nX = df.drop(['{{num}}'], axis=1).select_dtypes(include='number')\ny = df['{{num}}']\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)", example: "X_test_scaled = scaler.transform(X_test)" },
  interpret_scatter: { ko: "시각화 해석", pron: "인터프릿", en: "Plot Interpretation", def: "그래프를 보고 인사이트를 작성", usage: "insight = 'Scatter shows positive relationship between {{num}} and {{num2}}.'", example: "insight" },
  seaborn_scatter: { ko: "산점도", pron: "스캐터", en: "seaborn.scatterplot", def: "두 변수의 관계를 산점도로 시각화", usage: "import seaborn as sns\nsns.scatterplot(data=df, x='{{num}}', y='{{num2}}')", example: "sns.scatterplot(data=df, x='{{num}}', y='{{num2}}')" },
  seaborn_box: { ko: "박스플롯", pron: "박스 플롯", en: "seaborn.boxplot", def: "범주별 분포를 박스플롯으로 시각화", usage: "import seaborn as sns\nsns.boxplot(data=df, x='{{cat}}', y='{{num}}')", example: "sns.boxplot(data=df, x='{{cat}}', y='{{num}}')" },
  seaborn_count: { ko: "카운트플롯", pron: "카운트 플롯", en: "seaborn.countplot", def: "범주형 빈도를 시각화", usage: "import seaborn as sns\nsns.countplot(data=df, x='{{cat}}')", example: "sns.countplot(data=df, x='{{cat}}')" },
  matplotlib_hist: { ko: "히스토그램", pron: "히스토그램", en: "matplotlib.hist", def: "수치형 분포를 히스토그램으로 시각화", usage: "import matplotlib.pyplot as plt\nplt.hist(df['{{num}}'], bins=20)\nplt.show()", example: "plt.hist(df['{{num}}'], bins=20)" },
  matplotlib_line: { ko: "라인차트", pron: "라인 차트", en: "matplotlib.plot", def: "두 수치형 변수의 추이를 선 그래프로 표시", usage: "import matplotlib.pyplot as plt\nplt.plot(df['{{num}}'], df['{{num2}}'])\nplt.show()", example: "plt.plot(df['{{num}}'], df['{{num2}}'])" },
  matplotlib_bar: { ko: "막대차트", pron: "바 차트", en: "matplotlib.bar", def: "범주형 집계를 막대 그래프로 시각화", usage: "import matplotlib.pyplot as plt\ncounts = df['{{cat}}'].value_counts()\nplt.bar(counts.index, counts.values)\nplt.show()", example: "plt.bar(counts.index, counts.values)" },
  numpy_mean: { ko: "평균", pron: "민", en: "numpy.mean", def: "수치형 평균 계산", usage: "import numpy as np\nnp.mean(df['{{num}}'])", example: "np.mean(df['{{num}}'])" },
  numpy_std: { ko: "표준편차", pron: "스탠다드 데비에이션", en: "numpy.std", def: "수치형 표준편차 계산", usage: "import numpy as np\nnp.std(df['{{num}}'])", example: "np.std(df['{{num}}'])" },
  numpy_corr: { ko: "상관계수", pron: "코릴레이션", en: "numpy.corrcoef", def: "두 수치형 변수의 상관계수 계산", usage: "import numpy as np\nnp.corrcoef(df['{{num}}'], df['{{num2}}'])", example: "np.corrcoef(df['{{num}}'], df['{{num2}}'])" },
  tf_regression: { ko: "텐서플로 회귀", pron: "텐서플로", en: "TensorFlow Regression", def: "간단한 Dense 모델로 회귀 학습", usage: "import tensorflow as tf\nfrom tensorflow import keras\nX = df.drop(['{{num}}'], axis=1).select_dtypes(include='number')\ny = df['{{num}}']\nmodel = keras.Sequential([keras.layers.Dense(32, activation='relu'), keras.layers.Dense(1)])\nmodel.compile(optimizer='adam', loss='mse')\nmodel.fit(X, y, epochs=3, verbose=0)\nmodel.predict(X[:5])", example: "model.predict(X[:5])" },
  tf_classification: { ko: "텐서플로 분류", pron: "텐서플로", en: "TensorFlow Classification", def: "간단한 Dense 모델로 분류 학습", usage: "import tensorflow as tf\nfrom tensorflow import keras\nX = pd.get_dummies(df.drop(['{{cat}}'], axis=1), drop_first=True)\ny = pd.factorize(df['{{cat}}'])[0]\nmodel = keras.Sequential([keras.layers.Dense(32, activation='relu'), keras.layers.Dense(1, activation='sigmoid')])\nmodel.compile(optimizer='adam', loss='binary_crossentropy')\nmodel.fit(X, y, epochs=3, verbose=0)\nmodel.predict(X[:5])", example: "model.predict(X[:5])" },
  xgb_regression: { ko: "XGBoost 회귀", pron: "엑스지부스트", en: "XGBoost Regressor", def: "XGBoost 회귀 모델 학습", usage: "import xgboost as xgb\nX = df.drop(['{{num}}'], axis=1).select_dtypes(include='number')\ny = df['{{num}}']\nmodel = xgb.XGBRegressor(n_estimators=20, max_depth=3, learning_rate=0.1)\nmodel.fit(X, y)\nmodel.predict(X[:5])", example: "model.predict(X[:5])" },
  xgb_classification: { ko: "XGBoost 분류", pron: "엑스지부스트", en: "XGBoost Classifier", def: "XGBoost 분류 모델 학습", usage: "import xgboost as xgb\nX = pd.get_dummies(df.drop(['{{cat}}'], axis=1), drop_first=True)\ny = pd.factorize(df['{{cat}}'])[0]\nmodel = xgb.XGBClassifier(n_estimators=20, max_depth=3, learning_rate=0.1, eval_metric='logloss')\nmodel.fit(X, y)\nmodel.predict(X[:5])", example: "model.predict(X[:5])" }
};

const datasetSchemas = {
  iris: { numeric: ["sepal_length", "sepal_width", "petal_length", "petal_width"], categorical: ["species"] },
  tips: { numeric: ["total_bill", "tip", "size"], categorical: ["sex", "smoker", "day", "time"] },
  titanic: { numeric: ["age", "sibsp", "parch", "fare"], categorical: ["survived", "pclass", "sex", "embarked", "class", "who", "embark_town", "alive", "alone"] },
  penguins: { numeric: ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "year"], categorical: ["species", "island", "sex"] },
  flights: { numeric: ["year", "passengers"], categorical: ["month"], dateParts: { year: "year", month: "month" } },
  exercise: { numeric: ["pulse"], categorical: ["diet", "kind", "time", "id"] },
  planets: { numeric: ["number", "orbital_period", "mass", "distance", "year"], categorical: ["method"] },
  fmri: { numeric: ["signal", "timepoint"], categorical: ["event", "region", "subject"] },
  winequality: { numeric: ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"], categorical: [] },
  student: { numeric: ["age", "Medu", "Fedu", "traveltime", "studytime", "failures", "famrel", "freetime", "goout", "Dalc", "Walc", "health", "absences", "G1", "G2", "G3"], categorical: ["school", "sex", "address", "famsize", "Pstatus", "Mjob", "Fjob", "reason", "guardian", "schoolsup", "famsup", "paid", "activities", "nursery", "higher", "internet", "romantic"] }
};

function pick(list, fallback) {
  if (list && list.length) return list[0];
  return fallback;
}

function pickSecond(list, fallback) {
  if (list && list.length > 1) return list[1];
  return fallback || pick(list, "");
}

const templates = {
  easy: [
    { op: "head", taskKo: "상위 5행을 확인하세요.", taskEn: "Show the first 5 rows.", needs: {} },
    { op: "info", taskKo: "데이터 타입과 결측치를 요약하세요.", taskEn: "Summarize dtypes and missing values.", needs: {} },
    { op: "describe", taskKo: "기초 통계량을 확인하세요.", taskEn: "Check basic statistics.", needs: {} },
    { op: "isna", taskKo: "컬럼별 결측치 개수를 구하세요.", taskEn: "Count missing values per column.", needs: {} },
    { op: "value_counts", taskKo: "범주형 컬럼 {{cat}}의 빈도를 계산하세요.", taskEn: "Compute value counts of {{cat}}.", needs: { cat: 1 } },
    { op: "unique", taskKo: "컬럼 {{cat}}의 고유값을 출력하세요.", taskEn: "List unique values in {{cat}}.", needs: { cat: 1 } },
    { op: "nunique", taskKo: "컬럼 {{cat}}의 고유값 개수를 계산하세요.", taskEn: "Count unique values in {{cat}}.", needs: { cat: 1 } },
    { op: "sort_values", taskKo: "수치형 컬럼 {{num}} 기준으로 내림차순 정렬하세요.", taskEn: "Sort by {{num}} descending.", needs: { num: 1 } }
  ],
  medium: [
    { op: "fillna", taskKo: "수치형 컬럼 {{num}}의 결측치를 평균으로 채우세요.", taskEn: "Fill missing values in {{num}} with mean.", needs: { num: 1 } },
    { op: "dropna", taskKo: "컬럼 {{num}} 결측치가 있는 행을 제거하세요.", taskEn: "Drop rows with missing {{num}}.", needs: { num: 1 } },
    { op: "astype", taskKo: "컬럼 {{cat}} 타입을 category로 변환하세요.", taskEn: "Convert {{cat}} to category dtype.", needs: { cat: 1 } },
    { op: "query", taskKo: "{{num}}가 평균보다 큰 행을 필터링하세요.", taskEn: "Filter rows where {{num}} is above mean.", needs: { num: 1 } },
    { op: "loc", taskKo: "{{cat}}, {{num}} 열만 선택하세요.", taskEn: "Select columns {{cat}} and {{num}} using loc.", needs: { cat: 1, num: 1 } },
    { op: "iloc", taskKo: "상위 5행, 앞 3열을 선택하세요.", taskEn: "Select top 5 rows and first 3 columns.", needs: {} },
    { op: "groupby", taskKo: "{{cat}}별 {{num}} 평균을 계산하세요.", taskEn: "Compute mean of {{num}} by {{cat}}.", needs: { cat: 1, num: 1 } },
    { op: "agg", taskKo: "{{cat}}별 {{num}}의 평균과 최대값을 계산하세요.", taskEn: "Aggregate {{num}} mean and max by {{cat}}.", needs: { cat: 1, num: 1 } },
    { op: "pivot_table", taskKo: "피벗: index={{cat}}, columns={{cat2}}, values={{num}}.", taskEn: "Pivot with index={{cat}}, columns={{cat2}}, values={{num}}.", needs: { cat: 2, num: 1 } },
    { op: "cut", taskKo: "{{num}}를 3구간으로 나누세요.", taskEn: "Bin {{num}} into 3 bins.", needs: { num: 1 } },
    { op: "qcut", taskKo: "{{num}}를 4분위로 나누세요.", taskEn: "Quantile-bin {{num}} into 4.", needs: { num: 1 } },
    { op: "apply", taskKo: "{{num}}에 대해 제곱 컬럼을 생성하세요.", taskEn: "Create squared feature from {{num}} using apply.", needs: { num: 1 } },
    { op: "map", taskKo: "{{cat}}을 숫자 값으로 매핑하세요.", taskEn: "Map {{cat}} to numeric values.", needs: { cat: 1 } },
    { op: "drop_duplicates", taskKo: "{{cat}} 기준 중복 행을 제거하세요.", taskEn: "Drop duplicates based on {{cat}}.", needs: { cat: 1 } },
    { op: "sample", taskKo: "랜덤으로 5행을 추출하세요.", taskEn: "Sample 5 random rows.", needs: {} },
    { op: "get_dummies", taskKo: "범주형 컬럼 {{cat}}을 원-핫 인코딩하세요.", taskEn: "One-hot encode {{cat}}.", needs: { cat: 1 } },
    { op: "train_test_split", taskKo: "타겟 {{num}}을 기준으로 학습/검증을 분리하세요.", taskEn: "Split features/target using {{num}}.", needs: { num: 1 } }
  ],
  hard: [
    { op: "merge", taskKo: "데이터를 index 키로 분리 후 병합하세요.", taskEn: "Split by index and merge back.", needs: { num: 1 } },
    { op: "concat", taskKo: "상위 5행과 하위 5행을 연결하세요.", taskEn: "Concatenate top 5 and bottom 5 rows.", needs: {} },
    { op: "groupby", taskKo: "{{cat}}와 {{cat2}}로 그룹화하여 {{num}} 평균을 계산하세요.", taskEn: "Group by {{cat}} and {{cat2}}, mean {{num}}.", needs: { cat: 2, num: 1 } },
    { op: "pivot_table", taskKo: "피벗: index={{cat}}, columns={{cat2}}, values={{num}} (agg=mean).", taskEn: "Pivot with mean aggregation.", needs: { cat: 2, num: 1 } },
    { op: "apply", taskKo: "{{num}}가 상위 25%면 1, 아니면 0을 생성하세요.", taskEn: "Create binary flag for top 25% {{num}}.", needs: { num: 1 } },
    { op: "replace", taskKo: "{{cat}} 값 일부를 치환하세요.", taskEn: "Replace some values in {{cat}}.", needs: { cat: 1 } }
  ],
  aice: [
    { op: "get_dummies", taskKo: "문제 지시에 따라 {{cat}}을 원-핫 인코딩하세요.", taskEn: "One-hot encode {{cat}} as required.", needs: { cat: 1 } },
    { op: "standard_scaler", taskKo: "수치형 피처를 표준화하세요.", taskEn: "Standardize numeric features.", needs: { num: 1 } },
    { op: "minmax_scaler", taskKo: "수치형 피처를 0~1 범위로 정규화하세요.", taskEn: "Normalize numeric features to 0-1.", needs: { num: 1 } },
    { op: "train_test_split", taskKo: "피처/타겟을 분리하고 학습/검증 셋으로 나누세요.", taskEn: "Split features/target and train/test.", needs: { num: 1 } },
    { op: "linear_regression", taskKo: "회귀 모델을 학습하세요. 타겟은 {{num}}.", taskEn: "Train a regression model with target {{num}}.", needs: { num: 1 } },
    { op: "logistic_regression", taskKo: "분류 모델을 학습하세요. 타겟은 {{cat}}.", taskEn: "Train a classifier with target {{cat}}.", needs: { cat: 1 } },
    { op: "eval_regression", taskKo: "회귀 모델을 평가하세요 (RMSE/R2).", taskEn: "Evaluate regression with RMSE/R2.", needs: { num: 1 } },
    { op: "eval_classification", taskKo: "분류 모델을 평가하세요 (Accuracy/F1).", taskEn: "Evaluate classifier with Accuracy/F1.", needs: { cat: 1 } },
    { op: "groupby", taskKo: "{{cat}}별 {{num}} 평균을 산출해 인사이트를 작성하세요.", taskEn: "Compute mean {{num}} by {{cat}}.", needs: { cat: 1, num: 1 } },
    { op: "pivot_table", taskKo: "피벗 테이블로 핵심 지표를 요약하세요.", taskEn: "Summarize key metrics with pivot table.", needs: { cat: 2, num: 1 } }
  ],
  pipeline: [
    { op: "pipeline_regression", taskKo: "{{num}} 타겟 회귀 파이프라인을 구성하세요.", taskEn: "Build a regression pipeline for {{num}}.", needs: { num: 1 } },
    { op: "pipeline_classification", taskKo: "{{cat}} 타겟 분류 파이프라인을 구성하세요.", taskEn: "Build a classification pipeline for {{cat}}.", needs: { cat: 1 } },
    { op: "leakage_check", taskKo: "전처리 순서를 올바르게 적용해 누수를 방지하세요.", taskEn: "Apply preprocessing in the right order to avoid leakage.", needs: { num: 1 } }
  ],
  evaluation: [
    { op: "eval_regression_full", taskKo: "회귀 평가 지표(RMSE/MAE/R2)를 계산하세요.", taskEn: "Compute RMSE/MAE/R2 for regression.", needs: { num: 1 } },
    { op: "eval_classification_full", taskKo: "분류 지표(Accuracy/Precision/Recall/F1)를 계산하세요.", taskEn: "Compute Accuracy/Precision/Recall/F1.", needs: { cat: 1 } }
  ],
  interpret: [
    { op: "interpret_scatter", taskKo: "{{num}}와 {{num2}} 산점도를 보고 한 줄 인사이트를 작성하세요.", taskEn: "Write one-line insight from {{num}} vs {{num2}}.", needs: { num: 2 } }
  ],
  viz: [
    { op: "seaborn_scatter", taskKo: "{{num}}와 {{num2}}의 관계를 산점도로 그리세요.", taskEn: "Draw a scatter plot of {{num}} vs {{num2}}.", needs: { num: 2 } },
    { op: "seaborn_box", taskKo: "{{cat}}별 {{num}} 분포를 박스플롯으로 그리세요.", taskEn: "Draw a boxplot of {{num}} by {{cat}}.", needs: { cat: 1, num: 1 } },
    { op: "seaborn_count", taskKo: "{{cat}}의 빈도를 카운트플롯으로 그리세요.", taskEn: "Draw a countplot for {{cat}}.", needs: { cat: 1 } },
    { op: "matplotlib_hist", taskKo: "{{num}} 분포를 히스토그램으로 표시하세요.", taskEn: "Plot a histogram of {{num}}.", needs: { num: 1 } },
    { op: "matplotlib_line", taskKo: "{{num}}와 {{num2}}를 라인차트로 그리세요.", taskEn: "Plot a line chart for {{num}} vs {{num2}}.", needs: { num: 2 } },
    { op: "matplotlib_bar", taskKo: "{{cat}} 빈도를 막대차트로 표시하세요.", taskEn: "Plot a bar chart of {{cat}} counts.", needs: { cat: 1 } }
  ],
  numpy: [
    { op: "numpy_mean", taskKo: "{{num}}의 평균을 계산하세요.", taskEn: "Compute the mean of {{num}}.", needs: { num: 1 } },
    { op: "numpy_std", taskKo: "{{num}}의 표준편차를 계산하세요.", taskEn: "Compute the standard deviation of {{num}}.", needs: { num: 1 } },
    { op: "numpy_corr", taskKo: "{{num}}와 {{num2}}의 상관계수를 계산하세요.", taskEn: "Compute correlation of {{num}} and {{num2}}.", needs: { num: 2 } }
  ],
  tensorflow: [
    { op: "tf_regression", taskKo: "{{num}} 타겟으로 간단한 회귀 모델을 학습하세요.", taskEn: "Train a regression model with target {{num}}.", needs: { num: 1 } },
    { op: "tf_classification", taskKo: "{{cat}} 타겟으로 간단한 분류 모델을 학습하세요.", taskEn: "Train a classifier with target {{cat}}.", needs: { cat: 1 } }
  ],
  xgboost: [
    { op: "xgb_regression", taskKo: "{{num}} 타겟으로 XGBoost 회귀 모델을 학습하세요.", taskEn: "Train XGBoost regressor with target {{num}}.", needs: { num: 1 } },
    { op: "xgb_classification", taskKo: "{{cat}} 타겟으로 XGBoost 분류 모델을 학습하세요.", taskEn: "Train XGBoost classifier with target {{cat}}.", needs: { cat: 1 } }
  ]
};

function buildQuestion(id, diff, ds, template) {
  const g = glossary[template.op];
  const schema = datasetSchemas[ds.id] || { numeric: [], categorical: [] };
  const num = pick(schema.numeric, "col");
  const num2 = pickSecond(schema.numeric, num);
  const cat = pick(schema.categorical, "col");
  const cat2 = pickSecond(schema.categorical, cat);
  const replacements = { "{{num}}": num, "{{num2}}": num2, "{{cat}}": cat, "{{cat2}}": cat2 };
  const fill = (text) => Object.keys(replacements).reduce((acc, key) => acc.replaceAll(key, replacements[key]), text);
  const title = `${id}. (${diff.toUpperCase()}) ${template.op} - ${ds.name}`;
  const problemKo = `${fill(template.taskKo)} 데이터셋: ${ds.name}.`;
  const problemEn = `Dataset: ${ds.name}. ${fill(template.taskEn)}`;
  const hintKo = `힌트: ${g.en} (${g.pron})를 사용해 보세요.`;
  const hintEn = `Hint: Try using ${g.en}.`;
  const basePrep = [
    `# load dataset`,
    `import pandas as pd`,
    `df = pd.read_csv(DATASET_URL)`
  ];
  const needsXY = [
    "train_test_split",
    "linear_regression",
    "logistic_regression",
    "eval_regression",
    "eval_classification",
    "eval_regression_full",
    "eval_classification_full",
    "pipeline_regression",
    "pipeline_classification",
    "leakage_check",
    "standard_scaler",
    "minmax_scaler",
    "tf_regression",
    "tf_classification",
    "xgb_regression",
    "xgb_classification"
  ];
  const isClassification = ["logistic_regression", "eval_classification", "eval_classification_full", "pipeline_classification", "tf_classification", "xgb_classification"].includes(template.op);
  const targetCol = isClassification ? (cat || num) : num;
  const xyBlock = [
    ``,
    `# basic feature/target split`,
    `X = df.drop(['${targetCol}'], axis=1)`,
    `y = df['${targetCol}']`
  ];
  const answer = [
    ...basePrep,
    ...(needsXY.includes(template.op) ? xyBlock : [""]),
    `# ${g.en} example`,
    fill(g.usage)
  ].join("\n");
  const detail = {
    term: g.en,
    meaningKo: g.ko,
    pron: g.pron,
    defKo: g.def,
    defEn: g.defEn || `Definition: ${g.en}.`,
    usage: fill(g.usage),
    example: fill(g.example),
    columns: { num, num2, cat, cat2 }
  };
  const libraries = ["pandas"];
  if (["train_test_split", "standard_scaler", "minmax_scaler", "eval_regression_full", "eval_classification_full", "pipeline_regression", "pipeline_classification", "leakage_check"].includes(template.op)) {
    libraries.push("sklearn");
  }
  if (["linear_regression", "logistic_regression"].includes(template.op)) {
    libraries.push("sklearn");
  }
  if (["eval_regression", "eval_classification"].includes(template.op)) {
    libraries.push("sklearn");
  }
  if (template.op.startsWith("seaborn_")) {
    libraries.push("seaborn", "matplotlib");
  }
  if (template.op.startsWith("matplotlib_")) {
    libraries.push("matplotlib");
  }
  if (template.op.startsWith("numpy_")) {
    libraries.push("numpy");
  }
  if (template.op.startsWith("tf_")) {
    libraries.push("tensorflow");
  }
  if (template.op.startsWith("xgb_")) {
    libraries.push("xgboost");
  }
  return {
    id,
    diff,
    datasetId: ds.id,
    datasetName: ds.name,
    source: ds.source,
    title,
    problemKo,
    problemEn,
    hintKo,
    hintEn,
    answer,
    detail,
    libraries
  };
}

function generateQuestions() {
  const list = [];
  let id = 1;
  const easyCount = 100;
  const mediumCount = 170;
  const hardCount = 60;
  const aiceCount = 60;
  const vizCount = 30;
  const numpyCount = 20;
  const tfCount = 10;
  const xgbCount = 10;
  const pipelineCount = 20;
  const evaluationCount = 15;
  const interpretCount = 5;
  const dsList = datasets;

  function pushQuestions(count, diff, templateList) {
    for (let i = 0; i < count; i++) {
      const ds = dsList[i % dsList.length];
      const tpl = templateList[i % templateList.length];
      list.push(buildQuestion(id++, diff, ds, tpl));
    }
  }

  pushQuestions(easyCount, "easy", templates.easy);
  pushQuestions(mediumCount, "medium", templates.medium);
  pushQuestions(hardCount, "hard", templates.hard);
  pushQuestions(aiceCount, "medium", templates.aice);
  pushQuestions(vizCount, "medium", templates.viz);
  pushQuestions(numpyCount, "medium", templates.numpy);
  pushQuestions(tfCount, "hard", templates.tensorflow);
  pushQuestions(xgbCount, "hard", templates.xgboost);
  pushQuestions(pipelineCount, "medium", templates.pipeline);
  pushQuestions(evaluationCount, "medium", templates.evaluation);
  pushQuestions(interpretCount, "easy", templates.interpret);
  return list;
}

const questions = generateQuestions();
const PAGE_SIZE = 1;
const MAX_RENDERED = 1;
let filteredQuestions = questions;
let renderedCount = 0;
let observer = null;
const questionMap = new Map(questions.map(q => [q.id, q]));
let adminDebug = false;
let adminToggleLoaded = 0;
let adminLogEl = null;
let adminLastEventEl = null;
let adminRenderCountEl = null;
let adminToggleLoadedEl = null;
let adminDebugToggleEl = null;
let adminClearLogEl = null;
let adminRunTestsEl = null;
let adminCopyTestEl = null;
let adminTestResultEl = null;
let adminFirstRenderMsEl = null;
let adminLastToggleMsEl = null;
let uxSpeedEl = null;
let uxFlowEl = null;
let uxNotebookEl = null;
let uxNotesEl = null;
let uxSaveEl = null;
let uxLastSavedEl = null;
const ADMIN_LOG_MAX = 200;
let currentQuestionId = null;
const sessionStart = performance.now();
let firstRenderMs = null;
let questionProgressEl = null;
let nextQuestionBtn = null;
let runDebugTestBtn = null;

function renderDatasets() {
  const container = document.getElementById("datasetList");
  container.innerHTML = datasets.map(d => `
    <div class="dataset-card">
      <h3>${d.name} <span class="tag ${d.source === "UCI" ? "hard" : "easy"}">${d.source}</span></h3>
      <p>${d.desc}</p>
      <p>Source: <a href="${d.url}" target="_blank" rel="noopener noreferrer">${d.url}</a></p>
      <a class="download" href="${d.file}" download>⬇️ Download CSV</a>
    </div>
  `).join("");
}

function renderQuestions(list, append = false) {
  const container = document.getElementById("questionList");
  if (!append) container.innerHTML = "";
  container.insertAdjacentHTML("beforeend", list.map(q => `
    <div class="question" data-qid="${q.id}">
      <div class="meta">
        <span class="tag ${q.diff}">${q.diff}</span>
        <strong>${q.datasetName}</strong> · ${q.source}
      </div>
      <div class="question-header">
        <h3>${q.title}</h3>
        <div class="copy-answer-wrap">
          <span class="copy-answer-label">정답코드복사</span>
          <button class="copy-answer-icon" data-id="${q.id}" type="button" title="정답 코드 복사">⧉</button>
        </div>
      </div>
      <p><strong>KR:</strong> ${q.problemKo}</p>
      <p><strong>EN:</strong> ${q.problemEn}</p>
      <div class="answer-input">
        <label>내 답안 (힌트 보기 전 작성)</label>
        <textarea rows="6" placeholder="여기에 코드를 입력하세요." spellcheck="false"></textarea>
        <div class="answer-actions">
          <button class="answer-run-btn" data-id="${q.id}">실행</button>
          <button class="answer-check-btn" data-id="${q.id}">정답 확인</button>
          <span class="answer-result" data-id="${q.id}">-</span>
        </div>
        <div class="answer-output" data-id="${q.id}">
          <div class="answer-output-title">실행 결과</div>
          <pre class="answer-output-text"></pre>
          <div class="answer-output-image"></div>
          <div class="answer-output-table"></div>
        </div>
        <div class="answer-note">정답 코드는 공백을 무시하고 비교합니다.</div>
      </div>
      <details data-id="${q.id}" data-section="hint" data-loaded="false">
        <summary>Hint / 힌트</summary>
        <div class="detail-body"></div>
      </details>
      <details data-id="${q.id}" data-section="answer" data-loaded="false">
        <summary>Answer Code / 정답 코드</summary>
        <div class="detail-body"></div>
      </details>
      <details data-id="${q.id}" data-section="solution" data-loaded="false">
        <summary>Detailed Solution / 상세 풀이</summary>
        <div class="detail-body"></div>
      </details>
    </div>
  `).join(""));
}

function normalizeCode(text) {
  return (text || "").replace(/\s+/g, "");
}

function normalizeOutput(text) {
  return (text || "").replace(/\s+/g, "");
}

const API_BASE = "http://localhost:8001";
const READONLY_KEY = "df_training_readonly";
let readonlyMode = false;
let statusTimer = null;

async function runCodeOnServer({ code, datasetId, questionId }) {
  const res = await fetch(`${API_BASE}/run`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code, datasetId, questionId })
  });
  return res.json();
}

async function checkServerReady() {
  try {
    const res = await fetch(`${API_BASE}/debug`);
    return res.ok;
  } catch (err) {
    return false;
  }
}

async function updateServerStatus() {
  const statusEl = document.getElementById("serverStatus");
  if (!statusEl) return;
  const ok = await checkServerReady();
  statusEl.textContent = ok ? "연결됨" : "미연결";
  statusEl.dataset.status = ok ? "ok" : "fail";
}

function detectOS() {
  const ua = navigator.userAgent.toLowerCase();
  if (ua.includes("windows")) return "windows";
  if (ua.includes("mac os") || ua.includes("macintosh")) return "mac";
  if (ua.includes("linux")) return "linux";
  return "other";
}

function setReadonlyMode(enabled) {
  readonlyMode = enabled;
  document.body.classList.toggle("readonly", enabled);
  const banner = document.getElementById("readonlyBanner");
  if (banner) banner.classList.toggle("show", enabled);
}

function hideInstallModal() {
  const modal = document.getElementById("installModal");
  if (modal) modal.classList.add("hidden");
}

function showInstallModal() {
  const modal = document.getElementById("installModal");
  if (modal) modal.classList.remove("hidden");
}

async function copyLocalRunCommand(buttonEl) {
  const commandEl = document.getElementById("localRunCommand");
  if (!commandEl) return;
  const text = commandEl.textContent.trim();
  if (!text) return;
  try {
    await navigator.clipboard.writeText(text);
    if (buttonEl) {
      const original = buttonEl.textContent;
      buttonEl.textContent = "복사 완료";
      setTimeout(() => {
        buttonEl.textContent = original;
      }, 1200);
    }
  } catch (err) {
    alert("클립보드 복사에 실패했습니다. 수동으로 복사해 주세요.");
  }
}

async function copyAnswerById(id, buttonEl) {
  const q = questionMap.get(id);
  if (!q) return;
  try {
    await navigator.clipboard.writeText(q.answer);
    if (buttonEl) {
      buttonEl.textContent = "✓";
      setTimeout(() => {
        buttonEl.textContent = "⧉";
      }, 1200);
    }
  } catch (err) {
    alert("클립보드 복사에 실패했습니다. 수동으로 복사해 주세요.");
  }
}

document.getElementById("questionList").addEventListener("click", async (e) => {
  const copyIcon = e.target.closest(".copy-answer-icon");
  if (copyIcon) {
    const id = Number(copyIcon.dataset.id);
    await copyAnswerById(id, copyIcon);
    return;
  }
  const runBtn = e.target.closest(".answer-run-btn");
  if (runBtn) {
    if (readonlyMode) return;
    const id = Number(runBtn.dataset.id);
    const q = questionMap.get(id);
    if (!q) return;
    const questionEl = runBtn.closest(".question");
    if (!questionEl) return;
    const textarea = questionEl.querySelector(".answer-input textarea");
    const outputEl = questionEl.querySelector(".answer-output");
    const outputText = questionEl.querySelector(".answer-output-text");
    const outputTable = questionEl.querySelector(".answer-output-table");
    const outputImage = questionEl.querySelector(".answer-output-image");
    if (!textarea || !outputEl || !outputText || !outputTable || !outputImage) return;
    const code = textarea.value.trim();
    if (!code) {
      outputText.textContent = "실행할 코드를 입력하세요.";
      outputTable.innerHTML = "";
      outputImage.innerHTML = "";
      return;
    }
    outputText.textContent = "실행 중...";
    outputTable.innerHTML = "";
    outputImage.innerHTML = "";
    try {
      const result = await runCodeOnServer({
        code,
        datasetId: q.datasetId,
        questionId: q.id
      });
      if (result.error) {
        outputText.textContent = result.error;
        outputTable.innerHTML = "";
        outputImage.innerHTML = "";
        return;
      }
      outputText.textContent = result.stdout || "(출력 없음)";
      outputTable.innerHTML = result.table_html || "";
      outputImage.innerHTML = result.image_base64 ? `<img src="${result.image_base64}" alt="plot" />` : "";
    } catch (err) {
      outputText.textContent = "서버에 연결할 수 없습니다. FastAPI 서버를 실행했는지 확인하세요.";
      outputTable.innerHTML = "";
      outputImage.innerHTML = "";
    }
    return;
  }
  const btn = e.target.closest(".answer-check-btn");
  if (!btn) return;
  const id = Number(btn.dataset.id);
  const q = questionMap.get(id);
  if (!q) return;
  const questionEl = btn.closest(".question");
  if (!questionEl) return;
  const textarea = questionEl.querySelector(".answer-input textarea");
  const resultEl = questionEl.querySelector(".answer-result");
  if (!textarea || !resultEl) return;
  const user = textarea.value.trim();
  if (!user) {
    resultEl.textContent = "답안을 입력하세요.";
    resultEl.dataset.status = "empty";
    return;
  }
  resultEl.textContent = "채점 중...";
  resultEl.dataset.status = "checking";
  try {
    const userResult = await runCodeOnServer({
      code: user,
      datasetId: q.datasetId,
      questionId: q.id
    });
    if (userResult.error) {
      resultEl.textContent = "실행 오류가 있어 채점할 수 없습니다.";
      resultEl.dataset.status = "wrong";
      return;
    }
    const expectedResult = await runCodeOnServer({
      code: q.answer,
      datasetId: q.datasetId,
      questionId: q.id
    });
    if (expectedResult.error) {
      resultEl.textContent = "정답 코드를 실행할 수 없습니다.";
      resultEl.dataset.status = "wrong";
      return;
    }
    const sameStdout = (userResult.stdout_hash || "") === (expectedResult.stdout_hash || "");
    const sameResult = (userResult.result_hash || "") === (expectedResult.result_hash || "");
    const sameImage = normalizeOutput(userResult.image_base64 || "") === normalizeOutput(expectedResult.image_base64 || "");
    if ((sameStdout || !expectedResult.stdout_hash) && (sameResult || !expectedResult.result_hash) && (sameImage || !expectedResult.image_base64)) {
      resultEl.textContent = "실행 결과가 정답과 같습니다.";
      resultEl.dataset.status = "correct";
    } else {
      resultEl.textContent = "실행 결과가 다릅니다. 힌트를 참고해 보세요.";
      resultEl.dataset.status = "wrong";
    }
  } catch (err) {
    resultEl.textContent = "채점 중 오류가 발생했습니다.";
    resultEl.dataset.status = "wrong";
  }
});

document.getElementById("questionList").addEventListener("keydown", async (e) => {
  if (!(e.ctrlKey && e.key === "Enter")) return;
  const textarea = e.target.closest(".answer-input textarea");
  if (!textarea) return;
  if (readonlyMode) return;
  const questionEl = textarea.closest(".question");
  if (!questionEl) return;
  const runBtn = questionEl.querySelector(".answer-run-btn");
  if (!runBtn) return;
  runBtn.click();
});

function trimRendered() {
  const container = document.getElementById("questionList");
  while (container.children.length > MAX_RENDERED) {
    container.removeChild(container.firstElementChild);
  }
}

function renderDetailBody(q, section) {
  if (section === "hint") {
    const cols = q.detail.columns || {};
    const colLine = cols.num || cols.cat ? `<p><strong>컬럼 정보:</strong> num=${cols.num || "-"}, num2=${cols.num2 || "-"}, cat=${cols.cat || "-"}, cat2=${cols.cat2 || "-"}</p>` : "";
    return `<p>${q.hintKo}</p><p>${q.hintEn}</p>${colLine}`;
  }
  if (section === "answer") {
    return `<pre>${q.answer}</pre>`;
  }
  return `
    <p><strong>핵심 개념:</strong> ${q.detail.term} (발음: ${q.detail.pron}, 뜻: ${q.detail.meaningKo})</p>
    <p><strong>정의(KR):</strong> ${q.detail.defKo}</p>
    <p><strong>Definition(EN):</strong> ${q.detail.defEn}</p>
    <p><strong>왜 필요한가?</strong> 이 문제는 <em>${q.detail.term}</em>를 실제 데이터셋에 적용해 “문제 상황을 해결하는 최소 단위”를 익히기 위한 것입니다. 시험에서는 문제 조건이 구체적으로 주어지므로, 조건에 맞는 컬럼을 정확히 선택하는 것이 핵심입니다.</p>
    <p><strong>사용 절차(논리 흐름):</strong> 1) 데이터셋 로딩 → 2) 대상 컬럼/조건 확인 → 3) 메서드 적용 → 4) 결과 검증. 이 흐름을 따르면 어떤 데이터셋에서도 재현 가능합니다.</p>
    <p><strong>사용법(패턴):</strong> <code>${q.detail.usage}</code></p>
    <p><strong>실사용 예제(정답형):</strong> <code>${q.detail.example}</code></p>
    <p><strong>검증 포인트:</strong> 결과가 기대한 형태인지(행/열 수, 결측치 감소, 통계 값 등)를 확인하세요. 필요하면 <code>df.head()</code> 또는 <code>value_counts()</code>로 빠르게 점검합니다.</p>
    <p><strong>오답이 많이 나는 이유:</strong> 컬럼명을 잘못 지정하거나, 적용 대상(수치형/범주형)을 혼동하는 경우가 많습니다. 문제에 제시된 컬럼을 그대로 사용하세요.</p>
    <p><strong>컬럼 사용:</strong> num=${(q.detail.columns || {}).num || "-"}, num2=${(q.detail.columns || {}).num2 || "-"}, cat=${(q.detail.columns || {}).cat || "-"}, cat2=${(q.detail.columns || {}).cat2 || "-"}</p>
  `;
}

function renderNotebookGuide(q) {
  const cols = q.detail.columns || {};
  const target = cols.num || cols.cat || "target";
  const datasetFile = datasets.find(d => d.id === q.datasetId)?.file || "datasets/iris.csv";
  const localPath = `practice/${datasetFile}`;
  const remoteBase = "https://raw.githubusercontent.com/gncorpseo-commits/AICE_ASSOCIATE/main/";
  const remoteUrl = `${remoteBase}${localPath}`;
  const problem = [
    `# 문제 (KR)`,
    q.problemKo,
    ``,
    `# Problem (EN)`,
    q.problemEn
  ].join("\\n");
  const hint = [
    `# 힌트 (KR)`,
    q.hintKo,
    ``,
    `# Hint (EN)`,
    q.hintEn
  ].join("\\n");
  const answer = [
    `# 정답 코드`,
    q.answer
  ].join("\\n");
  const detail = [
    `# 상세 풀이`,
    `Term: ${q.detail.term} (발음: ${q.detail.pron}, 뜻: ${q.detail.meaningKo})`,
    `정의(KR): ${q.detail.defKo}`,
    `Definition(EN): ${q.detail.defEn}`,
    `사용법: ${q.detail.usage}`,
    `예제: ${q.detail.example}`
  ].join("\\n");
  const loader = [
    "# 데이터 로딩",
    "import os",
    "import pandas as pd",
    `LOCAL_PATH = "${localPath}"`,
    `REMOTE_URL = "${remoteUrl}"`,
    "DATASET_PATH = LOCAL_PATH if os.path.exists(LOCAL_PATH) else REMOTE_URL",
    "df = pd.read_csv(DATASET_PATH)",
    "df.head()",
    "",
    "# Suggested target/feature split",
    `X = df.drop(['${target}'], axis=1)`,
    `y = df['${target}']`
  ].join("\\n");
  return { loader, problem, hint, answer, detail, datasetFile, target };
}

function downloadNotebook(q) {
  const nb = renderNotebookGuide(q);
  const notebook = {
    nbformat: 4,
    nbformat_minor: 4,
    metadata: {
      kernelspec: { display_name: "Python 3", language: "python", name: "python3" },
      language_info: { name: "python", version: "3.8.0" }
    },
    cells: [
      { cell_type: "markdown", metadata: {}, source: [`# 문제은행 노트북\\n\\nDataset: ${q.datasetName}\\nTarget: ${nb.target}\\n`] },
      { cell_type: "code", metadata: {}, execution_count: null, outputs: [], source: [nb.loader] },
      { cell_type: "markdown", metadata: {}, source: [nb.problem] },
      { cell_type: "markdown", metadata: {}, source: [nb.hint] },
      { cell_type: "code", metadata: {}, execution_count: null, outputs: [], source: [nb.answer] },
      { cell_type: "markdown", metadata: {}, source: [nb.detail] }
    ]
  };
  const blob = new Blob([JSON.stringify(notebook, null, 2)], { type: "application/json" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `df_training_${q.id}.ipynb`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function updateStatus() {
  const status = document.getElementById("loadingStatus");
  const total = filteredQuestions.length;
  if (renderedCount >= total) {
    status.textContent = `모든 문제를 불러왔습니다. (총 ${total}개, 화면 최대 ${MAX_RENDERED}개 유지)`;
  } else {
    status.textContent = `로드됨: ${renderedCount} / ${total} (화면 최대 ${MAX_RENDERED}개 유지)`;
  }
}

function updateProgress() {
  if (!questionProgressEl) return;
  const total = filteredQuestions.length;
  const index = currentQuestionId ? filteredQuestions.findIndex(q => q.id === currentQuestionId) + 1 : 0;
  questionProgressEl.textContent = total ? `현재: ${index} / ${total}` : "현재: -";
}

function renderNextBatch() {
  const next = filteredQuestions.slice(renderedCount, renderedCount + PAGE_SIZE);
  renderQuestions(next, true);
  renderedCount += next.length;
  trimRendered();
  updateStatus();
  updateAdminRenderCount();
  adminLog("render_batch", { added: next.length, renderedCount });
  if (next.length > 0) currentQuestionId = next[next.length - 1].id;
  if (firstRenderMs === null) {
    firstRenderMs = Math.round(performance.now() - sessionStart);
    updateAdminTimings();
  }
  updateProgress();
}

function resetInfiniteScroll() {
  renderedCount = 0;
  renderQuestions([], false);
  renderNextBatch();
}

function applyFilters() {
  const diff = document.getElementById("filterDifficulty").value;
  const ds = document.getElementById("filterDataset").value;
  const lib = document.getElementById("filterLibrary").value;
  const q = document.getElementById("filterQuery").value.toLowerCase();

  let filtered = questions;
  if (diff !== "all") filtered = filtered.filter(x => x.diff === diff);
  if (ds !== "all") filtered = filtered.filter(x => x.datasetId === ds);
  if (lib !== "all") filtered = filtered.filter(x => (x.libraries || []).includes(lib));
  if (q) {
    filtered = filtered.filter(x =>
      x.title.toLowerCase().includes(q) ||
      x.problemKo.toLowerCase().includes(q) ||
      x.problemEn.toLowerCase().includes(q) ||
      x.detail.term.toLowerCase().includes(q)
    );
  }
  filteredQuestions = filtered;
  document.getElementById("totalCount").textContent = filteredQuestions.length;
  resetInfiniteScroll();
}

function initQuestionControls() {
  questionProgressEl = document.getElementById("questionProgress");
  nextQuestionBtn = document.getElementById("nextQuestionBtn");
  if (!nextQuestionBtn) return;
  nextQuestionBtn.addEventListener("click", () => {
    if (renderedCount >= filteredQuestions.length) {
      updateProgress();
      return;
    }
    renderNextBatch();
  });
  updateProgress();
}

function initFilters() {
  const dsSelect = document.getElementById("filterDataset");
  const libSelect = document.getElementById("filterLibrary");
  dsSelect.innerHTML = `<option value="all">All Datasets</option>` + datasets.map(d => `<option value="${d.id}">${d.name}</option>`).join("");
  document.getElementById("filterDifficulty").addEventListener("change", applyFilters);
  dsSelect.addEventListener("change", applyFilters);
  if (libSelect) {
    const libs = ["pandas", "numpy", "matplotlib", "seaborn", "sklearn", "tensorflow", "xgboost"];
    libSelect.innerHTML = `<option value="all">All Libraries (전체)</option>` + libs.map(l => `<option value="${l}">${l}</option>`).join("");
    libSelect.addEventListener("change", applyFilters);
  }
  document.getElementById("filterQuery").addEventListener("input", applyFilters);
}

function initInfiniteScroll() {
  const sentinel = document.getElementById("scrollSentinel");
  if (observer) observer.disconnect();
  if (sentinel) sentinel.innerHTML = "";
}

function initAdminModule() {
  adminLogEl = document.getElementById("adminLog");
  adminLastEventEl = document.getElementById("adminLastEvent");
  adminRenderCountEl = document.getElementById("adminRenderCount");
  adminToggleLoadedEl = document.getElementById("adminToggleLoaded");
  adminDebugToggleEl = document.getElementById("adminDebugToggle");
  adminClearLogEl = document.getElementById("adminClearLog");
  adminRunTestsEl = document.getElementById("adminRunTests");
  adminCopyTestEl = document.getElementById("adminCopyTest");
  adminTestResultEl = document.getElementById("adminTestResult");
  runDebugTestBtn = document.getElementById("adminRunDebugTest");
  adminFirstRenderMsEl = document.getElementById("adminFirstRenderMs");
  adminLastToggleMsEl = document.getElementById("adminLastToggleMs");
  const adminToggleEventEl = document.getElementById("adminToggleEvent");
  const adminToggleCaptureEl = document.getElementById("adminToggleCapture");

  const saved = localStorage.getItem("df_training_admin_debug");
  adminDebug = saved === "true";
  adminDebugToggleEl.checked = adminDebug;

  adminDebugToggleEl.addEventListener("change", () => {
    adminDebug = adminDebugToggleEl.checked;
    localStorage.setItem("df_training_admin_debug", String(adminDebug));
    adminLog("debug_toggle", { enabled: adminDebug });
  });

  adminClearLogEl.addEventListener("click", () => {
    if (adminLogEl) adminLogEl.textContent = "";
  });

  if (adminRunTestsEl) {
    adminRunTestsEl.addEventListener("click", () => {
      const result = runMethodTests();
      if (adminTestResultEl) adminTestResultEl.textContent = result;
    });
  }

  if (adminCopyTestEl) {
    adminCopyTestEl.addEventListener("click", () => {
      if (!adminTestResultEl) return;
      const text = adminTestResultEl.textContent || "";
      if (!text) {
        alert("복사할 테스트 결과가 없습니다.");
        return;
      }
      navigator.clipboard.writeText(text).then(() => {
        alert("테스트 결과가 클립보드에 복사되었습니다.");
      }).catch(() => {
        alert("복사에 실패했습니다. 수동으로 복사해 주세요.");
      });
    });
  }

  if (runDebugTestBtn) {
    runDebugTestBtn.addEventListener("click", async () => {
      if (!adminTestResultEl) return;
      adminTestResultEl.textContent = "서버 경로 테스트 중...";
      try {
        const res = await fetch(`${API_BASE}/debug`);
        const data = await res.json();
        adminTestResultEl.textContent = JSON.stringify(data, null, 2);
      } catch (err) {
        adminTestResultEl.textContent = "서버에 연결할 수 없습니다.";
      }
    });
  }

  updateAdminRenderCount();
  updateAdminToggleLoaded();
  updateAdminTimings();

  if (adminToggleEventEl) {
    adminToggleEventEl.textContent = "ready";
  }
  if (adminToggleCaptureEl) {
    adminToggleCaptureEl.textContent = "true";
  }
}

function adminLog(type, payload = {}) {
  if (!adminDebug || !adminLogEl) return;
  const time = new Date().toLocaleTimeString();
  const line = `[${time}] ${type} ${JSON.stringify(payload)}\n`;
  adminLogEl.textContent = line + adminLogEl.textContent;
  const lines = adminLogEl.textContent.split("\n");
  if (lines.length > ADMIN_LOG_MAX) {
    adminLogEl.textContent = lines.slice(0, ADMIN_LOG_MAX).join("\n");
  }
  if (adminLastEventEl) adminLastEventEl.textContent = type;
}

function updateAdminRenderCount() {
  if (adminRenderCountEl) adminRenderCountEl.textContent = String(renderedCount);
}

function updateAdminToggleLoaded() {
  if (adminToggleLoadedEl) adminToggleLoadedEl.textContent = String(adminToggleLoaded);
}

function updateAdminTimings() {
  if (adminFirstRenderMsEl) {
    adminFirstRenderMsEl.textContent = firstRenderMs === null ? "-" : `${firstRenderMs}ms`;
  }
}

function updateLastToggleMs(ms) {
  if (adminLastToggleMsEl) adminLastToggleMsEl.textContent = `${ms}ms`;
}

function getFirstDetails(section) {
  return document.querySelector(`#questionList details[data-section="${section}"]`);
}

function runToggleTest(section) {
  const detail = getFirstDetails(section);
  if (!detail) return { section, ok: false, reason: "details_not_found" };
  const beforeLoaded = detail.dataset.loaded === "true";
  const start = performance.now();
  detail.open = true;
  const afterLoaded = detail.dataset.loaded === "true";
  const ms = Math.round(performance.now() - start);
  return { section, ok: afterLoaded, beforeLoaded, ms };
}

function runRenderTest() {
  const before = renderedCount;
  renderNextBatch();
  const after = renderedCount;
  return { before, after, added: after - before };
}

function runMethodTests() {
  const results = [];
  results.push({ name: "render_next_batch", ...runRenderTest() });
  results.push({ name: "toggle_hint", ...runToggleTest("hint") });
  results.push({ name: "toggle_answer", ...runToggleTest("answer") });
  results.push({ name: "toggle_solution", ...runToggleTest("solution") });
  const stamp = new Date().toLocaleString();
  const summary = {
    time: stamp,
    renderedCount,
    firstRenderMs,
    lastToggleMs: adminLastToggleMsEl ? adminLastToggleMsEl.textContent : "-"
  };
  const output = [
    `# method_test_report`,
    `time: ${summary.time}`,
    `renderedCount: ${summary.renderedCount}`,
    `firstRenderMs: ${summary.firstRenderMs === null ? "-" : summary.firstRenderMs + "ms"}`,
    `lastToggleMs: ${summary.lastToggleMs}`,
    `results:`,
    ...results.map(r => `- ${r.name}: ${JSON.stringify(r)}`)
  ].join("\n");
  adminLog("method_tests", { results });
  return output;
}

window.MethodTests = {
  run: runMethodTests,
  render: runRenderTest,
  toggle: runToggleTest
};

document.addEventListener("DOMContentLoaded", () => {
  renderDatasets();
  initFilters();
  document.getElementById("totalCount").textContent = questions.length;
  filteredQuestions = questions;
  initInfiniteScroll();
  initAdminModule();
  initUxFeedback();
  initQuestionControls();
  resetInfiniteScroll();

  const savedReadonly = localStorage.getItem(READONLY_KEY);
  if (savedReadonly === "true") {
    setReadonlyMode(true);
    hideInstallModal();
    return;
  }

  updateServerStatus();
  statusTimer = window.setInterval(updateServerStatus, 5000);

  checkServerReady().then((ok) => {
    if (ok) {
      setReadonlyMode(false);
      hideInstallModal();
    } else {
      setReadonlyMode(true);
      showInstallModal();
    }
  });

  const continueBtn = document.getElementById("continueReadonly");
  if (continueBtn) {
    continueBtn.addEventListener("click", () => {
      localStorage.setItem(READONLY_KEY, "true");
      setReadonlyMode(true);
      hideInstallModal();
    });
  }

  const retryBtn = document.getElementById("retryConnection");
  if (retryBtn) {
    retryBtn.addEventListener("click", async () => {
      const ok = await checkServerReady();
      if (ok) {
        localStorage.removeItem(READONLY_KEY);
        setReadonlyMode(false);
        hideInstallModal();
      } else {
        setReadonlyMode(true);
        showInstallModal();
      }
    });
  }

  const guideBtn = document.getElementById("openInstallGuide");
  if (guideBtn) {
    guideBtn.addEventListener("click", () => {
      const section = document.getElementById("localSetup");
      if (section) section.scrollIntoView({ behavior: "smooth" });
    });
  }

  const copyLocalRun = document.getElementById("copyLocalRun");
  if (copyLocalRun) {
    copyLocalRun.addEventListener("click", () => {
      copyLocalRunCommand(copyLocalRun);
    });
  }

  const os = detectOS();
  const reco = document.getElementById("installReco");
  if (reco) {
    if (os === "windows") reco.textContent = "추천: Windows용 설치/실행";
    else if (os === "mac") reco.textContent = "추천: macOS/Linux용 설치/실행";
    else if (os === "linux") reco.textContent = "추천: Linux용 설치/실행";
    else reco.textContent = "추천: 사용 중인 OS에 맞는 설치/실행 스크립트";
  }

  const winPs = document.getElementById("downloadWinPs");
  const winBat = document.getElementById("downloadWinBat");
  const unixSh = document.getElementById("downloadUnixSh");
  if (os === "windows") {
    if (unixSh) unixSh.style.display = "none";
  } else if (os === "mac" || os === "linux") {
    if (winPs) winPs.style.display = "none";
    if (winBat) winBat.style.display = "none";
  }
});

document.getElementById("openInNotebook").addEventListener("click", () => {
  const q = questionMap.get(currentQuestionId);
  if (!q) {
    alert("현재 표시된 문제가 없습니다.");
    return;
  }
  const nb = renderNotebookGuide(q);
  const clipboardText = [
    nb.problem,
    "",
    nb.hint,
    "",
    nb.loader,
    "",
    nb.answer,
    "",
    nb.detail
  ].join("\\n");
  navigator.clipboard.writeText(clipboardText).then(() => {
    alert("노트북용 템플릿이 클립보드에 복사되었습니다.");
  }).catch(() => {
    alert("클립보드 복사에 실패했습니다. 수동으로 복사해 주세요.");
  });
});

document.getElementById("downloadNotebook").addEventListener("click", () => {
  const q = questionMap.get(currentQuestionId);
  if (!q) {
    alert("현재 표시된 문제가 없습니다.");
    return;
  }
  downloadNotebook(q);
});

document.getElementById("openNotebookLink").addEventListener("click", () => {
  const url = "http://localhost:8888/notebooks/practice/df_training.ipynb";
  window.open(url, "_blank", "noopener,noreferrer");
});

document.getElementById("openColabLink").addEventListener("click", () => {
  const q = questionMap.get(currentQuestionId);
  if (!q) {
    alert("현재 표시된 문제가 없습니다.");
    return;
  }
  const url = "https://colab.research.google.com/github/gncorpseo-commits/AICE_ASSOCIATE/blob/main/practice/df_training.ipynb";
  window.open(url, "_blank", "noopener,noreferrer");
  alert("Colab에서 GitHub 노트북을 바로 엽니다. 데이터는 GitHub Raw URL로 로드됩니다.");
});

document.getElementById("questionList").addEventListener("toggle", (e) => {
  const target = e.target;
  if (!(target instanceof HTMLDetailsElement)) return;
  if (!target.open) return;
  if (target.dataset.loaded === "true") return;
  const id = Number(target.dataset.id);
  const section = target.dataset.section;
  const q = questionMap.get(id);
  if (!q) return;
  const body = target.querySelector(".detail-body");
  if (!body) return;
  const toggleStart = performance.now();
  body.innerHTML = renderDetailBody(q, section);
  target.dataset.loaded = "true";
  const toggleMs = Math.round(performance.now() - toggleStart);
  adminToggleLoaded += 1;
  updateAdminToggleLoaded();
  updateLastToggleMs(toggleMs);
  adminLog("toggle_loaded", { id, section });
}, true);

function initUxFeedback() {
  uxSpeedEl = document.getElementById("uxSpeed");
  uxFlowEl = document.getElementById("uxFlow");
  uxNotebookEl = document.getElementById("uxNotebook");
  uxNotesEl = document.getElementById("uxNotes");
  uxSaveEl = document.getElementById("uxSave");
  uxLastSavedEl = document.getElementById("uxLastSaved");
  if (!uxSaveEl) return;
  const saved = localStorage.getItem("df_training_ux_feedback");
  if (saved) {
    const data = JSON.parse(saved);
    uxSpeedEl.value = data.speed || "3";
    uxFlowEl.value = data.flow || "3";
    uxNotebookEl.value = data.notebook || "3";
    uxNotesEl.value = data.notes || "";
    uxLastSavedEl.textContent = data.savedAt || "-";
  }
  uxSaveEl.addEventListener("click", () => {
    const payload = {
      speed: uxSpeedEl.value,
      flow: uxFlowEl.value,
      notebook: uxNotebookEl.value,
      notes: uxNotesEl.value.trim(),
      savedAt: new Date().toLocaleString()
    };
    localStorage.setItem("df_training_ux_feedback", JSON.stringify(payload));
    uxLastSavedEl.textContent = payload.savedAt;
  });
}
