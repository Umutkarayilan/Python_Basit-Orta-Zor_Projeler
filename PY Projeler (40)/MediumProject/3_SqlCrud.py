import sqlite3  # SQLite veritabanı işlemleri için kullanılır

# Veritabanına bağlan veya oluştur
conn = sqlite3.connect('kullanicilar.db')
c = conn.cursor()

# Tablo oluşturma
c.execute('''
    CREATE TABLE IF NOT EXISTS kullanicilar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Veri ekleme
def ekle(ad, email):
    try:
        c.execute("INSERT INTO kullanicilar (ad, email) VALUES (?, ?)", (ad, email))
        conn.commit()
        print("Kullanıcı eklendi.")
    except sqlite3.IntegrityError:
        print("Bu e-posta zaten kayıtlı.")

# Veri okuma
def oku():
    c.execute("SELECT * FROM kullanicilar")
    for row in c.fetchall():
        print(row)

# Veri güncelleme
def guncelle(kullanici_id, yeni_ad):
    c.execute("UPDATE kullanicilar SET ad = ? WHERE id = ?", (yeni_ad, kullanici_id))
    conn.commit()
    print("Kullanıcı güncellendi.")

# Veri silme
def sil(kullanici_id):
    c.execute("DELETE FROM kullanicilar WHERE id = ?", (kullanici_id,))
    conn.commit()
    print("Kullanıcı silindi.")

# Örnek kullanım
ekle("Ahmet", "ahmet@example.com")
ekle("Ayşe", "ayse@example.com")
oku()
guncelle(1, "Ahmet Yılmaz")
sil(2)
oku()

# Bağlantıyı kapat
conn.close()
