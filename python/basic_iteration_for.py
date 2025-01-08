# for 문

for i in range(5): # range(0,5)
    print(i, end = "")
print()

for i in range(2,7,2): # step: 음수값도 가능
    print(i, end = "")
print()


fruits = ["사과","바나나","포도","체리"] # 리스트, 딕셔너리, 튜플의 경우, 복수형으로 변수 선언
                                        # 집합의 경우, Index 값이 없기 때문에 출력할 때마다 값이 변형됨 
for fruit in fruits:
    print(fruit, end="|")
print()


my_dic = {
    "name": "홍길동",
    "address": "서울시 은평구",
    "gender": "남자",
    "hobby": ["런닝", "헬스", "낚시"],
}

# key 값만 출력
for i in my_dic:
    print(i, end=" ")
print()

for i in my_dic.keys():
    print(i, end=" ")
print()

# value 값만 출력
for i in my_dic:
    print(my_dic[i], end = " ")
print()

for i in my_dic.values():
    print(i, end = " ")
print()

# key, value 동시 출력
for key, value in my_dic.items():
    print(f"{key}, {value}", end = "|")
print()

# 이중 For 문
# 외부 반복문 / 내부 반복문
# 리스트 내포: 리스트 안에 for 문 사용
# 표현식 for 요소 in 시퀀스 (if 조건)

matrix2 = [
   [4,21,67],
    [99,20,12],
    [23,59,12]
]

# 원소의 합계 계산
for row in matrix2:
    # print(f"외부반복문의 row: {row}")

    for elem in row:
        # print(f"내부반복문의 elem: {elem}")
        if elem%2 == 0:
            print(elem, end = "\n")

# VS code 단축키: ctrl + d
# 현재 블럭잡힌 단어와 동일한 단어를 블럭 잡아준다. 2번 누르면 뒤의 2개까지 블럭 잡아줌. 같이 수정 가능

