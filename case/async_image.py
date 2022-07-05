# 1. Get the url of each photobook from the top100 page.
# 2. Get all the pagination urls from the photobook page.
# 3. Get the url of the image from each pagination.
# 4. Download the image with the obtained url.

import requests
from lxml import etree
import asyncio
import aiohttp
import aiofiles
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


# 4. Download the image with the obtained url.
async def download_image(image_url, full_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url, headers=headers, verify_ssl=False) as response:
            image_data = await response.read()
            if response.status == 200:
                async with aiofiles.open(full_path, "wb") as f:
                    await f.write(image_data)
                    print(f"{full_path} is downloaded.")
            else:
                print(f"didn't find image {image_url}")


# 3. Get the url of the image from each pagination.
async def get_image_url(single_page_url, file_path):
    tasks = []
    home_page_url = "https://www.xiurenb.com"
    async with aiohttp.ClientSession() as session:
        async with session.get(single_page_url, headers=headers, verify_ssl=False) as response:
            page_source = await response.text(encoding="utf-8")
            tree = etree.HTML(page_source)
            image_urls = tree.xpath("//div[@class='content'][2]//@src")
            if image_urls:
                for image_url in image_urls:
                    url = image_url
                    full_path = f"{file_path}/{url.split('/')[-1]}"
                    url = home_page_url + url
                    task = asyncio.create_task(download_image(url, full_path))
                    tasks.append(task)
                await asyncio.gather(*tasks)
            else:
                print(f"didn't find image {single_page_url}")


# 2. Get all the pagination urls from the photobook page.
async def get_pagination_url(unit):
    file_path = f"image/{unit['file_name']}"
    url = unit['unit_page_url']
    home_page_url = "https://www.xiurenb.com"
    if not os.path.exists(file_path):  # Check if the file exists
        os.mkdir(file_path)  # Create the file if it doesn't exist.
    tasks = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, verify_ssl=False) as response:
            page_source = await response.text(encoding="utf-8")
            tree = etree.HTML(page_source)
            page_urls = tree.xpath("//div[@class='main']//div[@class='content'][1]//a")[1:-1]
            if page_urls:
                for page_url in page_urls:
                    page_url = page_url.xpath("./@href")[0]
                    page_url = home_page_url + page_url
                    task = asyncio.create_task(get_image_url(page_url, file_path))
                    tasks.append(task)
                await asyncio.gather(*tasks)
            else:
                print(f"didn't find page {unit['file_name'], url}")


# 1. Get the url of each photobook from the top100 page.
def get_top100_photobooks_url(main_page_url):
    page_url = main_page_url.split("/hot")[0]
    response = requests.get(main_page_url, headers=headers)
    response.encoding = "utf-8"
    main_page_source = response.text
    tree = etree.HTML(main_page_source)
    lis = tree.xpath("//li[@class='i_list list_n2']")
    url_list = []
    for li in lis:
        file_name = li.xpath(".//a/@title")[0]
        unit_page_url = li.xpath(".//a/@href")[0]
        file_name = file_name.split("]")[1]
        unit_page_url = page_url + unit_page_url
        dic = {
            "file_name": file_name,
            "unit_page_url": unit_page_url
        }
        url_list.append(dic)
    return url_list


async def main(number):
    url = "https://www.xiurenb.com/hot.html"
    top100_url = get_top100_photobooks_url(url)[:int(number)]
    tasks = []
    for unit in top100_url:
        task = asyncio.create_task(get_pagination_url(unit))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    number = input("How many pages(max 100) to grab: ")
    asyncio.run(main(number))
