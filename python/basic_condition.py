# 조건문
# 숫자형: 0은 거짓 / 그 외의 숫자는 참
# 리스트, 딕셔너리, 튜플, 셋(Set) 의 값이 비어있는 경우: 거짓

age = int(input("나이를 입력하세요"))

# if, elif, else 로 나눠지는 것을 "분기처리"라고 함
if age < 20:
    print("미성년자 입니다")
elif age < 30:
    print("20대입니다.")
elif age < 40:
    print("30대입니다")
elif age < 50:
    print("40대입니다")
elif age < 60:
    print("50대입니다")
else:
    print("60대 이상입니다")

print(f"나이는 {age}세 입니다.")


# 실습
# 1번
password = input("비밀번호를 입력하세요 : ")
if password == "abc123":
    print("비밀번호가 맞습니다")
else:
    print("비밀번호가 틀렸습니다")

# 2번
num = int(input("숫자를 입력하세요 : "))
if num%2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

# 3번
score = int(input("점수를 입력하세요 : "))
if score < 60:
    grade = "F"
elif score < 70:
    grade = "D"
elif score < 80:
    grade = "C"
elif score < 90:
    grade = "B"
else:
    grade = "A"

print(f"학점 : {grade}")

# Quiz. 얕은 복사 vs 깊은 복사
# 얕은 복사 Ex
a = [1,2,3,4]
b = a
print(id(a), print(b))
# 깊은 복사
a = [1,2,3,4]
b = a.copy()
print(id(a), id(b))

# 삼항연산자
# 조건문을 한줄로 줄여 쓰는 방법
# 간단한 조건을 처리할 때 주로 사용
# 참일 때의 값 if 조건 else 거짓일 때의 값

age = int(input("나이를 입력해주세요: "))
message = "성인" if age >= 20 else "미성년자"
print(message)

# 중첩 조건문

is_login = True
role = "admin"
if is_login:
    print("로그인 상태입니다")
    if role == "admin":
        print("관리자 권한을 갖습니다")
    elif role == "editor":
        print("편집자 권한을 갖습니다")
    else:
        print("일반 사용자입니다.")
else:
    print("로그인이 필요합니다")