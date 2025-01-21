# Pandas
import pandas as pd

data = [10,20,30,40]
series = pd.Series(data) # 0 ~ index 설정
series = pd.Series(data, index = ['1','2','3','4']) # custom index 설정

# Series: 1차원
# Dictionary 형태로 설정
data = {
    "a":30,
    "b":True,
    "c":3.14,
    "d":"Python"
}
series = pd.Series(data, name = "딕셔너리") # 딕셔너리의 index는 자동 맵핑

print(series.index)
print(series.values)
print(series.shape)

# Tuple 형태로 설정
data = "민지", "여", False
series = pd.Series(data)
print(series)

# 실습. Series 만들기
import pandas as pd

data = ["4 cups", "1 cup", "2 large", "1 can"]
series = pd.Series(data, index =["밀가루", "우유", "계란","참치캔"], name ="Dinner")
print(series)

# DataFrame: 2차원
import pandas as pd

data = {
	'Name': ['홍길동', '임꺽정', '성춘향'],
	'Age': [25,30,35],
	'City': ['Seoul', 'Busan', 'Incheon']
}
df = pd.DataFrame(data, index = ["a","b","c"])

print(df.head()) # 위에서 5개
print(df.tail()) # 아래에서 5개

print(df.info())

print(df.columns) # 열 값
print(df.values) # 행 값을 행렬 형태로 반환

# loc: 라벨(Label) 기반 접근
# 행렬 이름 사용하여 데이터를 선택
# 슬라이싱 사용 시 끝 값이 포함
# df.loc[row_labels, column_labels]

print(df.loc["a", "Name"])
print(df.loc[df['Age']>=30])
print(df.loc["a",:]) # : 는 생략해도 상관없음
print(df.loc["a":"c","Name":"Age"])

# iloc: 정수(Interger) 기반 접근
# 순서 기반 접근
# 슬라이싱 사용 시 끝 값이 포함되지 않음
# df.iloc[row_indices, column_indices]

print(df.iloc[0:3,0:1])
print(df.iloc[[0,2],[0,1]])

# 행 추가
new_data = {"Name":"이몽룡", "Age":27, "City":"Pyeongyang"}
result = pd.concat([df, pd.DataFrame([new_data])],ignore_index=True) # 배열 합치기
result.index = ["a","b","c","d"]
print(result)
result.loc[:,"직업"] =["의사","경찰","간호사","디자이너"]
print(result)
# result.at[1,"City"] = "천안" # 없는 인덱스의 경우 값이 추가됨

# 열 추가
result["직업"] = ["의사","경찰","간호사","디자이너"]

# 값 수정
result.at["a","City"] = "천안"
result.iloc[1,2] = "간호사"
result.loc["a","City"] = "대전"
    
# 칼럼 이름 변경
# index: 행 명 변경 / columns: 컬럼명 변경
# inplace: 기존 객체 수정 여부
result.rename(index={"a":"1","b":"2"}, columns={"City":"a","직업":"b"}, inplace=True)

# 데이터 정렬
result.sort_index(axis=1,inplace=True) # 열 기준 정렬
result.sort_values(by = "a", ascending=True) # 행 기준 정렬

# 행 및 열 삭제
df_new = result.drop(index = "1", columns=["b"])

# 실습2. 데이터 프레임 만들기
import pandas as pd

df = pd.DataFrame(
    {"이름":["홍길동","임꺽정","성춘향"],
      "수학": [85,90,78],
      "영어":[88,76,92],
      "과학":[95,89,84]}
)

# 데이터 추가
df.loc["3",:] = ["이몽룡",88,85,90]
df["Total"] = df[["수학","영어","과학"]].sum(axis=1)
df = df.astype({"수학": int, "영어": int, "과학": int, "Total": int})
df.rename(columns = {"수학":"Math"},inplace=True)
print(df)

# 결측값
import pandas as pd
data = {
    "Name": ["이동건","이나린"],
    "Age": [None, "300살"]
}

df = pd.DataFrame(data)

# 결측값
print(df.isnull().sum())
print(df.fillna("1"))
print(df.dropna())

# 메서드
# isin(): 기본적으로 결측값을 무시
print(df.isin([None]))

# value_counts()
# normalize = True: 빈도를 비율로 계산
# sort=False: 결과를 정렬하지 않음
# ascending = True: 결과를 오름차순으로 정렬
# dropna = False: 결측값도 빈도로 계산
print(df.value_counts())


# agg 다중 적용
result = df.groupby('group').agg{
    'value1':['sum','mean','max'],
    'value2':['sum','std']
}

# lambda
result = df.groupby('group'.filter(lambda x: x['value1'.sum() > 30]))