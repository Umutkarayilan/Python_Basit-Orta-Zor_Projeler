import asyncio  # Asenkron programlama için kullanılır
import aiohttp  # Asenkron HTTP istekleri için kullanılır

# Asenkron bir fonksiyon ile web sayfasından veri çeker
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# Ana asenkron fonksiyon
async def main():
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.github.com'
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]  # Görev listesi oluşturur
        contents = await asyncio.gather(*tasks)  # Tüm görevleri paralel olarak çalıştırır
        
        for url, content in zip(urls, contents):
            print(f"{url} sayfası {len(content)} karakter içeriyor.")

# Programı çalıştırır
asyncio.run(main())
