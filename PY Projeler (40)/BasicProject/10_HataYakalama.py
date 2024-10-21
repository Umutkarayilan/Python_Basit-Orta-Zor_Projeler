try:
    # Kullanıcıdan sayı alır
    sayi = int(input("Bir sayı girin: "))
    # Sayıyı 10 ile böler
    sonuc = 10 / sayi
    print(f"10 / {sayi} = {sonuc}")
except ValueError:
    # Kullanıcı geçerli bir sayı girmezse
    print("Geçersiz giriş! Lütfen bir sayı girin.")
except ZeroDivisionError:
    # Kullanıcı sıfır girerse
    print("Bir sayıyı sıfıra bölemezsiniz.")
finally:
    # Her durumda çalışacak kod
    print("Program sona erdi.")
