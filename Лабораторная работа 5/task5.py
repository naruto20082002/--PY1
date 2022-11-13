import random
n = 8
def get_random_password() -> str:
    import string
    NABOR = string.ascii_letters +string.digits
    list_ = random.sample(NABOR,n)
    strr = ''.join(list_)
    return strr


 # TODO написать функцию генерации случайных паролей


print(get_random_password())
