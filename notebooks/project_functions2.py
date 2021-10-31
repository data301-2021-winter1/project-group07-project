import pandas as pd
import numpy as np


def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df



def load_and_process(csv_file):
    
    df = pd.read_csv(csv_file)
    df
    df1 = (df.drop(columns = ['ID', 'usd pledged', 'currency', 'goal', 'pledged', 'country'], inplace = False)
           .dropna()
           .rename(columns={"usd_pledged_real": "pledged", "usd_goal_real": "goal", "state": "status"}))
           
    df2 = add_calculated_column_to_data(df1)
    df3 = filter_data(df2)
    
    return df3
           
def add_calculated_column_to_data(df):
    
    df1 = df.copy()
    df1['launched'] = pd.to_datetime(df1['launched'])
    df1['deadline'] = pd.to_datetime(df1['deadline'])
    df1['duration'] = (df1['deadline'] - df1['launched']).dt.days
    df1['completion'] = (df1['pledged'] / df1['goal'])*100
    
    return df1

def filter_data(df):
    
    df1 = df.copy()
    df1 = df1[(df1['status'] != 'canceled')
                    & (df1['status'] != 'undefined')
                    & (df1['status'] != 'live')
                    & (df1['status'] != 'suspended')]
    
    df1 = df1[(df1['goal'] < 60000)
                   & (df1['backers'] < 200)
                   & (df1['completion'] < 200)
                   & (df1['pledged'] < 15000)]
    
    return df1
