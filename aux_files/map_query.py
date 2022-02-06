from geopy import Nominatim
import json

geolocator = Nominatim(user_agent="http")
dists = ["Kannur", "Kasaragod", "Kollam", "Kottayam", "Kozhikode",
         "Malappuram", "Palakkad", "Pathanamthitta", "Thiruvananthapuram",
         "Thrissur", "Wayanad", "Alappuzha", "Ernakulam", "Idukki"]
dist_data = []
for d in dists:
    geo_results = geolocator.geocode(d, exactly_one=True)
    dist_data.append(geo_results)

map_names = {}
for i, j in enumerate(dist_data):
    anylist = j.address.split(",")
    map_names[dists[i]] = [
        anylist[k - 1].lstrip()
        for k in range(len(anylist))
        if anylist[k].strip(" ") == "Kerala"][0]

dist_dict = {}
for d in range(len(map_names)):
    if dists[d] in ["Thiruvananthapuram", "Kollam"]:
        gr = geolocator.geocode(map_names[dists[d]], exactly_one=False,
                                limit=3)
        osmid = [c.raw.get("osm_id") for c in gr
                 if len(str(c.raw.get("osm_id"))) <= 7][0]
    else:
        gr = geolocator.geocode(map_names[dists[d]], exactly_one=True)
        osmid = gr.raw.get("osm_id")
    dist_dict[dists[d]] = int(osmid) + 3600000000

with open("dist_id.json", mode="w") as f:
    json.dump(dist_dict, f)
