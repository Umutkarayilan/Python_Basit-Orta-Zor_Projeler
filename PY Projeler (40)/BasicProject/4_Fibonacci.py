# Kullanıcıdan dizinin uzunluğunu alır
n = int(input("Fibonacci dizisinin kaç terimini istiyorsunuz? "))
fib = [0, 1]

# Fibonacci dizisini oluşturur
for i in range(2, n):
    sonraki = fib[i-1] + fib[i-2]
    fib.append(sonraki)

# Diziyi ekrana yazdırır
print("Fibonacci Dizisi:", fib[:n])
