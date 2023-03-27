"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.18.6
"""
import pandas as pd

def load_data_kobe():
    data = pd.read_csv('data/01_raw/kobe_dataset.csv')
    data = data[data['shot_type'] == '2PT Field Goal']
    data = data[['lat','lon','minutes_remaining', 'period', 'playoffs', 'shot_distance','shot_made_flag']]
    data = data.dropna()
    return data