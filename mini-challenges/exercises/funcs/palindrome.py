def palindrome(texto) -> str:
    tam = len(texto)
    j = tam - 1
    palind = 1

    for i in range(0, tam):
        if texto[i] != texto[j]:
            palind = 0
            break
        j -= 1

    if palind == 1:
       return True, texto
    else:
        return False, texto


logico, texto = palindrome(input("Escreva algo: ").lower().replace(" ", ""))
print(f"{logico} " + "\n")
if logico == True:
    print(f"O seu texto: {texto} é um palíndromo")
else:
    print(f"O seu texto: {texto} não é um palíndromo")


# Trick given by AI

# def palindrome(texto_original):
#     # Remove espaços e converte para minúsculo para a verificação
#     texto_limpo = texto_original.lower().replace(" ", "")
    
#     # Inverte a string limpa
#     texto_invertido = texto_limpo[::-1]
    
#     # Compara a string limpa com ela invertida
#     if texto_limpo == texto_invertido:
#         return True, texto_original
#     else:
#         return False, texto_original

# entrada = input("Escreva algo: ")
# logico, texto = palindrome(entrada)

# if logico == True:
#     print(f"\nO seu texto: {texto} é um palíndromo!")
# else:
#     print(f"\nO seu texto: {texto} não é um palíndromo.")

