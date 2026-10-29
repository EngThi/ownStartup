import base64
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

RAIZ_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(RAIZ_DIR))

from engine import simular_cenario

st.set_page_config(
    page_title="ownStartup - Financial Simulator",
    page_icon="assets/code.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

.sim-header {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 24px;
}

.sim-title {
    margin: 0;
    font-size: 1.8rem;
    font-weight: 700;
    color: #f8fafc;
}

.sim-subtitle {
    margin: 4px 0 0 0;
    color: #cbd5e1;
    font-size: 0.95rem;
}

div[data-testid="stMetric"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 14px 18px;
}

div[data-testid="stMetric"] label {
    color: #94a3b8 !important;
    font-size: 0.85rem !important;
}

div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-weight: 700 !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
<div class="sim-header">
    <h1 class="sim-title">ownStartup | Financial Simulator</h1>
    <p class="sim-subtitle">Deterministic modeling of unit economics, net cash burn, and operational break-even points.</p>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------
# 1. SIDEBAR: Parameters & Presets
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

st.sidebar.markdown("### Reference Presets")
cenario_escolhido = st.sidebar.selectbox(
    "Load reference profile:",
    [
        "Custom",
        "Early-Stage Bootstrap",
        "High Growth (SaaS)",
        "Operational Risk / High Burn",
    ],
    index=0,
)

# Default values per preset
if cenario_escolhido == "Early-Stage Bootstrap":
    def_caixa, def_cli, def_novos, def_mens, def_cac, def_fixo, def_churn = (
        15000.0,
        15,
        8,
        150.0,
        40,
        1800.0,
        2.5,
    )
elif cenario_escolhido == "High Growth (SaaS)":
    def_caixa, def_cli, def_novos, def_mens, def_cac, def_fixo, def_churn = (
        60000.0,
        50,
        45,
        120.0,
        110,
        5000.0,
        3.0,
    )
elif cenario_escolhido == "Operational Risk / High Burn":
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
st.sidebar.markdown("### Operational Parameters")

caixa = st.sidebar.number_input(
    "Starting Cash ($)", min_value=0.0, value=def_caixa, step=2500.0, format="%.2f"
)
clientes_iniciais = st.sidebar.number_input(
    "Initial Customers", min_value=0, value=int(def_cli), step=5
)
novos_clientes = st.sidebar.slider(
    "New Customers / Month", min_value=1, max_value=200, value=int(def_novos)
)
mensalidade = st.sidebar.number_input(
    "Average Monthly Price ($)", min_value=5.0, value=def_mens, step=10.0, format="%.2f"
)
cac = st.sidebar.slider(
    "Customer Acquisition Cost (CAC) ($)",
    min_value=10,
    max_value=800,
    value=int(def_cac),
    step=5,
)
custos_fixos = st.sidebar.number_input(
    "Monthly Fixed Costs ($)",
    min_value=0.0,
    value=def_fixo,
    step=200.0,
    format="%.2f",
)
churn_rate = st.sidebar.slider(
    "Monthly Churn Rate (%)", min_value=0.0, max_value=25.0, value=float(def_churn), step=0.5
)

# Run simulation
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

# Build projection DataFrame with English columns for display
df_projecao = pd.DataFrame(historico)
df_display = df_projecao.rename(
    columns={
        "Mês": "Month",
        "Caixa": "Cash",
        "Receita": "Revenue",
        "Despesas": "Expenses",
        "Burn": "Net Burn",
        "Clientes": "Customers",
        "Cancelados": "Churned",
    }
)

# -------------------------------------------------------------
# 2. KEY METRIC CARDS
# -------------------------------------------------------------
st.markdown("### Key Metrics")
c1, c2, c3, c4 = st.columns(4)

with c1:
    if runway == float("inf"):
        st.metric(
            "Runway",
            "Sustainable",
            delta="Profitable",
            help="Monthly revenue exceeds total expenses; zero cash burn.",
        )
    else:
        st.metric(
            "Runway",
            f"{runway:.1f} months",
            delta="Critical (< 6m)" if runway < 6 else "Safe Buffer (>= 6m)",
            delta_color="inverse" if runway < 6 else "normal",
            help="Estimated cash exhaustion horizon based on current net burn.",
        )

with c2:
    st.metric(
        "LTV / CAC Ratio",
        f"{ltv_cac:.2f}x",
        delta="Efficient (>= 3x)" if ltv_cac >= 3 else "Below Target (< 3x)",
        delta_color="normal" if ltv_cac >= 3 else "inverse",
        help=f"Estimated LTV: ${ltv:,.2f} | CAC: ${cac:,.2f}",
    )

with c3:
    mrr_12 = historico[-1]["Receita"]
    mrr_1 = historico[0]["Receita"]
    delta_mrr = ((mrr_12 - mrr_1) / mrr_1 * 100) if mrr_1 > 0 else 0
    st.metric("MRR (Month 12)", f"${mrr_12:,.2f}", delta=f"+{delta_mrr:.1f}% YoY")

with c4:
    caixa_12 = historico[-1]["Caixa"]
    var_caixa = caixa_12 - caixa
    st.metric(
        "Final Cash (Month 12)",
        f"${caixa_12:,.2f}",
        delta=f"${var_caixa:,.2f}",
        delta_color="normal" if var_caixa >= 0 else "inverse",
    )

st.markdown("---")

# -------------------------------------------------------------
# 3. OPERATIONAL DIAGNOSTIC
# -------------------------------------------------------------
st.markdown("### Operational Diagnostic")
col_diag1, col_diag2 = st.columns(2)

with col_diag1:
    if falencia is not None:
        st.error(
            f"**Cash Depletion Projected in Month {falencia}**: Capital reserve reaches zero before month 12. Adjust CAC or reduce fixed burn to prevent insolvency."
        )
    elif runway < 6:
        st.error(
            f"**Critical Runway Warning ({runway:.1f} months)**: Current reserve provides less than 6 months of operational runway."
        )
    else:
        st.success(
            f"**Secure Operating Reserve ({runway:.1f} months)**: Stable financial buffer to absorb market shifts and fund acquisition."
        )

with col_diag2:
    if breakeven is not None:
        st.info(
            f"**Operational Break-even Reached in Month {breakeven}**: Monthly revenue fully covers recurring fixed and variable expenses."
        )
    elif ltv_cac < 3:
        st.warning(
            f"**Low LTV/CAC Ratio ({ltv_cac:.2f}x)**: Customer lifetime value is compressed relative to acquisition cost. Market benchmark is $\\ge 3.0\\times$."
        )
    else:
        st.success(
            f"**Sustainable Unit Economics ({ltv_cac:.2f}x)**: Healthy customer margins supporting scalable customer acquisition."
        )

st.markdown("---")

# -------------------------------------------------------------
# 4. TEMPORAL CHARTS (12-MONTH HORIZON)
# -------------------------------------------------------------
st.markdown("### 12-Month Projection")

tab_caixa, tab_receita_despesa, tab_clientes = st.tabs(
    [
        "💵 Cash Balance",
        "⚖️ Revenue vs. Expenses (Burn)",
        "👥 Customer Base Growth",
    ]
)

with tab_caixa:
    df_chart_cash = df_display.set_index("Month")[["Cash"]]
    st.line_chart(df_chart_cash)

with tab_receita_despesa:
    df_chart_flow = df_display.set_index("Month")[["Revenue", "Expenses", "Net Burn"]]
    st.line_chart(df_chart_flow)

with tab_clientes:
    df_chart_customers = df_display.set_index("Month")[["Customers", "Churned"]]
    st.line_chart(df_chart_customers)

with st.expander("📄 View Full Month-by-Month Projection Table"):
    st.dataframe(
        df_display.style.format(
            {
                "Cash": "${:,.2f}",
                "Revenue": "${:,.2f}",
                "Expenses": "${:,.2f}",
                "Net Burn": "${:,.2f}",
                "Customers": "{:d}",
                "Churned": "{:d}",
            }
        ),
        width="stretch",
    )
