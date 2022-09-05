import pandas as pd

def read_csv_return_json(file, n_rows, html = False, html_index = True):
    """"
    Returns first n_rows in dict/html variant of csv/xls/xlsx file
    """
    if file.name.split('.')[-1] == 'csv':
        data = pd.read_csv(file)
    elif file.name.split('.')[-1] == 'xls' or file.name.split('.')[-1] == 'xlsx':
        data = pd.read_excel(file)
    else:
        return -1
    data_first_n = data.head(n_rows)
    if not html:
        return data_first_n.to_dict()
    else:
        return data_first_n.to_html(index = html_index)

