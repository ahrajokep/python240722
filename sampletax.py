import pandas as pd
import numpy as np

df = pd.read_excel('납부대상확인.xlsx')
# df.head(2)

cond1 = df['세입구분'] == '지방세'
# 세입구분:지방세 선택
df = df[cond1]
# df.head(2)

#자치단체 문자열 자르기
df[['주소1(도)', '주소2(시)', '주소3(구)']] = df['자치단체'].str.split(expand=True)
# df.head(2)

#세금조건 3가지

tax_type = ['재산세(건축물)','재산세(주택)','재산세(토지)']

city_name = [
    '경기도 과천시',
    '경기도 광명시',
    '경기도 광주시',
    '경기도 군포시',
    '경기도 성남시 분당구',
    '경기도 성남시 수정구',
    '경기도 성남시 중원구',
    '경기도 수원시 권선구',
    '경기도 수원시 영통구',
    '경기도 수원시 장안구',
    '경기도 수원시 팔달구',
    '경기도 안산시 단원구',
    '경기도 안산시 상록구',
    '경기도 안성시',
    '경기도 안양시 동안구',
    '경기도 안양시 만안구',
    '경기도 여주시',
    '경기도 오산시',
    '경기도 용인시 기흥구',
    '경기도 용인시 수지구',
    '경기도 용인시 처인구',
    '경기도 의왕시',
    '경기도 이천시',
    '경기도 평택시',
    '경기도 평택시 송탄출장소',
    '경기도 평택시 안중출장소',
    '경기도 하남시',
    '경기도 화성시',
    '경기도 화성시 동부출장소',
    '경기도 화성시 동탄출장소']

# print(city_name[9])

complete=0
for i in range(3):
    tax_cond = df['세목']==tax_type[i]
    for j in range(30):
      city_cond = df['자치단체']==city_name[j]
      temp = df[tax_cond&city_cond]
      complete=complete+len(temp)
      count_temp = str(len(temp))
      temp_filepath= tax_type[i] +"_"+ city_name[j] +"_"+ count_temp + "건.xlsx"
      temp.to_excel(temp_filepath, index=False)

print("완료:"+str(complete)+"건")

# tax_cond = df['세목']==tax_type[0]
# city_cond = df['자치단체']==city_name[9]
# temp = df[tax_cond&city_cond]
# temp

