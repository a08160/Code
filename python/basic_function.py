# 함수
# 사용자 정의 함수
# 사용자가 직접 정의해서 사용하는 함수(Customizing)

'''
def 함수명(매개변수):
    수행문1
    수행문2
    return 반환값

* 매개변수 / 리턴값 둘다 있어도 되고 없어도 됨
'''

# 1. 매개변수X / 리턴값X
def say_hello():
    print("hello")

say_hello()

# 2. 매개변수O / 리턴값X
def say_hello(name):
    print(f"hello, {name}")

say_hello("Allie")

def gugudan(dan,end):
    print(f'{dan}단')
    for i in range(1, end+1):
        print(f'{dan} x {i} = {dan*i}')

gugudan(7,15)

# 3. 매개변수X / 리턴값O
def say_hello():
    a = "hello"
    return a

hi = say_hello()
print(hi)

# 4.매개변수O / 리턴값O
def add_numbers(x,y):
    print("덧셈을 시작합니다.")
    return x+y

result2 = add_numbers(40,50)
print(result2)

# 다양한 타입을 return 하는 함수
# 1. list 타입을 반환하는 함수
# ex. 제한값(limit) 까지의 짝수를 출력하는 함수

def print_even_numbers(limit):
    return [i for i in range(0,limit) if i%2 == 0]

print(print_even_numbers(10))

# 2.
def print_user_info(name, grade):
    return {"user_name":name, "user_grade":grade}

print(print_user_info("Allie",2))

# print(set("hello")) # 각 철자를 중복없이 구분

def print_unique_char(word):
    return set(word)

print(print_unique_char("Hi, My name is Sean"))

# 혼합 Collection 반환
# Ex. 딕셔너리 안에 리스트가 있는 경우

def double(nums):
    return [i*2 for i in nums]
print(double([1,2,3,4,5]))

# 실습1
def program1(x,y):
    print(f"결과(곱): {x*y}" if x==y else f"결과(합): {x+y}")

# 실습2
def program2(product,cost):
    print(f"{product} 가격: {cost+2500}원" if cost < 20000 else f"{product} 가격: {cost}원")



# 내장 함수
'''
abs(x) # 절댓값 내장 함수
pow(x,y) # x^y 거듭제곱 내장 함수
map(function, 반복 가능한 객체) # 리스트의 각 요소에 주어진 함수를 적용하여 새로운 리스트를 반환
filter(함수, 반복가능한 객체) # 리스트에서 주어진 조건을 만족하는 요소만 필터링하여 반환
							# 튜플 사용 시 key 값에 대해 함수 적용. 함수나 객체 값 수정 필요
'''

def square(x):
    return x**3

numbers = [2,4,6,8,10]

print(list(map(square, numbers)))

# 실습4. 함수 만들기 (배수 개수 구하기기)

# Ver.1
def multiple1(x,y): # x는 기본값, y는 최대 범위
    list1 = []
    a = 0
    while a < y:
        a += x
        list1.append(a)
    print(" ".join(map(str,list1)))
    print(f"{x}의 배수의 개수: {len(list1)}")


# Ver.2 중첩 함수.
def multiple2(num):

    def check(x):
        return x % num == 0

    lists = filter(check, range(1,31))
    return (lists, len(lists))

# max / min 에 대한 함수 로직 작성
# 매개변수 2개 or 매개변수 n개

# max 함수 로직 작성

def my_max(*args):
    return sorted(args)[-1]

# min 함수 로직 작성

def my_min(*args):
    return sorted(args)[0]

# 함수에 대한 시간적 성능 측정 함수

import time

def time_performance(function):
    start = time.time()
    function
    end = time.time()
    print(f"{end-start:.10f}")

# 재귀함수

# 실습5. 피보나치 수열 만들기

def fibonacci(num):
    if num != 0 and num != 1:
        return fibonacci(num-1) + fibonacci(num-2)
    else:
        return num

print(fibonacci(6))