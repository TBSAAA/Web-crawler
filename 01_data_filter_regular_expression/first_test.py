import requests

url = 'https://www.sogou.com/web?query=%E5%94%90%E5%B1%B1%E6%89%93%E4%BA%BA'

urlFlash = 'http://23.106.147.168/'

# dic = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }

# response = requests.get(url, headers=dic)
response = requests.get(urlFlash)
# print(response)  # <Response [200]>
print(response.text)

