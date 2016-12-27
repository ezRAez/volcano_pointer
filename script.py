import folium, pandas

vol_df = pandas.read_csv("data/Volcanoes-USA.txt")

map = folium.Map(location=[45.372, -121.697], zoom_start=10, tiles="Stamen Terrain")

for lat,lon,name in zip(vol_df["LAT"], vol_df["LON"], vol_df["NAME"]):
    map.simple_marker(location=[lat, lon], popup=name, marker_color="red")

map.create_map(path="index.html")
