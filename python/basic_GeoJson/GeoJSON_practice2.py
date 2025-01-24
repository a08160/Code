import folium
import geojson
import json

# 실무 실습
my_map = folium.Map(location=[37.555108, 126.950098], zoom_start=7)

# geojson
with open("basic_GeoJson/HangJeongDong_ver20241001.geojson", "r", encoding = "utf-8") as file:
    geojson_data = json.load(file)

folium.GeoJson(
    geojson_data,
    name = "대한민국 경계",
    style_function= lambda _: {
        "fillcolor" : "blue",
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.1
    }
).add_to(my_map)

my_map.save("basic_GeoJson/my_map.html")