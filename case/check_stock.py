import requests
import json
import time
import smtplib
import random
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# from wxauto import WeChat


def check_stock(id):
    url = "https://www.mecca.com.au/product/get"

    dic = {
        "id": id
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers, params=dic)
    data = response.json()
    brand_name = data["brandNameLabel"]
    specific_name = data["variationType"]["value"]
    product_id = data["productId"]
    availability = data["availability"]
    allowable_quantity = data["stockIndicator"]["allowableQuantity"]
    if allowable_quantity != 0:
        check = True
    else:
        check = False
    print(brand_name, specific_name, product_id, availability, allowable_quantity, check)
    result = {
        "brand_name": brand_name,
        "specific_name": specific_name,
        "product_id": product_id,
        "availability": availability,
        "allowable_quantity": allowable_quantity,
        "check": check
    }
    response.close()
    return result


def send_email(stock):
    host_server = 'smtp.gmail.com'

    sender = 'xxxxxxxxxx@gmail.com'
    pwd = "xxxxxxxxxx"

    sender_mail = 'xxxxxxxxxx@gmail.com'
    receiver = 'xxxxxxxxxx@gmail.com'

    mail_title = f"{stock['brand_name']}: {stock['specific_name']} is in stock now!"

    mail_content = f"{stock['specific_name']} currently has {stock['allowable_quantity']} in stock, hurry up!"

    try:
        msg = MIMEMultipart()
        msg['subject'] = Header(mail_title, 'utf_8')
        msg['From'] = sender_mail
        msg['To'] = Header('Susie', 'UTF-8')
        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

        stmp = SMTP_SSL(host_server)

        stmp.login(sender, pwd)
        stmp.sendmail(sender_mail, receiver, msg.as_string())
        stmp.quit()
        print('email sent successfully')
    except Exception as e:
        print('email sent failed')
        print(e)

def send_wechat():
    pass


if __name__ == '__main__':
    id_list = ["I-053325"]
    result = {}
    while True:
        for id in id_list:
            result = check_stock(id)
            if result["check"]:
                send_email(result)
                break
        if result["check"]:
            break
        time.sleep(random.randint(60, 300))
    print("done")
