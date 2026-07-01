import re

def converter_horas(horario):
    hora_min = re.split(':', horario)
    minutos = hora_min[1]
    hora = int(hora_min[0])
    
    meridien = 'AM'
    if hora > 12:
        hora = hora - 12
        meridien = 'PM'
        
    return f"{hora}:{minutos} {meridien}" # Correção de sintaxe e interpolação

def imprime_tela(hora):
    print(hora)

horario_digitado = input("Digite o horário (formato 24h, ex: 14:25): ")
hora_convertida = converter_horas(horario_digitado)
imprime_tela(hora_convertida)
