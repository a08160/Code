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