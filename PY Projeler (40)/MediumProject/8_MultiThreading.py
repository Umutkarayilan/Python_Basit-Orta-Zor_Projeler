import threading  # İş parçacıkları için kullanılır
import time

# İş parçacığında çalışacak fonksiyon
def sayi_say(sayi):
    for i in range(1, sayi + 1):
        print(f"Sayı: {i}")
        time.sleep(0.5)

# İki iş parçacığı oluşturur
thread1 = threading.Thread(target=sayi_say, args=(5,))
thread2 = threading.Thread(target=sayi_say, args=(3,))

# İş parçacıklarını başlatır
thread1.start()
thread2.start()

# İş parçacıklarının bitmesini bekler
thread1.join()
thread2.join()

print("İşlem tamamlandı.")
