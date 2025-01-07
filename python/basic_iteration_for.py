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
    print(f"{key}, {value}", end = " ")
print()