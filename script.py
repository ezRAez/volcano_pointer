import folium, pandas

# creates dataframe from volcano data
vol_df = pandas.read_csv("data/Volcanoes-USA.txt")

avg_lat = vol_df['LAT'].mean()
avg_lon = vol_df['LON'].mean()


def color_picker(elevation):
    minimum = int(min(vol_df['ELEV']))
    step = int((max(vol_df['ELEV']) - min(vol_df['ELEV'])) / 3)
    if elevation in range(minimum, minimum+step):
        return "green"
    elif elevation in range(minimum + step, minimum + step * 2):
        return "orange"
    else:
        return "red"

map = folium.Map(location=[avg_lat, avg_lon], zoom_start=6, tiles="Stamen Terrain")

for lat,lon,name, elev in zip(vol_df["LAT"], vol_df["LON"], vol_df["NAME"], vol_df["ELEV"]):
    map.simple_marker(location=[lat, lon], popup=name, marker_color=color_picker(elev))

map.create_map(path="index.html")
