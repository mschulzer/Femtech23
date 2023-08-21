import network
import urequests

# Initier WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Autorisation
ssid = ''
password = ''

#wlan.scan()
wlan.connect(ssid, password)


# API: hent data fra EnergiNet
url = 'https://api.energidataservice.dk/dataset/DatahubMeasuringPointStatistics?limit=5'

response = urequests.get(url)
result = response.json()

records = result.get('records', [])
for record in records:
  print(record['GridCompanyName'])
