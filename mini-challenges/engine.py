def simular_cenario(
    caixa_inicial,
    clientes_iniciais,
    novos_clientes_mes,
    mensalidade,
    CAC=20,
    custos_fixos=200,  # Fixei 200
    churn_rate=3,
    meses=12,  # Padrão
):

    taxa_churn = churn_rate / 100.0 if churn_rate > 1 else churn_rate
    LTV = mensalidade if taxa_churn == 0 else mensalidade / taxa_churn
    razao_ltv_cac = LTV / CAC if CAC > 0 else 0

    caixa = caixa_inicial
    clientes = clientes_iniciais
    historico = []

    for mes in range(1, meses + 1):
        cancelados = int(clientes * taxa_churn)
        clientes = clientes - cancelados + novos_clientes_mes
        receita = clientes * mensalidade
        custo_marketing = novos_clientes_mes * CAC
        despesas = custos_fixos + custo_marketing
        burn = despesas - receita
        caixa = caixa - burn

        historico.append(
            {
                "Mês": mes,
                "Caixa": caixa,
                "Receita": receita,
                "Burn": burn,
                "Clientes": clientes,
            }
        )
    burn_atual = historico[0]["Burn"] if historico else 0
    if burn_atual > 0:
        runway = caixa_inicial / burn_atual

    else:
        runway = float("inf")

    return {
        "historico": historico,
        "runway": runway,
        "ltv_cac": razao_ltv_cac,
        "LTV": LTV,
    }
