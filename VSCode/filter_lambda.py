items = [('product1', 10), ('product2', 8), ('product3', 12), ('product4', 3)]
print(items)
filter_obj = filter(lambda item: item[1] < 10, items)
print(filter_obj)
filtered_list = list(filter_obj)
print(filtered_list)