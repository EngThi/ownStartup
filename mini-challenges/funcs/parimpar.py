def par(num):
    return num % 2 == 0

while True:
    entrada = input("Digite um número inteiro: ")
    if entrada.isdigit():
        n = int(entrada)
        logico = par(n)
        
        if logico:
            print(f"O número {n} é par")
        else:
            print(f"O número {n} é ímpar")
        break
    else:
        print("Digite apenas um número inteiro")


# def par(num):
#     if num % 2 == 0:
#         eh_par = True
#     else:
#         eh_par = False
#     return eh_par

# while not n.isdigit() :
#     try:
#         n = int(input("Digite um número inteiro: "))
#         logico = par(n)
#         if logico == True:
#             print(f"O número {n} é par")
#         else:
#             print(f"O número {n} é ímpar")
#     except ValueError:
#         print("Digite apenas um número inteiro")