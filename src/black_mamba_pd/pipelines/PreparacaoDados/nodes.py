"""
Funções relacionadas ao pipeline 'PreparacaoDados'
"""
import pandas as pd

from sklearn.model_selection import train_test_split

def load_data_kobe(data):
    data = data[data['shot_type'] == '2PT Field Goal']
    data = data[['lat','lon','minutes_remaining', 'period', 'playoffs', 'shot_distance','shot_made_flag']]
    return data

def conform_data_kobe(data):
    data = data.dropna()
    return data   

def train_test_split_data_kobe(data):
    X = data.drop(columns=['shot_made_flag']).copy()
    y = data['shot_made_flag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=17042023)
    base_train = pd.merge(X_train, y_train, left_index=True, right_index=True)
    base_test = pd.merge(X_test, y_test, left_index=True, right_index=True)
    return base_train, base_test