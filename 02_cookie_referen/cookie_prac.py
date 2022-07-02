import requests

url = 'https://passport.17k.com/ck/user/login'

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
}
data = {
    "loginName": "16538989670",
    "password": "q6035945",
}

response = requests.post(url, headers=headers, data=data)
cookie = response.cookies  # requestscookieJar

# bookshelf
bookshelf_url = "https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919"
response_bookshelf = requests.get(bookshelf_url, cookies=cookie, headers=headers)
print(response_bookshelf.text)
