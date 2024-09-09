import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.set_page_config(page_title="answers",page_icon="image/estatis.png", layout="wide")

with st.sidebar:
    st.write("Filtrar os dados")

def carrega_dados(uploaded_file):
    data = pd.read_csv(uploaded_file)
    return data

# ============================== header ===========================#
with st.container():
    col1,col2 = st.columns(spec=[0.7,0.3])
    with col1:
        st.title("Desempenho dos alunos")
    with col2:
        st.image("image/logoask2.png", width=150)
    st.subheader("Avaliar as respostas dos alunos e observar o desempenho deles nas respostas das questões objetivas e das discursivas.")
st.divider()
# ============================== dados ===========================#
st.header("Carregamento dos dados")

# ============================== dados ===========================#
st.subheader("As respostas dos alunos nas questões objetivas e discursivas")

uploaded_file = st.file_uploader("Escolha o arquivo csv")
st.divider()
# ====================================== upload do arquivo ========================== #
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    #data_carregado =
if st.sidebar.button("Dados"):
    st.subheader("Dados dos alunos")
    st.data_editor(data=dataframe)
# ====================================== botão da descrição ========================== #
if st.sidebar.button("Tipos de dados"):
    st.subheader("Tipos de dados")
    st.write('''
        Saber o tipo de dados é muito importante para a análise estística e, consequentemente, para definir o tipo de medida utilizar.
        ''')
    st.table(dataframe.dtypes)

# ========= radio button ===========#

st.sidebar.divider()
st.sidebar.write("Questões")
radio_opcoes = st.sidebar.radio("Selecione o tipo de questão", ("Discursiva", "Objetiva"),index=None)
with  st.container(border=True):
    if radio_opcoes == "Discursiva":
        st.write('''Tabela dos dados absolutos para as questões discursivas \n
         Interpretação de texto (A moça tecelã)
        * Questão 1 - Escreva de forma sintética a história que você leu.
        * Questão 2 - Qual a imagem de mulher é descrita nos diferentes momentos da narrativa?
        * Questão 3 - Quem foi o responsável pela mudança de vida da tecelã?
        ''')
        df1 = dataframe.groupby('Q_1')['Q_1'].size()
        df2 = dataframe.groupby('Q_2')['Q_2'].size()
        df3 = dataframe.groupby('Q_3')['Q_3'].size()
        df_merged_1 = pd.merge(df1, df2, left_index=True, right_index=True)
        df_merged_2 = pd.merge(df_merged_1, df2, left_index=True, right_index=True)
        df = pd.DataFrame(df_merged_2)
        map_colunas = {'Q_1': 'Questão 1', 'Q_2_x': 'Questão 2', 'Q_2_y': 'Questão 3'}
        df.columns = df.columns.map(map_colunas)
        #adiciona e soma os valores das colunas e das linhas
        df["Totais"] = df.sum(axis=1)
        df.loc["Totais"] = df.sum()
        st.table(df)
        st.divider()
        st.write("Gráficos dos dados absolutos para as questões objetivas")
        st.bar_chart(df,
                     x_label="Quantidade por questão",
                     y_label="Quantidade de ocorrências")

    elif radio_opcoes == "Objetiva":
        st.write('''Tabela dos dados absolutos para as questões objetivas \n
        Análise linguística e semiótica (A moça tecelã)
        * Questão 1 - A que classe de palavra pertencem as palavras destacas no texto? 
        a) Adjetivo
        b) substativo (correta) 
        c) Advérbio
        * Questão 2 - Qual é a função sintática das palavras destacas?
        a) Função de adjunto adnominal
        b) Função de adjunto adverbial
        c) Função de complemento (correta)
        * Questão 3 - Qual a função sintática da palavra mãe na sentença: A mãe foi reconhecida por todos.
        a) Sujeito passiente (correta)
        b) Sujeito ativo
        c) Complemento nominal
        ''')
        df1 = dataframe.groupby('Q_4')['Q_4'].size()
        df2 = dataframe.groupby('Q_5')['Q_5'].size()
        df3 = dataframe.groupby('Q_6')['Q_6'].size()
        df_merged_1 = pd.merge(df1, df2, left_index=True, right_index=True)
        df_merged_2 = pd.merge(df_merged_1, df2, left_index=True, right_index=True)
        df = pd.DataFrame(df_merged_2)
        map_colunas = {'Q_4': 'Questão 4', 'Q_5_x': 'Questão 5', 'Q_5_y': 'Questão 6'}
        df.columns = df.columns.map(map_colunas)
        df["Totais"] = df.sum(axis=1)
        df.loc["Totais"] = df.sum()
        st.table(df)
        st.divider()
        st.write("Gráficos dos dados absolutos para as questões objetivas")
        st.bar_chart(df,
                     x_label="Quantidade por questão",
                     y_label="Quantidade de ocorrências")

st.sidebar.divider()