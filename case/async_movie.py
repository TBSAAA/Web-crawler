import requests
from lxml import etree
import re
import asyncio
import aiohttp
import aiofiles
import os
from urllib.parse import urljoin
from Crypto.Cipher import AES

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


# merge the all movie clip
def merge_movie_clip():
    # windows command: copy /b a.ts+b.ts c.ts "movie.mp4"
    # macOS/linux command: cat a.ts b.ts c.ts > movie.mp4

    # Merge in order
    file_list = []
    with open("second_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()
                file_name = line.split("/")[-1]
                file_list.append(file_name)

    # switch directory to after_decryption
    os.chdir("after_decryption")
    # segment merge
    n = 1
    temp = []
    for i in range(len(file_list)):
        # Every 20 merges
        file_name = file_list[i]
        temp.append(file_name)
        if i % 20 == 0 and i != 0:
            command = f"cat {' '.join(temp)} > {n}.ts"
            os.system(command)
            print(f"{n}.ts is finished.")
            temp = []
            n += 1
    # merge the last part
    command = f"cat {' '.join(temp)} > {n}.ts"
    os.system(command)
    temp = []
    n += 1

    # The second merger
    for i in range(1, n):
        temp.append(f"{i}.ts")
    # merge the all part
    command = f"cat {' '.join(temp)} > 春夏秋冬又一春.mp4"
    os.system(command)


# decrypt the clip of movie
async def decrypt_clip(file_path, key):
    file_name = file_path.split("/")[-1]
    new_file_path = f"after_decryption/{file_name}"
    async with aiofiles.open(file_path, "rb") as f, aiofiles.open(new_file_path, "wb") as f2:
        content = await f.read()
        # create a decryptor
        decryptor = AES.new(key, AES.MODE_CBC, b'\x00' * 16)
        # decrypt
        decrypted = decryptor.decrypt(content)
        # write to file
        await f2.write(decrypted)
        print("decrypt:", file_name, "is finished.")


# decrypt all movie
async def decrypt(key):
    tasks = []
    with open("second_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()
                file_name = line.split("/")[-1]
                file_path = f"before_decryption/{file_name}"
                # create task to decrypt
                task = asyncio.create_task(decrypt_clip(file_path, key))
                tasks.append(task)
    await asyncio.gather(*tasks)


def get_key():
    with open("second_m3u8.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
        obj = re.compile(r'URI="(?P<key_url>.*?)"', re.S)
        key_url = obj.search(file_content).group('key_url')
        response = requests.get(key_url, headers=headers)
        return response.content


async def download_movie_clip(url, sem):
    async with sem:
        file_name = url.split("/")[-1]
        file_path = f"before_decryption/{file_name}"
        print("start download:", file_name)
        flag = True
        for i in range(10):
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, verify_ssl=False) as response:
                        content = await response.read()
                        async with aiofiles.open(file_path, "wb") as f:
                            await f.write(content)
                print("download:", file_name, "is finished.")
                flag = False
                break
            except Exception as e:
                print(file_name, "is failed.", e)
                continue
        if flag:
            with open("failed_list.txt", "a", encoding="utf-8") as f:
                f.write(url + "\n")


# download all movie
async def download_movie():
    # control the number of tasks
    sem = asyncio.Semaphore(100)
    tasks = []
    with open("second_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()
                # create task
                task = asyncio.create_task(download_movie_clip(line, sem))
                tasks.append(task)
    await asyncio.gather(*tasks)


# download m3u8 file
def download_m3u8(url):
    response = requests.get(url, headers=headers)
    with open("first_m3u8.txt", "w", encoding="utf-8") as f:
        f.write(response.text)
        print("first m3u8 file is downloaded.")
        response.close()
    with open("first_m3u8.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("#"):
                continue
            else:
                line = line.strip()

            # download second m3u8 file
            line = urljoin(url, line)
            response = requests.get(line, headers=headers)
            with open("second_m3u8.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
                print("second m3u8 file is downloaded.")
                response.close()
                break


# get m3u8_url
def get_m3u8_url(url):
    response = requests.get(url, headers=headers)
    obj = re.compile(r'url: "(?P<m3u8>.*?)"', re.S)
    m3u8 = obj.search(response.text).group('m3u8')
    return m3u8


# get the iframe url
def get_ifram_url(url):
    for i in range(10):
        try:
            response = requests.get(url, headers=headers)
            tree = etree.HTML(response.text)
            src = tree.xpath("//iframe/@src")[0]
            return src
        except Exception as e:
            print(e)


def main():
    # url = "http://www.wbdy.tv/play/63690_1_1.html"
    # # get iframe url
    # iframe_url = get_ifram_url(url)
    # iframe_url = urljoin(url, iframe_url)
    # # Get the url of m3u8 through iframe url
    # m3u8 = get_m3u8_url(iframe_url)
    # # download m3u8 file
    # download_m3u8(m3u8)
    # # Download movies via m3u8
    # asyncio.run(download_movie())
    # Get decrypted key
    # key = get_key()
    # Decrypt
    # asyncio.run(decrypt(key))
    # merge the clip
    merge_movie_clip()


if __name__ == '__main__':
    main()
