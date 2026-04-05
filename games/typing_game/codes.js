// AICE Associate 필수 코드 패턴 (설명, 발음, 문법 포함)
const codeData = {
    // 카테고리 1: 라이브러리 Import
    library: {
        name: "라이브러리 Import",
        icon: "📚",
        codes: [
            { 
                code: "import numpy as np", 
                desc: "수치 연산 라이브러리 numpy를 np로 불러오기",
                pron: "임포트 넘파이 애즈 엔피",
                grammar: "import [라이브러리] as [별칭] - 라이브러리를 짧은 별칭으로 불러옴"
            },
            { 
                code: "import pandas as pd", 
                desc: "데이터 분석 라이브러리 pandas를 pd로 불러오기",
                pron: "임포트 판다스 애즈 피디",
                grammar: "import [라이브러리] as [별칭] - 라이브러리를 짧은 별칭으로 불러옴"
            },
            { 
                code: "import matplotlib.pyplot as plt", 
                desc: "시각화 라이브러리 matplotlib을 plt로 불러오기",
                pron: "임포트 맷플롯립 닷 파이플롯 애즈 피엘티",
                grammar: "import [패키지.모듈] as [별칭] - 패키지 내 특정 모듈을 별칭으로 불러옴"
            },
            { 
                code: "import seaborn as sns", 
                desc: "고급 시각화 라이브러리 seaborn을 sns로 불러오기",
                pron: "임포트 시본 애즈 에스엔에스",
                grammar: "import [라이브러리] as [별칭] - seaborn의 공식 별칭은 sns"
            },
            { 
                code: "from sklearn.model_selection import train_test_split", 
                desc: "데이터 분할 함수 불러오기",
                pron: "프롬 에스케이런 닷 모델셀렉션 임포트 트레인테스트스플릿",
                grammar: "from [패키지.모듈] import [함수] - 특정 함수만 직접 불러옴"
            },
            { 
                code: "from sklearn.linear_model import LinearRegression", 
                desc: "선형 회귀 모델 불러오기",
                pron: "프롬 에스케이런 닷 리니어모델 임포트 리니어리그레션",
                grammar: "from [패키지.모듈] import [클래스] - 특정 클래스를 직접 불러옴"
            },
            { 
                code: "from sklearn.linear_model import LogisticRegression", 
                desc: "로지스틱 회귀 모델 불러오기",
                pron: "프롬 에스케이런 닷 리니어모델 임포트 로지스틱리그레션",
                grammar: "from [패키지.모듈] import [클래스] - 분류용 로지스틱 회귀 클래스"
            },
            { 
                code: "from sklearn.ensemble import RandomForestRegressor", 
                desc: "랜덤포레스트 회귀 모델 불러오기",
                pron: "프롬 에스케이런 닷 앙상블 임포트 랜덤포레스트리그레서",
                grammar: "from sklearn.ensemble import [모델] - 앙상블 모듈에서 회귀 모델 불러옴"
            },
            { 
                code: "from sklearn.ensemble import RandomForestClassifier", 
                desc: "랜덤포레스트 분류 모델 불러오기",
                pron: "프롬 에스케이런 닷 앙상블 임포트 랜덤포레스트클래시파이어",
                grammar: "from sklearn.ensemble import [모델] - 앙상블 모듈에서 분류 모델 불러옴"
            },
            { 
                code: "from sklearn.tree import DecisionTreeClassifier", 
                desc: "의사결정나무 분류 모델 불러오기",
                pron: "프롬 에스케이런 닷 트리 임포트 디시전트리클래시파이어",
                grammar: "from sklearn.tree import [모델] - tree 모듈에서 분류 모델 불러옴"
            },
            { 
                code: "from sklearn.metrics import mean_squared_error", 
                desc: "MSE(평균제곱오차) 평가지표 불러오기",
                pron: "프롬 에스케이런 닷 메트릭스 임포트 민스퀘어드에러",
                grammar: "from sklearn.metrics import [지표] - 회귀 평가 지표 함수"
            },
            { 
                code: "from sklearn.metrics import r2_score", 
                desc: "R2 스코어 평가지표 불러오기",
                pron: "프롬 에스케이런 닷 메트릭스 임포트 알투스코어",
                grammar: "from sklearn.metrics import [지표] - 결정계수(R²) 평가 함수"
            },
            { 
                code: "from sklearn.metrics import accuracy_score", 
                desc: "정확도 평가지표 불러오기",
                pron: "프롬 에스케이런 닷 메트릭스 임포트 액큐러시스코어",
                grammar: "from sklearn.metrics import [지표] - 분류 정확도 평가 함수"
            },
            { 
                code: "from sklearn.metrics import f1_score", 
                desc: "F1 스코어 평가지표 불러오기",
                pron: "프롬 에스케이런 닷 메트릭스 임포트 에프원스코어",
                grammar: "from sklearn.metrics import [지표] - 정밀도와 재현율의 조화평균"
            },
            { 
                code: "from sklearn.metrics import confusion_matrix", 
                desc: "혼동 행렬 불러오기",
                pron: "프롬 에스케이런 닷 메트릭스 임포트 컨퓨전매트릭스",
                grammar: "from sklearn.metrics import [함수] - 실제값과 예측값 비교 행렬"
            },
            { 
                code: "from sklearn.preprocessing import LabelEncoder", 
                desc: "라벨 인코더 불러오기",
                pron: "프롬 에스케이런 닷 프리프로세싱 임포트 라벨인코더",
                grammar: "from sklearn.preprocessing import [클래스] - 범주형을 숫자로 변환"
            },
            { 
                code: "from sklearn.preprocessing import StandardScaler", 
                desc: "표준화 스케일러 불러오기",
                pron: "프롬 에스케이런 닷 프리프로세싱 임포트 스탠다드스케일러",
                grammar: "from sklearn.preprocessing import [클래스] - 평균0, 표준편차1로 변환"
            },
            { 
                code: "import warnings", 
                desc: "경고 메시지 관리 모듈 불러오기",
                pron: "임포트 워닝스",
                grammar: "import [모듈] - 파이썬 내장 경고 관리 모듈"
            },
            { 
                code: "warnings.filterwarnings('ignore')", 
                desc: "경고 메시지 무시하기",
                pron: "워닝스 닷 필터워닝스 이그노어",
                grammar: "모듈.함수('옵션') - 'ignore'로 경고 메시지 숨김"
            }
        ]
    },
    
    // 카테고리 2: 데이터 로딩 & 탐색
    exploration: {
        name: "데이터 탐색",
        icon: "🔍",
        codes: [
            { 
                code: "df = pd.read_csv('data.csv')", 
                desc: "CSV 파일을 데이터프레임으로 읽기",
                pron: "디에프 이퀄 피디 닷 리드시에스브이 데이터 닷 시에스브이",
                grammar: "변수 = pd.read_csv('파일경로') - CSV를 DataFrame으로 로드"
            },
            { 
                code: "df.head()", 
                desc: "데이터 상위 5행 미리보기",
                pron: "디에프 닷 헤드",
                grammar: "df.head(n) - 상위 n행 반환, 기본값 5"
            },
            { 
                code: "df.head(10)", 
                desc: "데이터 상위 10행 미리보기",
                pron: "디에프 닷 헤드 텐",
                grammar: "df.head(10) - 상위 10행 반환"
            },
            { 
                code: "df.tail()", 
                desc: "데이터 하위 5행 미리보기",
                pron: "디에프 닷 테일",
                grammar: "df.tail(n) - 하위 n행 반환, 기본값 5"
            },
            { 
                code: "df.shape", 
                desc: "데이터 크기 확인 (행, 열)",
                pron: "디에프 닷 쉐이프",
                grammar: "df.shape - (행 수, 열 수) 튜플 반환, 괄호 없음"
            },
            { 
                code: "df.info()", 
                desc: "데이터 타입 및 결측치 정보 확인",
                pron: "디에프 닷 인포",
                grammar: "df.info() - 컬럼명, 타입, non-null 개수 출력"
            },
            { 
                code: "df.describe()", 
                desc: "수치형 컬럼 기초 통계량 확인",
                pron: "디에프 닷 디스크라이브",
                grammar: "df.describe() - count, mean, std, min, 25%, 50%, 75%, max"
            },
            { 
                code: "df.columns", 
                desc: "컬럼 목록 확인",
                pron: "디에프 닷 컬럼스",
                grammar: "df.columns - 컬럼명 Index 객체 반환, 괄호 없음"
            },
            { 
                code: "df.columns.tolist()", 
                desc: "컬럼 목록을 리스트로 변환",
                pron: "디에프 닷 컬럼스 닷 투리스트",
                grammar: "df.columns.tolist() - 컬럼명을 파이썬 리스트로 변환"
            },
            { 
                code: "df.dtypes", 
                desc: "각 컬럼의 데이터 타입 확인",
                pron: "디에프 닷 디타입스",
                grammar: "df.dtypes - 각 컬럼의 dtype 반환, 괄호 없음"
            },
            { 
                code: "len(df)", 
                desc: "데이터 행 개수 확인",
                pron: "렌 디에프",
                grammar: "len(df) - DataFrame의 행 수 반환"
            },
            { 
                code: "df.nunique()", 
                desc: "각 컬럼별 고유값 개수 확인",
                pron: "디에프 닷 엔유니크",
                grammar: "df.nunique() - 각 컬럼의 unique 값 개수"
            },
            { 
                code: "df['col'].unique()", 
                desc: "특정 컬럼의 고유값 목록 확인",
                pron: "디에프 컬 닷 유니크",
                grammar: "df['컬럼명'].unique() - 해당 컬럼의 고유값 배열 반환"
            },
            { 
                code: "df['col'].nunique()", 
                desc: "특정 컬럼의 고유값 개수 확인",
                pron: "디에프 컬 닷 엔유니크",
                grammar: "df['컬럼명'].nunique() - 고유값 개수(정수) 반환"
            },
            { 
                code: "df['col'].value_counts()", 
                desc: "값별 빈도수 확인",
                pron: "디에프 컬 닷 밸류카운츠",
                grammar: "df['컬럼명'].value_counts() - 값별 개수 내림차순 정렬"
            }
        ]
    },
    
    // 카테고리 3: 결측치 처리
    missing: {
        name: "결측치 처리",
        icon: "🔧",
        codes: [
            { 
                code: "df.isna().sum()", 
                desc: "각 컬럼별 결측치 개수 확인",
                pron: "디에프 닷 이즈나 닷 썸",
                grammar: "df.isna() - 결측치 True/False → .sum()으로 True 개수 합산"
            },
            { 
                code: "df.isnull().sum()", 
                desc: "각 컬럼별 결측치 개수 확인 (isna와 동일)",
                pron: "디에프 닷 이즈널 닷 썸",
                grammar: "df.isnull() - isna()와 동일한 기능, 별칭"
            },
            { 
                code: "df.isna().sum().sum()", 
                desc: "전체 결측치 총 개수 확인",
                pron: "디에프 닷 이즈나 닷 썸 닷 썸",
                grammar: ".sum().sum() - 컬럼별 합을 다시 합산하여 총 결측치 수"
            },
            { 
                code: "df['col'].fillna(df['col'].mean(), inplace=True)", 
                desc: "평균값으로 결측치 채우기",
                pron: "디에프 컬 닷 필나 디에프 컬 닷 민 인플레이스 트루",
                grammar: ".fillna(값, inplace=True) - 결측치를 지정값으로 채움, 원본 수정"
            },
            { 
                code: "df['col'].fillna(df['col'].median(), inplace=True)", 
                desc: "중앙값으로 결측치 채우기",
                pron: "디에프 컬 닷 필나 디에프 컬 닷 미디안 인플레이스 트루",
                grammar: ".median() - 중앙값 반환, 이상치에 강건함"
            },
            { 
                code: "df['col'].fillna(df['col'].mode()[0], inplace=True)", 
                desc: "최빈값으로 결측치 채우기",
                pron: "디에프 컬 닷 필나 디에프 컬 닷 모드 제로 인플레이스 트루",
                grammar: ".mode()[0] - 최빈값 시리즈에서 첫 번째 값 선택"
            },
            { 
                code: "df['col'].fillna(0, inplace=True)", 
                desc: "0으로 결측치 채우기",
                pron: "디에프 컬 닷 필나 제로 인플레이스 트루",
                grammar: ".fillna(0) - 결측치를 0으로 대체"
            },
            { 
                code: "df.dropna(inplace=True)", 
                desc: "결측치가 있는 모든 행 삭제",
                pron: "디에프 닷 드롭나 인플레이스 트루",
                grammar: ".dropna() - 결측치 포함 행 삭제, inplace로 원본 수정"
            },
            { 
                code: "df.dropna(subset=['col'], inplace=True)", 
                desc: "특정 컬럼 결측치 행만 삭제",
                pron: "디에프 닷 드롭나 서브셋 컬 인플레이스 트루",
                grammar: "subset=['컬럼'] - 지정 컬럼의 결측치 행만 삭제"
            },
            { 
                code: "df_clean = df.copy()", 
                desc: "원본 보존을 위해 데이터프레임 복사",
                pron: "디에프클린 이퀄 디에프 닷 카피",
                grammar: ".copy() - 깊은 복사로 원본과 독립적인 복사본 생성"
            },
            { 
                code: "df.select_dtypes(include=[np.number]).columns", 
                desc: "수치형 컬럼만 선택",
                pron: "디에프 닷 셀렉트디타입스 인클루드 넘파이넘버 닷 컬럼스",
                grammar: ".select_dtypes(include=[타입]) - 특정 타입 컬럼만 필터링"
            },
            { 
                code: "df.select_dtypes(include=['object']).columns", 
                desc: "문자형 컬럼만 선택",
                pron: "디에프 닷 셀렉트디타입스 인클루드 오브젝트 닷 컬럼스",
                grammar: "include=['object'] - 문자열(object) 타입 컬럼 선택"
            }
        ]
    },
    
    // 카테고리 4: 인코딩 & 전처리
    preprocessing: {
        name: "전처리",
        icon: "⚙️",
        codes: [
            { 
                code: "df_encoded = pd.get_dummies(df, columns=['col'])", 
                desc: "특정 컬럼 원핫인코딩",
                pron: "디에프인코디드 이퀄 피디 닷 겟더미스 디에프 컬럼스 컬",
                grammar: "pd.get_dummies(df, columns=[컬럼]) - 범주형을 이진 컬럼으로 변환"
            },
            { 
                code: "pd.get_dummies(df, drop_first=True)", 
                desc: "첫 번째 더미 제거하여 원핫인코딩",
                pron: "피디 닷 겟더미스 디에프 드롭퍼스트 트루",
                grammar: "drop_first=True - 다중공선성 방지를 위해 첫 더미 제거"
            },
            { 
                code: "le = LabelEncoder()", 
                desc: "라벨 인코더 객체 생성",
                pron: "엘이 이퀄 라벨인코더",
                grammar: "LabelEncoder() - 범주를 0,1,2... 정수로 변환하는 객체"
            },
            { 
                code: "df['col_encoded'] = le.fit_transform(df['col'])", 
                desc: "라벨 인코딩 적용",
                pron: "디에프 컬인코디드 이퀄 엘이 닷 핏트랜스폼 디에프 컬",
                grammar: ".fit_transform() - 학습과 변환을 한번에 수행"
            },
            { 
                code: "scaler = StandardScaler()", 
                desc: "표준화 스케일러 객체 생성",
                pron: "스케일러 이퀄 스탠다드스케일러",
                grammar: "StandardScaler() - (값-평균)/표준편차로 표준화"
            },
            { 
                code: "X_scaled = scaler.fit_transform(X)", 
                desc: "표준화 적용 (평균0, 표준편차1)",
                pron: "엑스스케일드 이퀄 스케일러 닷 핏트랜스폼 엑스",
                grammar: ".fit_transform(X) - 스케일러 학습 후 변환 적용"
            },
            { 
                code: "scaler = MinMaxScaler()", 
                desc: "정규화 스케일러 객체 생성",
                pron: "스케일러 이퀄 민맥스스케일러",
                grammar: "MinMaxScaler() - 0~1 범위로 정규화"
            },
            { 
                code: "df['col'].astype(int)", 
                desc: "정수형으로 타입 변환",
                pron: "디에프 컬 닷 애즈타입 인트",
                grammar: ".astype(타입) - 데이터 타입 변환, int/float/str 등"
            },
            { 
                code: "df['col'].astype(float)", 
                desc: "실수형으로 타입 변환",
                pron: "디에프 컬 닷 애즈타입 플로트",
                grammar: ".astype(float) - 실수형으로 변환"
            },
            { 
                code: "df.drop(['col'], axis=1, inplace=True)", 
                desc: "특정 컬럼 삭제",
                pron: "디에프 닷 드롭 컬 액시스원 인플레이스 트루",
                grammar: ".drop([컬럼], axis=1) - axis=1은 열 방향 삭제"
            },
            { 
                code: "df.drop_duplicates(inplace=True)", 
                desc: "중복 행 삭제",
                pron: "디에프 닷 드롭듀플리케이츠 인플레이스 트루",
                grammar: ".drop_duplicates() - 중복된 행 제거"
            },
            { 
                code: "df.reset_index(drop=True, inplace=True)", 
                desc: "인덱스 재설정",
                pron: "디에프 닷 리셋인덱스 드롭트루 인플레이스 트루",
                grammar: ".reset_index(drop=True) - 기존 인덱스 버리고 0부터 재설정"
            }
        ]
    },
    
    // 카테고리 5: 시각화
    visualization: {
        name: "시각화",
        icon: "📊",
        codes: [
            { 
                code: "plt.figure(figsize=(10, 6))", 
                desc: "그래프 크기 설정 (가로10, 세로6)",
                pron: "피엘티 닷 피겨 픽사이즈 텐 식스",
                grammar: "plt.figure(figsize=(가로,세로)) - 인치 단위 그래프 크기"
            },
            { 
                code: "sns.histplot(df['col'], kde=True)", 
                desc: "히스토그램 + 밀도곡선 그리기",
                pron: "에스엔에스 닷 히스트플롯 디에프 컬 케이디이 트루",
                grammar: "sns.histplot(데이터, kde=True) - kde는 커널밀도추정 곡선"
            },
            { 
                code: "sns.boxplot(x='col', data=df)", 
                desc: "박스플롯 그리기",
                pron: "에스엔에스 닷 박스플롯 엑스 컬 데이터 디에프",
                grammar: "sns.boxplot(x='컬럼', data=df) - 사분위수와 이상치 시각화"
            },
            { 
                code: "sns.boxplot(x='category', y='value', data=df)", 
                desc: "범주별 박스플롯 그리기",
                pron: "에스엔에스 닷 박스플롯 엑스 카테고리 와이 밸류 데이터 디에프",
                grammar: "x=범주, y=수치 - 범주별 분포 비교"
            },
            { 
                code: "sns.countplot(x='col', data=df)", 
                desc: "범주별 빈도 막대그래프",
                pron: "에스엔에스 닷 카운트플롯 엑스 컬 데이터 디에프",
                grammar: "sns.countplot() - 각 범주의 개수를 막대로 표시"
            },
            { 
                code: "sns.barplot(x='category', y='value', data=df)", 
                desc: "범주별 평균 막대그래프",
                pron: "에스엔에스 닷 바플롯 엑스 카테고리 와이 밸류 데이터 디에프",
                grammar: "sns.barplot() - 범주별 평균값 막대그래프, 신뢰구간 포함"
            },
            { 
                code: "sns.scatterplot(x='col1', y='col2', data=df)", 
                desc: "산점도 그리기",
                pron: "에스엔에스 닷 스캐터플롯 엑스 컬원 와이 컬투 데이터 디에프",
                grammar: "sns.scatterplot(x,y) - 두 변수 간 관계 시각화"
            },
            { 
                code: "sns.heatmap(df.corr(), annot=True, cmap='coolwarm')", 
                desc: "상관관계 히트맵 (수치 표시)",
                pron: "에스엔에스 닷 히트맵 디에프닷코어 아노트트루 씨맵 쿨웜",
                grammar: "annot=True - 셀에 숫자 표시, cmap - 색상 맵"
            },
            { 
                code: "sns.heatmap(df.corr(), annot=True, fmt='.2f')", 
                desc: "상관관계 히트맵 (소수점 2자리)",
                pron: "에스엔에스 닷 히트맵 디에프닷코어 아노트트루 포맷 포인트투에프",
                grammar: "fmt='.2f' - 소수점 2자리까지 표시 형식"
            },
            { 
                code: "plt.title('Title')", 
                desc: "그래프 제목 설정",
                pron: "피엘티 닷 타이틀 타이틀",
                grammar: "plt.title('문자열') - 그래프 상단에 제목 추가"
            },
            { 
                code: "plt.xlabel('X Label')", 
                desc: "X축 레이블 설정",
                pron: "피엘티 닷 엑스라벨 엑스라벨",
                grammar: "plt.xlabel('문자열') - X축 이름 설정"
            },
            { 
                code: "plt.ylabel('Y Label')", 
                desc: "Y축 레이블 설정",
                pron: "피엘티 닷 와이라벨 와이라벨",
                grammar: "plt.ylabel('문자열') - Y축 이름 설정"
            },
            { 
                code: "plt.xticks(rotation=45)", 
                desc: "X축 레이블 45도 회전",
                pron: "피엘티 닷 엑스틱스 로테이션 포티파이브",
                grammar: "plt.xticks(rotation=각도) - 레이블 회전으로 겹침 방지"
            },
            { 
                code: "plt.tight_layout()", 
                desc: "레이아웃 자동 조정",
                pron: "피엘티 닷 타이트레이아웃",
                grammar: "plt.tight_layout() - 요소 간 간격 자동 조정"
            },
            { 
                code: "plt.show()", 
                desc: "그래프 출력",
                pron: "피엘티 닷 쇼",
                grammar: "plt.show() - 그래프를 화면에 표시"
            },
            { 
                code: "df.corr()", 
                desc: "상관계수 행렬 계산",
                pron: "디에프 닷 코어",
                grammar: "df.corr() - 수치형 컬럼 간 피어슨 상관계수"
            },
            { 
                code: "df.corr()['target'].sort_values(ascending=False)", 
                desc: "타겟과의 상관관계 정렬",
                pron: "디에프닷코어 타겟 닷 소트밸류스 어센딩 폴스",
                grammar: "['타겟'].sort_values() - 타겟과의 상관관계 내림차순 정렬"
            }
        ]
    },
    
    // 카테고리 6: 모델링
    modeling: {
        name: "모델링",
        icon: "🤖",
        codes: [
            { 
                code: "X = df.drop(['target'], axis=1)", 
                desc: "피처(X) 분리 - 타겟 컬럼 제외",
                pron: "엑스 이퀄 디에프 닷 드롭 타겟 액시스원",
                grammar: "X = df.drop(['타겟'], axis=1) - 타겟 제외한 나머지가 피처"
            },
            { 
                code: "y = df['target']", 
                desc: "타겟(y) 분리",
                pron: "와이 이퀄 디에프 타겟",
                grammar: "y = df['타겟컬럼'] - 예측할 타겟 변수 분리"
            },
            { 
                code: "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)", 
                desc: "8:2 비율로 데이터 분할",
                pron: "엑스트레인 엑스테스트 와이트레인 와이테스트 이퀄 트레인테스트스플릿 엑스 와이 테스트사이즈 포인트투 랜덤스테이트 포티투",
                grammar: "test_size=0.2 - 20% 테스트, random_state - 재현성 위한 시드"
            },
            { 
                code: "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)", 
                desc: "7:3 비율로 데이터 분할",
                pron: "엑스트레인 엑스테스트 와이트레인 와이테스트 이퀄 트레인테스트스플릿 엑스 와이 테스트사이즈 포인트쓰리 랜덤스테이트 포티투",
                grammar: "test_size=0.3 - 30% 테스트 데이터"
            },
            { 
                code: "model = LinearRegression()", 
                desc: "선형 회귀 모델 생성",
                pron: "모델 이퀄 리니어리그레션",
                grammar: "LinearRegression() - 연속형 타겟 예측용 선형 모델"
            },
            { 
                code: "model = LogisticRegression(random_state=42)", 
                desc: "로지스틱 회귀 모델 생성",
                pron: "모델 이퀄 로지스틱리그레션 랜덤스테이트 포티투",
                grammar: "LogisticRegression() - 이진/다중 분류용 모델"
            },
            { 
                code: "model = RandomForestRegressor(random_state=42)", 
                desc: "랜덤포레스트 회귀 모델 생성",
                pron: "모델 이퀄 랜덤포레스트리그레서 랜덤스테이트 포티투",
                grammar: "RandomForestRegressor() - 여러 결정트리 앙상블 회귀 모델"
            },
            { 
                code: "model = RandomForestRegressor(random_state=42, n_estimators=100)", 
                desc: "랜덤포레스트 회귀 (트리 100개)",
                pron: "모델 이퀄 랜덤포레스트리그레서 랜덤스테이트 포티투 엔에스티메이터스 헌드레드",
                grammar: "n_estimators=100 - 트리 개수, 기본값 100"
            },
            { 
                code: "model = RandomForestClassifier(random_state=42)", 
                desc: "랜덤포레스트 분류 모델 생성",
                pron: "모델 이퀄 랜덤포레스트클래시파이어 랜덤스테이트 포티투",
                grammar: "RandomForestClassifier() - 앙상블 분류 모델"
            },
            { 
                code: "model = DecisionTreeClassifier(random_state=42)", 
                desc: "의사결정나무 분류 모델 생성",
                pron: "모델 이퀄 디시전트리클래시파이어 랜덤스테이트 포티투",
                grammar: "DecisionTreeClassifier() - 단일 트리 분류 모델"
            },
            { 
                code: "model.fit(X_train, y_train)", 
                desc: "모델 학습 (훈련 데이터로)",
                pron: "모델 닷 핏 엑스트레인 와이트레인",
                grammar: ".fit(X, y) - 피처와 타겟으로 모델 학습"
            },
            { 
                code: "y_pred = model.predict(X_test)", 
                desc: "테스트 데이터 예측",
                pron: "와이프레드 이퀄 모델 닷 프리딕트 엑스테스트",
                grammar: ".predict(X) - 학습된 모델로 예측값 생성"
            },
            { 
                code: "model.feature_importances_", 
                desc: "피처 중요도 확인 (트리 모델)",
                pron: "모델 닷 피처임포턴시스 언더스코어",
                grammar: ".feature_importances_ - 트리 모델의 피처별 중요도 배열"
            },
            { 
                code: "model.coef_", 
                desc: "회귀 계수 확인 (선형 모델)",
                pron: "모델 닷 코에프 언더스코어",
                grammar: ".coef_ - 선형 모델의 피처별 가중치(계수)"
            },
            { 
                code: "model.intercept_", 
                desc: "절편 확인 (선형 모델)",
                pron: "모델 닷 인터셉트 언더스코어",
                grammar: ".intercept_ - 선형 모델의 y절편"
            }
        ]
    },
    
    // 카테고리 7: 평가
    evaluation: {
        name: "평가",
        icon: "📈",
        codes: [
            { 
                code: "rmse = np.sqrt(mean_squared_error(y_test, y_pred))", 
                desc: "RMSE 계산 (회귀)",
                pron: "알엠에스이 이퀄 넘파이 닷 스퀘어루트 민스퀘어드에러 와이테스트 와이프레드",
                grammar: "np.sqrt(MSE) - MSE에 제곱근을 씌워 RMSE 계산"
            },
            { 
                code: "mse = mean_squared_error(y_test, y_pred)", 
                desc: "MSE 계산 (회귀)",
                pron: "엠에스이 이퀄 민스퀘어드에러 와이테스트 와이프레드",
                grammar: "mean_squared_error(실제, 예측) - 평균제곱오차"
            },
            { 
                code: "r2 = r2_score(y_test, y_pred)", 
                desc: "R2 스코어 계산 (회귀)",
                pron: "알투 이퀄 알투스코어 와이테스트 와이프레드",
                grammar: "r2_score(실제, 예측) - 1에 가까울수록 좋은 설명력"
            },
            { 
                code: "accuracy = accuracy_score(y_test, y_pred)", 
                desc: "정확도 계산 (분류)",
                pron: "액큐러시 이퀄 액큐러시스코어 와이테스트 와이프레드",
                grammar: "accuracy_score(실제, 예측) - 정답 비율"
            },
            { 
                code: "f1 = f1_score(y_test, y_pred)", 
                desc: "F1 스코어 계산 (이진 분류)",
                pron: "에프원 이퀄 에프원스코어 와이테스트 와이프레드",
                grammar: "f1_score(실제, 예측) - 정밀도와 재현율의 조화평균"
            },
            { 
                code: "f1 = f1_score(y_test, y_pred, average='weighted')", 
                desc: "F1 스코어 계산 (다중 분류)",
                pron: "에프원 이퀄 에프원스코어 와이테스트 와이프레드 애버리지 웨이티드",
                grammar: "average='weighted' - 클래스별 샘플 수로 가중 평균"
            },
            { 
                code: "cm = confusion_matrix(y_test, y_pred)", 
                desc: "혼동 행렬 생성",
                pron: "씨엠 이퀄 컨퓨전매트릭스 와이테스트 와이프레드",
                grammar: "confusion_matrix(실제, 예측) - TP, FP, FN, TN 행렬"
            },
            { 
                code: "print(classification_report(y_test, y_pred))", 
                desc: "분류 리포트 출력",
                pron: "프린트 클래시피케이션리포트 와이테스트 와이프레드",
                grammar: "classification_report() - precision, recall, f1 종합 보고서"
            },
            { 
                code: "print(f\"RMSE: {rmse:.4f}\")", 
                desc: "RMSE 소수점 4자리 출력",
                pron: "프린트 에프스트링 알엠에스이 알엠에스이 콜론 닷 포에프",
                grammar: "f\"{{변수:.4f}}\" - f-string으로 소수점 4자리 포맷"
            },
            { 
                code: "print(f\"R2 Score: {r2:.4f}\")", 
                desc: "R2 스코어 소수점 4자리 출력",
                pron: "프린트 에프스트링 알투스코어 알투 콜론 닷 포에프",
                grammar: ":.4f - 소수점 아래 4자리까지 출력"
            },
            { 
                code: "print(f\"Accuracy: {accuracy:.4f}\")", 
                desc: "정확도 소수점 4자리 출력",
                pron: "프린트 에프스트링 액큐러시 액큐러시 콜론 닷 포에프",
                grammar: "f-string 내 {변수:.4f}로 포맷팅"
            },
            { 
                code: "print(f\"F1 Score: {f1:.4f}\")", 
                desc: "F1 스코어 소수점 4자리 출력",
                pron: "프린트 에프스트링 에프원스코어 에프원 콜론 닷 포에프",
                grammar: ":.4f - float 소수점 4자리 지정"
            }
        ]
    },
    
    // 카테고리 8: 파생변수
    feature: {
        name: "파생변수",
        icon: "✨",
        codes: [
            { 
                code: "df['new_col'] = df['col1'] + df['col2']", 
                desc: "두 컬럼 덧셈으로 새 컬럼 생성",
                pron: "디에프 뉴컬 이퀄 디에프 컬원 플러스 디에프 컬투",
                grammar: "df['새컬럼'] = 연산 - 새 컬럼 생성 및 값 할당"
            },
            { 
                code: "df['new_col'] = df['col1'] - df['col2']", 
                desc: "두 컬럼 뺄셈으로 새 컬럼 생성",
                pron: "디에프 뉴컬 이퀄 디에프 컬원 마이너스 디에프 컬투",
                grammar: "컬럼 간 사칙연산으로 파생변수 생성"
            },
            { 
                code: "df['new_col'] = df['col1'] * df['col2']", 
                desc: "두 컬럼 곱셈으로 새 컬럼 생성",
                pron: "디에프 뉴컬 이퀄 디에프 컬원 곱하기 디에프 컬투",
                grammar: "* 연산자로 컬럼 간 곱셈"
            },
            { 
                code: "df['ratio'] = df['col1'] / df['col2']", 
                desc: "두 컬럼 비율 계산",
                pron: "디에프 레이시오 이퀄 디에프 컬원 나누기 디에프 컬투",
                grammar: "/ 연산자로 비율 계산, 0 나눗셈 주의"
            },
            { 
                code: "df['ratio'] = df['col1'] / (df['col2'] + 1)", 
                desc: "0 나눗셈 방지 비율 계산",
                pron: "디에프 레이시오 이퀄 디에프 컬원 나누기 디에프 컬투 플러스 원",
                grammar: "분모에 +1을 더해 0으로 나눔 방지"
            },
            { 
                code: "df['log_col'] = np.log1p(df['col'])", 
                desc: "로그 변환 (log1p)",
                pron: "디에프 로그컬 이퀄 넘파이 닷 로그원피 디에프 컬",
                grammar: "np.log1p(x) = log(1+x) - 0 포함 데이터도 변환 가능"
            },
            { 
                code: "df['sqrt_col'] = np.sqrt(df['col'])", 
                desc: "제곱근 변환",
                pron: "디에프 스퀘어루트컬 이퀄 넘파이 닷 스퀘어루트 디에프 컬",
                grammar: "np.sqrt(x) - 제곱근으로 스케일 축소"
            },
            { 
                code: "df['hour'] = pd.to_datetime(df['datetime']).dt.hour", 
                desc: "시간 추출",
                pron: "디에프 아워 이퀄 피디 닷 투데이트타임 디에프 데이트타임 닷 디티 닷 아워",
                grammar: "pd.to_datetime().dt.hour - datetime에서 시간만 추출"
            },
            { 
                code: "df['month'] = pd.to_datetime(df['datetime']).dt.month", 
                desc: "월 추출",
                pron: "디에프 먼쓰 이퀄 피디 닷 투데이트타임 디에프 데이트타임 닷 디티 닷 먼쓰",
                grammar: ".dt.month - 1~12 월 추출"
            },
            { 
                code: "df['dayofweek'] = pd.to_datetime(df['datetime']).dt.dayofweek", 
                desc: "요일 추출 (0=월요일)",
                pron: "디에프 데이오브위크 이퀄 피디 닷 투데이트타임 디에프 데이트타임 닷 디티 닷 데이오브위크",
                grammar: ".dt.dayofweek - 0(월)~6(일) 요일 숫자"
            },
            { 
                code: "df.groupby('col')['value'].mean()", 
                desc: "그룹별 평균 계산",
                pron: "디에프 닷 그룹바이 컬 밸류 닷 민",
                grammar: ".groupby('기준')['대상'].mean() - 그룹별 집계"
            },
            { 
                code: "df.groupby('col')['value'].sum()", 
                desc: "그룹별 합계 계산",
                pron: "디에프 닷 그룹바이 컬 밸류 닷 썸",
                grammar: ".groupby()['컬럼'].sum() - 그룹별 합계"
            },
            { 
                code: "df.groupby('col').agg({'col1': 'mean', 'col2': 'sum'})", 
                desc: "컬럼별 다른 집계 함수 적용",
                pron: "디에프 닷 그룹바이 컬 닷 애그 컬원 민 컬투 썸",
                grammar: ".agg({컬럼: 함수}) - 컬럼마다 다른 집계 적용"
            },
            { 
                code: "df.sort_values('col', ascending=False)", 
                desc: "내림차순 정렬",
                pron: "디에프 닷 소트밸류스 컬 어센딩 폴스",
                grammar: ".sort_values(컬럼, ascending=False) - 큰 값부터 정렬"
            },
            { 
                code: "df[df['col'] > 0]", 
                desc: "조건 필터링 (양수만)",
                pron: "디에프 디에프 컬 그레이터댄 제로",
                grammar: "df[조건] - 조건이 True인 행만 선택"
            },
            { 
                code: "df[(df['col1'] > 0) & (df['col2'] < 10)]", 
                desc: "다중 조건 필터링 (AND)",
                pron: "디에프 디에프 컬원 그레이터댄 제로 앤드 디에프 컬투 레스댄 텐",
                grammar: "(조건1) & (조건2) - 두 조건 모두 만족, 괄호 필수"
            },
            { 
                code: "df['col'].apply(lambda x: x * 2)", 
                desc: "람다 함수로 변환",
                pron: "디에프 컬 닷 어플라이 람다 엑스 콜론 엑스 곱하기 투",
                grammar: ".apply(lambda x: 연산) - 각 값에 함수 적용"
            },
            { 
                code: "df['col'].map({'A': 1, 'B': 2, 'C': 3})", 
                desc: "딕셔너리로 값 매핑",
                pron: "디에프 컬 닷 맵 에이 원 비 투 씨 쓰리",
                grammar: ".map({원래값: 변환값}) - 딕셔너리로 값 변환"
            },
            { 
                code: "pd.cut(df['col'], bins=3)", 
                desc: "수치형을 3구간으로 분할",
                pron: "피디 닷 컷 디에프 컬 빈스 쓰리",
                grammar: "pd.cut(데이터, bins=n) - 동일 너비 구간 분할"
            },
            { 
                code: "pd.qcut(df['col'], q=4)", 
                desc: "4분위수로 분할",
                pron: "피디 닷 큐컷 디에프 컬 큐 포",
                grammar: "pd.qcut(데이터, q=n) - 동일 개수 구간 분할(분위수)"
            }
        ]
    },
    
    // 카테고리 9: 결과 해석
    interpretation: {
        name: "결과 해석",
        icon: "💬",
        codes: [
            { 
                code: "print(f\"RMSE: {rmse:.2f}\")", 
                desc: "RMSE 소수점 2자리 출력",
                pron: "프린트 에프스트링 알엠에스이 알엠에스이 콜론 닷 투에프",
                grammar: ":.2f - 소수점 2자리까지 출력 포맷"
            },
            { 
                code: "print(f\"Accuracy: {accuracy*100:.1f}%\")", 
                desc: "정확도를 백분율로 출력",
                pron: "프린트 에프스트링 액큐러시 액큐러시 곱하기 백 콜론 닷 원에프 퍼센트",
                grammar: "*100으로 백분율 변환, :.1f로 소수점 1자리"
            },
            { 
                code: "print(f\"Train: {X_train.shape}, Test: {X_test.shape}\")", 
                desc: "학습/테스트 데이터 크기 출력",
                pron: "프린트 에프스트링 트레인 엑스트레인쉐이프 테스트 엑스테스트쉐이프",
                grammar: ".shape로 (행,열) 크기 확인하여 출력"
            },
            { 
                code: "print(f\"Features: {X.columns.tolist()}\")", 
                desc: "사용된 피처 목록 출력",
                pron: "프린트 에프스트링 피처스 엑스 닷 컬럼스 닷 투리스트",
                grammar: ".columns.tolist()로 피처명 리스트 출력"
            },
            { 
                code: "print(f\"Target: {y.name}\")", 
                desc: "타겟 변수명 출력",
                pron: "프린트 에프스트링 타겟 와이 닷 네임",
                grammar: ".name - Series의 컬럼명(이름) 속성"
            },
            { 
                code: "print(f\"Missing: {df.isna().sum().sum()}\")", 
                desc: "총 결측치 개수 출력",
                pron: "프린트 에프스트링 미싱 디에프 닷 이즈나 닷 썸 닷 썸",
                grammar: "isna().sum().sum()으로 전체 결측치 총합"
            }
        ]
    }
};

// 모든 카테고리 키 배열
const categories = Object.keys(codeData);

// 총 코드 패턴 수 계산
let totalCodes = 0;
categories.forEach(key => {
    totalCodes += codeData[key].codes.length;
});
console.log(`Total code patterns: ${totalCodes}`);
