import requests
import json

url = "https://fanyi.baidu.com/sug"

# prepare data
data = {
    "kw": "Susie"
}

# From Data => data
resp = requests.post(url, data=data)
# print(resp.text)  # this is a json string

# dic = json.loads(resp.text) # method 1

# The premise is that the server must return a Json string.
dic = resp.json()  # method 2
print(dic)
