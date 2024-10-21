# terminalde scrapy projesi oluşturun
# scrapy startproject ecommerce_scraper

# ecommerce_scraper/spiders/products.py
import scrapy

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ['https://www.example-ecommerce.com/products']

    def parse(self, response):
        for ürün in response.css('div.product-item'):
            yield {
                'isim': ürün.css('h2.product-title::text').get(),
                'fiyat': ürün.css('span.price::text').get(),
                'stok_durumu': ürün.css('p.stock::text').get(),
            }

        # Sonraki sayfayı takip et
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# verileri çekmek için terminalde
# scrapy crawl products -o products.csv

# veri analizi için Python betiği
import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını okur
df = pd.read_csv('products.csv')

# Fiyatları temizler ve sayısal hale getirir
df['fiyat'] = df['fiyat'].replace('[\$,]', '', regex=True).astype(float)

# Stok durumuna göre sayım yapar
stok_sayisi = df['stok_durumu'].value_counts()

# Veriyi görselleştirir
stok_sayisi.plot(kind='bar')
plt.title('Stok Durumuna Göre Ürün Sayısı')
plt.xlabel('Stok Durumu')
plt.ylabel('Ürün Sayısı')
plt.show()
