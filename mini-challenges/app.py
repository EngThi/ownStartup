import random

import streamlit as st
from exercises.funcC7.funcC7 import (
    calcular_estatisticas,
    detectar_anomalias,
    gerar_status,
)


# Helper functions
def maior_sequencia_consecutiva(nums):
    if not nums:
        return []
    sequencia_atual = [nums[0]]
    maior_sequencia = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            sequencia_atual.append(nums[i])
        else:
            if len(sequencia_atual) > len(maior_sequencia):
                maior_sequencia = sequencia_atual
            sequencia_atual = [nums[i]]

    if len(sequencia_atual) > len(maior_sequencia):
        maior_sequencia = sequencia_atual
    return maior_sequencia


def calcular_mediana(nums):
    if not nums:
        return 0
    ordenados = sorted(nums)
    n = len(ordenados)
    if n % 2 == 1:
        return ordenados[n // 2]
    else:
        return (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2


# Page configuration
st.set_page_config(
    page_title="ownStartup - Pattern Lab",
    page_icon="assets/code.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Technical & Clean CSS Styling
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

.lab-header {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 24px;
}

.lab-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin: 0;
    color: #f8fafc;
}

.lab-subtitle {
    margin: 4px 0 0 0;
    color: #cbd5e1;
    font-size: 0.95rem;
}

.module-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 15px;
    height: 100%;
}

.module-card h4 {
    color: #f1f5f9;
    font-size: 1.1rem;
    font-weight: 600;
    margin-top: 0;
    margin-bottom: 8px;
}

.module-card p {
    color: #e2e8f0 !important;
    font-size: 0.95rem;
    line-height: 1.5;
    margin: 0;
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

.status-badge {
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 600;
    font-size: 0.85rem;
    display: inline-block;
}
.status-normal {
    background-color: rgba(34, 197, 94, 0.2);
    color: #4ade80;
    border: 1px solid #22c55e;
}
.status-alerta {
    background-color: rgba(234, 179, 8, 0.2);
    color: #facc15;
    border: 1px solid #eab308;
}
.status-instavel {
    background-color: rgba(249, 115, 22, 0.2);
    color: #fb923c;
    border: 1px solid #f97316;
}
.status-critico {
    background-color: rgba(239, 68, 68, 0.2);
    color: #f87171;
    border: 1px solid #ef4444;
}
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
<div class="lab-header">
    <h1 class="lab-title">ownStartup | Pattern Lab</h1>
    <p class="lab-subtitle">Statistical analysis modules, time series anomaly detection, and technical documentation.</p>
</div>
""",
    unsafe_allow_html=True,
)

# Navigation Sidebar
st.sidebar.subheader("Navigation")
secao = st.sidebar.radio(
    "Modules:",
    [
        "Overview",
        "Anomaly Detector (Z-Score)",
        "Descriptive Statistics",
        "Signal Simulator",
        "Development Journal",
    ],
    index=0,
)

if "dados_entrada" not in st.session_state:
    st.session_state.dados_entrada = "12 15 14 13 16 15 52 14 13 15 8 14"

# Overview
if secao == "Overview":
    st.markdown("### System Architecture")
    st.write(
        "Pattern Lab gathers quantitative analysis routines implemented in pure Python to verify event streams, "
        "validate operational log statistics, and support decision modeling within the ownStartup ecosystem."
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
        <div class="module-card">
            <h4>Anomaly Detection (Z-Score)</h4>
            <p>
                Parametric deviation tracking relative to the sample mean. Identifies spikes in churn time series, service outages, or irregular traffic patterns.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="module-card">
            <h4>Descriptive Statistics</h4>
            <p>
                Calculates noise-resistant median, sample and population standard deviations, range, and linear consecutive sequence detection in O(N).
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="module-card">
            <h4>Synthetic Signal Generator</h4>
            <p>
                Controlled generation of synthetic sequences with stochastic anomaly injection to calibrate tolerance thresholds and evaluate false positives.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="module-card">
            <h4>Financial Simulator</h4>
            <p>
                Deterministic projection of cash runway, unit economics (LTV/CAC), and break-even points over a 12-month horizon. Access it via the sidebar.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Anomaly Detector
elif secao == "Anomaly Detector (Z-Score)":
    st.markdown("### Time Series Anomaly Detection")
    st.write(
        "Quantitative identification of statistical deviations relative to the historical baseline."
    )

    st.session_state.dados_entrada = st.text_input(
        "Numeric sequence (space-separated integers):",
        value=st.session_state.dados_entrada,
        help="Enter numeric values representing sequential event logs or metric records.",
    )

    limite = st.slider(
        "Z-Score Threshold:",
        min_value=0.5,
        max_value=3.5,
        value=1.5,
        step=0.1,
        help="Number of standard deviations from the mean before a data point is flagged as an anomaly.",
    )

    partes = st.session_state.dados_entrada.split()

    if not partes:
        st.info("Enter a sequence of numbers above to begin analysis.")
    elif not all(p.replace("-", "", 1).isdigit() for p in partes):
        st.error(
            "Invalid input. Please enter only space-separated integers."
        )
    else:
        dados = [int(p) for p in partes]
        total = len(dados)

        media, desvio = calcular_estatisticas(dados)
        resultados, anomalias = detectar_anomalias(dados, media, desvio, limite)
        status = gerar_status(total, anomalias)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total Records", total)
        with m2:
            st.metric("Sample Mean", f"{media:.2f}")
        with m3:
            st.metric("Standard Deviation", f"{desvio:.2f}")
        with m4:
            taxa_anomalias = (anomalias / total * 100) if total > 0 else 0
            st.metric("Detected Anomalies", f"{anomalias} ({taxa_anomalias:.1f}%)")

        st.markdown("---")

        badge_class = {
            "100% normal": "status-normal",
            "alerta": "status-alerta",
            "instável": "status-instavel",
            "crítico": "status-critico",
        }.get(status, "status-normal")

        status_en_label = {
            "100% normal": "NORMAL",
            "alerta": "ALERT",
            "instável": "UNSTABLE",
            "crítico": "CRITICAL",
        }.get(status, status.upper())

        st.markdown(
            f"**System Operational Status:** <span class='status-badge {badge_class}'>{status_en_label}</span>",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        col_g, col_t = st.columns([2, 1])
        with col_g:
            st.markdown("#### Series Chart")
            st.line_chart(dados)

        with col_t:
            st.markdown("#### Point-by-Point Classification")
            with st.container(height=280):
                for idx, (val, eh_anomalia) in enumerate(resultados):
                    if eh_anomalia:
                        st.markdown(f"**[{idx + 1:02d}]** `{val}` — Anomaly")
                    else:
                        st.markdown(f"**[{idx + 1:02d}]** `{val}` — Normal")

        relatorio_str = (
            "--------------------------------------------------\n"
            "        SIGNAL AUDIT REPORT - PATTERN LAB\n"
            "--------------------------------------------------\n"
            f"Total Samples: {total}\n"
            f"Detected Anomalies: {anomalias}\n"
            f"Mean: {media:.2f} | Standard Deviation: {desvio:.2f}\n"
            f"Operational Status: {status_en_label}\n"
            "--------------------------------------------------\n"
        )
        st.download_button(
            label="Download Report (.txt)",
            data=relatorio_str,
            file_name="signal_report_patternlab.txt",
            mime="text/plain",
        )

# Descriptive Statistics
elif secao == "Descriptive Statistics":
    st.markdown("### Statistical Analysis & Patterns")

    st.session_state.dados_entrada = st.text_input(
        "Numeric sequence:",
        value=st.session_state.dados_entrada,
    )

    partes = st.session_state.dados_entrada.split()

    if partes and all(p.replace("-", "", 1).isdigit() for p in partes):
        dados = [int(p) for p in partes]
        total = len(dados)

        media = sum(dados) / total
        mediana = calcular_mediana(dados)
        minimo = min(dados)
        maximo = max(dados)

        soma_quadrados = sum((x - media) ** 2 for x in dados)
        desvio_pop = (soma_quadrados / total) ** 0.5
        desvio_amostral = (soma_quadrados / (total - 1)) ** 0.5 if total > 1 else 0.0
        seq_consec = maior_sequencia_consecutiva(dados)

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Median", f"{mediana:.1f}")
            st.metric("Minimum Value", minimo)
        with c2:
            st.metric("Sample Std Dev (s)", f"{desvio_amostral:.3f}")
            st.metric("Maximum Value", maximo)
        with c3:
            st.metric("Population Std Dev (σ)", f"{desvio_pop:.3f}")
            st.metric("Total Range", maximo - minimo)
        with c4:
            st.metric("Longest Consecutive Run", f"{len(seq_consec)} elements")
            st.caption(f"Sequence: `{seq_consec}`")

        st.markdown("---")
        with st.expander("Algorithmic Definitions"):
            st.markdown(
                """
            - **Arithmetic Mean:** $\\mu = \\sum x_i / N$
            - **Sample Standard Deviation ($s$):** Bessel's correction applied ($N-1$) for unbiased variance estimation.
            - **Linear Tracking:** Deterministic $O(N)$ single-pass algorithm detecting consecutive runs where $x_i = x_{i-1} + 1$.
            """
            )
    else:
        st.warning("Please enter a valid sequence of integers.")

# Signal Simulator
elif secao == "Signal Simulator":
    st.markdown("### Synthetic Signal Generation & Validation")
    st.write(
        "Generate controlled numerical sequences with stochastic noise to benchmark detector sensitivity."
    )

    c_cfg1, c_cfg2 = st.columns(2)
    with c_cfg1:
        qtd_simular = st.slider("Sample Count", 10, 80, 30)
        media_simular = st.slider("Base Mean", 10, 100, 40)
    with c_cfg2:
        taxa_erros = st.slider("Anomaly Probability (%)", 0, 40, 15)
        limite_simular = st.slider("Detection Threshold (Z)", 0.5, 3.0, 1.2, 0.1)

    if st.button("Generate New Samples", type="primary"):
        st.session_state.seed_simulacao = random.randint(1, 99999)

    random.seed(st.session_state.get("seed_simulacao", 42))

    dados_simulados = []
    status_real = []

    for _ in range(qtd_simular):
        if random.random() < (taxa_erros / 100.0):
            ruido = random.choice([-1, 1]) * random.randint(25, 60)
            dados_simulados.append(media_simular + ruido)
            status_real.append(True)
        else:
            flutuacao = random.randint(-4, 4)
            dados_simulados.append(media_simular + flutuacao)
            status_real.append(False)

    media_calc, desvio_calc = calcular_estatisticas(dados_simulados)
    resultados_detec, anomalias_detec = detectar_anomalias(
        dados_simulados, media_calc, desvio_calc, limite_simular
    )

    tab_vis, tab_logs = st.tabs(["Chart View", "Classification Log"])

    with tab_vis:
        st.line_chart(dados_simulados)
        k1, k2, k3 = st.columns(3)
        with k1:
            st.metric("Total Generated", qtd_simular)
        with k2:
            st.metric("Injected Anomalies", sum(status_real))
        with k3:
            st.metric("Detected Anomalies", anomalias_detec)

    with tab_logs, st.container(height=300):
        for i, val in enumerate(dados_simulados):
            injetado = "Yes (Noise)" if status_real[i] else "No (Normal)"
            detectado = "Anomaly" if resultados_detec[i][1] else "Normal"
            st.markdown(
                f"**Point {i + 1:02d}:** value `{val}` | Injected: {injetado} | Detector: {detectado}"
            )

# Development Journal
elif secao == "Development Journal":
    st.markdown("### Technical Development Journal")
    st.caption("Chronological record of architecture decisions and engineering patterns.")

    with st.expander("Modules C1 & C2: File I/O and Robust Exception Handling"):
        st.markdown(
            """
        - Context manager (`with open(...)`) guarantees deterministic OS file descriptor release.
        - Strict exception handling (`FileNotFoundError`, `ValueError`) preventing runtime failure masking.
        """
        )

    with st.expander("Module C3: Consecutive Sequence Algorithm"):
        st.markdown(
            """
        - Single-pass $O(N)$ linear algorithm identifying longest contiguous runs without recursion.
        - Explicit state pointer and buffer management.
        """
        )

    with st.expander("Modules C4 & funcC7: Statistical Modeling & Z-Score"):
        st.markdown(
            """
        - Sample variance with Bessel's correction ($N-1$) vs. population variance ($N$).
        - Standardized metric normalization for deterministic outlier identification:
          $$Z = \\frac{x - \\mu}{\\sigma}$$
        - Pure, side-effect-free functions designed for straightforward unit testing.
        """
        )

    with st.expander("Modules C5 through C7: Modularization & Path Resolution"):
        st.markdown(
            """
        - Absolute path normalization via `pathlib.Path` relative to `__file__`, avoiding working directory (CWD) dependency.
        - Clean decoupling between analytical calculation routines and the Streamlit UI layer.
        """
        )

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>ownStartup | Quantitative Data & Engineering Lab</div>",
    unsafe_allow_html=True,
)
