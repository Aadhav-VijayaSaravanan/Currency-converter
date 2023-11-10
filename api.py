import os
import requests
import main


api_key = "YOUR API KEY from currencyfreaks.com"
endpoint = f"https://api.currencyfreaks.com/v2.0/rates/latest?apikey={api_key}"
response = requests.get(endpoint)

if response.status_code == 200:
        data = response.json()
        main.main()
else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
