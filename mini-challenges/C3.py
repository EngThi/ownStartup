nums = input("Digite alguns números: ")
nums = [int(i) for i in nums.split()]

if not nums:
    print("Nenhum número digitado.")
else:
    sequencia_atual = [nums[0]]
    maior_sequencia = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            sequencia_atual.append(nums[i])
        else:
            if len(sequencia_atual) > len(maior_sequencia):
                maior_sequencia = sequencia_atual
            sequencia_atual = [nums[i]]

    # Verificação final necessária para salvar a última sequência processada
    if len(sequencia_atual) > len(maior_sequencia):
        maior_sequencia = sequencia_atual

    print(f"A maior sequência consecutiva é: {maior_sequencia}")