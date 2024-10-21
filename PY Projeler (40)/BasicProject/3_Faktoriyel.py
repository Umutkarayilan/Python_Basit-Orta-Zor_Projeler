# Kullanıcıdan bir sayı alır
n = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
faktoryel = 1

# 1'den n'e kadar olan sayıları çarpar
for i in range(1, n + 1):
    faktoryel *= i

# Sonucu ekrana yazdırır
print(f"{n}! = {faktoryel}")
