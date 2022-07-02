import requests

# url = 'https://www.xiurenb.com/hot.html'
url = 'http://www.baidu.com/s?ie=utf-8&wd=ip'
headers = {
    "Referer": url,
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
}

proxy = {
    "http": "http://221.237.209.148:9091",
    # "https": "https://221.237.209.148:9091",
}

response = requests.get(url, headers=headers, proxies=proxy)
response.encoding = "utf-8"
print(response.text)
response.close()
