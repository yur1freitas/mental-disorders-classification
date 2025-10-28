from pandas import DataFrame


def strip_str(df: DataFrame) -> DataFrame:
    df_copy = df.copy(deep=True)

    df_obj = df_copy.select_dtypes('object')
    df_copy[df_obj.columns] = df_obj.map(str.strip)

    return df_copy


def to_snake_case(df: DataFrame) -> DataFrame:
    df_copy = df.copy(deep=True)

    df_copy.columns = df_copy.columns.str.strip()
    df_copy.columns = df_copy.columns.str.replace(r'\s+', '_', regex=True)
    df_copy.columns = df_copy.columns.str.replace(r'-', '_', regex=True)
    df_copy.columns = df_copy.columns.str.replace(r'&', 'and', regex=True)
    df_copy.columns = df_copy.columns.str.lower()

    return df_copy
