from random import randint

random_number = randint(3, 20)
password = []

for i in range(1, random_number):
    for j in range(1, random_number):
        if i != j and j > i:
            if random_number % (i + j) == 0:
                password.append([i, j])
result = "".join(str(digit) for sublist in password for digit in sublist)
print(f'{random_number} - Число из первой вставки')
print(f'{result} - пароль')
