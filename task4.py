import numpy
import pandas


if __name__ == '__main__':
    file = pandas.read_csv('./IMDB movies.csv', low_memory=False)
    quantity_by_years = file['year'].value_counts()

    all_attack_films = file.loc[file.title.str.match(r'[\w0-9\s]*[A|a]ttack[\w0-9\s]*')]
    result = all_attack_films[['title', 'duration', 'year']]
    result['duration'] = result['duration'].apply(lambda x: str(x // 60) + 'ч' + ' ' + '00м' if x % 60 == 0 else str(x // 60) + 'ч' + ' ' + str(x % 60) + 'м')
    result.sort_values(by=['year'], inplace=True, ascending=False)
    result.to_csv('./task4_result.csv', sep=';', encoding='utf-8')
