import pandas as pd


def read_data(file_location: str, drop_cols: list) -> pd.DataFrame:
    """
    Read in data
    :param file_location: File location to read from
    :param drop_cols: These are columns to drop
    :return: Dataframe
    """
    titanic = pd.read_csv(file_location)
    titanic = titanic.drop(drop_cols, axis=1, errors='ignore')
    return titanic
