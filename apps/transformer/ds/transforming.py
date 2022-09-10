import pandas as pd

from .load_table import HDF_FILENAME, get_hdf_and_stat_html
from .transformers import divide_and_transform


def select_dtypes(df: pd.DataFrame):
    numerics = list(df.select_dtypes(exclude=['object']).columns.values)
    categorics = list(df.select_dtypes(include=['object']).columns.values)
    return {'numerics': numerics, 'categorics': categorics}


def _restore_file():
    """"
     Returns origin data from HDF_FILENAME
    """
    data = pd.read_hdf(HDF_FILENAME, 'origin')
    return data


def load_hdf_to(origin=False, to_html=False, index=False):
    if origin:
        data = pd.read_hdf(HDF_FILENAME, 'origin')
    else:
        try:
            data = pd.read_hdf(HDF_FILENAME, 'actual')
        except:
            data = pd.read_hdf(HDF_FILENAME, 'origin')
            data.to_hdf(HDF_FILENAME, 'actual')
    if to_html:
        return data.head(20).to_html(index=index)
    else:
        return data


def _upload_to_hdf(df: pd.DataFrame, origin: bool = False):
    if origin:
        df.to_hdf(HDF_FILENAME, 'origin')
    else:
        df.to_hdf(HDF_FILENAME, 'actual')


def apply_todo(todo: dict) -> dict:
    """

    :param todo: transformers have apply to the data
    :return: transformed and loaded into 'actual.h5' data in html with basic stats.
            {'table': data_head.to_html(index=False), 'stats': get_basic_stats(data, to_html=True)}
    """
    data = load_hdf_to()
    data = divide_and_transform(data, todo)
    _upload_to_hdf(data, origin=False)
    return get_hdf_and_stat_html(head=20)
