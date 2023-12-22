import requests

def get_random_joke():
    keyword = "random"
    request_url = f"https://api.chucknorris.io/jokes/{keyword}"

    try:
        response = requests.get(request_url).json()
        joke_text = response.get("value", "No joke available.")
        return joke_text
    except requests.RequestException as e:
        return f"Error: {e}"


def main():
    random_joke = get_random_joke()
    print(f"Chuck Norris Joke: {random_joke}")

main()
