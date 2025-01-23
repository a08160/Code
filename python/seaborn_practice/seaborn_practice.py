# 실습1. Penguins 데이터셋 분석
# reset_index(): 인덱스를 초기화, 기존 인덱스를 데이터 프레임의 열로 변환환

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

penguin_df = sns.load_dataset("penguins")
pd.set_option('display.max_columns', None)

print(penguin_df.head())
print(penguin_df.info())

# Q1. 펭귄의 종(species)별 평균 몸무게(body_mass_g)를 막대 그래프로 나타내세요.
species_body_mass = penguin_df.groupby("species")["body_mass_g"].mean().round(2).reset_index()

bars = plt.bar(species_body_mass["species"], species_body_mass["body_mass_g"], color=["r", "g", "b"])

plt.title("Average Mass by Penguin Species")

# 바그래프별 텍스트 넣기
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,  # x좌표(막대의 중심)
        bar.get_height() + 230,  # y좌표
        str(bar.get_height())+"g",
        ha="center",
        va="top",
        color="black"
    )

plt.show()

# Q2. 부리 길이(bill_length_mm)와 부리 깊이(bill_depth_mm)의 관계를 산점도로 시각화
sns.scatterplot(penguin_df,x="bill_length_mm",y="bill_depth_mm", hue="species")
plt.title("Relation between Length and Depth of Bill")
plt.show()

# Q3. 펭귄의 섬(island)에 따라 몸무게의 분포를 violinplot으로 시각화하세요
sns.catplot(penguin_df, x= "island", y="body_mass_g",kind="violin",hue="island")
plt.title("Penguin Body Mass by Island")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# flights 데이터셋 로드
flight_df = sns.load_dataset("flights")
print(flight_df.head())
print(flight_df.info())

# Q1. 연도(year)별 승객 수(passengers)의 평균을 꺾은선 그래프로 나타내기
ye_pa_df = flight_df.groupby("year")["passengers"].mean().round(2)

# 꺾은선 그래프 그리기
plt.plot(ye_pa_df, marker='o', color='b')  # 'o'로 마커를 추가

# 그래프 제목 설정
plt.title("Average Passengers by Year")

# x축, y축 레이블 추가
plt.xlabel("Year")
plt.ylabel("Average Passengers")

plot = plt.plot(ye_pa_df, marker='o', color='b')  # 'o'로 마커를 추가

# 그래프 표시
plt.show()

# Q2.연도와 월별(month) 승객 수를 히트맵으로 시각화하세요.

mo_ye_pa = flight_df.groupby(["month","year"])["passengers"].sum().unstack()

sns.heatmap(mo_ye_pa, annot = False, linewidths = 2, cmap = "Blues")
plt.title("The Number of Passenger by Year and Month")
plt.show()

# Q3.특정 연도(예: 1958년)의 월별 승객 수를 막대 그래프로 나타내세요.

def year_passenger(year):
    global flight_df
    # 특정 연도에 대한 데이터 필터링 및 월별 승객 수 합계
    new_df = flight_df[flight_df["year"] == year].groupby("month")["passengers"].sum()

    # 색상 팔레트 생성 (순차적으로 색상이 바뀌도록)
    colors = sns.color_palette("Blues", n_colors=len(new_df))

    # 막대 그래프 그리기
    plt.figure(figsize=(10, 6))
    bars = plt.bar(new_df.index, new_df.values, color=colors)
    
    # 그래프 제목 및 레이블 설정
    plt.title(f"Monthly Passengers in {year}")
    plt.xlabel("Month")
    plt.ylabel("Total Passengers")

    # 그래프 표시
    plt.show()

# 예시: 1949년 데이터로 그래프 그리기
year_passenger(1949)


# 실습3. Titanic 데이터셋

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

pd.set_option('display.max_columns', None)

titanic_df = sns.load_dataset("titanic")
print(titanic_df.head())
print(titanic_df.info())

# Q1. 탑승 클래스(class)와 생존 여부(survived) 간의 관계를 catplot으로 시각화
plt.figure(figsize=(10, 6))
sns.catplot(data=titanic_df, x="class", y="survived",  kind="point")

plt.title("Relationship between Class and Survived")
plt.show()

# Q2. 나이(age)의 분포를 생존 여부(survived)에 따라 kdeplot으로 시각화

plt.figure(figsize=(10, 6))
sns.kdeplot(data=titanic_df, x="age", hue="survived", fill=True)

plt.title("Age Distribution by Survival Status")
plt.xlabel("Age")
plt.ylabel("Density")

plt.show()

# Pivot Method 데이터의 재구조화 pivot(index,column,value)