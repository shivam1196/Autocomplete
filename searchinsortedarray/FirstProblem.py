def rotated_array_search(input_list, number):
    pivot_element = find_rotated_index(input_list,0,len(input_list))

    if input_list[pivot_element] == number:
        return pivot_element

    elif (number >= input_list[0]):
        return binary_search_index(input_list[:pivot_element],number)

    else :
        return pivot_element+binary_search_index(input_list[pivot_element+1:],number)+1





def find_rotated_index(input_list,left,right):
    mid = len(input_list) //2


    if input_list[mid] > input_list[mid +1]:
        return mid

    elif input_list[mid] < input_list[mid -1]:
        return mid

    elif input_list[left] > input_list[mid]:
        return find_rotated_index(input_list,left,mid)

    else:
        return find_rotated_index(input_list,mid+1,right)

def binary_search_index(input_list,value):
    left = 0
    right = len(input_list)-1

    mid = int(left+right) /2




    while left <= right:
        if value == input_list[mid]:
            return mid

        elif value < input_list[mid]:
            right = mid
            mid = int(left+right) /2

        else:
            left = mid +1
            mid = int(left+right) /2


    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":

    #test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    #test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
   # test_function([[6, 7, 8, 1, 2, 3, 4], 8])
  #  test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])

