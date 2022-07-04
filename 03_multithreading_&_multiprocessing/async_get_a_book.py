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


async def download_chapter(chapter_url, file_path):
    async with aiohttp.ClientSession() as session:
        async with session.get(chapter_url, headers=headers, verify_ssl=False) as response:
            page_source = await response.text(encoding="utf-8")
            tree = etree.HTML(page_source)
            content = tree.xpath("//div[@class='content']/p/text()")[:-3]
            content = "\n".join(content).replace("　", "").replace("\r", "").replace(" ", "").strip()

            async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
                await f.write(content)



async def prepare_download(info):
    tasks = []
    for section in info:
        section_name = f"novel/{section['section']}"
        if not os.path.exists(section_name):  # Check if the file exists
            os.mkdir(section_name)  # Create the file if it doesn't exist.
        for chapter in section['chapters']:
            title = chapter['title']
            url = chapter['url']
            file_path = f"{section_name}/{title}.txt"
            task = asyncio.create_task(download_chapter(url, file_path))
            tasks.append(task)
    await asyncio.gather(*tasks)


def get_chapter_info(chapter_url):
    response = requests.get(chapter_url, headers=headers)
    response.encoding = "utf-8"
    page_source = response.text
    tree = etree.HTML(page_source)
    divs = tree.xpath("//div[@class='mulu']")
    all_info = []
    for div in divs:
        part = {}
        trs = div.xpath(".//table/tr")
        chapter_name = trs[0].xpath(".//a/text()")[0]
        chapter_name = chapter_name.replace("：", ":")
        delete_chapter = chapter_name.split(":")[1]
        chapters = []
        for tr in trs[1:]:
            tds = tr.xpath("./td/a")
            for td in tds:
                titles = td.xpath("./text()")[0]
                urls = td.xpath("./@href")[0]
                titles = titles.replace(delete_chapter, "").replace("，", ",").strip()
                chapters_info = {
                    "title": titles,
                    "url": urls
                }
                chapters.append(chapters_info)
        part['section'] = chapter_name
        part['chapters'] = chapters
        all_info.append(part)
    return all_info


def main():
    url = "https://www.mingchaonaxieshier.com/"
    all_info = get_chapter_info(url)
    asyncio.run(prepare_download(all_info))


if __name__ == '__main__':
    main()
