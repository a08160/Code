
# 입력 함수
a = input("너의 최애 노래는 ")
print(a)
print(type(a))

a = input("1 + 1 = ")
print(a)
print(a*2)

# 형 변환(type casting / type conversion)
# 정수 변환 int / 실수 변환 float / 문자 변환 str

# 형 변환 안 되는 예시
print(int("name"))
print(int("11.1")) # print(int(11.1)) 은 가능(소수점 아래 버림으로 실행)

b =2 
print(str(b)*10)

# 성적과 총점의 평균

math = int(input("수학점수: "))
eng = int(input("영어점수: "))

score = math + eng

avg = score / 2

print("합계 : " + str(score))
print("평균: " + str(avg))