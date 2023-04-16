"""
Funções relacionadas ao pipeline 'Treinamento_Clf'
"""
import numpy as np
import pandas as pd
from pycaret.classification import *

from sklearn.metrics import log_loss, f1_score

import logging
LOGGER = logging.getLogger(__name__)

def treinamento_modelo_clf(data_train, n_random_state):
    """
    Utiliza a base de treino para realizar o treinamento dos modelos usando a biblioteca pyCaret.
    """
    setup_clf = setup(data = data_train, target='shot_made_flag', session_id = n_random_state)
    setup_clf.add_metric('logloss','Log Loss', log_loss, greater_is_better=False)
    melhores_modelos = compare_models(n_select=5, sort="Log Loss")
    clf_model = melhores_modelos[0]
    return clf_model

def teste_modelo_clf(clf_model, data_test):
    """
    Realiza o teste com os modelos treinado na base de teste e oferece como saída os dados 
    com as colunas de predição e probabilidade da predição.
    """
    pred_clf = predict_model(clf_model, data_test)
    return pred_clf

def metrics_modelo_clf(pred_clf):
    """
    Faz o registro no MLFlow das métricas de “F1 Score” e “Log Loss” do modelo.
    """
    f1_metric = f1_score(pred_clf[['shot_made_flag']], pred_clf[['prediction_label']])
    log_loss_metric = log_loss(pred_clf[['shot_made_flag']], pred_clf[['prediction_label']])
    LOGGER.info(f"F1 Score : {f1_metric}")
    LOGGER.info(f"Log loss: {log_loss_metric}")
    return {
        'F1 Score': {'value': f1_metric, 'step':1},
        'Log loss': {'value': log_loss_metric, 'step':1},
    }