"""
This is a boilerplate pipeline 'PreparacaoDados'
generated using Kedro 0.18.6
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import load_data_kobe

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = load_data_kobe,
            inputs = None,
            # No Output vc coloca uma string do local onde vai salvar o resultado
            outputs='data_filtered',
            # Nome do nó
            name = "load_data_kobe"
        )
        
        
    ])
