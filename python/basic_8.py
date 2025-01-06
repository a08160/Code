# dictionary
# 키와 값으로 이루어진 자료형
# 키는 중복될 수 없음
# {} or dict{} 로 생성
# 접근/추가/삭제 가능
# 메서드: get/update/keys/values/items/clear()

dict1 = {}
dict1 = dict()

dict1 = {
    "name":"홍길동",
    "age":20,
    "city":"Seoul",
    "hoddy":["런닝","등산","헬스"]
} # {} 를 활용한 딕셔너리 생성

dict2 = dict(name = "홍길동", age = "21") # dict 함수를 통한 딕셔너리 생성

# 값 접근
print(dict1["name"])

# 값 수정
dict1["name"] = "이동건" 
print(dict1)

# 요소 추가
dict1["birth"] = "19900101"
print(dict1)

del dict1["birth"] # birth 라는 키 자체를 삭제
print(dict1)

# 딕셔너리 메서드
fruits = {"apple":"사과", "banana":"바나나"}
print(fruits.get("apple"))
print(fruits.get("peach")) # 존재하지 않는 key 사용 시 None 반환
print(fruits.get("peach","복숭아")) # 존재하지 않는 key 에 대해서 value 를 할당 / dictionary 요소 추가는 아님 !!!
print(fruits.get("apple","복숭아")) # apple 이라는 key 가 기존에 존재하기 때문에 기존의 "사과"를 반환
print(fruits)

fruits.update({"grapes":"포도", "melon":"멜론"})
print(fruits)

print(fruits.keys())
print(fruits.values())
print(fruits.items())

# 요소 모두 지우기
fruits.clear()

# dictionary 실습
score = {}
score.update({"Alice":85,"Bob":90,"Charlie":95})
score.update({"David":80})
score["Alice"] = 88
del score["Bob"]
print(score)

# 내장 함수 