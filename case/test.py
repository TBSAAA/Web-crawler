import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

url = "https://www.xiurenb.com/XiuRen/1111111.html"

response = requests.get(url, headers=headers)
response.encoding = "utf-8"
page_source = response.text

response.close()
tree = etree.HTML(page_source)
page_urls = tree.xpath("//div[@class='main']//div[@class='content'][1]//a")[1:-1]
image_urls = tree.xpath("//div[@class='content'][2]//@src")
if page_urls:
    for page_url in page_urls:
        page_url = page_url.xpath("./@href")[0]
        print("page", page_url)
    for image_url in image_urls:
        url = image_url
        print("image", url)
else:
    print("no page")
