# 변수
# 전역변수 vs 지역변수
# 전역 변수의 값을 함수 내부에서 변경하려면 global 키워드 사용

x = 0

def oneUp():
    global x
    x += 1
    return x
print(oneUp())
print(oneUp())
print(oneUp())


# 가변 매개변수
# 기본값 설정 매개변수는 무조건 뒤쪽에 위치
def pr_str(txt, count):
    print(txt, count)

pr_str("하이", 3)
pr_str("안녕", 3)

# _ 를 반복변수로 사용 => 코드 내부에 사용하지 않는 반복 변수임(단순 반복을 위함)
for _ in range(1,5):
    print("a")


# 순서를 맞추지 않고 키워드 사용해서 함수 호출 가능
# 위치 매개변수와 함께 사용하는 경우, 위치 매개변수가 무조건 앞에 있어야 함
# 프로그램이 인식할 때, 위치 매개변수의 위치를 정확하게 인식하기 위함함

def introduce(name, age, city):
    print(f"{name} + {age} + {city}")

introduce(age = 19, name = "이동건", city = "서울")
# 잘못된 예시 introduce(age = 19, name, city)

# 가변 위치 매개변수 / 가변 키워드 매개변수
# 가변 위치 매개변수
# *args 관례적으로 사용
# 여러 개의 매개변수를 튜플 형태로 제시


# 가변 키워드 매개변수
# **kwargs 관례적으로 사용
# 여러 개의 키워드 형식 사용 가능  

# 실습4. 함수 만들기
# 1~30까지의 자연수 중 배수와 배수의 개수를 계산하는 함수르 정의하시오
