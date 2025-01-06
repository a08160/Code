# 튜플
# 원소에 대한 수정/삭제/추가 가 불가능

t1 = (1,) # 요소가 1개인 플은 반드시 쉼표 사용 ! / () 쓰지 않아도 가능
not_tuple = (1) # 단순히 숫자 1을 의미

t2 = (1,2,3,4,1,2,3,4,5)
t3 = 1,2,3

t4 = ("a","b","c",("안녕","감자")) # 튜플 안에 튜플 자료형 가능
print(t4)

print(t1[0])
print(t2.count(3))
print(t3.index(2))
print(t4[3][0])

print("d" in t4) # False
print("a" in t4) # True

# t4[0] = 2 : Error - 수정 불가