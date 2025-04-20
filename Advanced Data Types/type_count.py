mixed_list = [1, 'string', 2.2, True, None, 42, 'world', False, [1,3], {'a': 1}]

type_count = {}

for item in mixed_list:
    item_type = type(item).__name__
    if item_type in type_count:
        type_count[item_type] += 1
    else:
        type_count[item_type] = 1

print('\nCount of elements by data type: ')
for dtype, count in type_count.items():
    print(f'{dtype}: {count}')