# Folium 지도 메서드

import folium

# 지도 열기
# tiles 색상 변경
my_map = folium.Map(location=[37.554558, 126.963986], zoom_start=12,
                    tiles= "CartoDB Positron", )

# 기본 마커
folium.Marker([37.566747, 127.009352], popup = "동대문ddp플라자").add_to(
    my_map
)

# https://fontawesome.com/icons 여기서 사용할 폰트 이미지 찾기
# 커스텀 아이콘
folium.Marker([37.536788, 126.977164], popup = "전쟁기념관", icon=folium.Icon(color="red", icon = "home")).add_to(
    my_map
)

# 커스텀 아이콘
folium.Marker([37.571120, 126.977916], popup = "교보문고 광화문점", icon=folium.Icon(color="blue", icon = "book")).add_to(my_map)


# 지도에 여러 개의 마커를 딕셔너리 형태로 추가
map_info = [
        {"location": [37.572412, 126.986649], "popup":"인사동 문화의 거리"},
        {"location": [37.574028, 126.990061], "popup":"익선동 한옥 마을"}
]

for info in map_info:
    folium.Marker(location=info["location"],popup=info["popup"], icon= folium.Icon(color="green", icon= "star")).add_to(my_map)

# 지도에 영역 표시
my_map = folium.Map(
    location = [37.579470, 126.991198], zoom_start = 12, tiles= "CartoDB Positron"
)

# 원형 영역 - 다른 다각형도 가능
folium.Circle(
    location = [37.580004, 126.977339],
    radius = 500, # 반지름 (미터 단위)
    popup = "창덕궁 일대",
    fill = True,
    fillcolor = "red"
).add_to(my_map)

my_map.save("basic_folium/my_map.html")