#dados = [10, 11, 10, 12, 50, 10, 9, 60]
dados = []
soma = 0
limite = 1
anomalias = 0

while not dados or not all(dado.isdigit() for dado in dados):
    entrada = input("Quais valores dos eventos?: ")
    dados = entrada.split()
    
    if not dados or not all(dado.isdigit() for dado in dados):
        print("Entrada inválida. Digite apenas números inteiros")

# Convertendo a lista de strings para uma lista de números (inteiros)
dados = [int(d) for d in dados]

tam = len(dados)

media = sum(dados) / tam

desvios = [num - media for num in dados]

quadrados_desvios = [desvio ** 2 for desvio in desvios]
for num in quadrados_desvios:
    soma += num

desvio_padrao = (soma / tam) ** 0.5

for num in dados:
    z_score = (num - media) / desvio_padrao
    if abs(z_score) < limite:
        print(f"{num}")
    else:
        print(f"{num}")
        anomalias += 1

print("\n")
print("-" * 50)
print(f"total: {tam}")
if anomalias == 0:
    print("Nenhuma ocorrência de anomalia. O sistema está 100%!")
else:
    print(f"anomalias: {anomalias}")

print("-" * 50)
print("\n")
if anomalias == 1: #tam * 0.2 and anomalias < tam * 0.4:
    print("status: alerta\n")
elif anomalias > tam * 0.2 and anomalias <= tam * 0.4:
    print("status: instável\n")
else:
    print("status: crítico!\n")

print(f"media: {media}")
min = dados[0]
for i in range(1, tam, 1):
    if dados[i] < min:
        min = dados[i]
print(f"Mín: {min}")
max = dados[0]
for i in range(1, tam, 1):
    if dados[i] > max:
        max = dados[i]
print(f"Máx: {max}")