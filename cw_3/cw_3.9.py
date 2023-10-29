sekwencje = [[1], [4], (1,2,3), [3,4,0], (5,6,7,10)]
sumy = []
for sekwencja in sekwencje:
    suma = sum(sekwencja)
    sumy.append(suma)

print(sumy)