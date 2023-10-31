import requests
def main():
  # Define the API key
  api_key = 'ee97e90c41354ebe9a2e1f900ccabdaf'  # my API key
  # Define the endpoint to retrieve data using the API key
  endpoint = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
  # Initialize the variable to hold the data
  data = None  # an empty variable for data
  # Ask the user to input currencies in desired format and split it into an array
  input_currencies = input("Please enter your currencies in the following format: USD to EUR or usd to eur: ").split()
  # Convert the input quantity to a decimal number
  try:
    quantity = float(input_currencies[0])
  except ValueError:
    print("Are you sure with your input? Please enter a numeric value.")
    exit()
  # Convert the primary currency to uppercase
  primary_currency = input_currencies[1].upper()
  # Convert the secondary currency to uppercase
  secondary_currency = input_currencies[3].upper()
  # Check if the primary and secondary currencies are the same 
  if primary_currency == secondary_currency:
    print("Nice try! Primary and secondary currencies cannot be the same.")
  try:
      response = requests.get(endpoint)
      response.raise_for_status()
      data = response.json()
  except requests.exceptions.HTTPError as e:
      print(f"Unable to get the current exchange rates: {e}")
  
  # Check if data is None (for example - there was an error getting data from the API)
  if data is None:
    print("Currency data not available. Please try again.")
    exit()
  
  if primary_currency in data['rates'] and secondary_currency in data['rates']:
      # Get the rate of the primary currency
      primary_currency_rate = data['rates'].get(primary_currency) 
      # Get the rate of the secondary currency
      secondary_currency_rate = data['rates'].get(secondary_currency)
      if primary_currency_rate and secondary_currency_rate:
          # Calculate the conversion rate using the rates of the currencies and the quantity
          conversion_rate = ((secondary_currency_rate / primary_currency_rate) * quantity)
          # Print the conversion result
          print(f"{primary_currency} to {secondary_currency} conversion rate is {conversion_rate:.2f} {secondary_currency}")
          inp = input("Would you like to continue? or exit the program? type Yes or No: ").lower()
          if inp == "yes":
            main()
          elif inp == "no":
            exit()
          else:
            print("Really wanna try again? but not today!")
            print("Thanks for using this program!")
            exit()
      else:
          # Handle invalid currency input or unavailable rates
          print("Invalid currency input or rates not available. Please try again.")
  else:
      # Handle invalid currencies
      print("Invalid currency, please try again!")
      exit()


main()
