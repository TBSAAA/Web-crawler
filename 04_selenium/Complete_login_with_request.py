import time
import requests
import base64
import json

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


# third-party api
def base64_api(uname, pwd, img, typeid):
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": img}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]


# get a raw cookie
session.get("http://www.ttshitu.com/login.html", headers=headers)

# send response, get a code
verify_url = "http://admin.ttshitu.com/captcha_v2?_=1650111626736"
verify_response = session.get(verify_url, headers=headers)
image = verify_response.json()["img"]
image_ID = verify_response.json()["imgId"]

# Identify verification code
verify_code = base64_api("q6035945", "q6035945", image, 1)
username = "q6035945"
password = "q6035945"

# login
login_url = "http://admin.ttshitu.com/common/api/login/user"
data = {
    "captcha": verify_code,
    "developerFlag": False,
    "imgId": image_ID,
    "needCheck": True,
    "password": password,
    "userName": username,
}
login_response = session.post(login_url, json=data, headers=headers)
print(login_response.text)
