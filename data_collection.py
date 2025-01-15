import requests, json

url = "https://api.sampleapis.com/avatar/info"
res = requests.get(url)
print(res.status_code) # 200: 요청 성공

if res.status_code == 200:
    data = res.json() # json 값으로 가져오기
    print(data[0]["synopsis"])

    print(res.text) # 응답의 본문 내용 전부 가져오기
    print(res.url) # 주소 가져오기

