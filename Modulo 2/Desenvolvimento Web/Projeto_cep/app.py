import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####
st.title("Buscar Cep")





##### Lista de Opções #####

##### BARRA LATERAL #####
st.sidebar.title("Busca Cep")
st.sidebar.image("Logo.png")
st.sidebar.markdown("Aplicação para buscar endereço a partir do CEP e mostrar a localização no mapa")
opcoes = ["Buscar CEP", "Descobrir CEP"]
opcao = st.sidebar.selectbox('escolha uma opcao',opcoes)

##### BOTÃO BUSCAR CEP #####
if opcao == "Buscar CEP":
   st.image('principal.png')
   st.header("Buscar Endereço pelo Cep")
   cep = st.text_input("Digite o Cep(somente números):")


   if st.button("Buscar"):
      if len(cep) != 8 or not cep.isdigit():
         st.error("Por  favor, insira um CEP vaálido com 8 dígitos numéricos.")
      else:
         try: 
            endereco = BuscarCep.buscar_cep(cep)
            if endereco:
               st.success("endereço encontrado:")
               st.write(f"CEP:{endereco[0]}")
               st.write(f"Endereço:{endereco[1]}")
               st.write(f"Bairro:{endereco[2]}")
               st.write(f"Cidade:{endereco[3]}")
               st.write(f"Estado:{endereco[4]}")


               ## Mapas
               st.title("Localização no Mapa")
               df = pd.DataFrame({"Latitude":[endereco[5]], "longitude": [endereco[6]]})
               st.map( df ,zoom=15)
            else:
               st.error("CEP não encontrato.")
         except Exception as e:
            st.error(f"Ocorreu um erro ao buscar o CEP: {e}")
               

##### BOTÃO DESCOBRIR CEP #####
elif opcao == 'Descobrir CEP':
   st.image('Descobrir.png')
   st.subheader('descobrir CEP pelo Endereço')
   endereco_usuario = st.text_input("Digite o endereço (ex: Rua olga , barueri, sp)")
   if st.button("Descobrir"):
      if not endereco_usuario.strip():
         st.error("Por favor, insira uma endereço válido.")
      else:
         try:
            resultado = BuscarCep.descobrir_cep(endereco_usuario)
            st.success("Link de buscar no Google:")    
            st.write(resultado)
         except Exception as e:
            st.error(f"Ocorreu um erro ao descobrir o CEP:{e}")  


