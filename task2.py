import re


if __name__ == '__main__':
    refs = [
        'abc_cmp_campaign1_xyz',
        'abc_def_cmp_campaign2',
        'cmp_campaign3-xyz',
        'abcd-xyz-cmp-campaign4-',
        'abc_cmpcampaign5-xyz',
    ]

    result = []
    expression = r'cmp[-_]?([A-Za-z0-9]+)'
    for ref in refs:
        result.append(*re.findall(expression, ref))
    print(result)
