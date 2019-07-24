def rearrange_digits(input_list):
    rearranged_list = merge_sort(input_list)
    return rearranged_final_list(rearranged_list)


def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2

    left = list[:mid]

    right = list[mid:]

    left = merge_sort(left)

    right = merge_sort(right)

    return merge_list(left, right)


def rearranged_final_list(input_list):
    highest_number = ""

    lowest_number = ""

    final_list = []

    for i in range(len(input_list)):
        if i % 2 == 0:
            highest_number = highest_number + str(input_list[i])
        elif i % 2 != 0:
            lowest_number = lowest_number + str(input_list[i])

    final_list.append(int(highest_number))
    final_list.append(int(lowest_number))

    return final_list


def merge_list(left, right):
    merged_list = []

    left_index = 0

    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1

        else:
            merged_list.append(left[left_index])
            left_index += 1

    merged_list += left[left_index:]

    merged_list += right[right_index:]

    return merged_list


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
