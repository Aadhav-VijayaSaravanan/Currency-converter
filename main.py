import requests

api_key = 'ee97e90c41354ebe9a2e1f900ccabdaf'
endpoint = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
data = None

try:
    response = requests.get(endpoint)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as e:
    print(f"Unable to get the current exchange rates: {e}")

input_currencies = input("Input your currencies in the format - USD to EUR - or usd to eur: ").split()
if len(input_currencies) != 4:
    print("Invalid input. Please try again.")
else:
    quantity = float(input_currencies[0])
    primary_currency = input_currencies[1].upper()
    secondary_currency = input_currencies[3].upper()

    if primary_currency in data['rates'] and secondary_currency in data['rates']:
        primary_currency_rate = data['rates'].get(primary_currency)
        secondary_currency_rate = data['rates'].get(secondary_currency)

    if primary_currency_rate and secondary_currency_rate:
        conversion_rate = ((secondary_currency_rate / primary_currency_rate) * quantity)
        print(f"{primary_currency} to {secondary_currency} conversion rate is {conversion_rate:.2f}")
    else:
        print("Invalid currency input or rates not available. Please try again.")
