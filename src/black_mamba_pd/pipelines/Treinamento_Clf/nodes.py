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
    setup_clf = setup(data = data_train, target='shot_made_flag', session_id = n_random_state )
    melhores_modelos = compare_models(n_select=5)
    clf_model = melhores_modelos[0]
    return clf_model

def teste_modelo_clf(clf_model, data_test):
    pred_clf = predict_model(clf_model, data_test)
    return pred_clf

def metrics_modelo_clf(pred_clf):
    f1_metric = f1_score(pred_clf[['shot_made_flag']], pred_clf[['prediction_label']])
    # Capturar a probabilidade de acerto apenas (label = 1) para cálculo do Log Loss
    pred_clf['prediction_score_label_1'] = np.where(pred_clf['prediction_label']==1, pred_clf['prediction_score'], 1-pred_clf['prediction_score'])
    log_loss_metric = log_loss(pred_clf[['shot_made_flag']], pred_clf[['prediction_score_label_1']])
    LOGGER.info(f"F1 Score : {f1_metric}")
    LOGGER.info(f"Log loss: {log_loss_metric}")
    return {
        'F1 Score': {'value': f1_metric, 'step':1},
        'Log loss': {'value': log_loss_metric, 'step':1},
    }