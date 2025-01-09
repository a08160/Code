# lambda function

add2 = lambda x,y: x+y
print(add2(4,5))

# 매개변수가 1개인 람다식
square = lambda x: x**2


# 실습6. 함수 종합 프로그래밍

weather_data = [ # 날짜, 지역, 온도, 강수량 순
    ["2024-11-20", "서울", 15.2,0.0],
    ["2024-11-20", "부산", 18.4,0.0],
    ["2024-11-21", "서울", 10.5,2.3],
    ["2024-11-21", "부산", 14.6,1.2],
    ["2024-11-22", "서울", 8.3,0.0],
    ["2024-11-22", "부산", 12.0,0.0]
]

# 함수
# 도시별 데이터를 분류
def city_info(list): # 지역을 값으로 저장
    for i in list:
        if city in i:
            i.pop(1)
            city_dict.update({tuple(i):city})
            list.remove(i)
    return list, city_dict, city


# 도시별 평균 기온 계산
def city_temp(city_dict,city):
    info = [ i[1] for i in city_dict if city_dict[i] == city]
    print(f"{city}의 평균 기온: {statistics.mean(info):.2f}℃")

# 도시별 최고/최소 기온 찾기
def max_min_temp(city_dict,city):
    info = [ i[1] for i in city_dict if city_dict[i] == city]
    print(f"{city}의 최고 기온: {max(info):.2f}℃, 최저 기온: {min(info):.2f}℃")

    
# 도시별 강수량 분석
def rainfall(city_dict,city):
    info = [ i[2] for i in city_dict if city_dict[i] == city and i[2] != 0]
    print(f"{city}의 총 강수량: {sum(info):.2f}mm")
    print(f"{city}의 강수량이 있었던 날: {len(info)}일")
    

# 데이터 추가
def add_data(list):
    date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요 : ")
    temp = float(input("평균 기온을 입력하세요 (℃): "))
    rain = float(input("강수량을 입력하세요 (mm): "))
    list.append([date,city,temp,rain])
    print(f"{city}의 날씨 데이터가 추가되었습니다.")
    return list
        
# 전체 데이터 출력
def full_data(list):
    print("현재 저장된 날씨 데이터:\n")
    for i in list:
        print("날짜: %s, 도시: %s, 평균 기온: %f℃, 강수량: %fmm"%(i[0],i[1],i[2],i[3]), end = "\n")

import copy
import statistics

data = copy.deepcopy(weather_data)

city_dict = {}

while True:
    func = int(input("""[날씨 데이터 분석 프로그램]
1. 평균 기온 계산
2. 최고/최저 기온 찾기
3. 강수량 분석
4. 날씨 데이터 추가
5. 전체 데이터 출력
6. 종료
원하는 기능의 번호를 입력하세요: """))
    if func == 4:
        add_data(data)
        add_data(weather_data)
    if func == 6:
        print("프로그램을 종료합니다")
        break
    city = input("도시 이름을 입력하세요 : ")
    city_info(data)
    if func == 1:
        city_temp(city_dict,city)
    if func == 2:
        max_min_temp(city_dict,city)
    if func == 3:
        rainfall(city_dict,city)
    if func == 5:
        full_data(weather_data)