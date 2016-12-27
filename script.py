import folium, pandas

vol_df = pandas.read_csv("data/Volcanoes-USA.txt")

map = folium.Map(location=[45.372, -121.697], zoom_start=10, tiles="Stamen Terrain")

for lat,lon,name, elev in zip(vol_df["LAT"], vol_df["LON"], vol_df["NAME"], vol_df["ELEV"]):
    map.simple_marker(location=[lat, lon], popup=name, marker_color="green" if elev in range(0,1000) else 'orange' if elev in range(1000,3000) else "red")

map.create_map(path="index.html")
