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


# import streamlit as st
# import random
# from datetime import datetime, timedelta

# # Configuração da página
# st.set_page_config(
#     page_title="Meu Dashboard Pessoal",
#     page_icon="📊",
#     layout="wide"
# )

# st.title("📊 Meu Dashboard Pessoal")
# st.markdown("---")

# # Sidebar para navegação
# st.sidebar.title("🎛️ Controles")
# secao = st.sidebar.selectbox(
#     "Escolha uma seção:",
#     ["📈 Visão Geral", "💰 Finanças", "🏃‍♂️ Exercícios", "📚 Estudos", "🎯 Metas"]
# )

# # Dados simulados (você pode substituir por dados reais)
# if "dados_financas" not in st.session_state:
#     st.session_state.dados_financas = {
#         "receitas": 2500,
#         "gastos": 1800,
#         "economia": 700
#     }

# if "exercicios" not in st.session_state:
#     st.session_state.exercicios = [30, 45, 0, 60, 30, 45, 0]  # minutos por dia

# # === SEÇÃO: VISÃO GERAL ===
# if secao == "📈 Visão Geral":
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.metric(
#             label="💰 Saldo Atual",
#             value="R$ 2.500",
#             delta="R$ 300"
#         )

#     with col2:
#         st.metric(
#             label="🏃‍♂️ Exercícios (semana)",
#             value="5 dias",
#             delta="2 dias"
#         )

#     with col3:
#         st.metric(
#             label="📚 Horas de Estudo",
#             value="25h",
#             delta="5h"
#         )

#     with col4:
#         st.metric(
#             label="🎯 Metas Concluídas",
#             value="3/5",
#             delta="1"
#         )

#     st.markdown("---")

#     # Gráfico simples com st.bar_chart (dados nativos)
#     st.subheader("📊 Atividades da Semana")
#     dados_semana = {
#         "Segunda": 8,
#         "Terça": 6,
#         "Quarta": 9,
#         "Quinta": 7,
#         "Sexta": 5,
#         "Sábado": 3,
#         "Domingo": 4
#     }
#     st.bar_chart(dados_semana)

# # === SEÇÃO: FINANÇAS ===
# elif secao == "💰 Finanças":
#     st.header("💰 Controle Financeiro")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("💵 Receitas")
#         receita = st.number_input("Adicionar receita:", min_value=0.0, step=10.0)
#         if st.button("➕ Adicionar Receita"):
#             st.session_state.dados_financas["receitas"] += receita
#             st.success(f"Receita de R$ {receita} adicionada!")

#     with col2:
#         st.subheader("💸 Gastos")
#         gasto = st.number_input("Adicionar gasto:", min_value=0.0, step=10.0)
#         categoria = st.selectbox("Categoria:", ["🍔 Alimentação", "🚗 Transporte", "🎮 Lazer", "📚 Educação"])
#         if st.button("➖ Adicionar Gasto"):
#             st.session_state.dados_financas["gastos"] += gasto
#             st.warning(f"Gasto de R$ {gasto} em {categoria} adicionado!")

#     # Resumo financeiro
#     st.markdown("---")
#     dados = st.session_state.dados_financas
#     saldo = dados["receitas"] - dados["gastos"]

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("💰 Total Receitas", f"R$ {dados['receitas']}")
#     with col2:
#         st.metric("💸 Total Gastos", f"R$ {dados['gastos']}")
#     with col3:
#         st.metric("💎 Saldo", f"R$ {saldo}", delta=f"R$ {saldo}")

#     # Gráfico de pizza simples (usando progress bars)
#     st.subheader("📊 Distribuição de Gastos")
#     categorias = {"Alimentação": 40, "Transporte": 30, "Lazer": 20, "Educação": 10}
#     for categoria, porcentagem in categorias.items():
#         st.write(f"{categoria}: {porcentagem}%")
#         st.progress(porcentagem / 100)

# # === SEÇÃO: EXERCÍCIOS ===
# elif secao == "🏃‍♂️ Exercícios":
#     st.header("🏃‍♂️ Tracking de Exercícios")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("📝 Registrar Exercício")
#         minutos = st.slider("Minutos de exercício hoje:", 0, 120, 30)
#         tipo_exercicio = st.selectbox("Tipo:", ["🏃‍♂️ Corrida", "🏋️‍♂️ Musculação", "🧘‍♀️ Yoga", "🚴‍♂️ Ciclismo"])

#         if st.button("✅ Registrar"):
#             st.success(f"Registrado: {minutos} minutos de {tipo_exercicio}!")
#             st.balloons()

#     with col2:
#         st.subheader("📊 Progresso Semanal")
#         exercicios = st.session_state.exercicios
#         total_semana = sum(exercicios)
#         media_dia = total_semana / 7

#         st.metric("⏱️ Total da Semana", f"{total_semana} min")
#         st.metric("📈 Média Diária", f"{media_dia:.1f} min")

#     # Gráfico de linha simples
#     st.subheader("📈 Exercícios por Dia")
#     dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
#     dados_exercicio = dict(zip(dias, st.session_state.exercicios))
#     st.line_chart(dados_exercicio)

# # === SEÇÃO: ESTUDOS ===
# elif secao == "📚 Estudos":
#     st.header("📚 Controle de Estudos")

#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("📖 Sessão de Estudo")
#         materia = st.text_input("Matéria/Assunto:")
#         horas = st.number_input("Horas estudadas:", min_value=0.0, max_value=12.0, step=0.5)
#         dificuldade = st.select_slider("Dificuldade:", ["😴 Fácil", "🤔 Médio", "🔥 Difícil"])

#         if st.button("📝 Registrar Estudo"):
#             st.success(f"Registrado: {horas}h de {materia} - {dificuldade}")

#     with col2:
#         st.subheader("📊 Estatísticas")
#         # Dados simulados
#         materias = {"Python": 15, "Matemática": 12, "Inglês": 8, "Streamlit": 10}

#         for materia, horas in materias.items():
#             st.write(f"**{materia}**: {horas}h")
#             st.progress(horas / 20)  # Máximo 20h para a barra

# # === SEÇÃO: METAS ===
# elif secao == "🎯 Metas":
#     st.header("🎯 Minhas Metas")

#     # Lista de metas
#     if "metas" not in st.session_state:
#         st.session_state.metas = [
#             {"meta": "Estudar Python 1h por dia", "concluida": True},
#             {"meta": "Exercitar-se 5x na semana", "concluida": False},
#             {"meta": "Economizar R$ 500", "concluida": True},
#             {"meta": "Ler 2 livros no mês", "concluida": False},
#             {"meta": "Criar 3 projetos Streamlit", "concluida": False}
#         ]

#     st.subheader("📋 Lista de Metas")

#     for i, meta in enumerate(st.session_state.metas):
#         col1, col2 = st.columns([4, 1])

#         with col1:
#             if meta["concluida"]:
#                 st.success(f"✅ {meta['meta']}")
#             else:
#                 st.info(f"⏳ {meta['meta']}")

#         with col2:
#             if st.button("✅", key=f"meta_{i}"):
#                 st.session_state.metas[i]["concluida"] = True
#                 st.rerun()

#     # Adicionar nova meta
#     st.markdown("---")
#     st.subheader("➕ Adicionar Nova Meta")
#     nova_meta = st.text_input("Digite sua nova meta:")
#     if st.button("Adicionar Meta") and nova_meta:
#         st.session_state.metas.append({"meta": nova_meta, "concluida": False})
#         st.success("Meta adicionada!")
#         st.rerun()

# # Footer
# st.markdown("---")
# st.markdown("*Dashboard criado usando Streamlit*")