import pandas as pd

from .load_table import HDF_FILENAME


def _restore_file():
    """"
     Returns origin data from HDF_FILENAME
    """
    data = pd.read_hdf(HDF_FILENAME, 'origin')
    return data

