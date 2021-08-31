import requests

api_endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en/"

# https://dictionaryapi.dev/


async def dict(message, client):
    search_word = message.content.replace("$dict ", "")

    try:
        if " " in search_word:
            raise KeyError
        response = requests.get(url=f"{api_endpoint}{search_word}")
        response.raise_for_status()
        word = response.json()[0]["word"]
        response_str = f"__Dictionary__\n**{word}**"

        for meaning in response.json()[0]["meanings"]:
            part_of_speech = meaning["partOfSpeech"]
            definition = meaning["definitions"][0]["definition"]
            try:
                example = meaning["definitions"][0]["example"]
                response_str += f"\n\n*{part_of_speech}*\n{definition}\n'{example}'"
            except: # need to check which error to capture
                response_str += f"\n\n*{part_of_speech}*\n{definition}"

        await message.channel.send(response_str)

    except (IndexError, ValueError, KeyError):
        await message.channel.send(f"`$dict [word to search]`")

    except requests.exceptions.HTTPError: #undone messy error exception capture due to 5min code
        await message.channel.send(f"Error\nWIP Function, let owner know the word u searched so can debug it.")
