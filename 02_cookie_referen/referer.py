import requests
from bs4 import BeautifulSoup


url = 'https://www.pearvideo.com/video_1765875'
headers = {
    "Referer": url,
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
}
main_page_response = requests.get(url, headers=headers)
main_page_source = main_page_response.text
main_page_bs4 = BeautifulSoup(main_page_source, "html.parser")
main_page_response.close()
video_name = main_page_bs4.find("h1", class_="video-tt").text

video_id = url.split("_")[-1]
video_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={video_id}"
response = requests.get(video_url, headers=headers)
dic = response.json()
response.close()
# fake   https://video.pearvideo.com/mp4/adshort/20220621/1656767251353-15898547_adpkg-ad_hd.mp4
fake_url = dic["videoInfo"]["videos"]["srcUrl"]

# really https://video.pearvideo.com/mp4/adshort/20220621/cont-1765875-15898547_adpkg-ad_hd.mp4
really_url = fake_url.replace(dic["systemTime"], f"cont-{video_id}")

video_response = requests.get(really_url, headers=headers)
with open(f"video/{video_name}.mp4", "wb") as f:
    f.write(video_response.content)
print(f"Download {video_name} successful.")
video_response.close()