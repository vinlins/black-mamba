import streamlit as st 
import pandas as pd
import requests
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score, log_loss

url = 'http://localhost:5000/invocations'

def pagina_um_arremesso():
  st.header("Realize a inferência com base em dados de um arremesso")
  lat_arremesso = st.number_input("Digite a latitude do arremesso")
  lon_arremesso = st.number_input("Digite a longitude do arremesso")
  min_fim_periodo_arremesso = st.number_input("Digite os minutos que faltam para o fim do período")
  periodo_arremesso = st.number_input("Digite o período do jogo do arremesso")
  playoffs_arremesso_sn = st.radio("A partida era play off", ["Sim","Não"])
  if (playoffs_arremesso_sn == "Sim"):
    playoffs_arremesso = 1
  else:
    playoffs_arremesso = 0
  distancia_arremesso = st.number_input("Digite a distância do arremesso")
  if lat_arremesso and lon_arremesso and min_fim_periodo_arremesso and periodo_arremesso and playoffs_arremesso_sn and distancia_arremesso:
    if(st.button("Inferir arremesso")):
        data = {"dataframe_records": 
            [{'lat': lat_arremesso,
              'lon': lon_arremesso,
              'minutes_remaining': min_fim_periodo_arremesso,
              'period': periodo_arremesso,
              'playoffs':playoffs_arremesso,
              'shot_distance': distancia_arremesso}
            ]}
        results = requests.post(url, json = data)
        # results.status_code
        res = results.json()
        # st.text(results.json())
        res_arremesso = res['predictions'][0]
        if (res_arremesso == 0):
          st.error("Previsão de fracasso no arremesso")
        else:
          st.success("Previsão de sucesso no arremesso")

def pagina_varios_arremessos():
    st.title("Realize a inferência com base em dados de vários arremessos")
    uploaded_file = st.file_uploader("""Escolha um arquivo .csv com os dados de arremessos.
                                        Esses dados devem conter também a informação se o arremesso foi realizado
                                        com sucesso ou não. 
                                     """)
    if uploaded_file is not None:
      data_inference = pd.read_csv(uploaded_file)
      df_shot_flag = data_inference['shot_made_flag']
      data_inference.drop('shot_made_flag', axis = 1,inplace=True)
      results_inference = requests.post(url, json = {"dataframe_records": data_inference.to_dict(orient='records')})
      df_pred = pd.DataFrame(results_inference.json())
      st.write("**F1 Score**")
      st.text(f1_score(df_shot_flag, df_pred['predictions']))
      st.write("**Log Loss**")
      st.text(log_loss(df_shot_flag, df_pred['predictions']))      
      st.write("**Precisão**")
      st.text(precision_score(df_shot_flag, df_pred['predictions']))
      st.write("**Recall**")
      st.text(recall_score(df_shot_flag, df_pred['predictions']))
      cm = confusion_matrix(df_shot_flag, df_pred['predictions'])
      # Plot confusion matrix using matplotlib
      fig, ax = plt.subplots()
      im = ax.imshow(cm, cmap='Blues')

      ax.set_xlabel('Previsão do arremesso')
      ax.set_ylabel('Arremesso realizado')

      # Set tick labels for x and y axes
      ax.set_xticks([0, 1])
      ax.set_xticklabels(['Fracasso', 'Sucesso'])
      ax.set_yticks([0, 1])
      ax.set_yticklabels(['Fracasso', 'Sucesso'])
      for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
          ax.text(j, i, str(cm[i, j]), ha='center', va='center', color='black')


      # Set title for plot
      ax.set_title('Matriz de confusão')

      # Add colorbar
      cbar = ax.figure.colorbar(im, ax=ax)

      # Show plot in Streamlit app
      st.pyplot(fig)

      


st.sidebar.title("Inferências em arremessos")
paginaSelecionada = st.sidebar.selectbox("Selecione a página", ['Um arremesso', 'Arquivo com vários arremessos'])
if paginaSelecionada == 'Um arremesso':
  pagina_um_arremesso()
elif paginaSelecionada == 'Arquivo com vários arremessos':
    pagina_varios_arremessos()