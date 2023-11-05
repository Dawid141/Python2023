# **********algorytm.edu.pl***************
def fibonacci(n):
    a, b = 1, 1
    if n < 3:
        return 1

    for i in range(n):
        b += a
        a = b - a

    return b - a


n = int(input("Podaj długość ciągu: "))
print(fibonacci(n))
