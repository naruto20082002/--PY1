def get_count_char(str_):
    list_world = str_.lower()
    dict_letter = {}
    for letter in list_world:
        if letter.isalpha():
            if letter in dict_letter:
                dict_letter[letter] +=1
            else:
                dict_letter[letter] = 1

    return dict_letter


def percent_(dict_letter):
    totalletter = sum(dict_letter.values())
    newdict_letter = {}
    for letter in dict_letter:
        newdict_letter[letter] = round((dict_letter[letter] / totalletter) * 100, 1)
    return newdict_letter


 # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(percent_(get_count_char(main_str)))