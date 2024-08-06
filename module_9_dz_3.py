# first = ['Strings', 'Student', 'Computers']
# second = ['Строка', 'Урбан', 'Компьютер']

# first_result = [len(i) - len(j) for i, j in zip(first, second) if len(i) - len(j) != 0]
# second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]
# print(f'{first_result}-----{second_result}')


class Iter:

    def __init__(self):
        self.first = 'Первый'
        self.second = 'Второй'
        self.thrid = 'Третий'
        self.element = 0

    def __iter__(self):
        self.element = 0
        return self

    def __next__(self):
        self.element += 1
        if self.element == 1:
            return self.first
        if self.element == 2:
            return self.second
        if self.element == 3:
            return self.thrid
        if self.element == 4:
            return 'Подсчет окончен'
        raise StopIteration()

obj = Iter()

for value in obj:
    print(value)

for value in obj:
    print(value)