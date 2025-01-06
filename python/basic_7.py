# Set 집합 {} / set() 
# 중복을 허용하지 않고, 순서가 없음 / 수학의 집합과 동일한 개념 => 인덱스 사용 불가
# 요소의 추가나 삭제가 가능
# add(), update, remove(), discard(), clear()
# 연산: |(합집합), union() / &(교집합), intersection() / -(차집합), difference()

s1 = {1,2,3,3,4}
print(s1)

s1.add(5) # 원소 추가
print(s1)

# update() : 다른 set, list, tuple 의 요소들을 현재 집합에 추가하는 기능
s1.update([6,7,8,9,10])
print(s1)

# remove() : 존재하는 요소만 삭제 가능(없는 값을 삭제하려고 하면 Error 발생)
s1.remove(3)
print(s1)

# discard() : 존재하지 않는 요소를 삭제해도 오류가 발생하지 않음
# Ex. 없는 요소를 삭제해도 무방한 경우 사용(아니라면 remove() 사용)
s1.discard(9)
print(s1)
s1.discard(100)

# clear() : 집합의 모든 원소를 제거
s1.clear()
print(s1)

# set 연산
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# 합집합
s3 = s1.union(s2)
s3 = s1 | s2
print(s3)

# 교집합
s4 = s1.intersection(s2)
s4 = s1 & s2
print(s4)

# 차집합
s5 = s1.difference(s2)
s5 = s1 - s2
print(s5)

# in 키워드
print(1 in s1)
print(100 in s1)

print(len(s1))