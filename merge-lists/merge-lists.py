def merge_lists(list1, list2):

    list1_index = 0
    while len(list2) != 0:
        if list1_index >= len(list1) or list1[list1_index] > list2[0]:
            list1.insert(list1_index, list2.pop(0))

        list1_index += 1

    return list1


test_list1 = [1, 5, 8, 12, 14, 19]
test_list2 = [3, 4, 6, 10, 11, 15]

print merge_lists(test_list1, test_list2)
