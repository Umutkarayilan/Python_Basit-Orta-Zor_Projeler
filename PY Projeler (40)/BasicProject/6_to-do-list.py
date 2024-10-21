# Yapılacaklar listesini başlatır
todo_list = []

while True:
    # Kullanıcıdan seçenek alır
    secim = input("1. Ekle\n2. Listele\n3. Çıkış\nSeçiminiz: ")
    
    if secim == '1':
        # Listeye yeni bir görev ekler
        gorev = input("Eklemek istediğiniz görevi yazın: ")
        todo_list.append(gorev)
        print("Görev eklendi.")
    elif secim == '2':
        # Listeyi ekrana yazdırır
        print("Yapılacaklar Listesi:")
        for index, gorev in enumerate(todo_list, start=1):
            print(f"{index}. {gorev}")
    elif secim == '3':
        # Programdan çıkar
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
