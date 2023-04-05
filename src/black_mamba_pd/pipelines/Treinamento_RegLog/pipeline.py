"""
Pipeline 'Treinamento_RegLog'
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import treinamento_modelo_reglog,teste_modelo_reglog, metrics_modelo_reglog


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = treinamento_modelo_reglog,
            name = "treinamento_modelo_reglog",            
            inputs = ['base_train','params:random_state'],
            outputs='lr_model'
        ),
        node(
            func = teste_modelo_reglog,
            name = "teste_modelo_reglog",            
            inputs = ['lr_model','base_test'],
            outputs='pred_lr_model'
        ),
        node(
            func = metrics_modelo_reglog,
            name = "metrics_modelo_reglog",            
            inputs = 'pred_lr_model',
            outputs='modelo_reglog_metrics'
        ),
    ])