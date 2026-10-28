# ownStartup

    Simulador de métricas financeiras para startups e pequenos negócios, acompanhado de um laboratório de testes estatísticos que construí para praticar Python e análise de dados.

    ## Sobre o Projeto

    No início, há alguns meses, eu queria testar na prática conceitos de matemática e manipulação de arquivos em Python que vinha estudando no meu curso. Comecei criando pequenos scripts e desafios na pasta `exercises/` (como
    cálculos de médias, desvios e sequências numéricas), tratando como exercícios práticos de disciplina escolar.

    Conforme fui avançando nesses exercícios, senti falta de uma interface para visualizar esses dados saindo do papel e do terminal. Foi aí que decidi usar o Streamlit pela agilidade de construir dashboards interativos e
    compartilhar aplicações em Python.

    Depois de estruturar a parte estatística e a detecção de anomalias (usando Z-score para apontar desvios fora do padrão), percebi que esses mesmos dados poderiam responder a um problema real: a tomada de decisão em uma startup.

    Adicionei então um motor financeiro em Python (`engine.py`) para simular o ciclo de vida de um negócio:
    - Quanto tempo o dinheiro em caixa dura (Runway) com base no custo fixo e no CAC.
    - Se a relação entre aquisição e o valor do cliente ao longo do tempo (LTV/CAC) é saudável.
    - Uma projeção de caixa e receita para os próximos 12 meses, com alertas automáticos para indicar se o negócio está no caminho certo ou correndo risco de quebrar.

    Tudo isso ficou concentrado em uma interface simples e interativa que permite simular diferentes cenários operacionais.

    ---

    ## Como Rodar Localmente

    ### 1. Clonar o repositório
    ```bash
    git clone https://github.com/EngThi/ownStartup
    cd ownStartup/mini-challenges

### 2. Instalar dependências

    pip install -r requirements.txt

### 3. Iniciar a aplicação

    streamlit run app.py

Você também pode acessar a versão online pelo Deploy no Streamlit Cloud https://ownstartup.streamlit.app/.
