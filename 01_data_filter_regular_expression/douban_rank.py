import requests
import time

# Option 1: Not good, because the parameter is too long
# url = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100:90&action=&start=0&limit=20"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
# }
# requests.exceptions.JSONDecodeError: [Errno Expecting value] : 0
# this means that the server is not sending a valid JSON response
# response = requests.get(url)
# print(response.json())

# response = requests.get(url, headers=headers)
# print(response.text)

# lis = response.json()
# print(lis)


# Option 2:

for i in range(1):
    start = i * 20
    url = "https://movie.douban.com/j/chart/top_list"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    }
    dic = {
        "type": "13",
        "interval_id": "100:90",
        "action": "",
        "start": start,  # 0, 20, 40, 60, 80
        "limit": "20"
    }
    response = requests.get(url, params=dic, headers=headers)
    print(response.json())
    time.sleep(1)
