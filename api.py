import requests

app_id = "YOUR API KEY"
base_url = "https://openexchangerates.org/api/"
latest_endpoint = "latest.json"
url = f"{base_url}{latest_endpoint}?app_id={app_id}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    rates = data.get("rates")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
