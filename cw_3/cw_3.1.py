
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y; ##problem jest z wcieciami oraz srednikami, ten kod powinien wyglądac tak:

x = 2
y = 3

if x > y:
    result = x
else:
    result = y

## 2 kod:

for i in "axby": if ord(i) < 100: print (i) ##tak samo tutaj, kod poprawny powinien wyglądac nastepujaco

for i in "axby":
    if ord(i) < 100:
        print(i)

## 3 kod:

for i in "axby": print (ord(i) if ord(i) < 100 else i) ##zmiana którą możemy dokonać polega na:

for i in "axby":
    print(str(ord(i) if ord(i) < 100 else i))




