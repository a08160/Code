# 클래스
'''
class 클래스명: # 클래스 정의
    함수

a = 클래스명() # 객체 생성
'''

class Car:
    model = ""  # model과 cc의 두가지 속성
    cc = 0

car1 = Car() # 인스턴스 생성
car1.model = "아반떼"
car1.cc = 1600

car2 = Car() # 인스턴스 생성
car2.model = "K%"
car2.cc = 2000

print(f"모델명: {car1.model}")
print(f"배기량: {car1.cc}")
print(f"모델명: {car2.model}")
print(f"배기량: {car2.cc}")


# 클래스 메서드 실습.
# 실습1. 사칙연산 클래스 만들기

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y

    def sub(self):
        return abs(self.x-self.y)

    def mul(self):
        return self.x*self.y

    def div(self):
        if self.y != 0:
            return round(self.x/self.y,3)
        else:
            return "Infinity"

calc = Calculator(10, 7)
print(calc.add()) # 17
print(calc.sub()) # 3
print(calc.mul()) # 70
print(calc.div()) # 1.429


# 클래스 변수 vs 인스턴스 변수

# 클래스 변수: "클래스에 속한" 변수 -> 모든 인스턴스(객체)가 공유하는 변수
# 인스턴스 변수: "각각의 인스턴스에 속한" 변수 -> 각 인스턴스(객체)가 독립적으로 관리하는 변수

class Dog:
	kind = "진돗개" # 클래스 변수
	
	def __init__(self,name):
		self.name = name # 인스턴스 변수
		
# 객체(인스턴스) 생성
dog1 = Dog("백구")
dog2 = Dog("검둥이")

print(dog1.name) # 백구
print(dog2.name) # 검둥이

# 클래스 변수에 접근
print(dog1.kind) # 진돗개
print(dog1.kind) # 진돗개
print(Dog.kind) # 진돗개


# 실습
# 사번 자동부여 클래스 실습.
# 클래스 변수 사용
class Employee:

    serial_num = 1000

    def __init__(self,name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):
        return f"사번: {self.id}, 이름: {self.name}"
        
# 인스턴스 변수 사용
class Employee:

    def __init__(self,name): # serial_num 1000으로 시작점이 계속 고정됨.
        self.serial_num = 1000
        self.serial_num += 1
        self.id = self.serial_num
        self.name = name

    def __str__(self):
        return f"사번: {self.id}, 이름: {self.name}"