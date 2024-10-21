# Proje Açıklaması: Python kullanarak basit bir blockchain yapısı oluşturun ve blok ekleme işlemlerini yönetin.
import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index  # Blok numarası
        self.timestamp = timestamp  # Oluşturulma zamanı
        self.data = data  # Blok verisi
        self.previous_hash = previous_hash  # Önceki bloğun hash değeri
        self.hash = self.calculate_hash()  # Blok hash değeri

    def calculate_hash(self):
        # Blok içeriğini SHA-256 ile hash'ler
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Zincir ilk bloğu

    def create_genesis_block(self):
        # İlk blok (genesis bloğu) oluşturur
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Yeni bloğun önceki hash'ini ayarlar
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Zincirin bütünlüğünü kontrol eder
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Blok hash'inin doğruluğunu kontrol eder
            if current.hash != current.calculate_hash():
                print(f"Blok {i} hash doğrulanamadı.")
                return False

            # Önceki blokun hash'inin doğru olup olmadığını kontrol eder
            if current.previous_hash != previous.hash:
                print(f"Blok {i} önceki hash ile uyuşmuyor.")
                return False

        print("Blockchain geçerli.")
        return True

# Blockchain kullanımı
if __name__ == '__main__':
    benim_blockchain = Blockchain()

    # Yeni bloklar ekler
    benim_blockchain.add_block(Block(1, time.time(), {"miktar": 4}))
    benim_blockchain.add_block(Block(2, time.time(), {"miktar": 10}))

    # Zinciri yazdırır
    for blok in benim_blockchain.chain:
        print(f"Blok {blok.index} - Hash: {blok.hash} - Veri: {blok.data}")

    # Zincirin geçerliliğini kontrol eder
    print("Blockchain geçerli mi?", benim_blockchain.is_chain_valid())

    # Zinciri manipüle etmeye çalışır
    benim_blockchain.chain[1].data = {"miktar": 100}
    benim_blockchain.chain[1].hash = benim_blockchain.chain[1].calculate_hash()

    # Geçerliliği tekrar kontrol eder
    print("Blockchain geçerli mi?", benim_blockchain.is_chain_valid())

# Block sınıfı, blockchain'deki her bloğun yapısını tanımlar.
# Blockchain sınıfı, blok zincirini yönetir ve yeni blok ekleme işlemlerini gerçekleştirir.
# Hashing işlemi ile blokların güvenliği sağlanır.
# Zincirin Geçerliliği kontrol edilerek veri bütünlüğü sağlanır.
# Basit bir blockchain yapısı ile temel kavramlar öğrenilir.
