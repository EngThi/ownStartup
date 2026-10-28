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
    page_title="ownstartup",
    page_icon="assets/code.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)
pg_home = st.Page("app.py", title="Pattern Lab", icon="📈", default=True)
pg_simulator = st.Page(
    "pages/simulador_startup.py",
    title="Simulador",
    icon="🚀",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"], .stMarkdown {
    font-family: 'Outfit', sans-serif !important;
}

/* Custom card style */
.custom-card {
    background-color: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

/* System status badges */
.status-badge {
    padding: 6px 12px;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.9rem;
    display: inline-block;
    text-align: center;
}
.status-normal {
    background-color: rgba(46, 204, 113, 0.15);
    color: #2ecc71;
    border: 1px solid rgba(46, 204, 113, 0.3);
}
.status-alerta {
    background-color: rgba(241, 196, 15, 0.15);
    color: #f1c40f;
    border: 1px solid rgba(241, 196, 15, 0.3);
}
.status-instavel {
    background-color: rgba(230, 126, 34, 0.15);
    color: #e67e22;
    border: 1px solid rgba(230, 126, 34, 0.3);
}
.status-critico {
    background-color: rgba(231, 76, 60, 0.15);
    color: #e74c3c;
    border: 1px solid rgba(231, 76, 60, 0.3);
}
</style>
""",
    unsafe_allow_html=True,
)

# Layout Columns for Title
esquerda, centro, direita = st.columns([1, 2, 3])

with centro:
    st.title("📈 Pattern Lab")
st.markdown("---")

# Navigation Sidebar
st.sidebar.title("🎛️ Controles")
secao = st.sidebar.selectbox(
    "Escolha uma seção",
    [
        "📈 Geral",
        "🔍 Detector de Anomalias",
        "📊 Estatísticas",
        "🧪 Simulador",
        # "Simulador Startup",
        "📘 Journal",
    ],
)

if "dados_entrada" not in st.session_state:
    st.session_state.dados_entrada = "10 40 6 78 60 50 7"

# Section: Geral
if secao == "📈 Geral":
    st.subheader("Bem-vindo ao Pattern Lab")
    st.write(
        "Este laboratório foi construído para analisar padrões numéricos, "
        "realizar diagnósticos estatísticos e detectar desvios anômalos "
        "em fluxos de dados de eventos (como logs de sensores e sistemas)."
    )

    st.markdown("### 🧩 Módulos do Sistema")
    col1, col2 = st.columns(2)
    with col1:
        st.info(
            "**🔍 Detector de Anomalias**\n\nIdentificação em tempo real de variações críticas em sequências de dados usando o Z-Score."
        )
        st.success(
            "**📊 Estatísticas Detalhadas**\n\nCálculos de médias, variância amostral/populacional e detecção de maiores sequências consecutivas."
        )
    with col2:
        st.warning(
            "**🧪 Simulador de Sinais**\n\nGeração de massa de dados artificial contendo ruídos e falhas para testar a robustez dos modelos de análise."
        )
        st.help(
            st.markdown(
                "**📘 Journal de Aprendizado**\n\nRegistro conceitual e diário de bordo com as lições aprendidas em cada desafio do projeto ownStartup."
            )
        )

# Section: Detector de Anomalias
elif secao == "🔍 Detector de Anomalias":
    st.subheader("🔍 Detector de Anomalias (Z-Score)")

    # Input Area
    st.session_state.dados_entrada = st.text_input(
        "Insira a sequência de valores (separados por espaço):",
        value=st.session_state.dados_entrada,
    )

    limite = st.slider("Limite de desvio (Z-Score Threshold):", 0.5, 3.0, 1.0, 0.1)

    partes = st.session_state.dados_entrada.split()

    if not partes:
        st.info("Insira alguns números na caixa acima para iniciar a análise.")
    elif not all(p.replace("-", "", 1).isdigit() for p in partes):
        st.error(
            "⚠️ Entrada inválida! Por favor, use apenas números inteiros separados por espaços."
        )
    else:
        dados = [int(p) for p in partes]
        total = len(dados)

        # Calculations
        media, desvio = calcular_estatisticas(dados)
        resultados, anomalias = detectar_anomalias(dados, media, desvio, limite)
        status = gerar_status(total, anomalias)

        # Layout Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total de Eventos", total)
        with col2:
            st.metric("Média dos Valores", f"{media:.2f}")
        with col3:
            st.metric(
                "Anomalias Detectadas",
                anomalias,
                delta=f"{anomalias} anômalo(s)" if anomalias else None,
                delta_color="inverse",
            )
        with col4:
            if status == "100% normal":
                st.markdown(
                    f"**Status do Sistema:**  \n<span class='status-badge status-normal'>🟢 {status.upper()}</span>",
                    unsafe_allow_html=True,
                )
            elif status == "alerta":
                st.markdown(
                    f"**Status do Sistema:**  \n<span class='status-badge status-alerta'>🟡 {status.upper()}</span>",
                    unsafe_allow_html=True,
                )
            elif status == "instável":
                st.markdown(
                    f"**Status do Sistema:**  \n<span class='status-badge status-instavel'>🟠 {status.upper()}</span>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"**Status do Sistema:**  \n<span class='status-badge status-critico'>🔴 {status.upper()}</span>",
                    unsafe_allow_html=True,
                )

        st.markdown("---")

        # Graphic and Table Columns
        col_g, col_t = st.columns([2, 1])

        with col_g:
            st.subheader("📈 Gráfico de Análise")
            st.line_chart(dados, y_label="Valor dos Eventos", x_label="Ordem temporal")

        with col_t:
            st.subheader("📋 Detalhamento")
            for idx, (val, eh_anomalia) in enumerate(resultados):
                if eh_anomalia:
                    st.markdown(f"**[{idx}]** `❌ {val}` (Anômalo)")
                else:
                    st.markdown(f"**[{idx}]** `✅ {val}` (Normal)")

        st.markdown("---")
        relatorio_str = (
            "-" * 50 + "\n"
            "           RELATÓRIO DE ANOMALIAS (PATTERN LAB)\n"
            "-" * 50 + "\n"
            f"Total de Eventos: {total}\n"
            f"Anomalias Detectadas: {anomalias}\n"
            f"Média dos Valores: {media:.2f}\n"
            f"Valor Mínimo: {min(dados)}\n"
            f"Valor Máximo: {max(dados)}\n"
            f"Status do Sistema: {status}\n"
            "-" * 50 + "\n"
        )
        st.download_button(
            label="📥 Baixar Relatório (TXT)",
            data=relatorio_str,
            file_name="relatorio_anomalias.txt",
            mime="text/plain",
        )

# Section: Estatísticas
elif secao == "📊 Estatísticas":
    st.subheader("📊 Análise Estatística Detalhada")

    st.session_state.dados_entrada = st.text_input(
        "Insira a sequência de valores (separados por espaço):",
        value=st.session_state.dados_entrada,
    )

    partes = st.session_state.dados_entrada.split()

    if not partes:
        st.info("Insira alguns números na caixa acima para iniciar a análise.")
    elif not all(p.replace("-", "", 1).isdigit() for p in partes):
        st.error(
            "⚠️ Entrada inválida! Por favor, use apenas números inteiros separados por espaços."
        )
    else:
        dados = [int(p) for p in partes]
        total = len(dados)

        # Math calculations
        media = sum(dados) / total
        mediana = calcular_mediana(dados)
        minimo = min(dados)
        maximo = max(dados)

        soma_quadrados = sum((x - media) ** 2 for x in dados)
        desvio_pop = (soma_quadrados / total) ** 0.5
        desvio_amostral = (soma_quadrados / (total - 1)) ** 0.5 if total > 1 else 0.0

        seq_consec = maior_sequencia_consecutiva(dados)

        # Columns for metrics
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Mediana", f"{mediana:.1f}")
            st.metric("Mínimo", minimo)
        with c2:
            st.metric("Desvio Padrão (Amostral)", f"{desvio_amostral:.3f}")
            st.metric("Máximo", maximo)
        with c3:
            st.metric("Desvio Padrão (Populacional)", f"{desvio_pop:.3f}")
        with c4:
            st.metric("Seq. Consecutiva Mais Longa", str(seq_consec))

        st.markdown("---")

        st.subheader("📖 Conceitos e Fórmulas")

        st.markdown("#### Média Aritmética")
        st.latex(r"\mu = \frac{\sum_{i=1}^{N} x_i}{N}")

        st.markdown("#### Desvio Padrão Populacional")
        st.latex(r"\sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}}")

        st.markdown("#### Desvio Padrão Amostral")
        st.latex(r"s = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \bar{x})^2}{N - 1}}")

# Section: Simulador
# elif secao == "Simulador Startup":
#     caixa = st.sidebar.number_input("Caixa inicial: ", value=1000.0)
#     cac = st.sidebar.slider("CAC", min_value=10, max_value=500, value=50)
#     clientes_iniciais = st.sidebar.number_input("Quantidade de clientes: ", 0, 20, 1)
#     novos_clientes = st.sidebar.number_input("Novos clientes: ", 0, 10, 1)

#     dados = simular_cenario(
#         caixa, int(clientes_iniciais), int(novos_clientes), 100, cac
#     )

#     historico = dados["historico"]
#     runway = dados["runway"]
#     ltv_cac = dados["ltv_cac"]
#     df_projecao = pd.DataFrame(historico)

#     # Aparece na tela
#     st.subheader("📊 Indicadores")
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         if runway == float("inf"):
#             st.metric("Runway", "Sustentável")
#         else:
#             st.metric("Runway", f"{runway:.1f} meses")

#     with col2:
#         st.metric("Razão LTV/CAC", f"{ltv_cac:.1f}x")

#     with col3:
#         mrr_final = historico[-1]["Receita"]
#         st.metric("MRR", f"{mrr_final:.2f}")

#     with col4:
#         caixa_final = historico[-1]["Caixa"]
#         st.metric("Caixa projetado", f"{caixa_final:,.2f}")

#     st.markdown("---")

#     st.subheader("Diagnóstico negócio")
#     if runway < 6:
#         st.error(f"Alerta crítico: Runway de apenas {runway} meses!")
#     elif ltv_cac < 3:
#         st.warning(f"Atenção {ltv_cac:.2f}x está abaixo do ideal (3x")
#     else:
#         st.success("Métricas operacionais")

#     st.markdown("---")

#     st.subheader("Projeção 12 meses")
#     df_chart = df_projecao.set_index("Mês")[["Caixa", "Receita"]]
#     st.line_chart(df_chart)

#     with st.expander("ver tabela detalhada mês a mês"):
#         st.dataframe(df_projecao)


elif secao == "🧪 Simulador":
    st.subheader("🧪 Simulador de Eventos e Anomalias")
    st.write(
        "Gere dados simulados para testar o comportamento do Z-score em diferentes cenários."
    )

    col1, col2 = st.columns(2)
    with col1:
        qtd_simular = st.slider("Quantidade de Eventos", 5, 50, 15)
        media_simular = st.slider("Média Esperada", 10, 100, 42)
    with col2:
        taxa_erros = st.slider("Probabilidade de Anomalia (%)", 0, 50, 20)
        limite_simular = st.slider("Z-Score de Detecção", 0.5, 3.0, 1.0, 0.1)

    if st.button("🚀 Iniciar Simulação"):
        dados_simulados = []
        status_real = []

        for _ in range(qtd_simular):
            chance = random.randint(0, 100)
            if chance < taxa_erros:
                direcao = random.choice([-1, 1])
                val_anomalo = int(media_simular + direcao * random.uniform(20, 60))
                dados_simulados.append(val_anomalo)
                status_real.append(True)
            else:
                val_normal = int(random.uniform(media_simular - 2, media_simular + 2))
                dados_simulados.append(val_normal)
                status_real.append(False)

        # Run detection
        media_calc, desvio_calc = calcular_estatisticas(dados_simulados)
        resultados_detec, anomalias_detec = detectar_anomalias(
            dados_simulados, media_calc, desvio_calc, limite_simular
        )

        st.markdown("### 📊 Resultado da Simulação")

        col_list1, col_list2 = st.columns(2)
        with col_list1:
            st.subheader("Dados Gerados vs Detecção")
            for idx, val in enumerate(dados_simulados):
                real_anom = status_real[idx]
                eh_detetado = resultados_detec[idx][1]

                label_real = "⚠️ ERRO SIMULADO" if real_anom else "✅ NORMAL SIMULADO"
                label_detec = "❌ DETECTADO" if eh_detetado else "✅ NORMAL"

                st.markdown(
                    f"**[{idx}]** Valor: `{val}` | **Simulado:** {label_real} | **Detector:** {label_detec}"
                )

        with col_list2:
            st.subheader("Precisão do Modelo")
            st.line_chart(dados_simulados)
            st.metric("Total Anomalias Reais", sum(status_real))
            st.metric("Total Anomalias Detetadas", anomalias_detec)

# Section: Journal
elif secao == "📘 Journal":
    st.subheader("📘 Diário de Bordo - ownStartup")
    st.write(
        "Registro técnico de aprendizado e consolidação de conceitos durante os desafios práticos."
    )

    with st.expander("📁 C1 & C2: Arquivos e Tratamento de Exceções"):
        st.markdown("""
        **Aprendizados:**
        * Manipulação de arquivos com `with open(...)` garantindo o fechamento automático.
        * Tratamento de exceções específicas como `FileNotFoundError` e `PermissionError`.
        * Evitar capturas genéricas sem necessidade, tornando o software robusto.
        """)

    with st.expander("📁 C3: Lógica e Padrões Consecutivos"):
        st.markdown("""
        **Aprendizados:**
        * Criação de algoritmos de rastreamento linear para sequências ordenadas.
        * Gerenciamento de múltiplos estados (`sequencia_atual` e `maior_sequencia`).
        """)

    with st.expander("📁 C4: Estatística e Z-Score"):
        st.markdown("""
        **Aprendizados:**
        * O Z-Score calcula quantos desvios padrões um dado está distante da média:
          $$Z = \\frac{x - \\mu}{\\sigma}$$
        * Emprego de variância e desvio padrão populacional vs. amostral ($N-1$).
        * Identificação matemática de outliers (anomalias).
        """)

    with st.expander("📁 C5 & C6: Validação de Entrada e Aleatoriedade"):
        st.markdown("""
        **Aprendizados:**
        * Importância de armazenar valores aleatórios em variáveis locais ao invés de recalcular múltiplas vezes em estruturas `if/elif`.
        * Uso de conjuntos (`sets`) para validação rápida de padrões de entrada.
        """)

    with st.expander("📁 C7 & funcC7: Modularização e Boas Práticas"):
        st.markdown("""
        **Aprendizados:**
        * Divisão de tarefas em funções puras (desacoplamento).
        * Uso de `pathlib.Path` para caminhos absolutos baseados na localização do arquivo (`__file__`), evitando erros de execução por diretório ativo (CWD).
        """)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; opacity: 0.5;'>Pattern Lab | ownStartup</div>",
    unsafe_allow_html=True,
)
