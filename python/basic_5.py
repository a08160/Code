"""
# 이차원 리스트 (행렬)
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

value = matrix[1][2] # 2번 행의 3번째 열 요소를 반환

# 요소 추가
matrix[1] = matrix[1] + [99]

# 행 추가
matrix = matrix + [10,11,12]

# 요소 수정
matrix[0][0] = 100
matrix[1][1] = 5000
print(matrix)

# 행 삭제
del matrix[2]

# 행 개수
rows = len(matrix)

# 실습
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[0].append(10) # 1번 행에 10 추가 
matrix.append([10,11,12]) # [10,11,12] 의 행을 추가
matrix[1].insert(1,100)
matrix.insert(2, ["안녕","반가워","어서와"]) # 행 삽입
matrix[0].extend([11,22])
"""
# Quiz 3차원 리스트에서 인덱싱을 이용해 아이스크림 문자열 만들기
words = [
    [["마", "크"], ["구", "이"]],
    [["피", "아"], ["림", "차"]],
    [["스", "사"], ["나", "가"]]
]
print(words[1][0][1]+words[0][1][1]+words[2][0][0]+words[0][0][1]+words[1][1][0])   

# 3차원 리스트의 인덱스를 출력
for i, layer in enumerate(words):          # 첫 번째 차원
    for j, row in enumerate(layer):        # 두 번째 차원
        for k, element in enumerate(row):  # 세 번째 차원
            print(f"Element: {element}, Index: ({i}, {j}, {k})")