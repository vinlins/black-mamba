# Projeto Black Mamba

## I - Objetivo

Esse projeto tem por objetivo estruturar uma solução de Aprendizado de Máquina seguindo a metodologia 
TDSP (*Team Data Science Process*) para prever o sucesso ou não do arremesso do famoso jogador de basquete Kobe Briant.

As informações sobre os arremessos de Kobe Briant foram disponibilizadas pelo site 
[kaggle](https://www.kaggle.com/c/kobe-bryant-shot-selection/data).

O Projeto está estruturado utilizando a biblioteca do [Kedro](https://kedro.readthedocs.io) que, ao utilizar uma padronização 
própria na solução, facilita a modularização e o reaproveitamento do código.  

## II - Visão geral da solução

* O projeto está sendo publicado em repositório GitHub de nome [black-mamba](https://github.com/vinlins/black-mamba).  

* Serão produzidos dois modelos para prever os arremessos: modelo de Regressão Logística e modelo Support Vector Machine.

* Serão utilizados os dados de posição da quadra, distância, minutos que faltam para o fim da partida, o período do jogo e se o jogo 
valia pelos *Play Offs* ou não. A variável preditora é o sucesso ou não do arremesso. 


### II.1) Criação da solução

### II.2) Etapas de um projeto de IA

### II.3) Estruturação do projeto

O TDSP (*Team Data Science Process*) recomenda a existência de um formato padronizado para a soluçao e 
a bilioteca `Kedro` nos auxiliou nesse objetivo. Ela separa os artefatos da solução em pastas próprias 
para dados, documentação e código. Além disso, o `Kedro` organiza o código utilizando um formato de *nós* 
e *pipelines* (fluxos de nós contínuos). Ele também cria uma forma unificada de registro das fonte de dados 
carregadas e geradas durante o desenvolvimento da solução, além de poder também centralizar as informações 
dos parâmetros utilizados.

Conforme descrito na documentação do [Kedro](https://kedro.readthedocs.io), um *nó* circunda uma função 
Python pura que nomeia as entradas e saídas dela. Assim, "os *nós* são o bloco de construção de um pipeline e 
a saída de um nó pode ser a entrada de outro". Enquanto um *pipeline* "organiza as dependências e a 
ordem de execução de uma coleção de *nós* e conecta entradas e saídas enquanto mantém seu código modular. 
O *pipeline* determina a ordem de execução do *nó* resolvendo as dependências e não necessariamente executa 
os *nós* na ordem em que são transmitidos."

Nesse projeto criou-se um pipeline de processamento de dados ("PreparacaoDados") e um para 
o treinamento do modelo, com esse mesmo nome.  


### II.4) Ferramentas

### II.5) Artefatos

## III - Desenvolvimento da Solução

### III.1) Preparação dos dados

Os seguintes dados relacionados ao arremesso efetuado serão utilizados na modelagem:  

* `lat`:  latitude do arremesso - (variável contínua)  
* `lon`:  logitude do arremesso - (variável contínua)   
* `minutes_remaining`: minutos que faltam para o fim do período (1 a 11 min)  - (variável contínua)  
* `period`: o período do jogo do arremesso. Um jogo de basquete possui, na NBA (*National Basketball Association*) ou liga internacional, 4 períodos de 12 minutos. Em caso de empate pode haver mais alguns períodos de 5 minutos para desempatar. (variável categórica)   
* `playoffs`: se a partida era dos *playoffs* ou não - (variável booleana e categórica)
* `shot_distance`: distância do arremesso - (variável contínua)    
* `shot_made_flag`: Se o arremesso foi bem sucedido ou não (variável booleana categórica - preditora da classificação)

### III.2) Treinamento

### III.3) Produção

### III.4) Monitoramento

## IV - Conclusão
