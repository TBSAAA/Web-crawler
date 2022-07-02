from lxml import etree
import time
import requests
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}


def get_page_data(writer, shearch_year):
    url = f"http://www.boxofficecn.com/boxoffice{shearch_year}"
    response = requests.get(url, headers=headers)
    page = etree.HTML(response.text)
    trs = page.xpath("//table/tbody/tr")[1:-1]
    for tr in trs:
        number = tr.xpath("./td[1]/text()")
        year = tr.xpath("./td[2]//text()")
        if not year:
            continue
        movie_name = tr.xpath("./td[3]//text()")
        if movie_name:
            movie_name = "".join(movie_name)
        box_office = tr.xpath("./td[4]/text()")
        if box_office:
            box_office = box_office[0].split("（")[0]
        writer.writerow([number[0], year[0], movie_name, box_office])
        response.close()


if __name__ == "__main__":
    with open("data/China_move_rank.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["number", "year", "movie_name", "box_office"])
        for year in range(2000, 2023):
            get_page_data(writer, year)
            time.sleep(1)
            print(f"{year} done")
            # break # Only crawl data for one year
