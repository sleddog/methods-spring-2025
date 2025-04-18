import requests

response = requests.get("http://127.0.0.1:5000/api/fizzbuzz", params={"number": 15})

if response.status_code == 200:
    data = response.json()
    print("Input:", data["input"])
    print("Result:", data["result"])
else:
    print("Error:", response.status_code)