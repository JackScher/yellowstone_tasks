if __name__ == '__main__':
    arr_0 = [1, 2, 3, 4, 5]
    arr_1 = [4, 5, 6, 7, 8]
    print(list(set(arr_0) & set(arr_1)))
    print(list(set(arr_0) ^ set(arr_1)))
