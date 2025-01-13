# 클래스 심화
# 상속
'''
이미 구현된 클래스를 상속받아서 속성이나 기능이 확장
새로운 클래스에서 필드, 메서드 추가 가능

예를 들어,
A class(부모, 슈퍼, 상위 클래스) B class(자식, 서브, 하위 클래스) 이라고 하자.

B class에 A 클래스의 기능을 똑같이 구현하고 다른 기능을 추가하고 싶다고 하자.

이 때, 동일한 기능을 구현하면 그만큼의 비효율성을 가중

=> 상속을 통해 코드를 작성하지 않아도 자동으로 A class(부모)의 기능을 적용할 수 있음.

부모 클래스. 대분류
자식 클래스. 소분류
로 이해하면 좋을 듯...??

class 클래스 이름(상속할 클래스)
'''

# Ver2. 부모 클래스에 생성자가 있는 경우
class Animal:
	def __init__(self,name):
		self.name = name
	
	def speak(self):
		print(f"{self.name}가 소리를 냅니다.")
	
class Dog(Animal):
	def __init__(self, name, sound):
		super().__init__(name)
		self.sound = sound
		
	def bark(self):
		print(f"{self.name}가 {self.sound} 찾습니다.")

dog = Dog("백구", "멍멍") # 객체 생성
dog.speak() # 동물이 소리를 냅니다.
dog.bark() # 멍멍 !

class Engine:
	def __init__(self, horsepower):
		self.horsepower = horsepower
		
class Wheels:
	def __init__(self, wheel_count):
		self.wheel_count = wheel_count
		
class Car(Engine, Wheels):
	def __init__(self, horsepower, wheel_count):
		Engine.__init__(self, horsepower)
		Wheels.__init__(self, wheel_count)
		
	def info(self):
		print(f"이 자동차는 {self.horsepower} 마력 엔진과 {self.wheel_count}개의 바퀴를 가지고 있습니다.")

car = Car(100,4)
print(Car.mro())

from abc import ABC, abstractmethod

# 추상 클래스 정의
class PaymentSystem(ABC):
	@abstractmethod
	def authenticate(self):
		pass
		
	@abstractmethod
	def process_payment(self, amount):
		pass
	
	def payment_summary(self, amount):
		print(f"{amount}원 결제가 되었습니다.")
	
# 카드 결제 구현
class CreditCard(PaymentSystem):
	def authenticate(self):
		print("신용카드 인증 완료.")
		
	def process_payment(self, amount):
		print(f"신용카드로 {amount}원을 결제합니다.")
		
amount = 3600
credit = CreditCard()
credit.authenticate()
credit.process_payment(amount)

# 자식 클래스 정의 - 네이버 페이

class NaverPay(PaymentSystem):
	def authenticate(self):
		print("네이버페이 인증 완료.")
		
	def process_payment(self, amount):
		print(f"네이버페이로 {amount}원을 결제합니다.")
		
    # 네이버페이에서만 사용하는 일반 메서드
	def discount(self, amount):
		discount_amount = amount*0.05
		print(f"[이벤트] 네이버페이 5% 이벤트 적용으로 {discount_amount}원 할인")
		return amount - discount_amount

naverpay = NaverPay()
print(naverpay.discount(amount))