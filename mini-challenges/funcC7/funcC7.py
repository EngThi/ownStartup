from pathlib import Path

def obter_dados():
    while True:
        entrada = input("Quais valores dos eventos?: ")
        partes = entrada.split()

        if partes and all(p.isdigit() for p in partes):
            return [int(p) for p in partes]

        print("Entrada inválida. Digite apenas números inteiros")

def calcular_estatisticas(dados):
    tam = len(dados)

    media = sum(dados) / tam

    soma = 0
    for num in dados:
        soma += (num - media) ** 2

    desvio_padrao = (soma / tam) ** 0.5

    return media, desvio_padrao

def detectar_anomalias(dados, media, desvio_padrao, limite):
    resultados = []
    anomalias = 0

    for num in dados:
        if desvio_padrao == 0:
            z_score = 0
        else:
            z_score = (num - media) / desvio_padrao

        eh_anomalia = abs(z_score) >= limite

        if eh_anomalia:
            anomalias += 1

        resultados.append((num, eh_anomalia))

    return resultados, anomalias

def mostrar_resultados(resultados):
    print("\nValores analisados:\n")

    for valor, eh_anomalia in resultados:
        if eh_anomalia:
            print(f"❌ {valor}")
        else:
            print(f"✅ {valor}")

def gerar_status(total, anomalias):
    proporcao = anomalias / total

    if proporcao == 0:
        return "100% normal"
    elif proporcao <= 0.2:
        return "alerta"
    elif proporcao <= 0.4:
        return "instável"
    else:
        return "crítico"

def mostrar_relatorio(dados, media, total, anomalias):
    print("\n" + "-" * 50)
    print(f"Total: {total}")
    print(f"Anomalias: {anomalias}")
    print(f"Média: {media:.2f}")

    print(f"Mín: {min(dados)}")
    print(f"Máx: {max(dados)}")

    status = gerar_status(total, anomalias)
    print(f"Status: {status}")

    print("-" * 50 + "\n")
    return dados, media, total, anomalias

def gerar_arquivo(dados, media, total, anomalias):
    status = gerar_status(total, anomalias)
    caminho_arquivo = Path(__file__).parent / 'relatorio.txt'
    
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("-" * 50 + "\n")
        arquivo.write("           RELATÓRIO DE ANOMALIAS\n")
        arquivo.write("-" * 50 + "\n")
        arquivo.write(f"Total de Eventos: {total}\n")
        arquivo.write(f"Anomalias Detectadas: {anomalias}\n")
        arquivo.write(f"Média dos Valores: {media:.2f}\n")
        arquivo.write(f"Valor Mínimo: {min(dados)}\n")
        arquivo.write(f"Valor Máximo: {max(dados)}\n")
        arquivo.write(f"Status do Sistema: {status}\n")
        arquivo.write("-" * 50 + "\n")
    
    print("Arquivo 'relatorio.txt' gerado com sucesso!")
    

def main():
    limite = 1

    dados = obter_dados()

    media, desvio = calcular_estatisticas(dados)

    resultados, anomalias = detectar_anomalias(dados, media, desvio, limite)

    mostrar_resultados(resultados)

    mostrar_relatorio(dados, media, len(dados), anomalias)

    gerar_arquivo(dados, media, len(dados), anomalias)

if __name__ == "__main__":
    main()