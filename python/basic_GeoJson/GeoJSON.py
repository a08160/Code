# Folium과 GeoJSON의 차이
# GeoJSON 은 정확한 지도 데이터를 가져옴
# Folium은 지도에 시각화 하는 기능
# GeoJSON에서 데이터 추출 => Folium 에서 시각화

# GeoJSON
from geojson import Feature, Point, FeatureCollection
import folium

feature1 = Feature(geometry = Point((126.994132,37.559240)),
                   properties={"name":"서울",
                               "population":"970만"}
                               )
feature2 = Feature(geometry = Point((129.041493,35.190651)),
                   properties={"name":"대전",
                               "population":"340만"}
                               )
feature3 = Feature(geometry = Point((127.129872,37.281708)),
                   properties={"name":"용인",
                               "population":"100만"}
                               )
feature4 = Feature(geometry = Point((129.363063,36.099861)),
                   properties={"name":"대구",
                               "population":"240만"}
                               )

my_map = folium.Map(location = [36.742362, 128.044406], zoom_start = 3)

# 데이터 하나로 묶기
geojson_data= FeatureCollection([feature1,feature2,feature3,feature4])

# 데이터를 지도에 추가
folium.GeoJson(
    geojson_data,
    name="GeoJSON Data",
    tooltip = folium.GeoJsonTooltip(
        fields = ["name","population"], # 표시할 속성
        aliases = ["도시이름: ","인구: "], # 속성의 별칭
    )
).add_to(my_map)

my_map.save("map.html")