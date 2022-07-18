from .info import get_default_info


def clean_header(header):
    """
    For cleaning file headers.
    - convert to uppercase
    - replace dashes '-' with underscores '_'
    - replace dots '.' (as in R) with underscores '_'
    - remove newlines ('\n')
    """
    return header.upper().replace('-', '_').replace('.', '_').replace('\n', '')


def check_header(input_data):
    """
    For know which type column is not in pd.DataFrame columns
    :param input_data: the pd.DataFrame
    :return: Two list,frist is which have, second is which not have
    """
    have_col = []
    for x in input_data.columns:
        if clean_header(x) in get_default_info()[0].keys():
            have_col.append(get_default_info()[0][clean_header(x)])
        else:
            have_col.append(x)
    name_dict = dict(zip(have_col, input_data.columns))
    dont_have_col = [x for x in get_default_info()[1].keys() if not x in have_col]
    for cid in dont_have_col:
        print('The input data lack of << {} >>, ===>:{}'.format(cid, get_default_info()[1][cid]))
    return have_col, dont_have_col, name_dict
