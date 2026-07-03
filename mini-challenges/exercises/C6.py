permitidos = {"ok", "fail"}
status = []

while not status or not all(item in permitidos for item in status):
    entrada = input("Quais os resultados dos eventos? (ex: ok fail ok): ")
    status = entrada.split()
    
    if not status or not all(item in permitidos for item in status):
        print("Entrada inválida. Use apenas 'ok' ou 'fail'.")

falhas = 0
for resultado in status:
    if resultado == 'fail':
        falhas += 1
print(f"Status processado: {status}")

if falhas == 0:
    print("\nNenhuma ocorrência de falhas")
elif falhas == 1:
    print("\nOcorreu uma falha")
else:
    print(f"\nOcorreram {falhas} falhas!")