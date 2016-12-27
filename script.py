import folium, pandas

# creates dataframe from volcano data
vol_df = pandas.read_csv("data/Volcanoes-USA.txt")

avg_lat = vol_df['LAT'].mean()
avg_lon = vol_df['LON'].mean()

map = folium.Map(location=[avg_lat, avg_lon], zoom_start=6, tiles="Stamen Terrain")

def color_picker(elevation):
    minimum = int(min(vol_df['ELEV']))
    step = int((max(vol_df['ELEV']) - min(vol_df['ELEV'])) / 3)
    if elevation in range(minimum, minimum+step):
        return "green"
    elif elevation in range(minimum + step, minimum + step * 2):
        return "orange"
    else:
        return "red"

for lat,lon,name, elev in zip(vol_df["LAT"], vol_df["LON"], vol_df["NAME"], vol_df["ELEV"]):
    map.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color_picker(elev))))

map.save(outfile="index.html")
