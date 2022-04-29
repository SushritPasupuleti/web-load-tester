import asyncio
import requests
import aiohttp
import datetime
import sys

async def fetch(session, url):
    start_time = datetime.datetime.now()
    # print(start_time)
    async with session.get(url) as response:
        # end_time = datetime.datetime.now()
        # print("Time: ",end_time-start_time);
        await response.text()
        return {'status': response.status, 'url': response.url, 'time': start_time}

async def main():
    base_url = sys.argv[1]
    count = 10
    urls = [base_url for i in range(count)]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        for html in htmls:
            end_time = datetime.datetime.now()
            start_time = html['time']
            print("Response: ", html['status']," Took: ", end_time-start_time, "s")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())    