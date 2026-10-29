import base64
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(RAIZ_DIR))

from engine import simular_cenario

st.set_page_config(
    page_title="ownStartup - Simulador Financeiro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', sans-serif !important;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

.sim-header {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.85) 0%, rgba(15, 23, 42, 0.95) 100%);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
}

.sim-title {
    margin: 0;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.sim-subtitle {
    margin: 6px 0 0 0;
    color: #94a3b8;
    font-size: 0.98rem;
}

div[data-testid="stMetric"] {
    background-color: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 14px;
    padding: 16px 20px;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    border-color: rgba(56, 189, 248, 0.4);
}
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
<div class="sim-header">
    <h1 class="sim-title">ownStartup · Simulador Financeiro</h1>
    <p class="sim-subtitle">Simulador determinístico de unit economics, fluxo de caixa e ponto de equilíbrio (Break-even).</p>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------
# 1. SIDEBAR: Logo & Cenários Rápidos
# -------------------------------------------------------------
gif_path = RAIZ_DIR / "assets" / "rocket_icon.gif"
if gif_path.exists():
    with open(gif_path, "rb") as f:
        gif_bytes = f.read()
    gif_b64 = base64.b64encode(gif_bytes).decode("utf-8")
    sidebar_gif_html = f"""
    <div style="text-align: center; margin-bottom: 15px;">
        <img src="data:image/gif;base64,{gif_b64}" width="115" style="filter: drop-shadow(0 4px 14px rgba(56,189,248,0.35));" />
    </div>
    """
    st.sidebar.markdown(sidebar_gif_html, unsafe_allow_html=True)

st.sidebar.markdown("### Cenários Pré-configurados")
cenario_escolhido = st.sidebar.selectbox(
    "Carregar parâmetros de referência:",
    [
        "Personalizado",
        "🌱 Early-Stage Bootstrap",
        "🚀 Hipercrescimento (SaaS)",
        "🛑 Risco Operacional / Burn Alto",
    ],
    index=0,
)

# Valores default por cenário
if cenario_escolhido == "🌱 Early-Stage Bootstrap":
    def_caixa, def_cli, def_novos, def_mens, def_cac, def_fixo, def_churn = (
        15000.0,
        15,
        8,
        150.0,
        40,
        1800.0,
        2.5,
    )
elif cenario_escolhido == "🚀 Hipercrescimento (SaaS)":
    def_caixa, def_cli, def_novos, def_mens, def_cac, def_fixo, def_churn = (
        60000.0,
        50,
        45,
        120.0,
        110,
        5000.0,
        3.0,
    )
elif cenario_escolhido == "🛑 Risco Operacional / Burn Alto":
    def_caixa, def_cli, def_novos, def_mens, def_cac, def_fixo, def_churn = (
        8000.0,
        10,
        5,
        80.0,
        160,
        3500.0,
        8.0,
    )
else:
    def_caixa, def_cli, def_novos, def_mens, def_cac, def_fixo, def_churn = (
        25000.0,
        20,
        12,
        100.0,
        50,
        1800.0,
        3.0,
    )

st.sidebar.markdown("---")
st.sidebar.markdown("### Parâmetros Operacionais")

caixa = st.sidebar.number_input(
    "Caixa Inicial (R$)", min_value=0.0, value=def_caixa, step=2500.0, format="%.2f"
)
clientes_iniciais = st.sidebar.number_input(
    "Clientes Iniciais", min_value=0, value=int(def_cli), step=5
)
novos_clientes = st.sidebar.slider(
    "Novos Clientes / Mês", min_value=1, max_value=200, value=int(def_novos)
)
mensalidade = st.sidebar.number_input(
    "Mensalidade (R$)", min_value=5.0, value=def_mens, step=10.0, format="%.2f"
)
cac = st.sidebar.slider(
    "CAC (Custo de Aquisição) (R$)",
    min_value=10,
    max_value=800,
    value=int(def_cac),
    step=5,
)
custos_fixos = st.sidebar.number_input(
    "Custos Fixos Mensais (R$)",
    min_value=0.0,
    value=def_fixo,
    step=200.0,
    format="%.2f",
)
churn_rate = st.sidebar.slider(
    "Taxa de Churn (%)", min_value=0.0, max_value=25.0, value=float(def_churn), step=0.5
)

# Execução da simulação
dados = simular_cenario(
    caixa_inicial=caixa,
    clientes_iniciais=int(clientes_iniciais),
    novos_clientes_mes=int(novos_clientes),
    mensalidade=mensalidade,
    CAC=cac,
    custos_fixos=int(custos_fixos),
    churn_rate=int(churn_rate),
    meses=12,
)

historico = dados["historico"]
runway = dados["runway"]
ltv_cac = dados["ltv_cac"]
ltv = dados["LTV"]
breakeven = dados["breakeven_mes"]
falencia = dados["falencia_mes"]
df_projecao = pd.DataFrame(historico)

# Cards

st.markdown("### Indicadores Principais")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if runway == float("inf"):
        st.metric(
            "Runway",
            "Sustentável",
            delta="Lucro Operacional",
            help="A receita mensal supera as despesas; não há consumo do caixa.",
        )
    else:
        st.metric(
            "Runway",
            f"{runway:.1f} meses",
            delta="Crítico (< 6m)" if runway < 6 else "Saudável (>= 6m)",
            delta_color="inverse" if runway < 6 else "normal",
            help="Tempo de sobrevida estimado do caixa bancário.",
        )

with c2:
    st.metric(
        "Razão LTV / CAC",
        f"{ltv_cac:.2f}x",
        delta="Eficiente (>= 3x)" if ltv_cac >= 3 else "Atenção (< 3x)",
        delta_color="normal" if ltv_cac >= 3 else "inverse",
        help=f"LTV: R$ {ltv:,.2f} | CAC: R$ {cac:,.2f}",
    )

with c3:
    mrr_12 = historico[-1]["Receita"]
    mrr_1 = historico[0]["Receita"]
    delta_mrr = ((mrr_12 - mrr_1) / mrr_1 * 100) if mrr_1 > 0 else 0
    st.metric("MRR (Mês 12)", f"R$ {mrr_12:,.2f}", delta=f"+{delta_mrr:.1f}% em 1 ano")

with c4:
    caixa_12 = historico[-1]["Caixa"]
    var_caixa = caixa_12 - caixa
    st.metric(
        "Caixa Final (Mês 12)",
        f"R$ {caixa_12:,.2f}",
        delta=f"R$ {var_caixa:,.2f}",
        delta_color="normal" if var_caixa >= 0 else "inverse",
    )

st.markdown("---")

# Diagnóstico

st.markdown("### Diagnóstico do Negócio")
col_diag1, col_diag2 = st.columns(2)

with col_diag1:
    if falencia is not None:
        st.error(
            f"**Esgotamento de Caixa Previsto no Mês {falencia}**: Seu capital disponível zera antes do final de 12 meses. É mandatório reduzir CAC ou custos fixos."
        )
    elif runway < 6:
        st.error(
            f"**Alerta Crítico de Runway ({runway:.1f} meses)**: O caixa atual durará menos de meio ano no ritmo de queima projetado."
        )
    else:
        st.success(
            f"**Reserva Operacional Segura ({runway:.1f} meses)**: Capacidade de absorver flutuações e financiar aquisição com margem."
        )

with col_diag2:
    if breakeven is not None:
        st.info(
            f"**Ponto de Equilíbrio (Break-even) Atingido no Mês {breakeven}**: A partir deste mês a receita mensal ultrapassa todas as despesas operacionais!"
        )
    elif ltv_cac < 3:
        st.warning(
            f"**Relação LTV/CAC Baixa ({ltv_cac:.2f}x)**: O retorno por cliente está muito próximo do custo de aquisição. O benchmark de segurança é $\\ge 3.0\\times$."
        )
    else:
        st.success(
            f"**Unit Economics Sustentáveis ({ltv_cac:.2f}x)**: Margem de contribuição saudável que permite acelerar marketing."
        )

st.markdown("---")

# Gráficos

st.markdown("### 📈 Evolução Temporal (12 Meses)")

tab_caixa, tab_receita_despesa, tab_clientes = st.tabs(
    [
        "💵 Saldo de Caixa",
        "⚖️ Receita vs. Despesas (Burn)",
        "👥 Evolução da Base de Clientes",
    ]
)

with tab_caixa:
    df_caixa = df_projecao.set_index("Mês")[["Caixa"]]
    st.line_chart(df_caixa)

with tab_receita_despesa:
    df_fluxo = df_projecao.set_index("Mês")[["Receita", "Despesas", "Burn"]]
    st.line_chart(df_fluxo)

with tab_clientes:
    df_cli = df_projecao.set_index("Mês")[["Clientes", "Cancelados"]]
    st.line_chart(df_cli)

with st.expander("📄 Ver Planilha Completa de Projeção Mês a Mês"):
    st.dataframe(
        df_projecao.style.format(
            {
                "Caixa": "R$ {:,.2f}",
                "Receita": "R$ {:,.2f}",
                "Despesas": "R$ {:,.2f}",
                "Burn": "R$ {:,.2f}",
                "Clientes": "{:d}",
                "Cancelados": "{:d}",
            }
        ),
        width="stretch",
    )
