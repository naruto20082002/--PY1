src = not False and True or False and not True

# src = True and True or False and False  # избавляемся от отрицаний
# src = True or False  # избавляемся от логического "И"
# src = True  # избавляемся от логического "ИЛИ"

result = True

print(src == result)
