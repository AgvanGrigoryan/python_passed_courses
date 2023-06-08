import requests
import pprint
starttime = input('Enter starttime(YYYY-MM-DD): ')
endtime = input('Enter endtime(YYYY-MM-DD): ')
latitude = input('Enter latitude(decimal): ')
longitude = input('Enter longitude(decimal): ')
maxradiuskm = input('Enter max radius in km: ')
minmagnitude = input('Enter min magnitude(decimal): ')
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?=2000"
response = requests.get(url, headers={'Accept': 'application/json'},
                        params={'format': 'geojson',
                                'starttime': starttime,
                                'endtime': endtime,
                                'latitude': latitude,
                                'longitude': longitude,
                                'maxradiuskm': maxradiuskm,
                                'minmagnitude': minmagnitude
                                }
                        )
data = response.json()
##pprint.pprint(data)
features = data['features']
for i in range(len(features)):
    print(f"{i+1}. Place: {features[i]['properties']['place']}. Magnitude: {features[i]['properties']['mag']}.")
##print(data['type'])
