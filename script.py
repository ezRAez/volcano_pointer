import folium, pandas

map = folium.Map(location=[45.372, -121.697], zoom_start=10, tiles="Stamen Terrain")

map.simple_marker(location=[45.372, -121.697], popup="Mt. Hood Meadows", marker_color="red")
map.simple_marker(location=[45.3311, -121.7311], popup="Timberlake Lodge", marker_color="green")

map.create_map(path="test.html")
