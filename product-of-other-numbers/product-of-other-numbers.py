numbers = input("Enter list of integers:")


product_before_index = 1
products = []
for current_index, current_number in enumerate(numbers):
    product_after_index = 1
    for after_index_number in numbers[current_index+1:]:
        product_after_index = product_after_index * after_index_number

    products.append(product_before_index * product_after_index)
    product_before_index = product_before_index * current_number

print products
