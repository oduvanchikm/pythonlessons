petya = int(input())
vasya = int(input())
tolya = int(input())

if petya > vasya:
    if petya > tolya:
        mest1 = "Петя"
        if vasya > tolya:
            mest2 = "Вася"
            mest3 = "Толя"
        else:
            mest2 = "Толя"
            mest3 = "Вася"             
    elif tolya > petya:
        mest1 = "Толя"
        mest2 = "Петя"
        mest3 = "Вася"
elif vasya > petya:
    if vasya > tolya:
        mest1 = "Вася"
        if petya > tolya:
            mest2 = "Петя"
            mest3 = "Толя"
        else:
            mest2 = "Толя"
            mest3 = "Петя"
    else:
        mest1 = "Толя"
        mest2 = "Вася"
        mest3 = "Петя"
        
print("{:^8}{:^8}{:^8}".format(" ", mest1, " "))
print("{:^8}{:^8}{:^8}".format(mest2, " ", " "))
print("{:^8}{:^8}{:^8}".format(" ", " ", mest3))
print("{:^8}{:^8}{:^8}".format("II", "I", "III"))