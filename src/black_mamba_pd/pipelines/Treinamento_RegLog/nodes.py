"""
Funções relacionadas ao pipeline 'Treinamento_RegLog'
"""
import numpy as np
import pandas as pd
from pycaret.classification import *

from sklearn.metrics import log_loss, f1_score

import logging
LOGGER = logging.getLogger(__name__)

def treinamento_modelo_reglog(data_train, n_random_state):
    """
    Utiliza a base de treino para realizar o treinamento dos modelos usando a biblioteca pyCaret.
    """
    setup_clf_lr = setup(data = data_train, target='shot_made_flag', session_id = n_random_state )
    setup_clf_lr.add_metric('logloss','Log Loss', log_loss, greater_is_better=False)
    lr_model = setup_clf_lr.create_model('lr')
    return lr_model

def teste_modelo_reglog(lr_model, data_test):
    """
    Realiza o teste com os modelos treinado na base de teste e oferece como saída os dados 
    com as colunas de predição e probabilidade da predição.
    """
    pred_lr = predict_model(lr_model, data_test)
    return pred_lr

def metrics_modelo_reglog(pred_lr):
    """
    Faz o registro no MLFlow das métricas de “F1 Score” e “Log Loss” do modelo.
    """
    f1_metric = f1_score(pred_lr[['shot_made_flag']], pred_lr[['prediction_label']])
    log_loss_metric = log_loss(pred_lr[['shot_made_flag']], pred_lr[['prediction_label']])
    LOGGER.info(f"F1 Score : {f1_metric}")
    LOGGER.info(f"Log loss: {log_loss_metric}")
    return {
        'F1 Score': {'value': f1_metric, 'step':1},
        'Log loss': {'value': log_loss_metric, 'step':1},
    }
	