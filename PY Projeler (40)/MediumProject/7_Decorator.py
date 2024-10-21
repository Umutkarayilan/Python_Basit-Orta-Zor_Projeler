import time  # Zaman ölçümü için kullanılır

# Fonksiyon performansını ölçen dekoratör
def zamanlayici(func):
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = func(*args, **kwargs)
        bitis = time.time()
        print(f"{func.__name__} fonksiyonu {bitis - baslangic:.4f} saniye sürdü.")
        return sonuc
    return wrapper

# Dekoratör ile süslenmiş bir fonksiyon
@zamanlayici
def us_alma(a, b):
    time.sleep(1)  # 1 saniye bekler
    return a ** b

# Fonksiyonu çağırır
print(us_alma(2, 10))
