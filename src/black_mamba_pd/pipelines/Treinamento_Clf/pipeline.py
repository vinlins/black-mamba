"""
Pipeline 'Treinamento_Clf'
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import treinamento_modelo_clf,teste_modelo_clf, metrics_modelo_clf


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = treinamento_modelo_clf,
            name = "treinamento_modelo_clf",            
            inputs = ['base_train','params:random_state'],
            outputs='clf_model'
        ),
        node(
            func = teste_modelo_clf,
            name = "teste_modelo_clf",            
            inputs = ['clf_model','base_test'],
            outputs='pred_clf_model'
        ),
        node(
            func = metrics_modelo_clf,
            name = "metrics_modelo_clf",            
            inputs = 'pred_clf_model',
            outputs='modelo_clf_metrics'
        ),
    ])