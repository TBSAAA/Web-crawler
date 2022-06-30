import re
import requests
import time

url = "https://www.3dst.cn/t/lizhigushi/"

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
main_page_source = response.text

main_obj = re.compile(r'<li class="blogs_list">.*?href="(?P<url>.*?)".*?<h2>(?P<title>.*?)</h2>', re.S)

child_obj = re.compile(r'<span>作者：(?P<author>.*?)</span>.*?时间：(?P<public_time>.*?)</span>.*?src=(?P<click>.*?)></scri', re.S)

click_obj = re.compile(r'document.write\(\'(?P<number>.*?)\'\);', re.S)

content_obj = re.compile(r'<p>(?P<content>.*?)</p>', re.S)

main_result = main_obj.finditer(main_page_source)
# print(main_page_source)
for item in main_result:
    child_url = item.group("url")
    child_tile = item.group("title")
    # print(child_tile, child_url)

    child_response = requests.get(child_url, headers= headers)
    child_response.encoding = 'utf-8'
    child_page_source = child_response.text
    # print(child_page_source)

    child_result = child_obj.search(child_page_source)
    if child_result:
        author = child_result.group("author")
        public_time = child_result.group("public_time")
        click = child_result.group("click")
        click_response = requests.get(click, headers=headers)
        click_response.encoding = 'utf-8'
        click_page_source = click_response.text
        click_result = click_obj.search(click_page_source)
        number_of_reading = click_result.group("number")

        content = []
        content_result = content_obj.finditer(child_page_source)
        for content_item in content_result:
            content.append(content_item.group("content").strip())

        # remove &ldquo;
        content = re.sub(r"&.*?;", "", "".join(content))
        # remove < >
        content = re.sub(r"<.*?>", "", content)
        # remove the ending content
        content = re.sub(r"上一篇：.*", "", content)
        # remove the beginning content
        content = re.sub(r"热门搜索/Hot Search", "", content)
        # remove the ending content
        content = re.sub(r"所有文章杂志更新", "", content)
        print(child_tile, author, public_time, number_of_reading)
        print(content)
    else:
        print("No result")
    break
    # time.sleep(2)
