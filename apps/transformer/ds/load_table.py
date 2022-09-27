import pandas as pd
import os


def get_hdf_file_name(user_name):
    return f"src/media/transformer/storage/{user_name}/data.h5"

def get_hdf_file_dir(user_name):
    return f"src/media/transformer/storage/{user_name}"

def get_basic_stats(df: pd.DataFrame, to_html=False):
    row_col = pd.DataFrame({'rows': [len(df)], 'cols': [len(df.columns)]})
    null_dtype = {'Column': [], 'Nulls': [], 'Dtype': []}
    for col in df.columns:
        null_dtype['Column'].append(str(col))
        null_dtype['Nulls'].append(str(df[col].isnull().sum()))
        null_dtype['Dtype'].append(str(df[col].dtype))
    null_dtype = pd.DataFrame(null_dtype)
    if to_html:
        null_dtype = null_dtype.to_html(index=False)
        row_col = row_col.to_html(index=False)
    return {'row_col': row_col, 'stat_table': null_dtype}


def read_csv_return_html(file, n_rows, username:str, html=False, html_index=True,
                         delimiter=',', stat_table_to_html=False):
    """"
    Returns first n_rows in dict/html variant of csv/xls/xlsx file
    + table count of coll/row
    """
    if file.name.split('.')[-1] == 'csv':
        data = pd.read_csv(file, delimiter=delimiter)
    elif file.name.split('.')[-1] == 'xls' or file.name.split('.')[-1] == 'xlsx':
        data = pd.read_excel(file)
    else:
        return -1
    file_dir = get_hdf_file_dir(username)
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    data.to_hdf(get_hdf_file_name(username), 'origin', 'w')
    if n_rows > len(data): n_rows = len(data)
    data_first_n = data.head(n_rows)
    if not html:
        return {'table': data_first_n.to_dict(), 'stats': get_basic_stats(data, to_html=stat_table_to_html)}
    else:
        return {'table': data_first_n.to_html(index=html_index),
                'stats': get_basic_stats(data, to_html=stat_table_to_html)}


def get_hdf_and_stat_html(username:str, origin=False, head=10):
    if origin:
        data = pd.read_hdf(get_hdf_file_name(username), 'origin')
    else:
        data = pd.read_hdf(get_hdf_file_name(username), 'actual')

    data_head = data.head(head)
    return {'table': data_head.to_html(index=False), 'stats': get_basic_stats(data, to_html=True)}
