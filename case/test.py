import requests

url = "https://www.xiurenji.vip/uploadfile/202110/20/1F214426892.jpg"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}

response = requests.get(url, headers=headers)
content = response.content

file_name = url.split("/")[-1]

with open(file_name, mode="wb") as f:
    f.write(content)
    f.close()
    print(f"{file_name} downloaded.")

response.close()