# Projeto Black Mamba - Project Charter

## Plano de negócios

* Trata-se de uma competição de previsão promovida pelo site de *Kaggle* 
* Esta competição é adequada para praticar noções de classificação e 
visa também validar o conhecimento sobre Engenharia de Machine Learning

## Scope

* Kobe Bryant marcou sua aposentadoria da NBA marcando 60 pontos em seu último jogo 
como Los Angeles Laker na quarta-feira, 12 de abril de 2016. Convocado para a NBA 
aos 17 anos, Kobe ganhou os maiores prêmios do esporte ao longo de sua longa carreira.

* Usando 20 anos de dados sobre os arremessos e erros de Kobe, esse projeto visa prever 
quais arremessos chegarão ao fundo da rede? 

## Pessoal

* Inicialmente apenas uma pessoa participará desse projeto por ter 
um objetivo de validação de conhecimentos.
	
## Métricas

* Objetivo é conseguir modelo de classificação que preveja o sucesso no arremesso do
jogador de basquete Kobe Bryant.

* Serão utilizados as medidas de *F1 Score* e a medida de custo de *Log Loss* para avaliação dos modelos


## Arquitetura
* Dados
  * Os dados são fornecidos pelo site *Kaggle*.  
  * Esses dados contêm a localização e as circunstâncias de cada cesta de campo tentada por Kobe Bryant durante seus 20 anos de carreira.

* Ferramentas
  * Os modelos serão desenvolvidos em Python utilizando a IDE *VS Code* e publicados em repositório do *Github*
  * Serão utilizadas as biliotecas abaixo:  
    * Kedro: para organização do projetos e artefatos
    * Streamlit: para implementar uma interface com o objetivo de facilitar a inferência dos arremessos para novos conjuntos de dados  
    * MLflow: facilitar a reprodução e o compartilhamento de código de aprendizado de máquina, rastrear experimentos para entender melhor o desempenho do modelo e simplificar a implantação do modelo  
    * pyCaret: utilizado para treinar e avaliar os modelos de aprendizado de máquinas  
    * Scikit-Learn: utilizado na separação das bases de treino e teste, nas métricas de avaliação dos modelos utilizados (*F1 Score* e *Log Loss*)

* Provisionamento
  * Após o treinamento dos modelos, o melhor modelo deverá ser disponibilizado em uma API em que os clientes do modelo 
  possam acessá-lo de forma desacoplada.  
  * Será utilizada a ferramenta MLflow, citada acima, para essa finalidade.

## Comunicação
* A comunicação do resultado foi disponibilizada em um relatório na plataforma *Moodle*  para o instrutor da disciplina
Engenharia em Machine Learning. 