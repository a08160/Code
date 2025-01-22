# 실습. 공공데이터 활용
import pandas as pd

df = pd.read_csv("서울시 공원 내 운동기구 설치 현황_201231.csv", encoding = "cp949")

df.columns = df.columns.str.strip() # 컬럼명에 공백 존재
df = df.map(lambda x: x.strip() if isinstance(x, str) else x) # 각 값들에 공백 존재

print(df.head()) 
print(df.info()) # 결측치 여부 확인


# 공원별 총 운동기구 설치 수
park_df = df.groupby("구분")["운동기구 수량"].sum()

with open("공원별 총 운동기구 설치 수.csv", "w", encoding = "utf-8") as f:
    f.write(park_df.to_csv(header = True))    

# 운동기구 종류별 설치 수
exercise_df = df.groupby("운동기구 기종명")["운동기구 수량"].sum()

with open("운동기구 종류별 설치 수.csv", "w", encoding = "utf-8") as f:
    f.write(exercise_df.to_csv(header = True))    

# 관리기관별 총 운동기구 설치 수
organ_df = df.groupby("관리기관")["운동기구 수량"].sum()

with open("관리기관별 총 운동기구 설치 수.csv", "w", encoding = "utf-8") as f:
    f.write(organ_df.to_csv(header = True))

# 특정 공원 데이터 필터링(예: 남산공원(회현))
def each_park(park_name):
    global df
    each_park_df = df[df["구분"]==park_name].drop(columns=["구분"])
    
    with open(f"{park_name}.csv", "w",encoding="utf-8") as f:
        f.write(each_park_df.to_csv(header=True, index= False))

each_park("남산공원(회현)")

# 특정 운동기구 종류 데이터 필터링(예: 스텝사이클)
def each_exercise(exercise_name):
    global df
    each_exercise_df = df[df["운동기구 기종명"]==exercise_name].drop(columns=["운동기구 기종명"])
    
    with open(f"{exercise_name}.csv", "w",encoding="utf-8") as f:
        f.write(each_exercise_df.to_csv(header=True, index= False))

each_exercise("스텝사이클")

# 운동기구 수량 기준 내림차순 정렬
new_df = df.sort_values(by = "운동기구 수량", ascending = False, inplace = False)

with open("운동기구 수량 기준 내림차순 정렬.csv", "w", encoding = "utf-8") as f:
    f.write(new_df.to_csv(header = True, index = False))