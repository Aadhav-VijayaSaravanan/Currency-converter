import api  # Import your own API module if needed

def main(data):
    inputi = input(
        "\033[1mCurrency Conversion\033[0m\nEnter the currency you want to convert: "
    ).upper().split()
    primary = inputi[1]
    secondary = inputi[3]

    if inputi[0].isnumeric():
        if isinstance(float(inputi[0]), float) or isinstance(int(inputi[0]), int):
            quantity = float(inputi[0])
        else:
            print("Trying to do something? Input only numeric digits, not in alphabetical form.

    if primary in data["rates"] and secondary in data["rates"]:
        primary_rate = data["rates"][primary]
        secondary_rate = data["rates"][secondary]
        conversion_rate = quantity * (secondary_rate / primary_rate)
        print(f"The conversion rate for {primary} is {conversion_rate:.2f}")
    else:
        print("Your currency isn't valid, please try again!")

    rates_sorted = sorted(data["rates"].items(), key=lambda x: x[1], reverse=False)
    for i, rate in enumerate(rates_sorted):
        currency, rate_value = rate
        if secondary == currency:
            ordinal_indicator = "th" if 11 <= i + 1 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get((i + 1) % 10, "th")
            print(f"{secondary} is the {i + 1}{ordinal_indicator} strongest currency in the world (including cryptocurrencies).")
            break

if __name__ == "__main__":
    main(api.data)
