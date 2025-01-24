# 실습
import folium
from geojson import Feature, FeatureCollection, Polygon

coordinates = [
    [
        [127.09509804922101, 38.27664540318193],
        [126.19106179015711, 37.691126942097284],
        [126.6763291246067, 37.644109114072236],
        [126.81944707415761, 37.5500606204985],
        [126.77406589079419, 37.39216561691303],
        [126.63442405112482, 37.24503304107668],
        [126.9102047125902, 36.91083555169048],
        [127.27651917544017, 36.91658377599485],
        [127.71287480743894, 37.20890846782734],
        [127.82749418292957, 37.547077962973944],
        [127.55181022191584, 37.62163708155093],
        [127.60431904941095, 37.93328574313473],
        [127.09509804922101, 38.27664540318193]
    ]
]

polygon = Polygon(coordinates)
feature = Feature(geometry=polygon, properties={"name": "수도권"})
feature_data = FeatureCollection([feature])

capital_map = folium.Map(location=[37.555607, 126.992801],
                         zoom_start=7)

folium.GeoJson(
    feature_data,
    name="Geo Data",
    tooltip=folium.GeoJsonTooltip(
        fields=["name"],
        aliases=["이름: "]
    ),
    style_function= lambda x : {
        "fillcolor": "yellow", # 다각형 내부 색상
        "color": "black" # 테두리 색상
        "weight": 2 # 테두리 두께
        "fillOpacity": 0.5 # 내부 투명도
    }
).add_to(capital_map)

capital_map.save("basic_GeoJson/Capital.html")
