def sort_012(input_list):
    zero_arranged_list = sort_zeros(input_list)

    return sort_twos(zero_arranged_list)


def sort_zeros(input_list):
    zero_pointer = 0

    for i in range(len(input_list)):
        if input_list[i] == 0:
            if input_list[zero_pointer] == 0 and input_list[0] != 0:
                zero_pointer += 1
                temp_value = input_list[i]
                input_list[i] = input_list[zero_pointer]
                input_list[zero_pointer] = temp_value
                zero_pointer += 1

            else:
                temp_value = input_list[i]
                input_list[i] = input_list[zero_pointer]
                input_list[zero_pointer] = temp_value
                zero_pointer += 1

    return input_list


def sort_twos(input_list):
    twos_pointer = len(input_list) - 1

    for i in range(len(input_list)-1,-1,-1):
        if input_list[i] == 2:
            if input_list[twos_pointer] == 2 and input_list[len(input_list)-1]!= 2:
                twos_pointer -=1
                temp_value = input_list[i]
                input_list[i] = input_list[twos_pointer]
                input_list[twos_pointer] = temp_value
                twos_pointer -=1
            else:
                temp_value = input_list[i]
                input_list[i] = input_list[twos_pointer]
                input_list[twos_pointer] = temp_value
                twos_pointer -= 1

    return input_list




def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    test_function([2,2,2,2,2,1,1,1,1,1,0,0,0,0,0])
