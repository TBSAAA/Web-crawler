from bs4 import BeautifulSoup
import requests
import time
# Import the library for address splicing.
from urllib.parse import urljoin

url = "https://desk.zol.com.cn/meinv/changtuimeinv/"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}


def get_bs4_object(page_url):
    print(f"Start getting the data from {page_url}.")
    response = requests.get(page_url, headers=headers)
    response.encoding = "gb2312"
    page_source = response.text
    # Parse the page source code to get the href value in the a tag.
    bs4_object = BeautifulSoup(page_source, "html.parser")
    time.sleep(1)
    return bs4_object

if __name__ == "__main__":
    main_page = get_bs4_object(url)
    # get ul tag from bs
    ul_list = main_page.find("ul", class_="pic-list2").find_all("a")
    for ul in ul_list:
        href = ul.get("href")
        if href.endswith(".exe"):
            continue

        # href = /bizhi/9099_111480_2.html
        href = urljoin(url, href)
        child_page = get_bs4_object(href)
        image_ul_list = child_page.find("ul", id="showImg").find_all("a")
        for image_ul in image_ul_list:
            image_ul_href = image_ul.get("href")
            image_ul_href = urljoin(url, image_ul_href)
            image_page = get_bs4_object(image_ul_href)
            img_src = image_page.find("img", id="bigImg").get("src")
            # get 1920x1080 image
            img_1080 = image_page.find("a", id="1920x1080").get("href")
            img_1080 = urljoin(url, img_1080)
            image_page_1080 = get_bs4_object(img_1080)
            img_1080_src = image_page_1080.find("img").get("src")
            # download the image
            img_response = requests.get(img_1080_src, headers=headers)
            time.sleep(1)
            print(f"Downloading the image {img_1080_src}.")
            file_name = img_1080_src.split("/")[-1]
            with open(f"image/{file_name}", "wb") as f:
                f.write(img_response.content)

