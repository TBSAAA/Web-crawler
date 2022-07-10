import requests
from lxml import etree
import pymongo

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_page_source(url):
    response = requests.get(url, headers=headers)
    return response.text


def parse_data(page_source):
    all_info = []
    tree = etree.HTML(page_source)
    li_list = tree.xpath('//*[@class="sellListContent"]/li')
    for li in li_list:
        title = li.xpath('.//*[@class="title"]/a/text()')
        if not title:
            continue
        title = title[0]
        position = li.xpath('.//*[@class="positionInfo"]//text()')
        position = ''.join(position).strip().replace(' ', '')
        house_info = li.xpath('.//*[@class="houseInfo"]//text()')
        house_info = house_info[0].replace(' ', '').split('|')
        house_total_price = li.xpath('.//*[@class="priceInfo"]/div[1]//text()')
        house_total_price = "".join(house_total_price).strip()
        house_price_per_square = li.xpath('.//*[@class="priceInfo"]/div[2]//text()')
        house_price_per_square = house_price_per_square[0]
        per_info = {
            'title': title,
            'position': position,
            'house_info': house_info,
            'house_total_price': house_total_price,
            'house_price_per_square': house_price_per_square
        }
        all_info.append(per_info)
    return all_info


def save_data_to_mongo(all_info):
    connection = pymongo.MongoClient(host='localhost', port=27017)
    db = connection['crawler_spider']
    db.lianjia.insert_many(all_info)
    print('save data to mongo success')


def main():
    url = 'https://cd.lianjia.com/ershoufang/'
    page_source = get_page_source(url)
    data = parse_data(page_source)
    save_data_to_mongo(data)


if __name__ == '__main__':
    main()
