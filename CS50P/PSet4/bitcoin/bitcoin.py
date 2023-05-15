import requests
import sys


def main():
    if len(sys.argv) == 2:
        try:
            num = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

        price = getPrice(num)
        print(f"${price}")
    else:
        sys.exit("Missing command-line argument")


def getPrice(num):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        jsonOfResponse = response.json()
        priceOne = jsonOfResponse["bpi"]["USD"]["rate_float"]
        return f"{num*priceOne:,.4f}"
    except requests.RequestException:
        return None


if __name__ == "__main__":
    main()
