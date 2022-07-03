import requests
from lxml import etree
import csv
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}


def get_page_data(shearch_year, file):
    print(f"{shearch_year} start")
    url = f"https://www.boxofficemojo.com/year/world/{shearch_year}/"
    response = requests.get(url, headers=headers)
    page = etree.HTML(response.text)
    response.close()
    trs = page.xpath("//table/tr")[1:]
    # with open(f"csv/boxofficemojo/movie_data_{shearch_year}", "w") as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(["movie_name", "world_box_office", "domestic_box_office",
    #                      "domestic_percentage", "foreign_box_office", "foreign_percentage"])
    for tr in trs:
        movie_name = tr.xpath("./td/a/text()")
        world_box_office = tr.xpath("./td[3]/text()")
        domestic_box_office = tr.xpath("./td[4]/text()")
        domestic_percentage = tr.xpath("./td[5]/text()")
        foreign_box_office = tr.xpath("./td[6]/text()")
        foreign_percentage = tr.xpath("./td[7]/text()")
        file.writerow([shearch_year, movie_name[0], world_box_office[0], domestic_box_office[0],
                       domestic_percentage[0], foreign_box_office[0], foreign_percentage[0]])
    print(f"{shearch_year} end")


if __name__ == '__main__':
    with open(f"csv/worldwide_movie_rank.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["year", "movie_name", "world_box_office", "domestic_box_office",
                         "domestic_percentage", "foreign_box_office", "foreign_percentage"])
        # create a thread pool
        with ThreadPoolExecutor(16) as executor:
            for year in range(2000, 2023):
                executor.submit(get_page_data, year, writer)
