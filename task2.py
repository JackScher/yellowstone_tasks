import re


def parser_function(arr):
    expression = r'cmp([A-Za-z0-9]+)|cmp[-_]([A-Za-z0-9]+)'
    result = []
    for line in arr:
        little_list = re.findall(expression, line)
        for list_tuple in little_list:
            for item in list_tuple:
                if item:
                    result.append(item)
    return result


if __name__ == '__main__':
    refs = [
        'abc_cmp_campaign1_xyz',
        'abc_def_cmp_campaign2',
        'cmp_campaign3-xyz',
        'abcd-xyz-cmp-campaign4-',
        'abc_cmpcampaign5-xyz',
    ]

    print(parser_function(refs))
