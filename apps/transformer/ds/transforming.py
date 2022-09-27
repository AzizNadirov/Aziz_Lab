import pandas as pd

from .load_table import get_hdf_file_name, get_hdf_and_stat_html
from .transformers import divide_and_transform


def select_dtypes(df: pd.DataFrame):
    numerics = list(df.select_dtypes(exclude=['object']).columns.values)
    categorics = list(df.select_dtypes(include=['object']).columns.values)
    return {'numerics': numerics, 'categorics': categorics}


def restore_user_file(username: str):
    """"
     Returns origin data from HDF_FILENAME
    """
    data = pd.read_hdf(get_hdf_file_name(username), 'origin')
    return data


def load_hdf_to(username, origin=False, to_html=False, index=False):
    if origin:
        data = pd.read_hdf(get_hdf_file_name(username), 'origin')
    else:
        try:
            data = pd.read_hdf(get_hdf_file_name(username), 'actual')
        except:
            data = pd.read_hdf(get_hdf_file_name(username), 'origin')
            data.to_hdf(get_hdf_file_name(username), 'actual')
    if to_html:
        return data.head(10).to_html(index=index)
    else:
        return data


def _upload_to_hdf(df: pd.DataFrame, username: str, origin: bool = False):
    if origin:
        df.to_hdf(get_hdf_file_name(username), 'origin')
    else:
        df.to_hdf(get_hdf_file_name(username), 'actual')


def apply_todo(username: str, todo: dict) -> dict:
    """

    :param todo: transformers have apply to the data
    :return: transformed and loaded into 'actual.h5' data in html with basic stats.
            {'table': data_head.to_html(index=False), 'stats': get_basic_stats(data, to_html=True)}
    """
    data = load_hdf_to(username)
    data = divide_and_transform(data, todo)
    _upload_to_hdf(data, username=username, origin=False)
    return get_hdf_and_stat_html(username, head=10)
