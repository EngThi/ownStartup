nums = [10, 11, 10, 12, 11, 50, 10]

tam = len(nums)
for i in nums:
    soma += i
print(f"A média é: {soma}")
print(f"A média é: {soma / tam:.3f}")

diferencas_quadradas = [(x - {soma / tam}) ** 2 for x in nums]
soma_quadrados = sum(diferencas_quadradas)

variancia_amostral = soma_quadrados / tam - 1

desvio_padrao_amostral = variancia_amostral ** 0.5

print(desvio_padrao_amostral)

diferencas_quadradas = [(x - soma / tam) ** 2 for x in nums]
soma_quadrados = sum(diferencas_quadradas)

variancia_amostral = soma_quadrados / len(nums) - 1

desvio_padrao_amostral = variancia_amostral ** 0.5

print(desvio_padrao_amostral)