data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    total_sum = 0

    def recursive_sum(element):
        nonlocal total_sum

        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (list, tuple, set)):
            for sub_element in element:
                recursive_sum(sub_element)
        elif isinstance(element, dict):
            for value in element.values():
                recursive_sum(value)
            for key in element.keys():
                recursive_sum(key)

    for item in data_structure:
        recursive_sum(item)
    return total_sum


result = calculate_structure_sum(data_structure)
print(result)
