print("Введите кол-во всех чисел, которые будут использоваться в операции.")
Nums = int(input())

print("Введите числа.")
spisok = list()
itog = 0
for Num in range(Nums):
    spisok.append(int(input()))

print("Введите номер вашей операции над введенными числами: 1 - Сложение. 2 - Вычитание. 3 - Умножение. 4 - Деление.")
vvod = int(input())


if vvod == 1:
    for Num in spisok:
        itog += Num

if vvod == 2:
    for Num in spisok:
        itog -= Num

if vvod == 3:
    itog += 1
    for Num in spisok:
        itog *= Num

if vvod == 4:
    itog = spisok[0]
    for Num in range(1, len(spisok)):
        if spisok[Num] != 0:
            itog /= spisok[Num]      
        else:
            print("На ноль делить нельзя!")
           
print("Ответ:", itog)


