import requests


def get_jokes():
    # endpoint = "https://official-joke-api.appspot.com/jokes"
    endpoint = "https://karljoke.herokuapp.com/jokes"
    joke_type = "general"
    # joke_type = "programming"
    joke_qty = "ten"
    # joke_qty = "random"

    url = '/'.join([endpoint, joke_type, joke_qty])
    print(url)
    jokes = requests.get(url).json()
    print(jokes)
    return jokes


if __name__ == "__main__":
    for joke in get_jokes():
        print(joke["setup"], joke["punchline"])
