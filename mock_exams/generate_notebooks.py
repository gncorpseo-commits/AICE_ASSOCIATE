"""
AICE Associate Mock Exam Notebooks Generator
30개의 모의고사 Jupyter Notebook을 생성합니다.
"""

import json
import os

# 노트북 생성 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 모의고사 정보 정의
MOCK_EXAMS = {
    # Level 1 - Basic (회귀 5개 + 분류 5개)
    'level_1_basic': [
        {'num': '01', 'name': 'delivery', 'title': '배달 소요시간 예측', 'type': 'regression', 
         'target': 'delivery_time', 'target_desc': '배달 소요시간 (분)', 'id_col': 'order_id',
         'scenario': '당신은 A 배달회사의 데이터 분석가입니다. 배달 주문 데이터를 분석하여 배달 소요시간을 예측하는 머신러닝 모델을 구축하세요.'},
        
        {'num': '02', 'name': 'sales', 'title': '월별 매출 예측', 'type': 'regression',
         'target': 'monthly_sales', 'target_desc': '월별 매출액', 'id_col': 'store_id',
         'scenario': '당신은 B 유통회사의 데이터 분석가입니다. 매장 데이터를 분석하여 월별 매출을 예측하는 모델을 구축하세요.'},
        
        {'num': '03', 'name': 'temperature', 'title': '기온 예측', 'type': 'regression',
         'target': 'temperature', 'target_desc': '기온 (섭씨)', 'id_col': None,
         'scenario': '당신은 기상청 데이터 분석가입니다. 기상 데이터를 분석하여 기온을 예측하는 모델을 구축하세요.'},
        
        {'num': '04', 'name': 'housing', 'title': '주택 가격 예측', 'type': 'regression',
         'target': 'price', 'target_desc': '주택 가격 (원)', 'id_col': 'house_id',
         'scenario': '당신은 C 부동산 회사의 데이터 분석가입니다. 주택 정보를 분석하여 가격을 예측하는 모델을 구축하세요.'},
        
        {'num': '05', 'name': 'traffic', 'title': '교통량 예측', 'type': 'regression',
         'target': 'traffic_volume', 'target_desc': '교통량', 'id_col': 'record_id',
         'scenario': '당신은 교통관리센터의 데이터 분석가입니다. 도로 데이터를 분석하여 교통량을 예측하는 모델을 구축하세요.'},
        
        {'num': '06', 'name': 'churn', 'title': '고객 이탈 예측', 'type': 'classification',
         'target': 'churn', 'target_desc': '이탈 여부 (0: 유지, 1: 이탈)', 'id_col': 'customer_id',
         'scenario': '당신은 D 서비스 회사의 데이터 분석가입니다. 고객 데이터를 분석하여 이탈 여부를 예측하는 모델을 구축하세요.'},
        
        {'num': '07', 'name': 'spam', 'title': '스팸 메일 분류', 'type': 'classification',
         'target': 'is_spam', 'target_desc': '스팸 여부 (0: 정상, 1: 스팸)', 'id_col': 'email_id',
         'scenario': '당신은 E 이메일 서비스의 데이터 분석가입니다. 이메일 데이터를 분석하여 스팸을 분류하는 모델을 구축하세요.'},
        
        {'num': '08', 'name': 'loan', 'title': '대출 승인 예측', 'type': 'classification',
         'target': 'approved', 'target_desc': '승인 여부 (0: 거절, 1: 승인)', 'id_col': 'applicant_id',
         'scenario': '당신은 F 금융회사의 데이터 분석가입니다. 대출 신청 데이터를 분석하여 승인 여부를 예측하는 모델을 구축하세요.'},
        
        {'num': '09', 'name': 'disease', 'title': '질병 예측', 'type': 'classification',
         'target': 'has_disease', 'target_desc': '질병 유무 (0: 정상, 1: 질병)', 'id_col': 'patient_id',
         'scenario': '당신은 G 병원의 데이터 분석가입니다. 환자 데이터를 분석하여 질병 유무를 예측하는 모델을 구축하세요.'},
        
        {'num': '10', 'name': 'satisfaction', 'title': '고객 만족도 분류', 'type': 'classification',
         'target': 'satisfaction', 'target_desc': '만족도 (Low/Medium/High)', 'id_col': 'customer_id',
         'scenario': '당신은 H 서비스 회사의 데이터 분석가입니다. 고객 피드백 데이터를 분석하여 만족도를 분류하는 모델을 구축하세요.'},
    ],
    
    # Level 2 - Intermediate
    'level_2_intermediate': [
        {'num': '11', 'name': 'taxi', 'title': '택시 이동시간 예측', 'type': 'regression',
         'target': 'trip_duration', 'target_desc': '이동시간 (분)', 'id_col': 'trip_id',
         'scenario': '당신은 택시 서비스 회사의 데이터 분석가입니다. 택시 운행 데이터를 분석하여 이동시간을 예측하는 모델을 구축하세요.'},
        
        {'num': '12', 'name': 'demand', 'title': '상품 수요 예측', 'type': 'regression',
         'target': 'demand', 'target_desc': '수요량', 'id_col': 'product_id',
         'scenario': '당신은 유통회사의 데이터 분석가입니다. 상품 데이터를 분석하여 수요를 예측하는 모델을 구축하세요.'},
        
        {'num': '13', 'name': 'energy', 'title': '에너지 소비 예측', 'type': 'regression',
         'target': 'energy_consumption', 'target_desc': '에너지 소비량', 'id_col': 'building_id',
         'scenario': '당신은 에너지 관리 회사의 데이터 분석가입니다. 건물 데이터를 분석하여 에너지 소비를 예측하는 모델을 구축하세요.'},
        
        {'num': '14', 'name': 'inventory', 'title': '적정 재고 예측', 'type': 'regression',
         'target': 'optimal_stock', 'target_desc': '적정 재고량', 'id_col': 'sku_id',
         'scenario': '당신은 물류회사의 데이터 분석가입니다. 상품 데이터를 분석하여 적정 재고를 예측하는 모델을 구축하세요.'},
        
        {'num': '15', 'name': 'waiting', 'title': '대기시간 예측', 'type': 'regression',
         'target': 'wait_time', 'target_desc': '대기시간 (분)', 'id_col': 'ticket_id',
         'scenario': '당신은 서비스 센터의 데이터 분석가입니다. 대기 데이터를 분석하여 대기시간을 예측하는 모델을 구축하세요.'},
        
        {'num': '16', 'name': 'fraud', 'title': '금융 사기 탐지', 'type': 'classification',
         'target': 'is_fraud', 'target_desc': '사기 여부 (0: 정상, 1: 사기)', 'id_col': 'transaction_id',
         'scenario': '당신은 금융회사의 데이터 분석가입니다. 거래 데이터를 분석하여 사기를 탐지하는 모델을 구축하세요.'},
        
        {'num': '17', 'name': 'conversion', 'title': '구매 전환 예측', 'type': 'classification',
         'target': 'converted', 'target_desc': '전환 여부 (0: 미전환, 1: 전환)', 'id_col': 'visitor_id',
         'scenario': '당신은 이커머스 회사의 데이터 분석가입니다. 방문자 데이터를 분석하여 구매 전환을 예측하는 모델을 구축하세요.'},
        
        {'num': '18', 'name': 'sentiment', 'title': '리뷰 감성 분류', 'type': 'classification',
         'target': 'sentiment', 'target_desc': '감성 (Negative/Neutral/Positive)', 'id_col': 'review_id',
         'scenario': '당신은 리뷰 분석 회사의 데이터 분석가입니다. 리뷰 데이터를 분석하여 감성을 분류하는 모델을 구축하세요.'},
        
        {'num': '19', 'name': 'credit', 'title': '신용 등급 예측', 'type': 'classification',
         'target': 'risk_grade', 'target_desc': '신용 등급 (A/B/C/D)', 'id_col': 'customer_id',
         'scenario': '당신은 신용평가 회사의 데이터 분석가입니다. 고객 데이터를 분석하여 신용 등급을 예측하는 모델을 구축하세요.'},
        
        {'num': '20', 'name': 'click', 'title': '광고 클릭 예측', 'type': 'classification',
         'target': 'clicked', 'target_desc': '클릭 여부 (0: 미클릭, 1: 클릭)', 'id_col': 'impression_id',
         'scenario': '당신은 광고 플랫폼의 데이터 분석가입니다. 광고 노출 데이터를 분석하여 클릭을 예측하는 모델을 구축하세요.'},
    ],
    
    # Level 3 - Advanced
    'level_3_advanced': [
        {'num': '21', 'name': 'navigation', 'title': '내비게이션 도착시간 예측 (실제 기출)', 'type': 'regression',
         'target': 'arrival_time', 'target_desc': '도착시간 (분)', 'id_col': 'route_id',
         'scenario': '당신은 내비게이션 서비스 회사의 데이터 분석가입니다. 경로 데이터를 분석하여 도착시간을 예측하는 머신러닝 모델을 구축하세요. 이 모델은 사용자에게 정확한 도착 예정 시간을 제공하는 데 활용됩니다.'},
        
        {'num': '22', 'name': 'telecom', 'title': '통신사 고객 해지 예측 (실제 기출)', 'type': 'classification',
         'target': 'churn', 'target_desc': '해지 여부 (0: 유지, 1: 해지)', 'id_col': 'customer_id',
         'scenario': '당신은 통신사의 데이터 분석가입니다. 고객 데이터를 분석하여 서비스 해지 여부를 예측하는 모델을 구축하세요. 이 모델은 이탈 위험 고객을 사전에 식별하여 유지 전략을 수립하는 데 활용됩니다.'},
        
        {'num': '23', 'name': 'usedcar', 'title': '중고차 가격 예측', 'type': 'regression',
         'target': 'price', 'target_desc': '가격 (달러)', 'id_col': 'car_id',
         'scenario': '당신은 중고차 거래 플랫폼의 데이터 분석가입니다. 차량 데이터를 분석하여 적정 가격을 예측하는 모델을 구축하세요.'},
        
        {'num': '24', 'name': 'quality', 'title': '제품 품질 예측', 'type': 'regression',
         'target': 'quality_score', 'target_desc': '품질 점수', 'id_col': 'batch_id',
         'scenario': '당신은 제조업체의 데이터 분석가입니다. 생산 데이터를 분석하여 제품 품질을 예측하는 모델을 구축하세요.'},
        
        {'num': '25', 'name': 'subscription', 'title': '구독 서비스 유지 예측', 'type': 'classification',
         'target': 'retained', 'target_desc': '유지 여부 (0: 해지, 1: 유지)', 'id_col': 'user_id',
         'scenario': '당신은 구독 서비스 회사의 데이터 분석가입니다. 사용자 데이터를 분석하여 구독 유지를 예측하는 모델을 구축하세요.'},
        
        {'num': '26', 'name': 'logistics', 'title': '물류 배송시간 예측', 'type': 'regression',
         'target': 'delivery_hours', 'target_desc': '배송시간 (시간)', 'id_col': 'shipment_id',
         'scenario': '당신은 물류회사의 데이터 분석가입니다. 배송 데이터를 분석하여 배송시간을 예측하는 모델을 구축하세요.'},
        
        {'num': '27', 'name': 'marketing', 'title': '마케팅 반응 예측', 'type': 'classification',
         'target': 'responded', 'target_desc': '반응 여부 (0: 무반응, 1: 반응)', 'id_col': 'customer_id',
         'scenario': '당신은 마케팅 회사의 데이터 분석가입니다. 고객 데이터를 분석하여 캠페인 반응을 예측하는 모델을 구축하세요.'},
        
        {'num': '28', 'name': 'production', 'title': '생산량 예측', 'type': 'regression',
         'target': 'production_units', 'target_desc': '생산량 (개)', 'id_col': 'shift_id',
         'scenario': '당신은 제조공장의 데이터 분석가입니다. 생산 데이터를 분석하여 생산량을 예측하는 모델을 구축하세요.'},
        
        {'num': '29', 'name': 'final_reg', 'title': '최종 모의고사 (회귀)', 'type': 'regression',
         'target': 'target', 'target_desc': '타겟 값', 'id_col': 'id',
         'scenario': '이것은 AICE Associate 최종 모의고사입니다. 주어진 데이터를 분석하여 타겟 값을 예측하는 머신러닝 모델을 구축하세요. 실제 시험과 동일한 환경에서 90분 내에 완료하세요.'},
        
        {'num': '30', 'name': 'final_clf', 'title': '최종 모의고사 (분류)', 'type': 'classification',
         'target': 'target', 'target_desc': '타겟 클래스', 'id_col': 'id',
         'scenario': '이것은 AICE Associate 최종 모의고사입니다. 주어진 데이터를 분석하여 타겟 클래스를 예측하는 머신러닝 모델을 구축하세요. 실제 시험과 동일한 환경에서 90분 내에 완료하세요.'},
    ],
}


def create_notebook(exam_info, level):
    """Create a Jupyter notebook for a mock exam"""
    
    num = exam_info['num']
    name = exam_info['name']
    title = exam_info['title']
    exam_type = exam_info['type']
    target = exam_info['target']
    target_desc = exam_info['target_desc']
    id_col = exam_info['id_col']
    scenario = exam_info['scenario']
    
    data_file = f"mock_{num}_{name}.csv"
    data_path = f"../data/{data_file}"
    
    is_regression = exam_type == 'regression'
    
    # Notebook cells
    cells = []
    
    # Title cell
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# AICE Associate Mock Exam {num}\n",
            f"## {title}\n",
            "\n",
            "---\n",
            "\n",
            f"**Scenario:** {scenario}\n",
            "\n",
            f"- **Data File:** `{data_file}`\n",
            f"- **Target Variable:** `{target}` ({target_desc})\n",
            f"- **Problem Type:** {'Regression' if is_regression else 'Classification'}\n",
            "\n",
            "**Time Limit:** 90 minutes\n",
            "\n",
            "**Total:** 15 questions / 100 points\n",
            "\n",
            "---"
        ]
    })
    
    # Q1: Import libraries (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 1. Import Libraries (5 points)\n",
            "\n",
            "Import the necessary libraries for data analysis and machine learning."
        ]
    })
    
    if is_regression:
        import_code = """# Your code here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Visualization settings
plt.rcParams['figure.figsize'] = (10, 6)
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported successfully!")"""
    else:
        import_code = """# Your code here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Visualization settings
plt.rcParams['figure.figsize'] = (10, 6)
import warnings
warnings.filterwarnings('ignore')

print("Libraries imported successfully!")"""
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [import_code],
        "execution_count": None,
        "outputs": []
    })
    
    # Q2: Load data (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 2. Load Data (5 points)\n",
            "\n",
            f"Load `{data_file}` and save it to variable `df`. Display the first 5 rows.\n",
            "\n",
            "**Important:** Use variable name `df`"
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [f"""# Your code here
df = pd.read_csv('{data_path}')
df.head()"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q3: Check shape (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 3. Check Data Shape (5 points)\n",
            "\n",
            "Check the number of rows and columns in the data."
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
print(f"Data shape: {df.shape}")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q4: Data info (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 4. Data Information (5 points)\n",
            "\n",
            "Check data types and basic statistics using `info()` and `describe()`."
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
print("=== Data Info ===")
print(df.info())
print("\\n=== Basic Statistics ===")
df.describe()"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q5: Check missing values (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 5. Check Missing Values (5 points)\n",
            "\n",
            "Check the number of missing values for each column."
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
print("=== Missing Values ===")
print(df.isna().sum())
print(f"\\nTotal missing values: {df.isna().sum().sum()}")"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q6: Handle missing values (10 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 6. Handle Missing Values (10 points)\n",
            "\n",
            "Handle missing values appropriately:\n",
            "- Numeric columns: Replace with mean\n",
            "- Categorical columns: Replace with mode\n",
            "\n",
            "Save the processed DataFrame to variable `df_clean`.\n",
            "\n",
            "**Important:** Use variable name `df_clean`"
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
df_clean = df.copy()

# Handle numeric columns (mean)
numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
for col in numeric_cols:
    if df_clean[col].isna().sum() > 0:
        df_clean[col].fillna(df_clean[col].mean(), inplace=True)

# Handle categorical columns (mode)
categorical_cols = df_clean.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if df_clean[col].isna().sum() > 0:
        df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

print("Missing values after processing:")
print(df_clean.isna().sum())"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q7: Visualize target (7 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 7. Visualize Target Variable (7 points)\n",
            "\n",
            f"Visualize the distribution of the target variable (`{target}`)."
        ]
    })
    
    if is_regression:
        viz_code = f"""# Your code here
plt.figure(figsize=(10, 6))
sns.histplot(df_clean['{target}'], kde=True, bins=30)
plt.title('Distribution of {target}')
plt.xlabel('{target_desc}')
plt.ylabel('Frequency')
plt.show()"""
    else:
        viz_code = f"""# Your code here
plt.figure(figsize=(10, 6))
df_clean['{target}'].value_counts().plot(kind='bar')
plt.title('Distribution of {target}')
plt.xlabel('{target}')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()"""
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [viz_code],
        "execution_count": None,
        "outputs": []
    })
    
    # Q8: Correlation analysis (8 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 8. Correlation Analysis (8 points)\n",
            "\n",
            "Visualize correlations between numeric variables using a heatmap."
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
plt.figure(figsize=(12, 8))
numeric_df = df_clean.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q9: Feature engineering (10 points) - varies by exam
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 9. Feature Engineering (10 points)\n",
            "\n",
            "Create new features if needed and prepare the data for modeling.\n",
            "\n",
            "Hint: Consider creating derived features or transforming existing ones."
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
# Example: Create derived features if applicable
# df_clean['new_feature'] = df_clean['feature1'] * df_clean['feature2']

# Check columns
print("Columns:", df_clean.columns.tolist())
print("\\nData types:")
print(df_clean.dtypes)"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q10: Encoding (8 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 10. Encode Categorical Variables (8 points)\n",
            "\n",
            "Encode categorical variables using appropriate methods.\n",
            "\n",
            "Save the encoded DataFrame to variable `df_encoded`.\n",
            "\n",
            "**Important:** Use variable name `df_encoded`"
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
# Get categorical columns
cat_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
print(f"Categorical columns: {cat_cols}")

# One-hot encoding
if len(cat_cols) > 0:
    df_encoded = pd.get_dummies(df_clean, columns=cat_cols)
else:
    df_encoded = df_clean.copy()

print(f"\\nShape after encoding: {df_encoded.shape}")
df_encoded.head()"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q11: Split features and target (5 points)
    drop_cols = f"['{target}'" + (f", '{id_col}']" if id_col else "]")
    
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 11. Split Features and Target (5 points)\n",
            "\n",
            f"Separate features (X) and target (y).\n",
            f"- Target: `{target}`\n",
            f"- Exclude: `{target}`" + (f", `{id_col}`" if id_col else "") + "\n",
            "\n",
            "**Important:** Use variable names `X` and `y`"
        ]
    })
    
    drop_code = f"['{target}'"
    if id_col:
        drop_code += f", '{id_col}'"
    drop_code += "]"
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [f"""# Your code here
# Columns to drop
drop_cols = {drop_code}
drop_cols = [col for col in drop_cols if col in df_encoded.columns]

X = df_encoded.drop(drop_cols, axis=1)
y = df_encoded['{target}']

print(f"X shape: {{X.shape}}")
print(f"y shape: {{y.shape}}")
print(f"\\nFeatures: {{list(X.columns)}}")"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q12: Train/Test split (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 12. Train/Test Split (5 points)\n",
            "\n",
            "Split the data into training (80%) and test (20%) sets.\n",
            "- Use `random_state=42`\n",
            "\n",
            "**Important:** Use variable names `X_train, X_test, y_train, y_test`"
        ]
    })
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": ["""# Your code here
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")"""],
        "execution_count": None,
        "outputs": []
    })
    
    # Q13: Train model (10 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 13. Train Model (10 points)\n",
            "\n",
            f"Train a {'regression' if is_regression else 'classification'} model.\n",
            "- Use `random_state=42` if applicable\n",
            "\n",
            "**Important:** Save the trained model to variable `model`"
        ]
    })
    
    if is_regression:
        model_code = """# Your code here
# Option 1: LinearRegression
# model = LinearRegression()

# Option 2: RandomForestRegressor (recommended)
model = RandomForestRegressor(random_state=42, n_estimators=100)

model.fit(X_train, y_train)
print(f"Model trained: {type(model).__name__}")"""
    else:
        model_code = """# Your code here
# Option 1: LogisticRegression
# model = LogisticRegression(random_state=42, max_iter=1000)

# Option 2: RandomForestClassifier (recommended)
model = RandomForestClassifier(random_state=42, n_estimators=100)

model.fit(X_train, y_train)
print(f"Model trained: {type(model).__name__}")"""
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [model_code],
        "execution_count": None,
        "outputs": []
    })
    
    # Q14: Predict and evaluate (7 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 14. Predict and Evaluate (7 points)\n",
            "\n",
            "Make predictions on the test set and calculate evaluation metrics.\n",
            "\n",
            "**Important:** Save predictions to variable `y_pred`"
        ]
    })
    
    if is_regression:
        eval_code = """# Your code here
y_pred = model.predict(X_test)

# Calculate metrics
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("=== Model Evaluation ===")
print(f"RMSE: {rmse:.4f}")
print(f"R2 Score: {r2:.4f}")"""
    else:
        eval_code = """# Your code here
y_pred = model.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

print("=== Model Evaluation ===")
print(f"Accuracy: {accuracy:.4f}")
print(f"F1 Score: {f1:.4f}")"""
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [eval_code],
        "execution_count": None,
        "outputs": []
    })
    
    # Q15: Interpret results (5 points)
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Question 15. Interpret Results (5 points)\n",
            "\n",
            "Interpret the model's performance and provide business insights."
        ]
    })
    
    if is_regression:
        interpret_code = f"""# Your code here
print('''
===============================================================================
                         MODEL PERFORMANCE INTERPRETATION
===============================================================================

1. RMSE (Root Mean Squared Error): {{rmse:.4f}}
   - The average prediction error is approximately {{rmse:.2f}} units.
   - This means the model's predictions deviate from actual values by about {{rmse:.2f}} on average.

2. R2 Score: {{r2:.4f}}
   - The model explains {{r2*100:.1f}}% of the variance in the target variable.
   - {'This indicates good predictive performance.' if 'r2 > 0.7' else 'There is room for improvement.'}

3. Business Application:
   - This model can be used to predict {target_desc}.
   - Recommendations for improvement:
     * Collect more relevant features
     * Try different algorithms
     * Perform hyperparameter tuning

===============================================================================
''')

# Visualization: Actual vs Predicted
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted')
plt.show()"""
    else:
        interpret_code = f"""# Your code here
print('''
===============================================================================
                         MODEL PERFORMANCE INTERPRETATION
===============================================================================

1. Accuracy: {{accuracy:.4f}}
   - The model correctly classifies {{accuracy*100:.1f}}% of the samples.

2. F1 Score: {{f1:.4f}}
   - The harmonic mean of precision and recall is {{f1:.4f}}.
   - This indicates {'good' if 'f1 > 0.7' else 'moderate'} classification performance.

3. Business Application:
   - This model can be used to predict {target_desc}.
   - Recommendations for improvement:
     * Address class imbalance if present
     * Try different algorithms
     * Perform feature engineering

===============================================================================
''')

# Visualization: Confusion Matrix
from sklearn.metrics import ConfusionMatrixDisplay
plt.figure(figsize=(8, 6))
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.title('Confusion Matrix')
plt.show()"""
    
    cells.append({
        "cell_type": "code",
        "metadata": {},
        "source": [interpret_code],
        "execution_count": None,
        "outputs": []
    })
    
    # End cell
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\n",
            "\n",
            "## End of Mock Exam\n",
            "\n",
            "**Checklist before submission:**\n",
            "- [ ] All cells executed\n",
            "- [ ] Variable names match requirements\n",
            "- [ ] Results interpretation included\n",
            "- [ ] No errors in output\n",
            "\n",
            "**Good luck!**"
        ]
    })
    
    # Create notebook structure
    notebook = {
        "nbformat": 4,
        "nbformat_minor": 4,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.8.0"
            }
        },
        "cells": cells
    }
    
    return notebook


def generate_all_notebooks():
    """Generate all mock exam notebooks"""
    
    print("=" * 60)
    print("Generating AICE Associate Mock Exam Notebooks")
    print("=" * 60)
    
    for level, exams in MOCK_EXAMS.items():
        level_dir = os.path.join(BASE_DIR, level)
        os.makedirs(level_dir, exist_ok=True)
        
        print(f"\n[{level}]")
        
        for exam in exams:
            notebook = create_notebook(exam, level)
            filename = f"mock_{exam['num']}_{exam['name']}.ipynb"
            filepath = os.path.join(level_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(notebook, f, ensure_ascii=False, indent=2)
            
            print(f"  [OK] {filename}")
    
    print("\n" + "=" * 60)
    print("All 30 mock exam notebooks generated!")
    print("=" * 60)


if __name__ == "__main__":
    generate_all_notebooks()
