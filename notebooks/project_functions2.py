import pandas as pd
import numpy as np


def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df



def load_and_process(csv_file):
    df = pd.read_csv(csv_file)
    df
    df1 = (df.drop(columns = ['usd pledged', 'currency', 'goal', 'pledged'], inplace = False)
           .rename(columns = {'state':'status'}, inplace = False))
    return df1