name = input()
prise = int(input())
weight = int(input())
money = int(input())

digit = prise * weight
digit1 = int(digit)

a = money - digit1

print('Чек')
print(f'{name} - {weight}кг - {prise}руб/кг')
print(f'Итого: {digit1}руб')
print(f'Внесено: {money}руб')
print(f'Сдача: {a}руб')