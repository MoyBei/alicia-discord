import requests
from pathlib import Path

API_LINK = "https://free.currconv.com/api/v7/convert"
api_file = Path(__file__).parent / "forex_API_KEY.txt"
API_KEY = Path(api_file).read_text().strip()

# Documentation link: https://www.currencyconverterapi.com/docs


def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)


async def forex(message, client):
    # $forex 250 SGD MYR
    message_content = message.content
    # default convert value = 1
    if not has_numbers(message_content):
        message_content = message_content.replace(" ", " 1 ", 1)
    # make the command of "$forex 250 sgd to myr" work
    split_message = message_content.replace("to ", "").split(" ")

    try:
        amount_to_exchange = float(split_message[1])
        currency_from = split_message[2]
        currency_to = split_message[3]
        # make api request
        query = f"{currency_from.upper()}_{currency_to.upper()}"
        parameters = {
            "q": query,
            "compact": "ultra",
            "apiKey": API_KEY
        }

        response = requests.get(url=API_LINK, params=parameters)
        response.raise_for_status()
        exchange_rate = response.json()[query]
        result = amount_to_exchange * exchange_rate

        await message.channel.send(f"Currency Exchange: {amount_to_exchange:.2f} {currency_from.upper()} "
                                   f"-> {result:.2f} {currency_to.upper()}")

    except (IndexError, ValueError, KeyError):
        await message.channel.send("`$forex [amount] [fromCurrency] to [toCurrency]`\n"
                                   "[amount] and 'to' is optional, default amount: 1")

    except requests.exceptions.HTTPError:
        await message.channel.send("Sorry Server DOWN ><")
