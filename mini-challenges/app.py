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

# CSS Customizado Técnico & Profissional (sem cores apagadas)
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

/* Header técnico e direto */
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

/* Cards com alto contraste e legibilidade */
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

/* Métricas limpas */
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

/* Badges de Status Operacional */
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
    <p class="lab-subtitle">Módulos de análise estatística, detecção de anomalias em séries temporais e documentação técnica.</p>
</div>
""",
    unsafe_allow_html=True,
)

# Navigation Sidebar
st.sidebar.subheader("Navegação")
secao = st.sidebar.radio(
    "Módulos:",
    [
        "Visão Geral",
        "Detector de Anomalias (Z-Score)",
        "Estatística Descritiva",
        "Simulador de Sinais",
        "Diário de Desenvolvimento",
    ],
    index=0,
)

if "dados_entrada" not in st.session_state:
    st.session_state.dados_entrada = "12 15 14 13 16 15 52 14 13 15 8 14"

# Geral

if secao == "Visão Geral":
    st.markdown("### Arquitetura do Sistema")
    st.write(
        "O Pattern Lab reúne rotinas de análise quantitativa implementadas em Python puro para verificação de fluxos de eventos, "
        "validação estatística de logs e modelagem de sustentabilidade operacional no ecossistema do ownStartup."
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
        <div class="module-card">
            <h4>Detecção de Anomalias (Z-Score)</h4>
            <p>
                Cálculo de desvio paramétrico em relação à média amostral. Identifica desvios em séries temporais de churn, falhas em serviços ou oscilações atípicas de tráfego.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="module-card">
            <h4>Estatística Descritiva</h4>
            <p>
                Determinação de mediana resistente a ruídos, desvio padrão amostral e populacional, amplitude e rastreamento linear de sequências contínuas em O(N).
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="module-card">
            <h4>Gerador de Sinais Sintéticos</h4>
            <p>
                Geração controlada de dados com injeção probabilística de desvios para validação de limites de tolerância e calibração de falsos positivos.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
        <div class="module-card">
            <h4>Simulador Financeiro</h4>
            <p>
                Projeção determinística de fluxo de caixa, tempo de sobrevida (Runway), unit economics (LTV/CAC) e ponto de equilíbrio nos próximos 12 meses. Acesse pela barra lateral.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

# Detector Anomalias

elif secao == "Detector de Anomalias (Z-Score)":
    st.markdown("### Detecção de Anomalias em Séries Temporais")
    st.write(
        "Identificação quantitativa de desvios em relação à média histórica do fluxo de dados."
    )

    st.session_state.dados_entrada = st.text_input(
        "Sequência numérica (valores inteiros separados por espaço):",
        value=st.session_state.dados_entrada,
        help="Insira valores numéricos representando registros cronológicos.",
    )

    limite = st.slider(
        "Limiar de Desvio (Z-Score Threshold):",
        min_value=0.5,
        max_value=3.5,
        value=1.5,
        step=0.1,
        help="Distância em desvios-padrão a partir da qual o evento é considerado fora da normalidade.",
    )

    partes = st.session_state.dados_entrada.split()

    if not partes:
        st.info("Insira uma sequência de dados para iniciar a análise.")
    elif not all(p.replace("-", "", 1).isdigit() for p in partes):
        st.error(
            "Entrada inválida. Utilize apenas números inteiros separados por espaço."
        )
    else:
        dados = [int(p) for p in partes]
        total = len(dados)

        media, desvio = calcular_estatisticas(dados)
        resultados, anomalias = detectar_anomalias(dados, media, desvio, limite)
        status = gerar_status(total, anomalias)

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Total de Registros", total)
        with m2:
            st.metric("Média Amostral", f"{media:.2f}")
        with m3:
            st.metric("Desvio Padrão", f"{desvio:.2f}")
        with m4:
            taxa_anomalias = (anomalias / total * 100) if total > 0 else 0
            st.metric("Anomalias Detectadas", f"{anomalias} ({taxa_anomalias:.1f}%)")

        st.markdown("---")

        badge_class = {
            "100% normal": "status-normal",
            "alerta": "status-alerta",
            "instável": "status-instavel",
            "crítico": "status-critico",
        }.get(status, "status-normal")

        st.markdown(
            f"**Status Operacional da Série:** <span class='status-badge {badge_class}'>{status.upper()}</span>",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        col_g, col_t = st.columns([2, 1])
        with col_g:
            st.markdown("#### Gráfico da Série")
            st.line_chart(dados)

        with col_t:
            st.markdown("#### Classificação por Ponto")
            with st.container(height=280):
                for idx, (val, eh_anomalia) in enumerate(resultados):
                    if eh_anomalia:
                        st.markdown(f"**[{idx + 1:02d}]** `{val}` — Anômalo")
                    else:
                        st.markdown(f"**[{idx + 1:02d}]** `{val}` — Normal")

        relatorio_str = (
            "--------------------------------------------------\n"
            "        RELATÓRIO DE SINAIS - PATTERN LAB\n"
            "--------------------------------------------------\n"
            f"Total de Amostras: {total}\n"
            f"Anomalias Identificadas: {anomalias}\n"
            f"Média: {media:.2f} | Desvio Padrão: {desvio:.2f}\n"
            f"Classificação: {status}\n"
            "--------------------------------------------------\n"
        )
        st.download_button(
            label="Baixar Relatório (.txt)",
            data=relatorio_str,
            file_name="relatorio_sinais_patternlab.txt",
            mime="text/plain",
        )


# Descrição estatísticas

elif secao == "Estatística Descritiva":
    st.markdown("### Análise Estatística e Padrões Numéricos")

    st.session_state.dados_entrada = st.text_input(
        "Sequência numérica:",
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
            st.metric("Mediana", f"{mediana:.1f}")
            st.metric("Valor Mínimo", minimo)
        with c2:
            st.metric("Desvio Amostral (s)", f"{desvio_amostral:.3f}")
            st.metric("Valor Máximo", maximo)
        with c3:
            st.metric("Desvio Populacional (σ)", f"{desvio_pop:.3f}")
            st.metric("Amplitude Total", maximo - minimo)
        with c4:
            st.metric("Maior Sequência Contínua", f"{len(seq_consec)} elementos")
            st.caption(f"Subconjunto: `{seq_consec}`")

        st.markdown("---")
        with st.expander("Definições Algorítmicas"):
            st.markdown(
                """
            - **Média Aritmética:** $\\mu = \\sum x_i / N$
            - **Desvio Padrão Amostral ($s$):** Aplicação de correção de Bessel ($N-1$) para estimativa não viesada da variância.
            - **Rastreamento Linear:** Algoritmo determinístico com complexidade temporal $O(N)$ para identificar cadeias ordenadas onde $x_i = x_{i-1} + 1$.
            """
            )
    else:
        st.warning("Insira uma sequência de inteiros válida.")

# Simulador de sinais

elif secao == "Simulador de Sinais":
    st.markdown("### Geração e Teste de Sinais Sintéticos")
    st.write(
        "Criação de séries numéricas com ruído controlado para aferir sensibilidade do modelo de detecção."
    )

    c_cfg1, c_cfg2 = st.columns(2)
    with c_cfg1:
        qtd_simular = st.slider("Quantidade de Amostras", 10, 80, 30)
        media_simular = st.slider("Média Base", 10, 100, 40)
    with c_cfg2:
        taxa_erros = st.slider("Probabilidade de Anomalia (%)", 0, 40, 15)
        limite_simular = st.slider("Limiar Z de Detecção", 0.5, 3.0, 1.2, 0.1)

    if st.button("Gerar Nova Amostra", type="primary"):
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

    tab_vis, tab_logs = st.tabs(["Visualização Gráfica", "Log de Classificação"])

    with tab_vis:
        st.line_chart(dados_simulados)
        k1, k2, k3 = st.columns(3)
        with k1:
            st.metric("Total de Amostras", qtd_simular)
        with k2:
            st.metric("Anomalias Inseridas", sum(status_real))
        with k3:
            st.metric("Anomalias Detectadas", anomalias_detec)

    with tab_logs, st.container(height=300):
        for i, val in enumerate(dados_simulados):
            injetado = "Sim (Ruído)" if status_real[i] else "Não (Normal)"
            detectado = "Anomalia" if resultados_detec[i][1] else "Normal"
            st.markdown(
                f"**Ponto {i + 1:02d}:** valor `{val}` | Injeção: {injetado} | Detector: {detectado}"
            )


# Journal legado

elif secao == "Diário de Desenvolvimento":
    st.markdown("### Diário Técnico de Desenvolvimento")
    st.caption("Documentação cronológica da arquitetura e das decisões de engenharia.")

    with st.expander("Módulos C1 e C2: I/O de Arquivos e Tratamento de Exceções"):
        st.markdown(
            """
        - Implementação de context managers (`with open(...)`) garantindo fechamento e liberação de descritores no sistema operacional.
        - Tratamento estrito de exceções (`FileNotFoundError`, `ValueError`) sem capturas genéricas que ocultem falhas de runtime.
        """
        )

    with st.expander("Módulo C3: Algoritmo de Sequências Consecutivas"):
        st.markdown(
            """
        - Rastreamento linear $O(N)$ em espaço contíguo para identificação de maiores subsequências sem recursão.
        - Controle explícito de buffers temporários e ponteiros de estado.
        """
        )

    with st.expander("Módulos C4 e funcC7: Modelagem Estatística e Z-Score"):
        st.markdown(
            """
        - Cálculo de variância amostral com correção de Bessel ($N-1$) e populacional ($N$).
        - Normalização de desvio padronizado para classificação determinística:
          $$Z = \\frac{x - \\mu}{\\sigma}$$
        - Estruturação em funções puras sem efeitos colaterais para facilitar testes unitários.
        """
        )

    with st.expander("Módulos C5 a C7: Modularização e Resolução de Caminhos"):
        st.markdown(
            """
        - Uso de `pathlib.Path` para resolução de caminhos absolutos relativos a `__file__`, evitando erros de CWD.
        - Desacoplamento entre o motor de cálculo e os componentes de visualização gráfica.
        """
        )

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>ownStartup | Laboratório de Engenharia e Análise de Dados</div>",
    unsafe_allow_html=True,
)
