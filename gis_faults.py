import pandas as pd
from decimal import Decimal, getcontext


#센서간 거리 Dict 2가지
distances_6100 = {
    ('Sensor1', 'Sensor2'): 200,
    ('Sensor1', 'Sensor3'): 400,
    ('Sensor1', 'Sensor4'): 420,
    ('Sensor2', 'Sensor3'): 200,
    ('Sensor2', 'Sensor4'): 620,
    ('Sensor3', 'Sensor4'): 820
}

# Distance data for 'T/L'
distances_TL = {
    ('Sensor1', 'Sensor2'): 300,
    ('Sensor1', 'Sensor3'): 180,
    ('Sensor1', 'Sensor4'): 280,
    ('Sensor1', 'Sensor5'): 320,
    ('Sensor1', 'Sensor6'): 360,
    ('Sensor1', 'Sensor7'): 470,
    ('Sensor2', 'Sensor3'): 480,
    ('Sensor2', 'Sensor4'): 580,
    ('Sensor2', 'Sensor5'): 620,
    ('Sensor2', 'Sensor6'): 660,
    ('Sensor2', 'Sensor7'): 770,
    ('Sensor3', 'Sensor4'): 100,
    ('Sensor3', 'Sensor5'): 140,
    ('Sensor3', 'Sensor6'): 180,
    ('Sensor3', 'Sensor7'): 290,
    ('Sensor4', 'Sensor5'): 40,
    ('Sensor4', 'Sensor6'): 115,
    ('Sensor4', 'Sensor7'): 155,
    ('Sensor5', 'Sensor6'): 155,
    ('Sensor5', 'Sensor7'): 115,
    ('Sensor6', 'Sensor7'): 270
}

print("Distances for '6100':")
print(distances_6100)

print("\nDistances for 'T/L':")
print(distances_TL)

#소숫점 9자리 사용(float 타입인 경우 소숫점 6자리 초과분을 잃어버림)
getcontext().prec = 10


# 1. pandas로 csv 파일 두 개를 각각 읽어 dataframe a,b를 만든다.
df_a = pd.read_csv("5-1.A.csv")
df_b = pd.read_csv("5-3.B.csv")

# 1. 결과 출력
# print("csv 파일을 dataframe으로 읽기")
# print(df_a)
# print(df_b)

# 2. 각 파일의 첫번째 column의 지수 값을 십진수 숫자로 표현 하도록 변환한다.
# Note: 절대값 우선 취하지 않았음
def convert_exponential_to_decimal(value):
    try:
        return '{:.10f}'.format(float(value))
    except ValueError:
        print("Time값이 잘못된 행이 있습니다.", value)
        return value


for idx, row in enumerate(df_a.itertuples(), start=1):
    if idx >= 5:  # csv 파일의 5번째 열부터 숫자가 시작됨
        df_a.iloc[idx - 1, 0] = convert_exponential_to_decimal(df_a.iloc[idx - 1, 0])

for idx, row in enumerate(df_b.itertuples(), start=1):
    if idx >= 5:
        df_b.iloc[idx - 1, 0] = convert_exponential_to_decimal(df_b.iloc[idx - 1, 0])

# 2. 결과 출력
# print("2. 지수에서 숫자 변환 후")
# print(df_a)
# print(df_b)


# 3. 각각 데이터 프레임의 Trigger 값을 구한다.(최대값 10개 평균의 20%)
# 3-1. 필요한 2번째열[Ampl1]의 5번째 row부터 숫자만 저장하는 df를 정제해서 생성
df_a.iloc[4:, 1] = pd.to_numeric(df_a.iloc[4:, 1], errors='coerce')
df_b.iloc[4:, 1] = pd.to_numeric(df_b.iloc[4:, 1], errors='coerce')

# 변수 너무 길어서 refined 로 하나 만들어줬어용
df_a_refined = df_a.iloc[4:, 1].apply(lambda x: f"{x:.10f}" if pd.notna(x) else x)
df_b_refined = df_b.iloc[4:, 1].apply(lambda x: f"{x:.10f}" if pd.notna(x) else x)

df_a_refined = df_a_refined.apply(Decimal) #소숫점 살리기(float 하면 3자리 잃어버림)
df_b_refined = df_b_refined.apply(Decimal)

print("정제된 df")
print(df_a_refined)
print(df_b_refined)
# 3-2. 가장 큰 10개의 파형 값의 평균 * 0.2
print("3. 가장 큰 10개 파형 값")
sorted_df_a = df_a_refined.sort_values(ascending=False)
sorted_df_b = df_b_refined.sort_values(ascending=False)

ten_largest_decimal_a = (sorted_df_a.head(10))
ten_largest_decimal_b = (sorted_df_a.head(10))

print(ten_largest_decimal_a, ten_largest_decimal_b)

print("3.파형 값들의 평균")
mean_value_a = sum(ten_largest_decimal_a)/Decimal(len(ten_largest_decimal_a))
mean_value_b = sum(ten_largest_decimal_b)/Decimal(len(ten_largest_decimal_b))

print(mean_value_a, mean_value_b)

trigger_a = mean_value_a * Decimal('0.2')
trigger_b = mean_value_b * Decimal('0.2')
print("trigger_a:", trigger_a, "trigger_b:", trigger_b)

# 4. Peak 계산
# [Note] 파형의 값이 트리거를 넘어선 첫번째 피크점을 찾는다.
for i in range(len(df_a_refined) - 1):
    if df_a_refined.iloc[i] > trigger_a:
        if df_a_refined.iloc[i] > df_a_refined.iloc[i + 1]:
            peak_a_time = df_a.iloc[i + 4, 0]
            peak_a_value = df_a_refined.iloc[i]
            break
        else:
            continue

print("a peak time :", peak_a_time, "a peak value:", peak_a_value)

for i in range(len(df_b_refined) - 1):
    if df_b_refined.iloc[i] > trigger_b:
        if df_b_refined.iloc[i] > df_b_refined.iloc[i + 1]:
            peak_b_time = df_b.iloc[i + 4, 0]
            peak_b_value = df_b_refined.iloc[i]
            break
        else:
            continue

print("b peak time :", peak_b_time, "b peak value:", peak_b_value)

# 5. 거리값 차이 계산
D = 200 #사용자에게 UI로 선택하게끔
distance = (D/100 - 300000000 * (float(peak_b_time) - float(peak_a_time))) / 2 * 100
print("D", D)
print("거리값 계산:", distance)
