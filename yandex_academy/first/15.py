hours = int(input())
minutes = int(input())
delivery = int(input())

if (hours >= 0) and (hours < 24) and (minutes >= 0) and (minutes < 60) and (delivery >= 30) and (delivery < 10 ** 10):

    time = hours * 60 + minutes + delivery
    hours = time // 60
    hours2 = hours % 24
    minutes1 = time % 60
    hours3 = str(hours2).zfill(2)
    minutes2 = str(minutes1).zfill(2)
    print(hours3, minutes2)


else:
    print('not')