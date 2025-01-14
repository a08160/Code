# 실습1. 상속과 오버라이딩

class Product:
    def __init__(self, name, price, quantity): # 상품의 이름, 가격, 개수 를 입력 받음
        self.name = name
        self.price = price
        self.quantity = quantity

    # 재고 업데이트
    def update_quantity(self,amount):
        self.quantity += amount
        print(f"{self.name} 재조가 {amount}만큼 {'증가' if amount > 0 else '감소'}했습니다. 현재 재고: {self.quantity}")

    # 상품 정보 출력 메서드
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")

class Electronic(Product):
    def __init__(self,name,price,quantity, warranty_period=12): # 추가변수 보증기간(기본값 12개월)
        super().__init__(name,price,quantity)
        self.warranty_period = warranty_period

    def extend_warranty(self,months):
        self.warranty_period += months
        print(f"보증기간이 {months}개월 연장되었습니다. 현재 보증 기간 : {self.warranty_period}")

    def display_info(self):
        super().display_info()
        print(f"보증 기간 : {self.warranty_period}개월")

from datetime import datetime

class Food(Product):
    def __init__(self,name, price, quantity, expiration_date): # 유통 기한 형태는 YYYY-MM-DD
        super().__init__(name,price,quantity)
        try:
            # 유통기한이 YYYY-MM-DD 형식인지 확인
            self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("유통기한은 'YYYY-MM-DD' 형식이어야 합니다.")

    def is_expired(self):
        today_date = datetime.today().date()
        print(f"{self.name}는 유통기한이 {"지나지 않았습니다." if self.expiration_date <= today_date else "지났습니다."}")

    def display_info(self):
        self.is_expired()
        super().display_info()


e = Food("스마트TV",15000,5,"2025-01-30")
e.is_expired()
e.display_info()



# 실습2. 날짜별 전력사용량

electricity_usage = [
    {"date":"2024-11-01", "usage": 12.5},
    {"date":"2024-11-02", "usage": 15.3},
    {"date":"2024-11-03", "usage": 10.8},
    {"date":"2024-11-04", "usage": 14.2},
    {"date":"2024-11-05", "usage": 13.6}
]

# 추상 클래스 ElectricityData 생성

from abc import ABC, abstractmethod

class ElectricityData(ABC):
    global electricity_usage
    
    def __init__(self, usage_data, total_usage):
        self._usage_data = usage_data
        self._total_usage = total_usage

    @property   
    def usage_data(self):
        return self._usage_data
        
    @usage_data.setter
    def usage_data(self,value):
        self._usage_data = value

    @property
    def total_usage(self):
        return self._total_usage

    @total_usage.setter
    def total_usage(self,value):
        self._total_usage = value
        
    @abstractmethod
    def calculate_total_usage(self):
        pass

    @abstractmethod
    def get_usage_on_date(self, date):
        pass

    def add_usage(self, date, usage):
        electricity_usage.update({"date":self._date, "usage": self._usage})
        return electricity_usage

    def remove_usage(date):
        for i in electricity_usage:
            if i["date"] == self._date:
                electricity_usage.remove(i)
        return electricity_usage


# 자식 클래스 HomeElectricityData 생성

class HomeElectircityData(ElectricityData):

    def calculate_total_usage(self):
        total_usage = sum(i["usage"] for i in electricity_usage)
        print(f"총 전력 사용량: {total_usage}")

    def get_usage_on_date(self, date):
        for i in electricity_usage:
            if i["date"] == self.date:
                date_usage = i["usage"] 
        print(f"{self.date}의 사용량: {date_usage}")

    @classmethod
    def period_usage(cls, start_date, end_date):
        # 날짜 문자열을 datetime 객체로 변환
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        
        # 필터링된 결과를 저장할 리스트
        list1 = []
        
        for usage in cls.electricity_usage:
            usage_date = datetime.strptime(usage["date"], "%Y-%m-%d")
            if start_date <= usage_date <= end_date:
                list1.append(usage)
        
        print(list1)  # 결과 반환


    @staticmethod
    def max_usage(self):
        list_usage = [i["usage"] for i in electricity_usage]
        max_index = list_usage.index(max(list_usage))
        print(f"가장 높은 사용량: {electricity_usage[max_index]}")

a = HomeElectircityData(10,20)
a.get_usage_on_date("2024-11-01")