list_w_duplicates = [0, 1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9,]
tmp = {}
result = tuple()

for value in list_w_duplicates:
    try:
        result += (tmp[value], )
    except KeyError:
        tmp[value] = value

print(list(result))
