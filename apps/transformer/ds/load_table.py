import pandas as pd



HDF_FILENAME = "src/media/transformer/storage/data.h5"

def get_basic_stats(df:pd.DataFrame):
    cols = len(df.columns)
    rows = len(df)
    null_dtype = {'Column':[], 'Nulls':[], 'Dtype':[]}
    for col in df.columns:
        null_dtype['Column'].append(str(col))
        null_dtype['Nulls'].append(str(df[col].isnull().sum()))
        null_dtype['Dtype'].append(str(df[col].dtype))
    null_dtype = pd.DataFrame(null_dtype).to_html(index = False)
    return {'cols':cols, 'rows':rows, 'stat_table': null_dtype}


def read_csv_return_html(file, n_rows, html = False, html_index = True, delimeter = ','):
    """"
    Returns first n_rows in dict/html variant of csv/xls/xlsx file
    + table count of coll/row
    """
    if file.name.split('.')[-1] == 'csv':
        data = pd.read_csv(file, delimiter=delimeter)
    elif file.name.split('.')[-1] == 'xls' or file.name.split('.')[-1] == 'xlsx':
        data = pd.read_excel(file)
    else:
        return -1
    data.to_hdf(HDF_FILENAME, 'origin')
    if n_rows > len(data): n_rows = len(data)
    data_first_n = data.head(n_rows)
    if not html:
        return {'table':data_first_n.to_dict(), 'stats':get_basic_stats(data)}
    else:
        return {'table':data_first_n.to_html(index = html_index), 'stats':get_basic_stats(data)}

if __name__ == '__main__':
    t = pd.DataFrame({'a':[1,2], 'b':[3,4]})
    print(get_basic_stats(t))
