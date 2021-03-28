import numpy
import pandas


if __name__ == '__main__':
    file = pandas.read_csv('./iris.csv')

    result = file.groupby('variety')[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']].aggregate(
        ['mean', 'median'])

    result.columns = [tuple(reversed(collection)) for collection in result.columns]

    result.columns = [
        '_'.join(tuple(''.join(tuple(letter if letter != '.' else '_' for letter in item)) if item != 'mean' else
                       'average' for item in collection)) for collection in result.columns]

    result.to_csv('./task3_result.csv')
