import streamlit as st

st.set_page_config(
    page_title="Pattern Lab",
    page_icon="assets/code.svg",
    layout='wide'
)

esquerda, centro, direita = st.columns([1, 2, 3])

with centro:
    st.title("Análises com Python")
st.markdown("---")

st.sidebar.title("Opções")
secao = st.sidebar.selectbox(
    "Escolha uma seção",
    [
        "📈 Geral",
        "🔍 Detector de Anomalias",
        "📊 Estatísticas",
        "🧪 Simulador",
        "📘 Journal"
    ]
)

if secao == "📈 Geral":
    st.header("Pattern Lab")

    st.write("""
    Laboratório para estudar padrões,
    estatísticas e comportamento anormal em conjuntos de dados.
    """)