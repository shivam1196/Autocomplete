def sqrt(number):
    input_list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    left = 0

    right = len(input_list)

    mid = int(right + left) / 2

    while left < right:
        if input_list[mid] * input_list[mid] == number:
            return input_list[mid]
        elif input_list[mid] * input_list[mid] < number < input_list[mid + 1] * input_list[mid + 1]:
            return input_list[mid]

        elif number < input_list[mid] * input_list[mid]:
            right = mid
            mid = int(left + right) / 2

        else:
            left = mid + 1
            mid = int(left + right) / 2

    return -1


if __name__ == "__main__":
    print ("Pass" if (3 == sqrt(9)) else "Fail")
    print ("Pass" if (0 == sqrt(0)) else "Fail")
    print ("Pass" if (4 == sqrt(16)) else "Fail")
    print ("Pass" if (1 == sqrt(1)) else "Fail")
    print ("Pass" if (5 == sqrt(27)) else "Fail")
