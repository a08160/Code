# �ǽ�1. ������ ����ö�� 5���� �����Ͽ� ��Ŀ�� ǥ���ϼ���.
# iterrow(): �����������ӿ��� ������� �ݺ��ϸ鼭 �ε����� ���� ���� ��ȯ�ϴ� �Լ�
import pandas as pd
import folium

subway_info = [
    {"location":[37.539846, 126.946061], "subway":"������"},
    {"location":[37.554989, 126.970793], "subway":"���￪"},
    {"location":[37.582340, 127.001914], "subway":"��ȭ��"},
    {"location":[37.648391, 127.034431], "subway":"�ֹ���"},
    {"location":[37.534840, 126.994596], "subway":"���¿���"},
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
������ ���
�����ʹ� �浵 ���� ���̸��� �ٸ� key ������ ����

1. lambda �ӵ����� �鿡�� lambda �� �ξ� ����
subway.apply(
    lambda x : folium.Marker(
        location=[x["Latitude"], x["Longitude]],
        popup = x["Station],
        icon = folium.Icon(color = "blue",icon = "home")
    ).add_to(my_map),
    axis = 1 # �� ��
)

2. iterrow()
for index, value in subway.iterrows():


'''