numbers = input("Enter list of integers:")


products_before_index = [None] * len(numbers)
product_so_far = 1
products = [None] * len(numbers)
for current_index, current_number in enumerate(numbers):
    products_before_index[current_index] = product_so_far
    product_so_far *= current_number

product_after_index = 1
for current_index, current_number in reversed(list(enumerate(numbers))):
    products[current_index] = products_before_index[current_index] * product_after_index
    product_after_index *= current_number

print products
