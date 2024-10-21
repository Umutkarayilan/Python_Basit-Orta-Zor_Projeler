# Dosyaya yazmak istediğiniz metni alır
metin = input("Dosyaya yazmak istediğiniz metni girin: ")

# 'ornek.txt' dosyasını yazma modunda açar ve metni yazar
with open("ornek.txt", "w") as dosya:
    dosya.write(metin)
    print("Metin dosyaya yazıldı.")

# Dosyayı okuma modunda açar ve içeriği okur
with open("ornek.txt", "r") as dosya:
    icerik = dosya.read()
    print("Dosya İçeriği:")
    print(icerik)
