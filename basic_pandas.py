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

# 요소 추가 및 삭제

new_data = {"Name":"이몽룡", "Age":27, "City":"Pyeongyang"}
result = pd.concat([df, pd.DataFrame([new_data])],ignore_index=True) # 배열 합치기기
print(result)
