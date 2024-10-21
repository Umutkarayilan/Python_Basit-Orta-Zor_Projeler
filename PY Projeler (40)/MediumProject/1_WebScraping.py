import requests  # HTTP istekleri yapmak için kullanılır
from bs4 import BeautifulSoup  # HTML parsing işlemleri için kullanılır

# Hedef web sayfasının URL'si
url = "https://www.realmadrid.com/en-US/news/football/first-team/latest-news/turquia-islandia-09-09-2024"

# Web sayfasına GET isteği gönderir
response = requests.get(url)

# İstek başarılı ise devam eder
if response.status_code == 200:
    # HTML içeriğini BeautifulSoup ile parse eder
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Haber başlıklarını seçmek için uygun HTML etiketini bulur
    basliklar = soup.find_all('h1', class_='news-detail__title')
    
    # Her başlığı ekrana yazdırır
    for baslik in basliklar:
        print(baslik.get_text())
    else:
        print("Web sayfasına erişilemedi.")
