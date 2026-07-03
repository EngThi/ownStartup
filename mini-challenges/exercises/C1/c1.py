numeros = []
soma = 0

with open('nums.txt', 'r') as arquivo:
    for linha in arquivo:
        numeros.append(int(linha.strip()))

for num in numeros:
    soma += num

print(numeros)
print(f"\nA soma dos números é: {soma}")
