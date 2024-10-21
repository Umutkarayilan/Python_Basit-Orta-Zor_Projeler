# Proje Açıklaması: argparse kullanarak kullanıcıdan komut satırı argümanları alabilen bir dosya yönetim aracı oluşturun.
import argparse
import os
import shutil

def dosya_listele(dizin):
    print(f"{dizin} dizinindeki dosyalar:")
    for dosya in os.listdir(dizin):
        print(dosya)

def dosya_kopyala(kaynak, hedef):
    try:
        shutil.copy(kaynak, hedef)
        print(f"{kaynak} dosyası {hedef} konumuna kopyalandı.")
    except Exception as e:
        print(f"Dosya kopyalama hatası: {e}")

def dosya_sil(dosya_yolu):
    try:
        os.remove(dosya_yolu)
        print(f"{dosya_yolu} dosyası silindi.")
    except Exception as e:
        print(f"Dosya silme hatası: {e}")

# Argument parser'ı oluşturur
parser = argparse.ArgumentParser(description='Basit Dosya Yönetim Aracı')

subparsers = parser.add_subparsers(dest='komut')

# Listele komutu
listele_parser = subparsers.add_parser('listele', help='Dizindeki dosyaları listeler')
listele_parser.add_argument('dizin', type=str, help='Dizin yolu')

# Kopyala komutu
kopyala_parser = subparsers.add_parser('kopyala', help='Dosya kopyalar')
kopyala_parser.add_argument('kaynak', type=str, help='Kaynak dosya yolu')
kopyala_parser.add_argument('hedef', type=str, help='Hedef dizin yolu')

# Sil komutu
sil_parser = subparsers.add_parser('sil', help='Dosya siler')
sil_parser.add_argument('dosya_yolu', type=str, help='Silinecek dosya yolu')

# Argümanları parse eder
args = parser.parse_args()

# Komutları çalıştırır
if args.komut == 'listele':
    dosya_listele(args.dizin)
elif args.komut == 'kopyala':
    dosya_kopyala(args.kaynak, args.hedef)
elif args.komut == 'sil':
    dosya_sil(args.dosya_yolu)
else:
    parser.print_help()

# argparse modülü ile komut satırı argümanları tanımlanır ve işlenir.
# subparsers kullanılarak farklı alt komutlar (listele, kopyala, sil) oluşturulur.
# os ve shutil modülleri ile dosya sistemine erişim sağlanır.
# Hata yönetimi ile kullanıcı dostu geri bildirimler sağlanır.
# Komut satırından araç kullanılabilir, örneğin:
# python dosya_yonetimi.py listele /path/to/directory
# python dosya_yonetimi.py kopyala /path/source.txt /path/destination/
# python dosya_yonetimi.py sil /path/to/file.txt
