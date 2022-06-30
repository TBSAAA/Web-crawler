import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Larus_canus_Common_Gull_in_Norway.jpg/220px-Larus_canus_Common_Gull_in_Norway.jpg"

response = requests.get(url)

content = response.content

# save the file
with open("../image/download_file.jpg", mode="wb") as f:
    f.write(content)
    f.close()
