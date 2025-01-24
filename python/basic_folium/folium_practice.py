# 실습1. 서울의 지하철역 5개를 선정하여 마커로 표시하세요.
# iterrow(): 데이터프레임에서 행단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수
import pandas as pd
import folium

subway_info = [
    {"location":[37.539846, 126.946061], "subway":"마포역"},
    {"location":[37.554989, 126.970793], "subway":"서울역"},
    {"location":[37.582340, 127.001914], "subway":"혜화역"},
    {"location":[37.648391, 127.034431], "subway":"쌍문역"},
    {"location":[37.534840, 126.994596], "subway":"이태원역"},
]
subway_df = pd.DataFrame(subway_info)
subway_df.to_csv("basic_folium/subway.csv", index = False, encoding = "EUC-KR")

subway_map = folium.Map(location=[37.572508, 126.976987], zoom_start=12)

for _,info in subway_df.iterrows():

    popup = folium.Popup(
        info["subway"], max_width=1000000, min_width=1
    )

    folium.CircleMarker(
        info["location"],
        popup = info["subway"],
        color = "blue",
        fill= True,
        fill_color ="blue").add_to(subway_map)

subway_map.save("basic_folium/subway.html")

'''
subway_map = folium.Map(location=[37.572508, 126.976987], zoom_start=12)

for info in subway_info:
    folium.CircleMarker(
        info["location"],
        popup = info["subway"],
        color = "blue",
        fill= True,
        fill_color ="blue").add_to(subway_map)

subway_map.save("basic_folium/subway.html")
'''


'''
리더님 방법
데이터는 경도 위도 역이름을 다른 key 값으로 저장

1. lambda 속도적인 면에서 lambda 가 훨씬 좋음
subway.apply(
    lambda x : folium.Marker(
        location=[x["Latitude"], x["Longitude]],
        popup = x["Station],
        icon = folium.Icon(color = "blue",icon = "home")
    ).add_to(my_map),
    axis = 1 # 열 값
)

2. iterrow()
for index, value in subway.iterrows():


'''