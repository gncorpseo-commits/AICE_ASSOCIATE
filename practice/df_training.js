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

const glossary = {
  head: { ko: "앞부분 보기", pron: "헤드", en: "head", def: "데이터프레임 상단 N행을 확인하는 함수", usage: "df.head(5)", example: "df.head(3)" },
  info: { ko: "정보 요약", pron: "인포", en: "info", def: "컬럼, 결측치, dtype 요약을 출력", usage: "df.info()", example: "df.info()" },
  describe: { ko: "기초 통계", pron: "디스크라이브", en: "describe", def: "수치형 컬럼의 요약 통계를 계산", usage: "df.describe()", example: "df.describe()" },
  isna: { ko: "결측치 확인", pron: "이즈나", en: "isna", def: "결측치 여부를 True/False로 반환", usage: "df.isna().sum()", example: "df.isna().sum()" },
  fillna: { ko: "결측치 채우기", pron: "필나", en: "fillna", def: "결측치를 지정한 값으로 채움", usage: "df['col'].fillna(0)", example: "df['age'].fillna(df['age'].mean())" },
  dropna: { ko: "결측치 제거", pron: "드롭나", en: "dropna", def: "결측치가 있는 행/열 제거", usage: "df.dropna()", example: "df.dropna(subset=['age'])" },
  astype: { ko: "형변환", pron: "애즈타입", en: "astype", def: "컬럼의 자료형 변환", usage: "df['col'].astype(int)", example: "df['sex'] = df['sex'].astype('category')" },
  sort_values: { ko: "정렬", pron: "소트 밸류즈", en: "sort_values", def: "컬럼 기준 정렬", usage: "df.sort_values('col')", example: "df.sort_values('fare', ascending=False)" },
  query: { ko: "조건 필터", pron: "쿼리", en: "query", def: "문자열 조건으로 필터링", usage: "df.query('age > 30')", example: "df.query('sex == \"male\"')" },
  loc: { ko: "라벨 인덱싱", pron: "록", en: "loc", def: "행/열 라벨 기반 선택", usage: "df.loc[rows, cols]", example: "df.loc[0:3, ['age','sex']]" },
  iloc: { ko: "정수 인덱싱", pron: "아이록", en: "iloc", def: "정수 위치 기반 선택", usage: "df.iloc[rows, cols]", example: "df.iloc[:5, 0:3]" },
  groupby: { ko: "그룹 집계", pron: "그룹바이", en: "groupby", def: "범주별로 묶어서 집계", usage: "df.groupby('col').mean()", example: "df.groupby('class')['fare'].mean()" },
  agg: { ko: "집계", pron: "애그", en: "agg", def: "다중 집계 함수 적용", usage: "df.groupby('col').agg(['mean','max'])", example: "df.groupby('sex')['age'].agg(['mean','median'])" },
  pivot_table: { ko: "피벗 테이블", pron: "피벗 테이블", en: "pivot_table", def: "행/열 기준 교차 집계", usage: "pd.pivot_table(df,...)", example: "pd.pivot_table(df, values='fare', index='class', columns='sex')" },
  merge: { ko: "병합", pron: "머지", en: "merge", def: "공통 키로 데이터프레임 결합", usage: "pd.merge(df1, df2, on='id')", example: "pd.merge(a, b, on='id', how='left')" },
  concat: { ko: "연결", pron: "컨캣", en: "concat", def: "행/열 방향 결합", usage: "pd.concat([a,b])", example: "pd.concat([train, test], axis=0)" },
  value_counts: { ko: "빈도수", pron: "밸류 카운츠", en: "value_counts", def: "범주 빈도 계산", usage: "df['col'].value_counts()", example: "df['class'].value_counts()" },
  unique: { ko: "고유값", pron: "유니크", en: "unique", def: "고유 값 목록 반환", usage: "df['col'].unique()", example: "df['sex'].unique()" },
  nunique: { ko: "고유값 개수", pron: "뉴-유니크", en: "nunique", def: "고유 값 개수 반환", usage: "df['col'].nunique()", example: "df['embarked'].nunique()" },
  cut: { ko: "구간화", pron: "컷", en: "cut", def: "연속형을 구간으로 분할", usage: "pd.cut(df['col'], bins=3)", example: "pd.cut(df['age'], bins=[0,18,60,100])" },
  qcut: { ko: "분위수 구간화", pron: "큐컷", en: "qcut", def: "동일 개수 기준 구간화", usage: "pd.qcut(df['col'], q=4)", example: "pd.qcut(df['fare'], q=4)" },
  to_datetime: { ko: "날짜 변환", pron: "투 데이트타임", en: "to_datetime", def: "문자열을 datetime으로 변환", usage: "pd.to_datetime(df['col'])", example: "df['date'] = pd.to_datetime(df['date'])" },
  dt: { ko: "날짜 접근자", pron: "디티", en: "dt", def: "datetime 속성 접근", usage: "df['date'].dt.year", example: "df['month'] = df['date'].dt.month" },
  apply: { ko: "행/열 함수 적용", pron: "어플라이", en: "apply", def: "함수를 행/열에 적용", usage: "df['col'].apply(func)", example: "df['name'].apply(len)" },
  map: { ko: "값 매핑", pron: "맵", en: "map", def: "값을 다른 값으로 치환", usage: "df['col'].map(dict)", example: "df['sex'].map({'male':1,'female':0})" },
  replace: { ko: "치환", pron: "리플레이스", en: "replace", def: "특정 값을 다른 값으로 변경", usage: "df.replace(old, new)", example: "df['sex'].replace('male', 'M')" },
  drop_duplicates: { ko: "중복 제거", pron: "드롭 듀플리케이츠", en: "drop_duplicates", def: "중복 행 제거", usage: "df.drop_duplicates()", example: "df.drop_duplicates(subset=['id'])" },
  sample: { ko: "무작위 샘플", pron: "샘플", en: "sample", def: "무작위 샘플 추출", usage: "df.sample(n=5)", example: "df.sample(frac=0.1, random_state=42)" },
  get_dummies: { ko: "원-핫 인코딩", pron: "겟 더미즈", en: "get_dummies", def: "범주형 컬럼을 원-핫 인코딩", usage: "pd.get_dummies(df, columns=['{{cat}}'])", example: "pd.get_dummies(df, columns=['{{cat}}'])" },
  train_test_split: { ko: "학습/검증 분리", pron: "트레인 테스트 스플릿", en: "train_test_split", def: "데이터를 학습/검증으로 분리", usage: "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)", example: "train_test_split(X, y, test_size=0.2, random_state=42)" },
  standard_scaler: { ko: "표준화", pron: "스탠다드 스케일러", en: "StandardScaler", def: "평균 0, 표준편차 1로 스케일링", usage: "from sklearn.preprocessing import StandardScaler\nscaler = StandardScaler()\nX_scaled = scaler.fit_transform(X)", example: "StandardScaler().fit_transform(X)" },
  minmax_scaler: { ko: "정규화", pron: "민맥스 스케일러", en: "MinMaxScaler", def: "0~1 범위로 스케일링", usage: "from sklearn.preprocessing import MinMaxScaler\nscaler = MinMaxScaler()\nX_scaled = scaler.fit_transform(X)", example: "MinMaxScaler().fit_transform(X)" },
  linear_regression: { ko: "선형회귀", pron: "리니어 리그레션", en: "LinearRegression", def: "회귀 문제를 위한 선형 모델", usage: "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)", example: "LinearRegression().fit(X_train, y_train)" },
  logistic_regression: { ko: "로지스틱 회귀", pron: "로지스틱 리그레션", en: "LogisticRegression", def: "분류 문제를 위한 로지스틱 회귀", usage: "from sklearn.linear_model import LogisticRegression\nmodel = LogisticRegression(max_iter=1000)\nmodel.fit(X_train, y_train)", example: "LogisticRegression(max_iter=1000).fit(X_train, y_train)" },
  eval_regression: { ko: "회귀 평가", pron: "이벨류에이션", en: "RMSE/R2", def: "회귀 성능 지표 계산", usage: "from sklearn.metrics import mean_squared_error, r2_score\nrmse = (mean_squared_error(y_test, y_pred) ** 0.5)\nr2 = r2_score(y_test, y_pred)", example: "rmse = (mean_squared_error(y_test, y_pred) ** 0.5)" },
  eval_classification: { ko: "분류 평가", pron: "이벨류에이션", en: "Accuracy/F1", def: "분류 성능 지표 계산", usage: "from sklearn.metrics import accuracy_score, f1_score\nacc = accuracy_score(y_test, y_pred)\nf1 = f1_score(y_test, y_pred, average='weighted')", example: "accuracy_score(y_test, y_pred)" }
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
  ]
};

function buildQuestion(id, diff, ds, template) {
  const g = glossary[template.op];
  const schema = datasetSchemas[ds.id] || { numeric: [], categorical: [] };
  const num = pick(schema.numeric, "col");
  const cat = pick(schema.categorical, "col");
  const cat2 = pickSecond(schema.categorical, cat);
  const replacements = { "{{num}}": num, "{{cat}}": cat, "{{cat2}}": cat2 };
  const fill = (text) => Object.keys(replacements).reduce((acc, key) => acc.replaceAll(key, replacements[key]), text);
  const title = `${id}. (${diff.toUpperCase()}) ${template.op} - ${ds.name}`;
  const problemKo = `${fill(template.taskKo)} 데이터셋: ${ds.name}.`;
  const problemEn = `Dataset: ${ds.name}. ${fill(template.taskEn)}`;
  const hintKo = `힌트: ${g.en} (${g.pron})를 사용해 보세요.`;
  const hintEn = `Hint: Try using ${g.en}.`;
  const basePrep = [
    `# load dataset`,
    `import pandas as pd`,
    `df = pd.read_csv('practice/datasets/${ds.file}')`
  ];
  const needsXY = ["train_test_split", "linear_regression", "logistic_regression", "eval_regression", "eval_classification", "standard_scaler", "minmax_scaler"];
  const isClassification = ["logistic_regression", "eval_classification"].includes(template.op);
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
    fill(g.usage.includes("df") ? g.usage : `${g.usage}`)
  ].join("\n");
  const detail = {
    term: g.en,
    meaningKo: g.ko,
    pron: g.pron,
    defKo: g.def,
    defEn: `Definition: ${g.en} in pandas.`,
    usage: fill(g.usage),
    example: fill(g.example),
    columns: { num, cat, cat2 }
  };
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
    detail
  };
}

function generateQuestions() {
  const list = [];
  let id = 1;
  const easyCount = 100;
  const mediumCount = 240;
  const hardCount = 100;
  const aiceCount = 60;
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
const ADMIN_LOG_MAX = 200;
let currentQuestionId = null;

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
      <h3>${q.title}</h3>
      <p><strong>KR:</strong> ${q.problemKo}</p>
      <p><strong>EN:</strong> ${q.problemEn}</p>
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

function trimRendered() {
  const container = document.getElementById("questionList");
  while (container.children.length > MAX_RENDERED) {
    container.removeChild(container.firstElementChild);
  }
}

function renderDetailBody(q, section) {
  if (section === "hint") {
    const cols = q.detail.columns || {};
    const colLine = cols.num || cols.cat ? `<p><strong>컬럼 정보:</strong> num=${cols.num || "-"}, cat=${cols.cat || "-"}, cat2=${cols.cat2 || "-"}</p>` : "";
    return `<p>${q.hintKo}</p><p>${q.hintEn}</p>${colLine}`;
  }
  if (section === "answer") {
    return `<pre>${q.answer}</pre>`;
  }
  return `
    <p><strong>Term:</strong> ${q.detail.term} (발음: ${q.detail.pron}, 뜻: ${q.detail.meaningKo})</p>
    <p><strong>정의(KR):</strong> ${q.detail.defKo}</p>
    <p><strong>Definition(EN):</strong> ${q.detail.defEn}</p>
    <p><strong>사용법:</strong> <code>${q.detail.usage}</code> 를 기본으로 사용합니다.</p>
    <p><strong>실사용 예제:</strong> <code>${q.detail.example}</code></p>
    <p><strong>설명:</strong> 이 문제는 <em>${q.detail.term}</em>의 기본 사용법을 익히기 위한 문제입니다. 데이터프레임에서 동일한 패턴을 반복 연습하세요.</p>
    <p><strong>Note:</strong> Practice the same pattern repeatedly to build muscle memory for ${q.detail.term}.</p>
    <p><strong>컬럼 사용:</strong> num=${(q.detail.columns || {}).num || "-"}, cat=${(q.detail.columns || {}).cat || "-"}, cat2=${(q.detail.columns || {}).cat2 || "-"}</p>
  `;
}

function renderNotebookGuide(q) {
  const cols = q.detail.columns || {};
  const target = cols.num || cols.cat || "target";
  const datasetFile = datasets.find(d => d.id === q.datasetId)?.file || "datasets/iris.csv";
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
    "import pandas as pd",
    `df = pd.read_csv('practice/datasets/${datasetFile}')`,
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

function renderNextBatch() {
  const next = filteredQuestions.slice(renderedCount, renderedCount + PAGE_SIZE);
  renderQuestions(next, true);
  renderedCount += next.length;
  trimRendered();
  updateStatus();
  updateAdminRenderCount();
  adminLog("render_batch", { added: next.length, renderedCount });
  if (next.length > 0) currentQuestionId = next[next.length - 1].id;
}

function resetInfiniteScroll() {
  renderedCount = 0;
  renderQuestions([], false);
  renderNextBatch();
}

function applyFilters() {
  const diff = document.getElementById("filterDifficulty").value;
  const ds = document.getElementById("filterDataset").value;
  const q = document.getElementById("filterQuery").value.toLowerCase();

  let filtered = questions;
  if (diff !== "all") filtered = filtered.filter(x => x.diff === diff);
  if (ds !== "all") filtered = filtered.filter(x => x.datasetId === ds);
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

function initFilters() {
  const dsSelect = document.getElementById("filterDataset");
  dsSelect.innerHTML = `<option value="all">All Datasets</option>` + datasets.map(d => `<option value="${d.id}">${d.name}</option>`).join("");
  document.getElementById("filterDifficulty").addEventListener("change", applyFilters);
  dsSelect.addEventListener("change", applyFilters);
  document.getElementById("filterQuery").addEventListener("input", applyFilters);
}

function initInfiniteScroll() {
  const sentinel = document.getElementById("scrollSentinel");
  observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) {
      renderNextBatch();
    }
  }, { rootMargin: "100px" });
  observer.observe(sentinel);
}

function initAdminModule() {
  adminLogEl = document.getElementById("adminLog");
  adminLastEventEl = document.getElementById("adminLastEvent");
  adminRenderCountEl = document.getElementById("adminRenderCount");
  adminToggleLoadedEl = document.getElementById("adminToggleLoaded");
  adminDebugToggleEl = document.getElementById("adminDebugToggle");
  adminClearLogEl = document.getElementById("adminClearLog");
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

  updateAdminRenderCount();
  updateAdminToggleLoaded();

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

document.addEventListener("DOMContentLoaded", () => {
  renderDatasets();
  initFilters();
  document.getElementById("totalCount").textContent = questions.length;
  filteredQuestions = questions;
  initInfiniteScroll();
  initAdminModule();
  resetInfiniteScroll();
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
  const url = "https://colab.research.google.com/github/gncorpseo-commits/AICE_ASSOCIATE/blob/main/practice/df_training.ipynb";
  window.open(url, "_blank", "noopener,noreferrer");
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
  body.innerHTML = renderDetailBody(q, section);
  target.dataset.loaded = "true";
  adminToggleLoaded += 1;
  updateAdminToggleLoaded();
  adminLog("toggle_loaded", { id, section });
}, true);
