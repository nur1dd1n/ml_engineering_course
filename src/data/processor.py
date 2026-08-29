import pandas as pd


def remove_missing_values(
    data: pd.DataFrame
) -> pd.DataFrame:
    return data.dropna()


def remove_duplicates(
    data: pd.DataFrame
) -> pd.DataFrame:
    return data.drop_duplicates()


def process_data(
    data: pd.DataFrame
) -> pd.DataFrame:

    data = remove_missing_values(data)
    data = remove_duplicates(data)

    return data