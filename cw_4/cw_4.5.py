def odwracanie(L, left, right):
    if left  < 0:
        return "error"
    if right >= len(L):
        return "error"

    if left >= right:
        return L

    while left < right:
        L[left], L[right] = L[right], L[left] # wersja rekurencyjna będzie niemal identyczna, po prostu po tej linijce wywoływalibyśmy
        left += 1                             # return odwracanie(L, left + 1, right - 1)
        right -= 1

    return L

L = [8, 7, 6, 5, 4, 3, 2, 1]
L2 = [1, 2, 3, 4, 4, 5, 6, 8, 8]

print(odwracanie(L, 2, 5))
print(odwracanie(L2, 1,6))

