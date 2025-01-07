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

a,b =5,8
max_value = a if a >= b else b

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

# 삼항 연산자의 중첩
score = 81
grade = "A" if score >= 90 else ("B" if score >=80 else "C")

# pass
# 조건을 만들어서 코드를 생성해야하지만 당장 코드가 필요하지 않은 경우 주로 사용
# 나중에 구현할 코드 자리

# In 연산자 w/ 조건문
user = ["Sean","Linda","Allie","Martin"]
username = input("Name >> ")

if username in user:
    print(f"환영합니다. {username}님")
else:
    print("등록되지 않은 사용자입니다. 회원가입을 진행해주세요")


# 중첩조건문 실습
age = int(input("나이를 숫자로 입력해주세요: "))
if age >=0:
    pay = input("결제방법을 입력해주세요 (현금 또는 카드): ")
    if age < 8 or age >= 75:
        cost = "무료"
    elif age < 14:
        cost = "450원"
    elif age < 20:
        if pay == "카드":
            cost = "720원"
        else:
            cost = "1000원"
    else:
        if pay == "카드":
            cost = "1200원"
        else:
            cost = "1300원"
    print(f"{age}세의 카드 요금은 {cost}입니다.")
else:
    print("나이로 음수값이 될 수 없습니다.")

# 위 실습에 대한 다른 코드
pay_list = [[0,450,720,1200,0],
            [0,450,1000,1300,0]]
years = input("나이를 숫자로 입력해주세요: ")
years = int(years)

how = input("결제방법을 입력해주세요 (카드 또는 현금): ")

code  = -1 # 초기값
result = 0 # 초기값

code = 0 if how == "카드" else 1\
        if how == "현금" else -1

# code 0 if how == "카드" else (1 if how == "현금" else -1) 로도 입력이 가능

result = pay_list[code][0] if years < 8 else pay_list[code][1]\
                           if years < 14 else pay_list[code][2]\
                           if years < 20 else pay_list[code][3]\
                           if years < 75 else pay_lsit[code][4]

if code == 0: # 카드
    print(f"{years}세의 카드 요금은 {result}입니다.")
else: 
    if code == 1: # 현금
    else:
        print("결제 방법을 잘못 입력하였습니다.")

# in 연산자 활용 실습
fru_cal = {}
fru_cal.update({"apple":95,"banana":105,"cherry":50})
fruit = input("과일을 영문으로 입력하세요. :")

if fruit in fru_cal:
    print(f"{fruit}의 칼로리는 {fru_cal[fruit]}Kcal입니다.")
else:
    print("과일이 목록에 없습니다.")
