import random

num = random.randint(1, 10)
attempts = 0
ans = 0
while ans != num:
    ans = int(input("Угадайте число от 1 до 10: "))
    if ans < num:
        print("Больше")
    elif ans > num:
        print("Меньше")
    attempts = attempts + 1
print(f"Молодец, тебе понадобилось {attempts} попыток")