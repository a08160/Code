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
	def __init__(self,name,cake):
		self.name = name
		self.cake = cake
	
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
