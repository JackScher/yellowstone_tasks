def general_items(arr_0, arr_1):
    result = [i for i in arr_0 if i in arr_1]
    return result


def separate_items(arr_0, arr_1):
    firs_half_of_result = [i for i in arr_0 if i not in arr_1]
    second_half_of_result = [i for i in arr_1 if i not in arr_0]
    result = firs_half_of_result + second_half_of_result
    return result


if __name__ == '__main__':
    arr_0 = [1, 2, 3, 4, 5]
    arr_1 = [4, 5, 6, 7, 8]
    print(general_items(arr_0, arr_1))
    print(separate_items(arr_0, arr_1))
