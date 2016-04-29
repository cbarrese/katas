numbers = input("Enter list of integers:")

highest_product_of_3 = float('-inf')
max_of_first_2=max(numbers[0], numbers[1])
min_of_first_2=min(numbers[0], numbers[1])
highest_2 = [max_of_first_2, min_of_first_2]
lowest_2 = [min_of_first_2, max_of_first_2]

for current_index, current_number in enumerate(numbers):
    if current_index < 2:
        continue

    product_of_highest_2 = highest_2[0] * highest_2[1]
    product_of_lowest_2 = lowest_2[0] * lowest_2[1]

    product_of_current_with_highest_2 = product_of_highest_2 * current_number
    product_of_current_with_highest_lowest = highest_2[0] * lowest_2[0] * current_number
    product_of_current_with_lowest_2 = product_of_lowest_2 * current_number

    highest_product_of_3 = max(product_of_current_with_highest_2,
                               product_of_current_with_lowest_2,
                               product_of_current_with_highest_lowest,
                               highest_product_of_3)

    if current_number > highest_2[0]:
        highest_2[1] = highest_2[0]
        highest_2[0] = current_number
    elif current_number > highest_2[1]:
        highest_2[1] = current_number

    if current_number < lowest_2[0]:
        lowest_2[1] = lowest_2[0]
        lowest_2[0] = current_number
    elif current_number < lowest_2[1]:
        lowest_2[1] = current_number

print highest_2
print lowest_2
print highest_product_of_3
