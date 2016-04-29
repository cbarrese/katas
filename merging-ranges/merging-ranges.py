ranges = input("Enter range tuples:")

sorted_ranges = sorted(ranges, key=lambda range_tuple: range_tuple[0])

merged_ranges = [sorted_ranges[0]]
for current_range in sorted_ranges[1:]:
    start_of_current_range, end_of_current_range = current_range
    start_of_working_range, end_of_working_range = merged_ranges[-1]

    if start_of_current_range <= end_of_working_range:
        merged_ranges[-1] = (start_of_working_range,
                             max(end_of_working_range, end_of_current_range))
    else:
        merged_ranges.append(current_range)

print merged_ranges
