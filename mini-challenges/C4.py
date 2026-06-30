nums = [10, 11, 10, 12, 11, 50, 10]

soma = 0
limite = 1

media = sum(nums) / len(nums)

desvios = [num - media for num in nums]

quadrados_desvios = [desvio ** 2 for desvio in desvios]
for num in quadrados_desvios:
    soma += num

desvio_padrao = (soma / len(nums)) ** 0.5

for num in nums:
    z_score = (num - media) / desvio_padrao
    if abs(z_score) > limite:
        print(f"{num} é estranho (Z-score: {z_score:.2f})")