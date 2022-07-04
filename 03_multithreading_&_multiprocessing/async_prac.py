import asyncio
import aiohttp  # =>requests
import aiofiles  # =>open

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
}


async def download(url):
    file_name = url.split("/")[-1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, verify_ssl=False) as resp:
            # page source
            # page_source = await resp.text(encoding="utf-8")
            # if need json
            # dic = await resp.json()
            content = await resp.content.read()
            async with aiofiles.open(file_name, "wb") as f:
                await f.write(content)
                print(f"{file_name} downloaded.")


async def main():
    urls = [
        "https://www.xiurenji.vip/uploadfile/202110/20/1F214426892.jpg",
        "https://www.xiurenji.vip/uploadfile/202110/20/91214426753.jpg"
    ]
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(download(url)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main())
    event_loop.close()
