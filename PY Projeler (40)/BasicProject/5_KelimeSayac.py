# Kullanıcıdan bir metin alır
metin = input("Bir metin girin: ")

# Metni kelimelere böler
kelimeler = metin.split()

# Kelime sayısını hesaplar
kelime_sayisi = len(kelimeler)

# Sonucu ekrana yazdırır
print(f"Metindeki kelime sayısı: {kelime_sayisi}")
