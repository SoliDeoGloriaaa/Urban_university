def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if compound_or_simple(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper


def compound_or_simple(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
