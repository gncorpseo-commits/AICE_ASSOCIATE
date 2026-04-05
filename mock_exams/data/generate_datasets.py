"""
AICE Associate 모의고사용 데이터셋 생성 스크립트
30개의 다양한 시나리오 데이터셋을 생성합니다.
"""

import numpy as np
import pandas as pd
import os

# 난수 시드 설정
np.random.seed(42)

# 데이터 저장 경로
DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_delivery_data(n=1000):
    """Mock 01: 배달 소요시간 예측 데이터"""
    data = {
        'order_id': range(1, n+1),
        'restaurant_lat': np.random.uniform(37.4, 37.6, n),
        'restaurant_lng': np.random.uniform(126.8, 127.1, n),
        'delivery_lat': np.random.uniform(37.4, 37.6, n),
        'delivery_lng': np.random.uniform(126.8, 127.1, n),
        'order_hour': np.random.randint(9, 23, n),
        'order_day': np.random.randint(0, 7, n),
        'weather': np.random.choice(['Clear', 'Cloudy', 'Rain'], n, p=[0.6, 0.25, 0.15]),
        'traffic': np.random.choice(['Low', 'Medium', 'High'], n, p=[0.3, 0.4, 0.3]),
    }
    df = pd.DataFrame(data)
    
    # 거리 계산
    distance = np.sqrt((df['delivery_lat'] - df['restaurant_lat'])**2 + 
                       (df['delivery_lng'] - df['restaurant_lng'])**2) * 100
    
    # 타겟 생성 (거리, 날씨, 교통에 따라)
    base_time = 15 + distance * 2
    weather_effect = df['weather'].map({'Clear': 0, 'Cloudy': 3, 'Rain': 8})
    traffic_effect = df['traffic'].map({'Low': 0, 'Medium': 5, 'High': 12})
    
    df['delivery_time'] = base_time + weather_effect + traffic_effect + np.random.normal(0, 3, n)
    df['delivery_time'] = df['delivery_time'].clip(10, 60)
    
    # 결측치 추가 (5%)
    for col in ['weather', 'traffic', 'order_hour']:
        mask = np.random.random(n) < 0.05
        df.loc[mask, col] = np.nan
    
    return df


def generate_sales_data(n=500):
    """Mock 02: 월별 매출 예측 데이터"""
    data = {
        'store_id': range(1, n+1),
        'month': np.random.randint(1, 13, n),
        'store_size': np.random.choice(['Small', 'Medium', 'Large'], n),
        'location': np.random.choice(['Urban', 'Suburban', 'Rural'], n),
        'employees': np.random.randint(5, 30, n),
        'marketing_budget': np.random.uniform(1000, 10000, n),
        'competitors': np.random.randint(0, 10, n),
    }
    df = pd.DataFrame(data)
    
    size_effect = df['store_size'].map({'Small': 50000, 'Medium': 100000, 'Large': 200000})
    location_effect = df['location'].map({'Urban': 50000, 'Suburban': 30000, 'Rural': 10000})
    
    df['monthly_sales'] = (size_effect + location_effect + 
                          df['employees'] * 5000 + 
                          df['marketing_budget'] * 5 -
                          df['competitors'] * 3000 +
                          np.random.normal(0, 20000, n))
    df['monthly_sales'] = df['monthly_sales'].clip(10000, 500000)
    
    # 결측치 추가
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'marketing_budget'] = np.nan
    
    return df


def generate_temperature_data(n=365):
    """Mock 03: 기온 예측 데이터"""
    days = pd.date_range('2024-01-01', periods=n)
    data = {
        'date': days,
        'day_of_year': days.dayofyear,
        'month': days.month,
        'humidity': np.random.uniform(30, 90, n),
        'wind_speed': np.random.uniform(0, 20, n),
        'cloud_cover': np.random.uniform(0, 100, n),
        'pressure': np.random.uniform(1000, 1030, n),
    }
    df = pd.DataFrame(data)
    
    # 계절성 반영한 기온
    seasonal = 15 * np.sin(2 * np.pi * (df['day_of_year'] - 80) / 365)
    df['temperature'] = 15 + seasonal - df['wind_speed'] * 0.2 + np.random.normal(0, 3, n)
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'humidity'] = np.nan
    
    return df


def generate_housing_data(n=800):
    """Mock 04: 주택 가격 예측 데이터"""
    data = {
        'house_id': range(1, n+1),
        'area': np.random.uniform(50, 200, n),
        'rooms': np.random.randint(1, 6, n),
        'bathrooms': np.random.randint(1, 4, n),
        'age': np.random.randint(0, 50, n),
        'floor': np.random.randint(1, 25, n),
        'has_parking': np.random.choice([0, 1], n),
        'has_elevator': np.random.choice([0, 1], n),
        'district': np.random.choice(['Gangnam', 'Seocho', 'Songpa', 'Mapo', 'Yongsan'], n),
    }
    df = pd.DataFrame(data)
    
    district_price = df['district'].map({
        'Gangnam': 50000, 'Seocho': 45000, 'Songpa': 40000, 
        'Mapo': 35000, 'Yongsan': 38000
    })
    
    df['price'] = (df['area'] * district_price + 
                  df['rooms'] * 10000000 +
                  df['bathrooms'] * 5000000 -
                  df['age'] * 1000000 +
                  df['has_parking'] * 20000000 +
                  df['has_elevator'] * 10000000 +
                  np.random.normal(0, 50000000, n))
    df['price'] = df['price'].clip(100000000, 2000000000)
    
    mask = np.random.random(n) < 0.04
    df.loc[mask, 'age'] = np.nan
    
    return df


def generate_traffic_data(n=1000):
    """Mock 05: 교통량 예측 데이터"""
    data = {
        'record_id': range(1, n+1),
        'hour': np.random.randint(0, 24, n),
        'day_of_week': np.random.randint(0, 7, n),
        'is_holiday': np.random.choice([0, 1], n, p=[0.9, 0.1]),
        'weather': np.random.choice(['Clear', 'Rain', 'Snow'], n, p=[0.7, 0.2, 0.1]),
        'road_type': np.random.choice(['Highway', 'Main', 'Local'], n),
        'lanes': np.random.randint(2, 6, n),
    }
    df = pd.DataFrame(data)
    
    # 시간대별 기본 교통량
    hour_effect = np.where((df['hour'] >= 7) & (df['hour'] <= 9), 300,
                  np.where((df['hour'] >= 17) & (df['hour'] <= 19), 350, 100))
    
    road_effect = df['road_type'].map({'Highway': 500, 'Main': 300, 'Local': 100})
    
    df['traffic_volume'] = (hour_effect + road_effect + 
                           df['lanes'] * 50 -
                           df['is_holiday'] * 100 +
                           np.random.normal(0, 50, n))
    df['traffic_volume'] = df['traffic_volume'].clip(50, 1000).astype(int)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'is_holiday'] = np.nan
    
    return df


def generate_churn_data(n=1000):
    """Mock 06: 고객 이탈 예측 데이터 (분류)"""
    data = {
        'customer_id': range(1, n+1),
        'tenure': np.random.randint(1, 72, n),
        'monthly_charges': np.random.uniform(20, 100, n),
        'total_charges': np.random.uniform(100, 5000, n),
        'contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n),
        'payment_method': np.random.choice(['Credit card', 'Bank transfer', 'Electronic check'], n),
        'tech_support': np.random.choice(['Yes', 'No'], n),
        'online_security': np.random.choice(['Yes', 'No'], n),
    }
    df = pd.DataFrame(data)
    
    # 이탈 확률 계산
    churn_prob = 0.3
    churn_prob -= df['tenure'] * 0.005
    churn_prob += (df['contract'] == 'Month-to-month') * 0.2
    churn_prob += (df['tech_support'] == 'No') * 0.1
    churn_prob = np.clip(churn_prob, 0.1, 0.8)
    
    df['churn'] = (np.random.random(n) < churn_prob).astype(int)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'tenure'] = np.nan
    
    return df


def generate_spam_data(n=800):
    """Mock 07: 스팸 분류 데이터"""
    data = {
        'email_id': range(1, n+1),
        'word_count': np.random.randint(10, 500, n),
        'link_count': np.random.randint(0, 20, n),
        'has_attachment': np.random.choice([0, 1], n),
        'capital_ratio': np.random.uniform(0, 0.5, n),
        'exclamation_count': np.random.randint(0, 10, n),
        'sender_domain': np.random.choice(['gmail', 'yahoo', 'unknown', 'company'], n),
        'time_sent': np.random.randint(0, 24, n),
    }
    df = pd.DataFrame(data)
    
    spam_prob = 0.2
    spam_prob += df['link_count'] * 0.03
    spam_prob += df['capital_ratio'] * 0.5
    spam_prob += df['exclamation_count'] * 0.05
    spam_prob += (df['sender_domain'] == 'unknown') * 0.3
    spam_prob = np.clip(spam_prob, 0.05, 0.95)
    
    df['is_spam'] = (np.random.random(n) < spam_prob).astype(int)
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'word_count'] = np.nan
    
    return df


def generate_loan_data(n=1000):
    """Mock 08: 대출 승인 예측 데이터"""
    data = {
        'applicant_id': range(1, n+1),
        'income': np.random.uniform(30000, 150000, n),
        'loan_amount': np.random.uniform(5000, 50000, n),
        'credit_score': np.random.randint(300, 850, n),
        'employment_years': np.random.randint(0, 30, n),
        'debt_ratio': np.random.uniform(0, 0.6, n),
        'has_mortgage': np.random.choice([0, 1], n),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n),
    }
    df = pd.DataFrame(data)
    
    approval_prob = 0.5
    approval_prob += (df['credit_score'] - 600) * 0.002
    approval_prob += df['employment_years'] * 0.02
    approval_prob -= df['debt_ratio'] * 0.5
    approval_prob = np.clip(approval_prob, 0.1, 0.9)
    
    df['approved'] = (np.random.random(n) < approval_prob).astype(int)
    
    mask = np.random.random(n) < 0.04
    df.loc[mask, 'credit_score'] = np.nan
    
    return df


def generate_disease_data(n=800):
    """Mock 09: 질병 예측 데이터"""
    data = {
        'patient_id': range(1, n+1),
        'age': np.random.randint(20, 80, n),
        'bmi': np.random.uniform(18, 40, n),
        'blood_pressure': np.random.randint(90, 180, n),
        'cholesterol': np.random.randint(150, 300, n),
        'glucose': np.random.randint(70, 200, n),
        'smoking': np.random.choice([0, 1], n),
        'exercise': np.random.choice(['None', 'Light', 'Moderate', 'Heavy'], n),
    }
    df = pd.DataFrame(data)
    
    disease_prob = 0.2
    disease_prob += (df['age'] - 40) * 0.005
    disease_prob += (df['bmi'] - 25) * 0.02
    disease_prob += (df['blood_pressure'] - 120) * 0.003
    disease_prob += df['smoking'] * 0.15
    disease_prob = np.clip(disease_prob, 0.05, 0.8)
    
    df['has_disease'] = (np.random.random(n) < disease_prob).astype(int)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'bmi'] = np.nan
    
    return df


def generate_satisfaction_data(n=1000):
    """Mock 10: 고객 만족도 분류 데이터"""
    data = {
        'customer_id': range(1, n+1),
        'wait_time': np.random.randint(1, 60, n),
        'service_quality': np.random.randint(1, 10, n),
        'product_quality': np.random.randint(1, 10, n),
        'price_fairness': np.random.randint(1, 10, n),
        'staff_friendliness': np.random.randint(1, 10, n),
        'visit_frequency': np.random.choice(['First', 'Occasional', 'Regular'], n),
        'age_group': np.random.choice(['18-25', '26-35', '36-50', '51+'], n),
    }
    df = pd.DataFrame(data)
    
    # 만족도 점수 계산
    score = (df['service_quality'] + df['product_quality'] + 
             df['price_fairness'] + df['staff_friendliness']) / 4
    score -= df['wait_time'] * 0.05
    
    df['satisfaction'] = pd.cut(score, bins=[0, 4, 6, 10], labels=['Low', 'Medium', 'High'])
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'wait_time'] = np.nan
    
    return df


# Level 2 데이터셋 생성 함수들
def generate_taxi_data(n=1000):
    """Mock 11: 택시 도착시간 예측"""
    data = {
        'trip_id': range(1, n+1),
        'pickup_lat': np.random.uniform(37.4, 37.6, n),
        'pickup_lng': np.random.uniform(126.8, 127.1, n),
        'dropoff_lat': np.random.uniform(37.4, 37.6, n),
        'dropoff_lng': np.random.uniform(126.8, 127.1, n),
        'pickup_hour': np.random.randint(0, 24, n),
        'pickup_day': np.random.randint(0, 7, n),
        'passenger_count': np.random.randint(1, 5, n),
        'weather': np.random.choice(['Clear', 'Rain', 'Snow'], n, p=[0.7, 0.2, 0.1]),
    }
    df = pd.DataFrame(data)
    
    distance = np.sqrt((df['dropoff_lat'] - df['pickup_lat'])**2 + 
                       (df['dropoff_lng'] - df['pickup_lng'])**2) * 100
    
    hour_effect = np.where((df['pickup_hour'] >= 7) & (df['pickup_hour'] <= 9), 10,
                  np.where((df['pickup_hour'] >= 17) & (df['pickup_hour'] <= 19), 12, 0))
    
    df['trip_duration'] = 5 + distance * 3 + hour_effect + np.random.normal(0, 5, n)
    df['trip_duration'] = df['trip_duration'].clip(5, 90)
    
    mask = np.random.random(n) < 0.04
    df.loc[mask, 'weather'] = np.nan
    
    return df


def generate_demand_data(n=500):
    """Mock 12: 상품 수요 예측"""
    data = {
        'product_id': range(1, n+1),
        'category': np.random.choice(['Electronics', 'Clothing', 'Food', 'Home'], n),
        'price': np.random.uniform(10, 500, n),
        'promotion': np.random.choice([0, 1], n),
        'season': np.random.choice(['Spring', 'Summer', 'Fall', 'Winter'], n),
        'competitor_price': np.random.uniform(10, 500, n),
        'ad_spend': np.random.uniform(0, 1000, n),
    }
    df = pd.DataFrame(data)
    
    base_demand = 100
    price_effect = -df['price'] * 0.2
    promo_effect = df['promotion'] * 50
    ad_effect = df['ad_spend'] * 0.1
    
    df['demand'] = base_demand + price_effect + promo_effect + ad_effect + np.random.normal(0, 20, n)
    df['demand'] = df['demand'].clip(10, 500).astype(int)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'ad_spend'] = np.nan
    
    return df


def generate_energy_data(n=1000):
    """Mock 13: 에너지 소비 예측"""
    data = {
        'building_id': range(1, n+1),
        'building_type': np.random.choice(['Residential', 'Commercial', 'Industrial'], n),
        'area': np.random.uniform(50, 500, n),
        'floors': np.random.randint(1, 20, n),
        'age': np.random.randint(1, 50, n),
        'occupancy': np.random.randint(1, 100, n),
        'has_solar': np.random.choice([0, 1], n),
        'temperature': np.random.uniform(-10, 35, n),
    }
    df = pd.DataFrame(data)
    
    type_effect = df['building_type'].map({'Residential': 100, 'Commercial': 300, 'Industrial': 500})
    
    df['energy_consumption'] = (type_effect + df['area'] * 0.5 + 
                                df['occupancy'] * 2 +
                                np.abs(df['temperature'] - 20) * 5 -
                                df['has_solar'] * 50 +
                                np.random.normal(0, 30, n))
    df['energy_consumption'] = df['energy_consumption'].clip(50, 1000)
    
    mask = np.random.random(n) < 0.04
    df.loc[mask, 'occupancy'] = np.nan
    
    return df


def generate_inventory_data(n=600):
    """Mock 14: 재고 수준 예측"""
    data = {
        'sku_id': range(1, n+1),
        'category': np.random.choice(['A', 'B', 'C', 'D'], n),
        'unit_price': np.random.uniform(5, 200, n),
        'lead_time': np.random.randint(1, 30, n),
        'supplier_reliability': np.random.uniform(0.7, 1.0, n),
        'monthly_sales': np.random.randint(10, 500, n),
        'seasonality': np.random.uniform(0.5, 1.5, n),
    }
    df = pd.DataFrame(data)
    
    df['optimal_stock'] = (df['monthly_sales'] * df['lead_time'] / 30 * 
                          df['seasonality'] / df['supplier_reliability'] +
                          np.random.normal(0, 10, n))
    df['optimal_stock'] = df['optimal_stock'].clip(10, 500).astype(int)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'lead_time'] = np.nan
    
    return df


def generate_waiting_data(n=800):
    """Mock 15: 대기시간 예측"""
    data = {
        'ticket_id': range(1, n+1),
        'service_type': np.random.choice(['Banking', 'Insurance', 'Consultation'], n),
        'arrival_hour': np.random.randint(9, 18, n),
        'day_of_week': np.random.randint(0, 5, n),
        'staff_count': np.random.randint(2, 10, n),
        'queue_length': np.random.randint(0, 20, n),
        'is_priority': np.random.choice([0, 1], n, p=[0.9, 0.1]),
    }
    df = pd.DataFrame(data)
    
    service_time = df['service_type'].map({'Banking': 5, 'Insurance': 15, 'Consultation': 20})
    
    df['wait_time'] = (df['queue_length'] * service_time / df['staff_count'] -
                      df['is_priority'] * 10 +
                      np.random.normal(0, 5, n))
    df['wait_time'] = df['wait_time'].clip(0, 60)
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'queue_length'] = np.nan
    
    return df


def generate_fraud_data(n=1000):
    """Mock 16: 금융 사기 탐지"""
    data = {
        'transaction_id': range(1, n+1),
        'amount': np.random.exponential(500, n),
        'hour': np.random.randint(0, 24, n),
        'day_of_week': np.random.randint(0, 7, n),
        'merchant_category': np.random.choice(['Retail', 'Online', 'ATM', 'Restaurant'], n),
        'location_distance': np.random.exponential(50, n),
        'transaction_count_1h': np.random.randint(1, 10, n),
    }
    df = pd.DataFrame(data)
    
    fraud_prob = 0.02
    fraud_prob += (df['amount'] > 1000) * 0.05
    fraud_prob += (df['hour'] < 6) * 0.03
    fraud_prob += (df['location_distance'] > 100) * 0.1
    fraud_prob += (df['transaction_count_1h'] > 5) * 0.08
    fraud_prob = np.clip(fraud_prob, 0.01, 0.5)
    
    df['is_fraud'] = (np.random.random(n) < fraud_prob).astype(int)
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'amount'] = np.nan
    
    return df


def generate_conversion_data(n=1000):
    """Mock 17: 구매 전환 예측"""
    data = {
        'visitor_id': range(1, n+1),
        'page_views': np.random.randint(1, 50, n),
        'time_on_site': np.random.uniform(10, 600, n),
        'bounce': np.random.choice([0, 1], n),
        'device': np.random.choice(['Desktop', 'Mobile', 'Tablet'], n),
        'traffic_source': np.random.choice(['Organic', 'Paid', 'Social', 'Direct'], n),
        'returning_visitor': np.random.choice([0, 1], n),
    }
    df = pd.DataFrame(data)
    
    conv_prob = 0.05
    conv_prob += df['page_views'] * 0.005
    conv_prob += df['time_on_site'] * 0.0002
    conv_prob -= df['bounce'] * 0.05
    conv_prob += df['returning_visitor'] * 0.05
    conv_prob = np.clip(conv_prob, 0.01, 0.5)
    
    df['converted'] = (np.random.random(n) < conv_prob).astype(int)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'time_on_site'] = np.nan
    
    return df


def generate_sentiment_data(n=800):
    """Mock 18: 리뷰 감성 분류"""
    data = {
        'review_id': range(1, n+1),
        'word_count': np.random.randint(10, 200, n),
        'positive_words': np.random.randint(0, 20, n),
        'negative_words': np.random.randint(0, 20, n),
        'exclamation_marks': np.random.randint(0, 5, n),
        'question_marks': np.random.randint(0, 3, n),
        'capital_ratio': np.random.uniform(0, 0.3, n),
        'rating': np.random.randint(1, 6, n),
    }
    df = pd.DataFrame(data)
    
    sentiment_score = df['positive_words'] - df['negative_words'] + (df['rating'] - 3) * 3
    df['sentiment'] = pd.cut(sentiment_score, bins=[-100, -2, 2, 100], labels=['Negative', 'Neutral', 'Positive'])
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'rating'] = np.nan
    
    return df


def generate_credit_data(n=1000):
    """Mock 19: 신용 위험 등급"""
    data = {
        'customer_id': range(1, n+1),
        'age': np.random.randint(20, 70, n),
        'income': np.random.uniform(20000, 200000, n),
        'employment_length': np.random.randint(0, 40, n),
        'num_credit_lines': np.random.randint(1, 15, n),
        'credit_utilization': np.random.uniform(0, 1, n),
        'num_late_payments': np.random.randint(0, 10, n),
        'home_ownership': np.random.choice(['Own', 'Rent', 'Mortgage'], n),
    }
    df = pd.DataFrame(data)
    
    risk_score = 50
    risk_score += df['employment_length'] * 0.5
    risk_score += df['income'] / 5000
    risk_score -= df['credit_utilization'] * 30
    risk_score -= df['num_late_payments'] * 10
    
    df['risk_grade'] = pd.cut(risk_score, bins=[0, 30, 50, 70, 100], labels=['D', 'C', 'B', 'A'])
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'income'] = np.nan
    
    return df


def generate_click_data(n=1000):
    """Mock 20: 광고 클릭 예측"""
    data = {
        'impression_id': range(1, n+1),
        'ad_position': np.random.randint(1, 5, n),
        'ad_size': np.random.choice(['Small', 'Medium', 'Large'], n),
        'page_type': np.random.choice(['Home', 'Article', 'Search', 'Product'], n),
        'time_of_day': np.random.choice(['Morning', 'Afternoon', 'Evening', 'Night'], n),
        'device': np.random.choice(['Desktop', 'Mobile', 'Tablet'], n),
        'user_age_group': np.random.choice(['18-24', '25-34', '35-44', '45-54', '55+'], n),
    }
    df = pd.DataFrame(data)
    
    click_prob = 0.02
    click_prob += (df['ad_position'] == 1) * 0.03
    click_prob += (df['ad_size'] == 'Large') * 0.02
    click_prob += (df['page_type'] == 'Search') * 0.02
    click_prob = np.clip(click_prob, 0.005, 0.15)
    
    df['clicked'] = (np.random.random(n) < click_prob).astype(int)
    
    mask = np.random.random(n) < 0.02
    df.loc[mask, 'ad_position'] = np.nan
    
    return df


# Level 3 데이터셋 생성 함수들
def generate_navigation_data(n=1200):
    """Mock 21: 내비게이션 도착시간 (실제 기출 유형)"""
    data = {
        'route_id': range(1, n+1),
        'origin_lat': np.random.uniform(37.4, 37.65, n),
        'origin_lng': np.random.uniform(126.8, 127.15, n),
        'dest_lat': np.random.uniform(37.4, 37.65, n),
        'dest_lng': np.random.uniform(126.8, 127.15, n),
        'departure_hour': np.random.randint(0, 24, n),
        'departure_day': np.random.randint(0, 7, n),
        'vehicle_type': np.random.choice(['Car', 'Truck', 'Motorcycle'], n, p=[0.7, 0.2, 0.1]),
        'weather': np.random.choice(['Clear', 'Cloudy', 'Rain', 'Snow'], n, p=[0.5, 0.25, 0.15, 0.1]),
        'traffic_level': np.random.randint(1, 6, n),
        'road_type': np.random.choice(['Highway', 'City', 'Mixed'], n),
        'has_toll': np.random.choice([0, 1], n),
    }
    df = pd.DataFrame(data)
    
    distance = np.sqrt((df['dest_lat'] - df['origin_lat'])**2 + 
                       (df['dest_lng'] - df['origin_lng'])**2) * 111  # km 변환
    
    speed = 60 - df['traffic_level'] * 8
    speed = np.where(df['road_type'] == 'Highway', speed + 20, speed)
    speed = np.where(df['weather'].isin(['Rain', 'Snow']), speed * 0.8, speed)
    
    df['arrival_time'] = distance / speed * 60 + np.random.normal(0, 5, n)
    df['arrival_time'] = df['arrival_time'].clip(5, 120)
    
    # 여러 컬럼에 결측치
    for col in ['weather', 'traffic_level', 'has_toll']:
        mask = np.random.random(n) < 0.03
        df.loc[mask, col] = np.nan
    
    return df


def generate_telecom_data(n=1000):
    """Mock 22: 통신사 고객 해지 (실제 기출 유형)"""
    data = {
        'customer_id': range(1, n+1),
        'gender': np.random.choice(['Male', 'Female'], n),
        'senior_citizen': np.random.choice([0, 1], n, p=[0.85, 0.15]),
        'partner': np.random.choice(['Yes', 'No'], n),
        'dependents': np.random.choice(['Yes', 'No'], n),
        'tenure': np.random.randint(1, 72, n),
        'phone_service': np.random.choice(['Yes', 'No'], n, p=[0.9, 0.1]),
        'internet_service': np.random.choice(['DSL', 'Fiber', 'No'], n),
        'online_security': np.random.choice(['Yes', 'No', 'No internet'], n),
        'tech_support': np.random.choice(['Yes', 'No', 'No internet'], n),
        'contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n),
        'payment_method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n),
        'monthly_charges': np.random.uniform(20, 110, n),
        'total_charges': np.random.uniform(100, 8000, n),
    }
    df = pd.DataFrame(data)
    
    churn_prob = 0.25
    churn_prob -= df['tenure'] * 0.004
    churn_prob += (df['contract'] == 'Month-to-month') * 0.2
    churn_prob += (df['internet_service'] == 'Fiber') * 0.1
    churn_prob += (df['tech_support'] == 'No') * 0.08
    churn_prob += (df['payment_method'] == 'Electronic check') * 0.1
    churn_prob = np.clip(churn_prob, 0.05, 0.7)
    
    df['churn'] = (np.random.random(n) < churn_prob).astype(int)
    
    for col in ['tenure', 'monthly_charges', 'online_security']:
        mask = np.random.random(n) < 0.03
        df.loc[mask, col] = np.nan
    
    return df


def generate_usedcar_data(n=800):
    """Mock 23: 중고차 가격 예측"""
    data = {
        'car_id': range(1, n+1),
        'brand': np.random.choice(['Hyundai', 'Kia', 'BMW', 'Mercedes', 'Toyota'], n),
        'model_year': np.random.randint(2010, 2024, n),
        'mileage': np.random.uniform(5000, 200000, n),
        'fuel_type': np.random.choice(['Gasoline', 'Diesel', 'Hybrid', 'Electric'], n),
        'transmission': np.random.choice(['Manual', 'Automatic'], n, p=[0.2, 0.8]),
        'engine_size': np.random.uniform(1.0, 4.0, n),
        'color': np.random.choice(['White', 'Black', 'Silver', 'Blue', 'Red'], n),
        'accident_history': np.random.choice([0, 1, 2, 3], n, p=[0.6, 0.25, 0.1, 0.05]),
    }
    df = pd.DataFrame(data)
    
    brand_value = df['brand'].map({
        'Hyundai': 15000, 'Kia': 14000, 'BMW': 35000, 
        'Mercedes': 40000, 'Toyota': 20000
    })
    
    age = 2024 - df['model_year']
    df['price'] = (brand_value - age * 1500 - df['mileage'] * 0.03 - 
                  df['accident_history'] * 2000 +
                  df['engine_size'] * 3000 +
                  np.random.normal(0, 3000, n))
    df['price'] = df['price'].clip(3000, 80000)
    
    for col in ['mileage', 'accident_history']:
        mask = np.random.random(n) < 0.04
        df.loc[mask, col] = np.nan
    
    return df


def generate_quality_data(n=600):
    """Mock 24: 제품 품질 예측"""
    data = {
        'batch_id': range(1, n+1),
        'temperature': np.random.uniform(150, 250, n),
        'pressure': np.random.uniform(1, 10, n),
        'humidity': np.random.uniform(30, 70, n),
        'processing_time': np.random.uniform(30, 120, n),
        'material_grade': np.random.choice(['A', 'B', 'C'], n),
        'operator_experience': np.random.randint(1, 20, n),
        'machine_age': np.random.randint(1, 15, n),
    }
    df = pd.DataFrame(data)
    
    grade_effect = df['material_grade'].map({'A': 10, 'B': 5, 'C': 0})
    
    df['quality_score'] = (50 + grade_effect + 
                          df['operator_experience'] * 0.5 -
                          df['machine_age'] * 0.3 -
                          np.abs(df['temperature'] - 200) * 0.1 +
                          np.random.normal(0, 5, n))
    df['quality_score'] = df['quality_score'].clip(30, 100)
    
    mask = np.random.random(n) < 0.03
    df.loc[mask, 'temperature'] = np.nan
    
    return df


def generate_subscription_data(n=1000):
    """Mock 25: 구독 서비스 유지 예측"""
    data = {
        'user_id': range(1, n+1),
        'subscription_type': np.random.choice(['Basic', 'Standard', 'Premium'], n),
        'tenure_months': np.random.randint(1, 48, n),
        'monthly_usage': np.random.uniform(0, 100, n),
        'support_tickets': np.random.randint(0, 10, n),
        'payment_delay_count': np.random.randint(0, 5, n),
        'age': np.random.randint(18, 65, n),
        'family_plan': np.random.choice([0, 1], n),
    }
    df = pd.DataFrame(data)
    
    retain_prob = 0.7
    retain_prob += df['tenure_months'] * 0.005
    retain_prob += df['monthly_usage'] * 0.003
    retain_prob -= df['support_tickets'] * 0.05
    retain_prob -= df['payment_delay_count'] * 0.1
    retain_prob += df['family_plan'] * 0.1
    retain_prob = np.clip(retain_prob, 0.2, 0.95)
    
    df['retained'] = (np.random.random(n) < retain_prob).astype(int)
    
    for col in ['monthly_usage', 'payment_delay_count']:
        mask = np.random.random(n) < 0.03
        df.loc[mask, col] = np.nan
    
    return df


def generate_logistics_data(n=1000):
    """Mock 26: 물류 배송시간 예측"""
    data = {
        'shipment_id': range(1, n+1),
        'origin_city': np.random.choice(['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon'], n),
        'dest_city': np.random.choice(['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon'], n),
        'weight': np.random.uniform(0.5, 50, n),
        'volume': np.random.uniform(0.01, 1, n),
        'shipping_type': np.random.choice(['Standard', 'Express', 'Same-day'], n),
        'is_fragile': np.random.choice([0, 1], n),
        'order_hour': np.random.randint(0, 24, n),
        'is_weekend': np.random.choice([0, 1], n, p=[0.7, 0.3]),
    }
    df = pd.DataFrame(data)
    
    # 도시 간 거리 (간단화)
    city_distances = {
        ('Seoul', 'Busan'): 400, ('Seoul', 'Incheon'): 30, ('Seoul', 'Daegu'): 300,
        ('Seoul', 'Daejeon'): 150, ('Busan', 'Incheon'): 430, ('Busan', 'Daegu'): 100,
        ('Busan', 'Daejeon'): 250, ('Incheon', 'Daegu'): 330, ('Incheon', 'Daejeon'): 180,
        ('Daegu', 'Daejeon'): 150
    }
    
    def get_distance(row):
        pair = tuple(sorted([row['origin_city'], row['dest_city']]))
        return city_distances.get(pair, 200)
    
    df['distance'] = df.apply(get_distance, axis=1)
    
    type_speed = df['shipping_type'].map({'Standard': 1, 'Express': 1.5, 'Same-day': 3})
    
    df['delivery_hours'] = df['distance'] / (50 * type_speed) + np.random.normal(0, 2, n)
    df['delivery_hours'] = df['delivery_hours'].clip(1, 48)
    
    for col in ['weight', 'is_fragile']:
        mask = np.random.random(n) < 0.03
        df.loc[mask, col] = np.nan
    
    return df


def generate_marketing_data(n=1000):
    """Mock 27: 마케팅 캠페인 반응 예측"""
    data = {
        'customer_id': range(1, n+1),
        'age': np.random.randint(18, 70, n),
        'income_bracket': np.random.choice(['Low', 'Medium', 'High'], n),
        'past_purchases': np.random.randint(0, 50, n),
        'email_opens': np.random.randint(0, 20, n),
        'website_visits': np.random.randint(0, 30, n),
        'days_since_last_purchase': np.random.randint(1, 365, n),
        'campaign_type': np.random.choice(['Email', 'SMS', 'Push', 'Call'], n),
        'offer_type': np.random.choice(['Discount', 'Free shipping', 'Loyalty points'], n),
    }
    df = pd.DataFrame(data)
    
    response_prob = 0.1
    response_prob += df['email_opens'] * 0.01
    response_prob += df['website_visits'] * 0.005
    response_prob += df['past_purchases'] * 0.005
    response_prob -= df['days_since_last_purchase'] * 0.0005
    response_prob = np.clip(response_prob, 0.02, 0.5)
    
    df['responded'] = (np.random.random(n) < response_prob).astype(int)
    
    for col in ['email_opens', 'days_since_last_purchase']:
        mask = np.random.random(n) < 0.03
        df.loc[mask, col] = np.nan
    
    return df


def generate_production_data(n=500):
    """Mock 28: 공장 생산량 예측"""
    data = {
        'shift_id': range(1, n+1),
        'machine_id': np.random.randint(1, 11, n),
        'operator_id': np.random.randint(1, 21, n),
        'shift_type': np.random.choice(['Morning', 'Afternoon', 'Night'], n),
        'raw_material_quality': np.random.uniform(0.8, 1.0, n),
        'machine_efficiency': np.random.uniform(0.7, 1.0, n),
        'maintenance_done': np.random.choice([0, 1], n),
        'temperature': np.random.uniform(18, 28, n),
        'humidity': np.random.uniform(40, 60, n),
    }
    df = pd.DataFrame(data)
    
    shift_effect = df['shift_type'].map({'Morning': 100, 'Afternoon': 95, 'Night': 85})
    
    df['production_units'] = (shift_effect * df['raw_material_quality'] * 
                             df['machine_efficiency'] * 
                             (1 + df['maintenance_done'] * 0.1) +
                             np.random.normal(0, 5, n))
    df['production_units'] = df['production_units'].clip(50, 150).astype(int)
    
    for col in ['raw_material_quality', 'machine_efficiency']:
        mask = np.random.random(n) < 0.04
        df.loc[mask, col] = np.nan
    
    return df


def generate_final_regression_data(n=1000):
    """Mock 29: 최종 모의고사 (회귀) - 종합 문제"""
    data = {
        'id': range(1, n+1),
        'feature_1': np.random.uniform(0, 100, n),
        'feature_2': np.random.uniform(0, 50, n),
        'feature_3': np.random.randint(1, 10, n),
        'category_1': np.random.choice(['A', 'B', 'C', 'D'], n),
        'category_2': np.random.choice(['X', 'Y', 'Z'], n),
        'date_feature': pd.date_range('2024-01-01', periods=n, freq='H').strftime('%Y-%m-%d %H:%M'),
        'binary_feature': np.random.choice([0, 1], n),
        'ordinal_feature': np.random.choice(['Low', 'Medium', 'High'], n),
    }
    df = pd.DataFrame(data)
    
    cat1_effect = df['category_1'].map({'A': 10, 'B': 20, 'C': 30, 'D': 40})
    ord_effect = df['ordinal_feature'].map({'Low': 0, 'Medium': 15, 'High': 30})
    
    df['target'] = (df['feature_1'] * 0.5 + df['feature_2'] * 0.8 + 
                   df['feature_3'] * 3 + cat1_effect + ord_effect +
                   df['binary_feature'] * 10 +
                   np.random.normal(0, 10, n))
    df['target'] = df['target'].clip(0, 200)
    
    for col in ['feature_1', 'feature_2', 'category_1']:
        mask = np.random.random(n) < 0.04
        df.loc[mask, col] = np.nan
    
    return df


def generate_final_classification_data(n=1000):
    """Mock 30: 최종 모의고사 (분류) - 종합 문제"""
    data = {
        'id': range(1, n+1),
        'numeric_1': np.random.uniform(0, 100, n),
        'numeric_2': np.random.uniform(0, 50, n),
        'numeric_3': np.random.randint(1, 100, n),
        'category_a': np.random.choice(['Type1', 'Type2', 'Type3'], n),
        'category_b': np.random.choice(['GroupA', 'GroupB', 'GroupC', 'GroupD'], n),
        'binary_1': np.random.choice([0, 1], n),
        'binary_2': np.random.choice([0, 1], n),
        'ordinal': np.random.choice(['Small', 'Medium', 'Large'], n),
    }
    df = pd.DataFrame(data)
    
    score = df['numeric_1'] * 0.3 + df['numeric_2'] * 0.5
    score += (df['category_a'] == 'Type1') * 20
    score += df['binary_1'] * 15
    score += df['ordinal'].map({'Small': 0, 'Medium': 10, 'Large': 20})
    score += np.random.normal(0, 15, n)
    
    df['target'] = pd.cut(score, bins=[0, 40, 60, 100], labels=['Class_C', 'Class_B', 'Class_A'])
    
    for col in ['numeric_1', 'category_a', 'binary_1']:
        mask = np.random.random(n) < 0.04
        df.loc[mask, col] = np.nan
    
    return df


# 모든 데이터셋 생성 및 저장
def generate_all_datasets():
    """모든 데이터셋 생성"""
    
    datasets = {
        # Level 1 - Basic
        'mock_01_delivery.csv': generate_delivery_data,
        'mock_02_sales.csv': generate_sales_data,
        'mock_03_temperature.csv': generate_temperature_data,
        'mock_04_housing.csv': generate_housing_data,
        'mock_05_traffic.csv': generate_traffic_data,
        'mock_06_churn.csv': generate_churn_data,
        'mock_07_spam.csv': generate_spam_data,
        'mock_08_loan.csv': generate_loan_data,
        'mock_09_disease.csv': generate_disease_data,
        'mock_10_satisfaction.csv': generate_satisfaction_data,
        
        # Level 2 - Intermediate
        'mock_11_taxi.csv': generate_taxi_data,
        'mock_12_demand.csv': generate_demand_data,
        'mock_13_energy.csv': generate_energy_data,
        'mock_14_inventory.csv': generate_inventory_data,
        'mock_15_waiting.csv': generate_waiting_data,
        'mock_16_fraud.csv': generate_fraud_data,
        'mock_17_conversion.csv': generate_conversion_data,
        'mock_18_sentiment.csv': generate_sentiment_data,
        'mock_19_credit.csv': generate_credit_data,
        'mock_20_click.csv': generate_click_data,
        
        # Level 3 - Advanced
        'mock_21_navigation.csv': generate_navigation_data,
        'mock_22_telecom.csv': generate_telecom_data,
        'mock_23_usedcar.csv': generate_usedcar_data,
        'mock_24_quality.csv': generate_quality_data,
        'mock_25_subscription.csv': generate_subscription_data,
        'mock_26_logistics.csv': generate_logistics_data,
        'mock_27_marketing.csv': generate_marketing_data,
        'mock_28_production.csv': generate_production_data,
        'mock_29_final_reg.csv': generate_final_regression_data,
        'mock_30_final_clf.csv': generate_final_classification_data,
    }
    
    print("=" * 60)
    print("AICE Associate Mock Exam Dataset Generation")
    print("=" * 60)
    
    for filename, generator in datasets.items():
        filepath = os.path.join(DATA_DIR, filename)
        df = generator()
        df.to_csv(filepath, index=False)
        print(f"[OK] {filename} created (shape: {df.shape})")
    
    print("=" * 60)
    print(f"Total {len(datasets)} datasets created!")
    print("=" * 60)


if __name__ == "__main__":
    generate_all_datasets()
