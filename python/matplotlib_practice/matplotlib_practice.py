# Matplotlib 실습
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("202412_202412_연령별인구현황_월간.csv", encoding= "EUC-KR")
print(df.head())
print(df.info())

age_columns = [col for col in df.columns if "세" in col]
print(df[age_columns].dtypes)

'''
# 숫자로 변환
for col in age_columns:
    if df[col].dtype == "object":
        df[col] = df[col].str.replace(",","").astype(int)

# 숫자로 변환하는 다른 방법
male_result = (
    region_data[male_columns].iloc[0].astype(str).replace(",","").astype(int)
)

male_result = region_data[female_columns].iloc[0].apply(lambda x : int(str(x)).replace(",",""))
'''

man_df = df.drop(columns=[col for col in df.columns if "여" in col])
woman_df = df.drop(columns=[col for col in df.columns if "남" in col])

print(man_df.head())

# 데이터 필터링
region_name = input("검색하고 싶은 지역명을 입력하세요: ")

man_region_data = man_df[man_df["행정구역"].str.contains(region_name, na=False)]
woman_region_data = woman_df[woman_df["행정구역"].str.contains(region_name, na=False)]

if man_region_data.empty and woman_region_data.empty:
    print(f"{region_name}의 지역은 존재하지 않습니다.")

man_age_columns = [col for col in age_columns if "남" in col]
woman_age_columns = [col for col in age_columns if "여" in col]

man_result = man_region_data[man_age_columns].iloc[0].values
woman_result = woman_region_data[woman_age_columns].iloc[0].values

# 남성 연령 그룹 추출
man_age_groups = [
    col.split("_남_")[1].replace("세", "").replace("이상", "over") for col in man_age_columns
]

# 여성 연령 그룹 추출
woman_age_groups = [
    col.split("_여_")[1].replace("세", "").replace("이상", "over") for col in woman_age_columns
]

# 그래프 그리기
plt.figure(figsize = (10,8))
plt.plot(man_age_groups, man_result, marker = "o", label="Man", color = "blue")
plt.plot(woman_age_groups, woman_result, marker = "o", label="Woman", color = "red")
plt.title(f"Population by Age Group", fontsize = 16, pad=10)
plt.xlabel("Age")
plt.ylabel("Population")
plt.grid(True, linestyle = "--",alpha=0.6)
plt.xticks(rotation=45)
plt.legend()
plt.show()

# 한글 폰트 적용 시 fontproperty = font 의 option을 추가해야 함