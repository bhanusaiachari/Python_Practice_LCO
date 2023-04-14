import requests as rq
import json


def getData(url):
    try:
        # jsb=rq.get(url).text
        # print(jsb)
        # print(json.dumps(jsb))
        return rq.get(url).text
    except Exception as e:
        print("unable to load url")


def load_json(data):
    if not data is None:
        j = json.loads(data)
        fname = j["results"][0]["name"]["first"]
        lname = j["results"][0]["name"]["last"]
        email = j["results"][0]["email"]

        return fname, lname,email


def main():
    url = "https://randomuser.me/api"
    values = load_json(getData(url))
    if not values is None:
        print("FirstName:", values[0])
        print("LastName:", values[1])
        print("Email:",values[2])
# if __name__ == '__main__': main()

main()
