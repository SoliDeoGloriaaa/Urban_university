first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = [
    'Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler'
]

first_result = [len(element) for element in first_strings if len(element) >= 5]
second_result = [
    (x, y) for x in first_strings for y in second_strings if len(x) == len(y)
]

combined_list = first_strings + second_strings  # объединяем два списка в один
third_result = {element: len(element) for element in combined_list if len(element) % 2 == 0 }

print(first_result)
print(second_result)
print(third_result)
