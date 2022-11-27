import json

INPUT_FILE = "input.csv"

list_ = []
def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    with open(INPUT_FILE) as f:  # TODO реализовать конвертер из csv в json
        columm = f.readline()
        colum = columm.rstrip().split(',')
        #print(colum)
        for yy in f:
            value = yy.rstrip().split(',')
            #print(value)

            dicct = dict(zip(colum, value))
            list_.append(dicct)
            #print(list_)
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
