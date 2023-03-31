"""
Pipeline 'PreparacaoDados'
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import load_data_kobe,conform_data_kobe, train_test_split_data_kobe

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
            inputs = 'data_conformed',
            outputs=['base_train','base_test'],
        )
    ])
