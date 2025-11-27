import pandas as pd
import numpy as np
from datetime import datetime as dt, timedelta

def cleaning_data(df):
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def convert_date_column(df, column):
    df[column] = pd.to_datetime(df[column])
    return df

def rfm_df(df, date_column, transaction_column, ID_column, total_column):
    reference_date = df[date_column].max() + timedelta(days=1)
    rfm = df.groupby(ID_column).agg({
        date_column : lambda x: (reference_date - x.max()).days,
        transaction_column : 'count',
        total_column : 'sum'
    })

    rfm.rename(columns = {date_column : 'Recency',
                          transaction_column : 'Frequency',
                          total_column : 'Monetary'},
                          inplace = True)
    return rfm

def save_csv(data, path_folder, file_name):
    return data.to_csv(path_folder + file_name)

def save_pickle(data, path_folder, file_name):
    return data.to_pickle(path_folder + file_name)
