import requests

r = requests.get(
    "https://opensky-network.org/api/flights/departure?airport=EDDF&begin=1651770587&end=1683310587")

print(r.text)