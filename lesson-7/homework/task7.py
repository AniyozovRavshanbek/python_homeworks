# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input('Enter a number: '))
print(is_prime(num))



# 2. digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    summa = 0
    for i in str(abs(k)):
        summa += int(i)
    return summa

k = int(input('Enter a number: '))
print(f'Result: {digit_sum(k)}')



# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def power_of_two(n):
    k = 1
    while True:
        if 2**k > n:
            break
        print(2**k, end = ' ')
        k += 1

n = int(input('Enter a number: '))
power_of_two(n)

        
