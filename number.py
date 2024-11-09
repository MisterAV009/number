import random

chisly = random.randint(1,10)
while True:
    try:
        number = int(input("назови число от 1 до 10: "))
    except:
        print("это не цифра")
        continue
    if number == chisly:
        print("ты угадал")
        break
    elif number < 1 or number > 10:
        print("эту цифру нельзя писать!")
    elif number > chisly:
        print("это слишком большое")
    elif number < chisly:
        print("это число слишком маленькое")