def soma_imposto(taxa_imposto, custo):
    valor_final = custo + custo * taxa_imposto / 100
    return valor_final


preco = float(input("Digite o valor do produto: "))
taxa = float(input("Qual a taxa em porcentagem(%) no produto?: "))

print(f"O valor final com impostos fica: {soma_imposto(taxa, preco)}")
