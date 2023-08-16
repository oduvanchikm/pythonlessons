name = input()
number = int(input())

number1 = number % 10
number2 = (number // 10) % 10
number3 = (number // 100) % 10


print(f'Группа №{number3}.')
print(f'{number1}. {name}.')
print(f'Шкафчик: {number}.')
print(f'Кроватка: {number2}.')