import json

with open('faturamento.json', 'r') as f:
    faturamento_diario = json.load(f)


menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

faturamento_sem_zero = [f for f in faturamento_diario if f != 0]
media_faturamento = sum(faturamento_sem_zero) / len(faturamento_sem_zero)


dias_acima_da_media = len([f for f in faturamento_sem_zero if f > media_faturamento])


print(f'Menor faturamento diário: R$ {menor_faturamento:.2f}')
print(f'Maior faturamento diário: R$ {maior_faturamento:.2f}')
print(f'Média de faturamento diário: R$ {media_faturamento:.2f}')
print(f'Número de dias acima da média mensal: {dias_acima_da_media}')
