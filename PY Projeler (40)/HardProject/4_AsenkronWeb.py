#Proje Açıklaması: aiohttp ve asyncio kullanarak aynı anda birden fazla web sitesine istek gönderin ve yanıt sürelerini ölçün.




import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        await response.text()
        return response.status

async def main():
    urls = [
        'https://www.python.org',
        'https://www.github.com',
        'https://www.stackoverflow.com',
        'https://www.google.com',
        'https://www.microsoft.com'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        start_time = time.time()
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        end_time = time.time()

        for url, status in zip(urls, responses):
            print(f"{url} returned status {status}")

        print(f"Toplam süre: {end_time - start_time:.2f} saniye")

# Programı çalıştırır
if __name__ == '__main__':
    asyncio.run(main())







# aiohttp ve asyncio kullanılarak asenkron HTTP istekleri yapılır.
# async/await sözdizimi ile asenkron fonksiyonlar tanımlanır.
# asyncio.gather ile birden fazla görevi aynı anda çalıştırır.
# Performans ölçümü için zaman hesaplaması yapılır.
