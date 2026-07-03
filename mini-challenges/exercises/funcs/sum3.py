def somar_tres(n1, n2, n3):
    return n1 + n2 + n3

try:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite mais um: "))
    num3 = float(input("O último: "))
    
    resultado = somar_tres(num1, num2, num3)
    print(f"A soma é: {resultado}")
    
except ValueError:
    print("Por favor, digite apenas números")
