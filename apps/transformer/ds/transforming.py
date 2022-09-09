import pandas as pd

from .load_table import HDF_FILENAME



def select_dtypes(df:pd.DataFrame):
    numerics = list(df.select_dtypes(exclude=['object']).columns.values)
    categorics = list(df.select_dtypes(include=['object']).columns.values)
    return {'numerics':numerics, 'categorics':categorics}

def _restore_file():
    """"
     Returns origin data from HDF_FILENAME
    """
    data = pd.read_hdf(HDF_FILENAME, 'origin')
    return data

def load_hdf_to(origin = False, to_html = False, index=False):
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



if __name__ == "__main__":
    df = pd.DataFrame({'a':[1,2],'b':['x', 'y']})
    type(select_dtypes(df))