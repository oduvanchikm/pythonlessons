name = input()
price = int(input())
total = int(input())
money = int(input())


print("================Чек================")
print(f"Товар:{' ' * (29 - len(name))}{name}")
print(f"Цена:{' ' * (19 - len(str(price)) - len(str(total)))}{total}кг * {price}руб/кг")
print(f"Итого:{' ' * (26 - len(str(total * price)))}{total * price}руб")
print(f"Внесено:{' ' * (24 - len(str(money)))}{money}руб")
print(f"Сдача:{' ' * (26 - len(str(money - total * price)))}{money - total * price}руб")
print("===================================")