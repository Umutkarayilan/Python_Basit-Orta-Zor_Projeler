# Kullanıcıdan iki sayı alır
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Kullanıcıdan işlem türünü seçmesini ister
islem = input("Toplama için '+', çıkarma için '-', çarpma için '*', bölme için '/' girin: ")

# Seçilen işleme göre sonucu hesaplar ve ekrana yazdırır
if islem == '+':
    print("Sonuç:", sayi1 + sayi2)
elif islem == '-':
    print("Sonuç:", sayi1 - sayi2)
elif islem == '*':
    print("Sonuç:", sayi1 * sayi2)
elif islem == '/':
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Bir sayıyı sıfıra bölemezsiniz.")
else:
    print("Geçersiz işlem.")
