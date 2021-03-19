import numpy
import pandas


def get_variety_list_function(file):
    variety_list = file['variety']
    check_name = ''
    start = 0
    finish = 0
    res_dict = {}
    for iteration in range(0, len(variety_list)):
        if check_name != variety_list[iteration]:
            start = iteration
            check_name = variety_list[iteration]
        if check_name == variety_list[iteration]:
            finish = iteration
            res_dict[check_name] = [start, finish]
    return res_dict


def get_avg_and_median_data(arr):
    result = [['variety', 'average_sepal_length', 'average_sepal_width', 'average_petal_length', 'average_petal_width',
               'median_sepal_length', 'median_sepal_width', 'median_petal_length', 'median_petal_width']]
    for item in arr:
        arr_avg = file.loc[arr[item][0]:arr[item][1],
                  ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].mean()
        arr_median = file.loc[arr[item][0]:arr[item][1],
                     ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].median()
        variety = [item]
        joined_list = [*variety, *arr_avg, *arr_median]
        result.append(joined_list)
    result_array = pandas.DataFrame(result)
    return result_array


if __name__ == '__main__':
    file = pandas.read_csv('./iris.csv')
    variety_list = get_variety_list_function(file)
    result = get_avg_and_median_data(variety_list)
    result.to_csv('./my_results.csv')
