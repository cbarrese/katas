numbers = input("Enter list of integers:")

products = []
for outer_index, outer_number in enumerate(numbers):
    product = 1
    for inner_index, inner_number in enumerate(numbers):
        if inner_index != outer_index:
            product = product * inner_number

    products.append(product)

print products
