nums = [10, 11, 10, 12, 11, 50, 10]
tam = len(nums)

soma = sum(nums)
media = soma / tam

diferencas_quadradas = [(x - media) ** 2 for x in nums]
soma_quadrados = sum(diferencas_quadradas)

variancia_amostral = soma_quadrados / (tam - 1)
desvio_padrao_amostral = variancia_amostral ** 0.5

variancia_populacional = soma_quadrados / tam
desvio_padrao_populacional = variancia_populacional ** 0.5

print(f"A média é: {media:.3f}")
print(f"Desvio Padrão Amostral: {desvio_padrao_amostral:.3f}")
print(f"Desvio Padrão Populacional: {desvio_padrao_populacional:.3f}\n")

