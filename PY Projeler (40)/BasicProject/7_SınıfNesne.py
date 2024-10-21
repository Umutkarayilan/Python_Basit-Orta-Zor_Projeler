# 'Araba' adında bir sınıf tanımlar
class Araba:
    # Sınıfın yapıcı metodu
    def __init__(self, marka, model, yil):
        self.marka = marka  # Marka özelliği
        self.model = model  # Model özelliği
        self.yil = yil      # Yıl özelliği

    # Araba bilgilerini ekrana yazdıran metot
    def bilgileri_goster(self):
        print(f"{self.yil} {self.marka} {self.model}")

# 'Araba' sınıfından bir nesne oluşturur
araba1 = Araba("Toyota", "Corolla", 2020)

# Nesnenin bilgilerini gösterir
araba1.bilgileri_goster()
