from lxml import etree

# 准备一段html
f = open("test.html", mode="r", encoding="utf-8")
content = f.read()  # 页面源代码  # type: xxxxxx

# 1.      etree.HTML(页面源代码) BeautfulSoup(页面源代码)
page = etree.HTML(content)

list_content = page.xpath('//div[@class="list-content"]/div')
with open("wft.txt", mode="w", encoding="utf-8") as f:
    for item in list_content:
        content = item.xpath('.//div[@class="title"]/text()')[0].strip().replace("\n", "").replace("   ", "")
        tag = item.xpath('.//div[@class="detail-list-left"]/span[1]/text()')[0].strip()
        if tag == "极高频":
            f.write(content + "     " + tag + "\n")
            print(content, tag)
