import streamlit as st

st.set_page_config(page_title="análise descritiva",page_icon="image/estatis.png", layout="wide")

# ============================== header ===========================#
with st.container():
    col1,col2 = st.columns(spec=[0.8, 0.2])
    with col1:
        st.title("Ferramenta estatística para o professor")
    with col2:
        st.image("image/estatis.png", width=150)
    st.subheader("Essa ferramenta auxilia o professor na prática avaliativa do ensino.")
st.divider()
with st.container():
    #st.write("Escolha")
    col3, col4 = st.columns(spec=[0.5, 0.5],vertical_alignment="center", gap="small")
    with col3:
        st.page_link("pages/measures_classroom.py", label="Avaliação das Turmas",use_container_width=True)
    with col4:
        st.page_link("pages/measures_answers.py", label="Avaliação dos alunos",use_container_width=True)

st.divider()
with st.container(border=True):
    st.write('''
        #### Informações gerais
        A avaliação do professor deve ser um processo reflexivo que analisa o desempenho do aluno e que produz estratégias de ensino para o professor. Nesse processo, é fundamental que o professor compare as respostas das atividades avaliativas dos alunos e das turmas, observando as semelhanças no desempenho e destacando as diferenças no aprendizado. Desse forma, o professor toma decisões sobre as técnicas de ensino e, ao mesmo tempo, elabora atividades compatíveis aos níveis de conhecimentos dos alunos. Pensando assim, uma abordagem avaliativa importante para a tomada de decisão do professor é a estatística descritiva. Através de dados quantitativos, é possível verificar se os objetivos pedagógicos traçados pelo professor foi satisfatório e o nível de aprendizagem dos alunos e das turmas. Essa prática beneficia tanto o professor, ao fornecer feedback construtivo para aprimorar suas práticas, quanto os alunos, ao garantir que eles estejam recebendo um ensino de qualidade.
        ''')
# =========================== Styles

st.markdown("""
<style>
    p {
    margin: 5px 5px ;
    padding: 20px;
    background-color: #F0F2F6;
    font-size: 1.25rem;
    font-weight: 400;
    text-align: center;
        }
    h1 {
    font-family: "Source Sans Pro", sans-serif;
    font-weight: 700;
    color: rgb(3.1, 61.6, 69.8);
    padding: 1.25rem 0px 1rem;
    margin: 0px;
    line-height: 1.2;
}
    h3 {
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 500;
        color: rgb(73.7, 35.7, 29.4);
        letter-spacing: -0.005em;
        padding: 0.5rem 0px 1rem;
        margin: 0px;
        line-height: 1.2;
}
.st-emotion-cache-ocqkz7 {
    display: flex;
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    -webkit-box-align: center;
    align-items: center;
    gap: 1rem;
}
a.st-emotion-cache-otndd2 {
    text-decoration: none;
    width: 335.5px;
    display: flex;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: start;
    justify-content: center;
    gap: 0.5rem;
    border-radius: 0.5rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    margin-top: 0.125rem;
    margin-bottom: 0.125rem;
    line-height: 2;
    background-color: transparent;
}
    a.st-emotion-cache-xtjyj5 {
    text-decoration: none;
    font-weight: 600;
    display: flex;
    flex-direction: row;
    -webkit-box-align: center;
    align-items: center;
    gap: 0.5rem;
    border-radius: 0.5rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    margin: 0.125rem 1.5rem;
    line-height: 2;
    color: rgb(85, 88, 103);
    background-color: rgba(151, 166, 195, 0.25);
}
</style> """, unsafe_allow_html=True)