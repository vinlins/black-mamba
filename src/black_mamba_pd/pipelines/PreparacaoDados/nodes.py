"""
Funções relacionadas ao pipeline 'PreparacaoDados'
"""
import pandas as pd

from sklearn.model_selection import train_test_split

import mlflow
from kedro_mlflow.io.metrics import MlflowMetricDataSet

import logging
LOGGER = logging.getLogger(__name__)

def load_data_kobe(data):
    data = data[data['shot_type'] == '2PT Field Goal']
    data = data[['lat','lon','minutes_remaining', 'period', 'playoffs', 'shot_distance','shot_made_flag']]
    return data

def generate_base_inference(data):
    data = data[data['shot_type'] == '3PT Field Goal']
    data = data[['lat','lon','minutes_remaining', 'period', 'playoffs', 'shot_distance','shot_made_flag']]
    data = data.dropna()
    return data

def conform_data_kobe(data):
    data = data.dropna()
    return data   

def train_test_split_data_kobe(data, n_test_size, n_random_state):
    X = data.drop(columns=['shot_made_flag']).copy()
    y = data['shot_made_flag']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=n_test_size, random_state = n_random_state)
    base_train = pd.merge(X_train, y_train, left_index=True, right_index=True)
    base_test = pd.merge(X_test, y_test, left_index=True, right_index=True)
    
    LOGGER.info(f"Percentual divisão base de teste: {n_test_size}")
    metric_perc_split_test_size = MlflowMetricDataSet(key = 'perc_split_test_size')
    metric_perc_split_test_size.save(n_test_size)
    
    return base_train, base_test

def metrics_preparacao_dados(data, data_train, data_test):
    LOGGER.info(f"Tamanho total da base: {data.shape[0]}")
    LOGGER.info(f"Tamanho da base de treino: {data_train.shape[0]}")
    LOGGER.info(f"Tamanho da base de teste: {data_test.shape[0]}")
    return {
        'n_total': {'value': data.shape[0], 'step':1},
        'n_treino': {'value': data_train.shape[0], 'step':1},
        'n_test': {'value': data_test.shape[0], 'step':1},
    }