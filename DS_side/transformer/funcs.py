import pandas as pd

def read_csv_return_json(file, n_rows):
    """"
    Returns first n_rows in json variant of csv/xls/xlsx file
    """
    if file.name.split('.')[-1] == 'csv':
        data = pd.read_csv(file)
    elif file.name.split('.')[-1] == 'xls' or file.name.split('.')[-1] == 'xlsx':
        data = pd.read_excel(file)
    else:
        return -1
    data_first_n = data.head(n_rows)
    return data_first_n.to_json()

