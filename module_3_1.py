calls = 0

def count_calls():
    global calls
    calls += 1
    print('Вызов сработал!')

def string_inf0(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return (True if string.lower() in list_to_search else False)

print(string_inf0('Urban'))
print(is_contains('URBAN', ['urban', '123']))


print(string_inf0('Urban2'))
print(is_contains('UrBan3', ['urban', '1423', 'TEST']))

print(f'Количество вызовов: {calls}')

