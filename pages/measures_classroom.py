import streamlit as st
import pandas as pd
st.set_page_config(page_title="classroom",page_icon="image/estatis.png", layout="wide")
with st.sidebar:
    st.write("Filtrar os dados")

def carrega_dados(uploaded_file):
    data = pd.read_csv(uploaded_file)
    return data

# ============================== header ===========================#
with st.container():
    col1,col2 = st.columns(spec=[0.7,0.3])
    with col1:
        st.title("Desempenho das turmas")
    with col2:
        st.image("image/logoclassroom.png", width=150)
    st.subheader("Ferramenta de avaliação para o ensino do português")
st.divider()
# ============================== dados ===========================#
st.header("Carregamento dos dados")
#uploaded_file = st.file_uploader(label="Escolha o arquivo",)

#read_file = pd.read_csv(uploaded_file)

# ============================== dados ===========================#
st.header("Avaliação de turmas e disciplinas")

uploaded_file = st.file_uploader("Escolha o arquivo csv")

# ====================================== upload do arquivo ========================== #
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file,sep=";")
    # convertendo os dados
    dataframe['unidade_3'] = dataframe['unidade_3'].apply(lambda x: x.replace(',', '.'))
    dataframe['unidade_1'] = dataframe['unidade_1'].apply(lambda x: x.replace(',', '.'))
    dataframe['unidade_2'] = dataframe['unidade_2'].apply(lambda x: x.replace(',', '.'))
    dataframe['M_final'] = dataframe['M_final'].apply(lambda x: x.replace(',', '.'))
    dataframe['unidade_3'] = dataframe['unidade_3'].astype(float)
    dataframe['unidade_1'] = dataframe['unidade_1'].astype(float)
    dataframe['unidade_2'] = dataframe['unidade_2'].astype(float)
    dataframe['M_final'] = dataframe['M_final'].astype(float)
    st.data_editor(dataframe)

# ====================================== botão da descrição ========================== #
if st.sidebar.button("Tipos de dados"):
    st.subheader("Tipos de dados")
    st.write('''
    Saber o tipo de dados é muito importante para a análise estística e, consequentemente, para definir o tipo de medida utilizar.
    ''')
    st.write(dataframe.dtypes)

if st.sidebar.button("Descrição dos dados"):
    st.write("#### Descrição dos dados")
    with st.container(border=2):
        col1, col2= st.columns(2)
        with col1:
            st.write("* #### Média das notas")
            mean_unidade1 = st.text(f'Na unidade 1 é {dataframe['unidade_1'].mean().round(3)}')
            mean_unidade2 = st.text(f'Na unidade 2 é {dataframe['unidade_2'].mean().round(3)}')
            mean_unidade3 = st.text(f'Na unidade 3 é {dataframe['unidade_3'].mean().round(3)}')
            mean_notafinal = st.text(f'Nota final é {dataframe['M_final'].mean().round(3)}')

            st.write("* #### Mediana das notas")
            median_unidade1 = st.text(f'Na unidade 1 é {dataframe['unidade_1'].median().round(3)}')
            median_unidade2 = st.text(f'Na unidade 2 é {dataframe['unidade_2'].median().round(3)}')
            median_unidade3 = st.text(f'Na unidade 3 é {dataframe['unidade_3'].median().round(3)}')
            median_notafinal = st.text(f'Nota final é {dataframe['M_final'].median().round(3)}')

        with col2:
            st.write("* #### Desvio padrão")
            std_unidade1 = st.text(f'Na unidade 1 é {dataframe['unidade_1'].std().round(3)}')
            std_unidade2 = st.text(f'Na unidade 2 é {dataframe['unidade_2'].std().round(3)}')
            std_unidade3 = st.text(f'Na unidade 3 é {dataframe['unidade_3'].std().round(3)}')
            std_notafinal = st.text(f'Nota final é {dataframe['M_final'].std().round(3)}')

# ====================================== radios button ========================== #
st.sidebar.divider()
radio_item = dataframe.dtypes.index
radio_quali = st.sidebar.radio("Filtrar os dados por:",radio_item[5:8],index=None)
radio_quanti = st.sidebar.radio("Opções quantitativas",radio_item[1:5],index=None)

# ====================== valores qualititivos ===========================#
if radio_quali == "status":
    grupo_status = dataframe.groupby("status")
    with st.container(border=True):
        col3, col4 = st.columns([0.5,0.5])
        with col3:
            st.write(f"#### Análise da variável {radio_item[5]}")
        with col4:
            item_selected = st.multiselect("Escolha os valores", grupo_status)
        data_selected = st.data_editor(dataframe.query(f"status == {item_selected}"))
        # Criar os gráficos

if radio_quali == "Semestre":
    grupo_status = dataframe.groupby("Semestre")
    with st.container(border=True):
        col3, col4 = st.columns([0.5,0.5])
        with col3:
            st.write(f"#### Análise da variável {radio_item[6]}")
        with col4:
            item_selected = st.multiselect("Escolha os valores", grupo_status)
        data_selected = st.data_editor(dataframe.query(f"Semestre == {item_selected}"))
        # Criar os gráficos

if radio_quali == "Disciplina":
    grupo_status = dataframe.groupby("Disciplina")
    with st.container(border=True):
        col3, col4 = st.columns([0.5,0.5])
        with col3:
            st.write(f"#### Análise da variável {radio_item[7]}")
        with col4:
            item_selected = st.multiselect("Escolha os valores", grupo_status)
        data_selected = st.data_editor(dataframe.query(f"Disciplina == {item_selected}"))
        # Criar os gráficos
# ====================== valores quantitativos ===========================#
if radio_quanti == "unidade_1":
    with st.container(border=True):
        #valor_inicial = dataframe["unidade_1"].min()
        #valor_final = dataframe["unidade_1"].max()
        col3, col4 = st.columns([0.6, 0.4])
        with col3:
            st.write(f"#### Análise da variável {radio_item[1]}")
        with col4:
            slider_value = st.slider("Escolha os valores",min_value=0.0, max_value= 10.0,  value=(5.0,7.0) )
        st.data_editor(dataframe.loc[slider_value[0]:slider_value[1]])
        #st.write("Valores", slider_value)

st.divider()