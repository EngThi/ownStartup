# soma = 0

# with open('data.txt', 'r') as arquivo:
#     for linha in arquivo:
#         dado = linha.strip()
        
#         if dado.isdigit():
#             soma += int(dado)

# print(f"A soma dos números é: {soma}")

soma = 0
nome_arquivo = 'data.txt'

try:
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dado = linha.strip()
            
            # Condicional que você já usa para proteger a conversão
            if dado.isdigit():
                soma += int(dado)
                
    print(f"A soma dos números é: {soma}")

except FileNotFoundError:
    print(f"Atenção: O arquivo '{nome_arquivo}' não foi encontrado.")
except PermissionError:
    print(f"Atenção: Você não tem permissão para ler o arquivo '{nome_arquivo}'.")
except Exception as erro:
    print(f"Ocorreu um erro inesperado: {erro}")
