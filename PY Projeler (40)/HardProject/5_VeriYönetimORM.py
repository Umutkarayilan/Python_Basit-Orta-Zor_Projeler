# Proje Açıklaması: SQLAlchemy kullanarak bir SQLite veritabanı ile etkileşimde bulunun ve CRUD işlemlerini gerçekleştirin.



from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Veritabanı bağlantısı oluşturur
engine = create_engine('sqlite:///kullanicilar.db', echo=True)
Base = declarative_base()

# Modeli tanımlar
class Kullanici(Base):
    __tablename__ = 'kullanicilar'
    id = Column(Integer, primary_key=True)
    ad = Column(String)
    email = Column(String, unique=True)

    def __repr__(self):
        return f"<Kullanici(ad='{self.ad}', email='{self.email}')>"

# Tabloyu oluşturur
Base.metadata.create_all(engine)

# Session oluşturur
Session = sessionmaker(bind=engine)
session = Session()

# CRUD İşlemleri

# Create
def kullanici_ekle(ad, email):
    yeni_kullanici = Kullanici(ad=ad, email=email)
    session.add(yeni_kullanici)
    session.commit()
    print("Kullanıcı eklendi.")

# Read
def kullanicilari_listele():
    kullanicilar = session.query(Kullanici).all()
    for kullanici in kullanicilar:
        print(kullanici)

# Update
def kullanici_guncelle(kullanici_id, yeni_ad):
    kullanici = session.query(Kullanici).filter_by(id=kullanici_id).first()
    if kullanici:
        kullanici.ad = yeni_ad
        session.commit()
        print("Kullanıcı güncellendi.")
    else:
        print("Kullanıcı bulunamadı.")

# Delete
def kullanici_sil(kullanici_id):
    kullanici = session.query(Kullanici).filter_by(id=kullanici_id).first()
    if kullanici:
        session.delete(kullanici)
        session.commit()
        print("Kullanıcı silindi.")
    else:
        print("Kullanıcı bulunamadı.")

# Örnek kullanım
if __name__ == '__main__':
    kullanici_ekle("Mehmet", "mehmet@example.com")
    kullanici_ekle("Elif", "elif@example.com")
    kullanicilari_listele()
    kullanici_guncelle(1, "Mehmet Yılmaz")
    kullanici_sil(2)
    kullanicilari_listele()



#     SQLAlchemy ORM kullanılarak veritabanı modelleri tanımlanır.
# CRUD (Create, Read, Update, Delete) işlemleri için fonksiyonlar oluşturulur.
# Session yönetimi ile veritabanı etkileşimleri gerçekleştirilir.
# Veritabanı işlemleri sırasında hata yönetimi yapılabilir.

