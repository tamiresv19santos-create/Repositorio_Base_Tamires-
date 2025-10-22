# import streamlit as st

# # aqui é o primordial, sempre precisamos criar o servidor 

# # python -m streamlit run app.py

# ## aqui eu coloco o titulo
# st.title('Olá, mundo')

# #criando um calendário 
# date = st.date_input("selecione uma Data")

# #permitindo o upload do arquivo
# file = st.file_uploader("Mande fotos salientes.... trakinagens")


import streamlit as st
import pandas as pd


 ### python -m streamlit run app.py

#------------------------------------------------------ Sidebar

st.sidebar.image("Logo.png")
st.sidebar.title('VIHEXPRESS')

carros = ['hb20s','jeep','gol','toro', 'fusca']

opcao = st.sidebar.selectbox('Escolha um carro que foi alugado', carros)


#-----------------------------------------------------------------Principal 
st.title('Viih Express - aluguel de carros')

st.image(f'{opcao}.png')
st.markdown(f'##Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f"por quantos dias o {opcao}foi alugado?")
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'hb20s':
    diaria = 50

elif opcao == 'jeep':
    diaria = 600

elif opcao == 'gol':
    diaria = 100

elif opcao == 'toro':
    diaria = 900

elif opcao == 'fusca':
    diaria = 100



if st. button('Calcular'):
    dias = int(dias)  
    km = float(km) 


    total_dias = dias * diaria
    total_km = km * 1.5
    aluguel_total = total_dias+total_km

    st.warning(f'você alugou o { opcao} por {dias} dias e rodou {km}km. o valor totala pagar é R${aluguel_total:.2f}')