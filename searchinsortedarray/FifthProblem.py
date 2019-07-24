import random


def get_min_max(ints):
    min_value = ints[0]
    max_value = ints[0]

    for i in range(len(ints)):
        if ints[i] < min_value:
            min_value = ints[i]

        if ints[i] > max_value:
            max_value = ints[i]

    return min_value, max_value


## Example Test Case of Ten Integers


if __name__ == "__main__":
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)

    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
