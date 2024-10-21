import unittest  # Test framework'ü
from math import sqrt

# Test edilecek fonksiyon
def karekok_al(x):
    if x < 0:
        raise ValueError("Negatif sayının karekökü alınamaz.")
    return sqrt(x)

# Test sınıfı
class TestKarekokAl(unittest.TestCase):
    
    # Geçerli girişler için test
    def test_gecerli_giris(self):
        self.assertEqual(karekok_al(9), 3)
        self.assertEqual(karekok_al(16), 4)
    
    # Geçersiz girişler için test
    def test_gecersiz_giris(self):
        with self.assertRaises(ValueError):
            karekok_al(-4)
    
    # Sıfır için test
    def test_sifir(self):
        self.assertEqual(karekok_al(0), 0)

# Testleri çalıştırır
if __name__ == '__main__':
    unittest.main()
