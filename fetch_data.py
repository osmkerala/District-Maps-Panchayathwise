import requests
import geojson

res = """
    [out:json]
    [timeout:500]
    ;
    area(3602018154)->.searchArea;
    (
    nwr
        ["boundary"="local_authority"]
        ["admin_level"="8"]
        (area.searchArea);
    );
    out meta;
    >;
    out meta qt;"""

url = 'http://overpass-api.de/api/interpreter'

r = requests.get(url, params={"data": res})


with open("kollam.geojson", mode="w") as f:
    geojson.dump(r.json(), f, indent=4)
