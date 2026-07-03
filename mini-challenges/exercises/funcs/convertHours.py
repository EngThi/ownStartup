def converter_horas(horario):
    hora_min = horario.split(':')
    minutos = hora_min[1]
    hora = int(hora_min[0])
    meridien = 'AM'
    
    if hora == 0:
        hora = 12
    if hora > 12:
        hora = hora - 12
        meridien = 'PM'
    if hora == 12 and int(hora_min[0]) == 12:
        meridien = 'PM'
        
    return f"{hora}:{minutos} {meridien}"

def imprime_tela(hora):
    print(f"Horário convertido: {hora}")

entrada_ok = False

while not entrada_ok:
    horario_digitado = input("Digite o horário (formato 24h, ex: 14:25): ")
    
    if ':' in horario_digitado:
        entrada_ok = True
        hora_convertida = converter_horas(horario_digitado)
        imprime_tela(hora_convertida)
    else:
        print("Formato inválido! Certifique-se de usar o ':' (ex: 14:25).")
