
# BobcatBuzz API

This API runs the **BobcatBuzz** algorithm, where:
- For numbers divisible by 3: "Bob"
- For numbers divisible by 5: "Cat"
- For numbers divisible by both 3 and 5: "BobCat"
- Otherwise, returns the number itself.

This can be ran with curl or through a browser

I attempted to use Docker and Kubernetes but got an error that I wasn't able to fix. Not sure why it didn't work. 

#### Example curl Request
```bash
curl -X POST http://127.0.0.1:5000/api/bobcatbuzz -H "Content-Type: application/json" -d '{"n": 15}'
```

#### Response
```json
{
  "result": [
    1,
    2,
    "Bob",
    4,
    "Cat",
    "Bob",
    7,
    8,
    "Bob",
    "Cat",
    11,
    "Bob",
    13,
    14,
    "BobCat"
  ]
}
```
---

#### Example Browser Request

```
http://127.0.0.1:5000/api/bobcatbuzz?n=17
```

#### Response
```json
{
  "result": [
    1,
    2,
    "Bob",
    4,
    "Cat",
    "Bob",
    7,
    8,
    "Bob",
    "Cat",
    11,
    "Bob",
    13,
    14,
    "BobCat",
    16,
    17
  ]
}
```

---

## Running the API

1. Install Flask:
   ```bash
   pip install flask
   ```

2. Run the server:
   ```bash
   python app.py
   ```
---
## Running Examples
#### Browser
![Screenshot 2025-04-29 at 23.44.34.png](Screenshot%202025-04-29%20at%2023.44.34.png)
#### Terminal
![Screenshot 2025-04-29 at 23.43.43.png](Screenshot%202025-04-29%20at%2023.43.43.png)
---
