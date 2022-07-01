# Run the program at any time to automatically obtain the latest information.

import requests
import time
import csv
from datetime import datetime, timedelta

# Get the time of the day as the query time. If there is no data on
# the day, the query will go back one day, up to 5 days back.
currentDateAndTime = datetime.now()
currentDateAndTime = currentDateAndTime.strftime("%Y/%m/%d")
flag = 1


while True:
    url = "http://www.xinfadi.com.cn/getPriceData.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    }

    dic = {
        "limit": "20",
        "current": "1",
        "pubDateStartTime": currentDateAndTime,
    }
    response = requests.post(url, headers=headers, data=dic)
    response_json = response.json()
    if response_json["list"] == []:
        currentDateAndTime = datetime.now() + timedelta(days=-flag)
        currentDateAndTime = currentDateAndTime.strftime("%Y/%m/%d")
        flag += 1

    if flag == 6 or response_json["list"] != []:
        break

    time.sleep(2)

print(f"Start getting the latest data for {currentDateAndTime}.")

with open("csv/xinfadi.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["primary_classification", "Secondary_classification", "product_name", "product_low_price",
                     "product_average_price", "product_high_price", "special_info", "place_of_origin", "unit_info",
                     "public_time"])
    # When the number of pagination is calculated, the content is crawled page by page.
    number_of_pagination = int(int(response_json["count"])/20+1)
    for j in range(number_of_pagination):

        url = "http://www.xinfadi.com.cn/getPriceData.html"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
        }

        dic = {
            "limit": "20",
            "current": j+1,
            "pubDateStartTime": currentDateAndTime,
        }
        response = requests.post(url, headers=headers, data=dic)
        response_json = response.json()
        # Get all product information on the current page.
        for i in range(int(response_json["limit"])):
            primary_classification = response_json["list"][i]["prodCat"]
            Secondary_classification = response_json["list"][i]["prodPcat"]
            product_name = response_json["list"][i]["prodName"]
            product_low_price = response_json["list"][i]["lowPrice"]
            product_average_price = response_json["list"][i]["avgPrice"]
            product_high_price = response_json["list"][i]["highPrice"]
            special_info = response_json["list"][i]["specInfo"]
            place_of_origin = response_json["list"][i]["place"]
            unit_info = response_json["list"][i]["unitInfo"]
            public_time = response_json["list"][i]["pubDate"]
            public_time = public_time.split(" ")[0]

            writer.writerow(
                [primary_classification, Secondary_classification, product_name, product_low_price, product_average_price,
                 product_high_price, special_info, place_of_origin, unit_info, public_time])

        time.sleep(2)
        print(f"Current progress: {j+1}/{number_of_pagination}")
