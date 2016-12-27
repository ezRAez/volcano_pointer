import folium, pandas

# creates dataframe from volcano data
vol_df = pandas.read_csv("data/Volcanoes-USA.txt")

avg_lat = vol_df['LAT'].mean()
avg_lon = vol_df['LON'].mean()

map = folium.Map(location=[avg_lat, avg_lon], zoom_start=6, tiles="Mapbox Bright")

def color_picker(elevation):
    minimum = int(min(vol_df['ELEV']))
    step = int((max(vol_df['ELEV']) - min(vol_df['ELEV'])) / 3)
    if elevation in range(minimum, minimum+step):
        return "green"
    elif elevation in range(minimum + step, minimum + step * 2):
        return "orange"
    else:
        return "red"

vol_fg = folium.FeatureGroup(name="Volcano Locations")

# markers will not show in layer Control for folium - must use feature group
for lat,lon,name, elev in zip(vol_df["LAT"], vol_df["LON"], vol_df["NAME"], vol_df["ELEV"]):
    vol_fg.add_child(folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(color=color_picker(elev))))

map.add_child(vol_fg)

# adds geojson pop data
map.add_child(folium.GeoJson(data=open('data/world_pop.geojson'),
name="World Population",
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(folium.LayerControl())

map.save(outfile="index.html")
