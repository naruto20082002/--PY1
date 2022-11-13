def get_unique_list_numbers() -> list[int]:
    import random
    list_ = []
    i = 15
    while len(list_) < i:
        num = random.randint(-10,10)
        list_ = set(list_)
        list_.add(num)
    return list(list_)

    # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
