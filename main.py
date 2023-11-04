import api

def main():
  inputi = input(
      "\033[1mCurrency Conversion\033[0m\nEnter the currency you want to convert: "
  ).upper().split()
  primary = inputi[1]
  secondary = inputi[3]

  if inputi[0].isnumeric:
    if isinstance(float(inputi[0]), float) or isinstance(int(inputi[0]), int):
      quantity = float(inputi[0])
  else:
    print(
        "Tring to do something?\n input only numeric digits not in alphabetical form"
    )

  if inputi[1] in api.data["rates"] and inputi[3] in api.data["rates"]:
    primary_rate = float(api.data["rates"].get(primary))
    secondary_rate = float(api.data["rates"].get(secondary))
    coversion_rate = float(quantity * (secondary_rate / primary_rate))
    print(f"The conversion rate for {primary} is {coversion_rate:.2f}")
  else:
    print("your currency isnt valid, try again!")

  sorte = sorted(api.data["rates"].items(), key=lambda x: float(x[1]), reverse=False)
  for i in range(len(sorte)):
    if secondary in sorte[i]:
      rem = i % 10
      if rem == 1:
        fini = "st"
      elif rem == 2:
        fini = "nd"
      elif rem == 3:
        fini = "rd"
      else:
        fini = "th"
      print(f"{secondary} is the {i}{fini} strongest currency in the world(this also includes crypto currencies!))
