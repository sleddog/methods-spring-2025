import requests
import json
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num_jokes", help="number of jokes to print", type=int)
args = parser.parse_args()
print(args)
num_jokes = args.num_jokes
print(num_jokes)

url = "https://icanhazdadjoke.com/search"
response = requests.get(url, headers={"Accept": "application/json"})
data = response.json()

jokes = data["results"]
for joke in jokes:
    if num_jokes <= 0:
        break
    print(joke["joke"])
    num_jokes = num_jokes - 1
