import requests

ride = {
    "duration_sec": "75284",
    "start_time": "2018-01-31 22:52:35.2390",
    "end_time": "2018-02-01 19:47:19.8240",
    "start_station_id": 120,
    "start_station_name": "Mission Dolores Park",
    "start_station_latitude": 37.7614205,
    "start_station_longitude": 122.4264353,
    "end_station_id": 285,
    "end_station_name": "Webster St at O'Farrell St	",
    "end_station_latitude": 37.7835208353,
    "end_station_longitude": 122.4311578274,
    "bike_id": 2765
}
url = 'http://localhost:9696/predict'
response = requests.post(url, json=ride)
print(response.json())
# features = predict.prepare_features(ride)
# pred = predict.predict(ride)
# print(pred[0 ])