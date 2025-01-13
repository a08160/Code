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
    

class HealthStatus:
    def __init__(self, name, exercise, alcohol, hp=100):
        self.name = name
        self.exercise = exercise
        self.alcohol = alcohol
        self.hp = hp  # 인스턴스 변수로 초기 HP 설정
    def add_data(self,add_exercise,add_alcohol): # 사용자의 정보를 누적시킴
        self.exercise += add_exercise
        self.alcohol += add_alcohol
    def status(self):
        self.hp = self.hp + self.exercise - self.alcohol
        if self.hp >= 100:
            self.hp = 100
        elif self.hp <= 1:
            self.hp = 1
        print(f'''{self.exercise}시간 운동하다
술을 {self.alcohol}잔 마시다
{self.name} - hp: {self.hp}''')
        
class Supermarket:
    new_product = ""
    def __init__(self, location, name, product, customer): # 위치, 가게 이름, 파는 물건, 고객의 수
        self.location = location
        self.name = name
        self. product = product
        self.customer = customer

    def print_location(self):
        print(f"위치: {self.location}")
    
    def change_category(self):
        Supermarket.new_product = self.product
        
    def show_list(self):
        print(f"상품: {Supermarket.new_product}")
        
    def enter_customer(self):
        self.customer += 1
        
    def show_info(self):
        print(f"위치: {self.location}, 이름: {self.name}, 상품: {Supermarket.new_product}, 고객수: {self.customer}")

s1 = Supermarket("수원시 장안구 율전동", "농민마트", "양념갈비", "20")
s1.enter_customer()
s1.print_location()
s1.show_list()
s1.change_category()
s1.show_info()


# 실습3. 건강상태 클래스 만들기
# 정보은닉 활용
class Health:
    def __init__(self,name):
        self._name = name # 인스턴스의 이름
        self._hp = 100 # 체력(health point): 초기값 100

    # hp,name 에 대한 getter, setter 메서드가 필요
    def setname(self, name):
        self._name = name

    def getname(self):
        return self._name

    def sethp(self, hp_value): # hp_value: 1~100
        if hp_value >= 100:
            self._hp = 100
        elif hp_value <= 1:
            self._hp = 1
        else:
            self._hp = hp_value

    def gethp(self):
        return self._hp
    
    def exercise(self, hour):
        # hour 만큼 hp 값 증가
        self.sethp(self._hp + hour)
        # 얼마나 운동했는 지 hour 값 출력
        print(f"{hour}시간 운동했다")

    def alcohol(self, cups):
        # hour 만큼 hp 값 증가
        self.sethp(self._hp - cups)
        # 얼마나 운동했는 지 hour 값 출력
        print(f"{cups}잔 마셨다")
    
    # 정보 출력
    def info(self):
        print(f"{self.getname())} 님의 hp: {self.gethp()}")

class Person:
	def __init__(self, name, age):
		self.__name = name # 비공개 속성
		self.__age = age # 비공개 속성
		
	# Getter
	@property
	def name(self):
		return self.__name
		
	# Setter
	@name.setter
	def name(self, value):
		self.__name = value

	# Getter
	@property
	def name(self):
		return self.__age
		
	# Setter
	@age.setter
	def age(self, value):
		self.__age = value