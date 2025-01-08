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

# 실습3
