import re  # Düzenli ifadeler için kullanılır

metin = """
İletişim: ahmet.yilmaz@example.com
Destek: destek@ornek.com
Satış: satis@ornek.com.tr
"""

# E-posta desenini tanımlar
email_deseni = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Metindeki tüm e-postaları bulur
emails = re.findall(email_deseni, metin)

# Bulunan e-postaları ekrana yazdırır
print("Bulunan E-postalar:")
for email in emails:
    print(email)
