import requests
from requests.exceptions import RequestException

IP = "http://movie.jd.com/3702"

print(IP)

def one(IP):
    try:
        result = requests.get(IP)
        if result.status_code == 200:
            print(result)
            return result
        return None
    except RequestException:
        print("NO")


def two(result):
    print(result.text)

two(one(IP))