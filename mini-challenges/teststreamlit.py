import streamlit as st

st.header("Começando no Streamlit")
st.title("Meu primeiro código Streamlit")
st.write("*Só escrevendo mais algo...*")

nome = st.text_input('Qual é o seu nome?')
if nome:
    st.write(f'Olá, {nome}!')

md = st.markdown("```\
escrevendo no bloco\
```")
img_md = st.image("https://s3.us-west-2.amazonaws.com/content.podia.com/o7q7latxjgv8seywsa8kkw13j8xb", caption="Logo Streamlit")

