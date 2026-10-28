import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from engine import simular_cenario

sys.path.append(str(Path(__file__).resolve().parent.parent))

caixa = st.sidebar.number_input("Caixa inicial: ", value=1000.0)
cac = st.sidebar.slider("CAC", min_value=10, max_value=500, value=50)
clientes_iniciais = st.sidebar.number_input("Quantidade de clientes: ", 0, 20, 1)
novos_clientes = st.sidebar.number_input("Novos clientes: ", 0, 10, 1)

dados = simular_cenario(caixa, int(clientes_iniciais), int(novos_clientes), 100, cac)

historico = dados["historico"]
runway = dados["runway"]
ltv_cac = dados["ltv_cac"]
df_projecao = pd.DataFrame(historico)

# Aparece na tela
st.subheader("📊 Indicadores")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if runway == float("inf"):
        st.metric("Runway", "Sustentável")
    else:
        st.metric("Runway", f"{runway:.1f} meses")

with col2:
    st.metric("Razão LTV/CAC", f"{ltv_cac:.1f}x")

with col3:
    mrr_final = historico[-1]["Receita"]
    st.metric("MRR", f"{mrr_final:.2f}")

with col4:
    caixa_final = historico[-1]["Caixa"]
    st.metric("Caixa projetado", f"{caixa_final:,.2f}")

st.markdown("---")

st.subheader("Diagnóstico negócio")
if runway < 6:
    st.error(f"Alerta crítico: Runway de apenas {runway} meses!")
elif ltv_cac < 3:
    st.warning(f"Atenção {ltv_cac:.2f}x está abaixo do ideal (3x")
else:
    st.success("Métricas operacionais")

st.markdown("---")

st.subheader("Projeção 12 meses")
df_chart = df_projecao.set_index("Mês")[["Caixa", "Receita"]]
st.line_chart(df_chart)

with st.expander("ver tabela detalhada mês a mês"):
    st.dataframe(df_projecao)
