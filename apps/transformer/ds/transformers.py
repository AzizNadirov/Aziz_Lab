from typing import Sequence
import pandas as pd


def _remover(df: pd.DataFrame, cols: Sequence) -> pd.DataFrame:
    return df.drop(columns=cols, axis=1)


def _uni_encoder(df: pd.DataFrame,
                 cols: Sequence, encoder: str) -> pd.DataFrame:
    """"
        Takes dataframe and column names. Returns dataframe concat dummied columns.

    """
    df = df.copy()

    def _label():
        from sklearn.preprocessing import LabelEncoder

        for col_name in cols:
            df[col_name] = LabelEncoder().fit_transform(df[col_name])

    def _ohe():
        from sklearn.preprocessing import OneHotEncoder
        nonlocal df
        for col_name in cols:
            columns = [f"{col_name}_{i}" for i in range(df[col_name].nunique())]
            df = pd.concat(
                [df, pd.DataFrame(OneHotEncoder(sparse=False).fit_transform(df[[col_name]]), columns=columns)],
                axis=1)

    if encoder == "lb":
        _label()
    elif encoder == "oh":
        _ohe()
    else:
        raise ValueError(f"Unknown encoder name: {encoder}")
    return df


def _uni_scaler(df: pd.DataFrame, cols_for_scaling: Sequence, scaler: str):
    """

    :param df: pandas DataFrame object
    :param cols_for_scaling: columns of DataFrame which ones have to scaled
    :param scaler: string name of scaler: 'std' - Standard Scaler, 'mm' - MinMax Scaler, 'rb' - Robust Scaler
    :return: DataFrame with scaled columns
    """
    if scaler == 'std':
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
    elif scaler == 'mm':
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
    elif scaler == 'rb':
        from sklearn.preprocessing import RobustScaler
        scaler = RobustScaler()
    else:
        raise ValueError(f'unknown parameter for scaler:{scaler}.')

    df = df.copy()
    for col in cols_for_scaling:
        df[col] = scaler.fit_transform(df[[col]])

    return df


def divide_and_transform(df: pd.DataFrame, todo: dict):
    SCALERS = ('std', 'mm', 'rb')
    ENCODERS = ('lb', 'oh')
    for_scale = {}
    for_encode = {}
    df = df.copy()
    for k in todo.keys():
        if k in SCALERS:
            for_scale[k] = todo[k]
        elif k in ENCODERS:
            for_encode[k] = todo[k]
        elif k == 'rm':
            df = _remover(df, todo.get('rm'))
        else:
            raise ValueError(f"Incorrect todo: {k}")
    # do scaling:
    for item in tuple(for_scale.items()):
        print(f"item:{item}")
        df = _uni_scaler(df, cols_for_scaling=item[1], scaler=item[0])
    # do encoding:
    for item in tuple(for_encode.items()):
        df = _uni_encoder(df, cols=item[1], encoder=item[0])

    return df
