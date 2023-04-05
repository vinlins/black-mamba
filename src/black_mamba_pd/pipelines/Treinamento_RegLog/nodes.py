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
    setup_clf_lr = setup(data = data_train, target='shot_made_flag', session_id = n_random_state )
    lr_model = setup_clf_lr.create_model('lr')
    return lr_model

def teste_modelo_reglog(lr_model, data_test):
    pred_lr = predict_model(lr_model, data_test)
    return pred_lr

def metrics_modelo_reglog(pred_lr):
    f1_metric = f1_score(pred_lr[['shot_made_flag']], pred_lr[['prediction_label']])
    # Capturar a probabilidade de acerto apenas (label = 1) para cálculo do Log Loss
    pred_lr['prediction_score_label_1'] = np.where(pred_lr['prediction_label']==1, pred_lr['prediction_score'], 1-pred_lr['prediction_score'])
    log_loss_metric = log_loss(pred_lr[['shot_made_flag']], pred_lr[['prediction_score_label_1']])
    LOGGER.info(f"F1 Score : {f1_metric}")
    LOGGER.info(f"Log loss: {log_loss_metric}")
    return {
        'F1 Score': {'value': f1_metric, 'step':1},
        'Log loss': {'value': log_loss_metric, 'step':1},
    }
	