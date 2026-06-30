from random import random
import random

qtd = 7
media = 42
qtd_erros = 0

for num in range(qtd):
    if random.randint(0, 100) > 40 and random.randint(0, 100) < 65:
        qtd_erros = 1
    elif random.randint(0, 100) > 64 and random.randint(0, 100) < 85:
        qtd_erros = 2
    else:
        qtd_erros = 3
        normais = qtd - qtd_erros
    normais = qtd - qtd_erros
for num in range(normais):
        print(f"{random.uniform(40, 42):.2f}")
for num in range(qtd_erros):
        print(f"{random.uniform(20, 80):.2f} ⟵——— erro")








    # valor_aleatorio = random.gauss(media, dispersao)
    # print(f"AQUI: {valor_aleatorio:.2f}\n")

# for num in range(qtd):
#     chance_erro = random.uniform(media * 0.5, media + media * 0.5)
#     chance_erro = random.uniform(media)
#     print(f"{chance_erro:.2f}")

# if chance_erro < 50:
#     sete_numeros = [random.uniform(40, 44) for _ in range(7)]
# elif chance_erro > 50 and chance_erro < 70:
#     sete_numeros = [random.uniform(40, 44) for _ in range(7)]

# for num in sete_numeros:
#     print(f"{num:.2f}")