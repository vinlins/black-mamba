"""
Pipeline 'PreparacaoDados'
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import load_data_kobe,conform_data_kobe, train_test_split_data_kobe,metrics_preparacao_dados

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = load_data_kobe,
            name = "load_data_kobe",            
            inputs = 'raw_data_kobe',
            outputs='data_filtered',
        ),
        node(
            func = conform_data_kobe,
            name = "conform_data_kobe",            
            inputs = 'data_filtered',
            outputs='data_conformed',
        ),
        node(
            func = train_test_split_data_kobe,
            name = "train_test_split_data_kobe",            
            inputs = ['data_conformed','params:test_size'],
            outputs=['base_train','base_test'],
        ),
        node(
            func = metrics_preparacao_dados,
            name = "metrics_preparacao_dados",            
            inputs = ['data_conformed','base_train','base_test'],
            outputs='preparacao_dados_metrics',
        )
    ])
