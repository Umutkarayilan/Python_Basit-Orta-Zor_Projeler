import pandas as pd  # Veri analizi için kullanılır
import matplotlib.pyplot as plt  # Grafik çizmek için kullanılır

# CSV dosyasını okur
df = pd.read_csv('veriler.csv')

# Veriyi inceler
print(df.head())  # İlk 5 satırı gösterir
print(df.describe())  # İstatistiksel özet

# Belirli bir sütunu gruplandırıp toplar
grup = df.groupby('kategori')['deger'].sum()

# Sonuçları görselleştirir
grup.plot(kind='bar')
plt.title('Kategoriye Göre Değerler')
plt.xlabel('Kategori')
plt.ylabel('Toplam Değer')
plt.show()
