import requests


def get_external_ip():
    raw_data = requests.get("https://api.ipify.org/?format=json").json()  # {"ip":"12.34.56.78"}
    return raw_data["ip"]


if __name__ == "__main__":
    print(get_external_ip())