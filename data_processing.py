
import pandas as pd

def remove_duplicates(df):
    return df.drop_duplicates()

def convert_types(df, column_types: dict):
    for col, dtype in column_types.items():
        df[col] = df[col].astype(dtype)
    return df

def filter_data(df, condition):
    return df.query(condition)

def check_nulls(df):
    return df.isnull().sum()

def missing_report(df):
    total = df.isnull().sum()
    percent = (total / len(df)) * 100
    return pd.DataFrame({'missing': total, 'percent': percent})

def fill_missing(df, strategy='mean'):
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ['int64', 'float64']:
                if strategy == 'mean':
                    df[col].fillna(df[col].mean(), inplace=True)
                elif strategy == 'median':
                    df[col].fillna(df[col].median(), inplace=True)
            else:
                df[col].fillna(df[col].mode()[0], inplace=True)
    return df
