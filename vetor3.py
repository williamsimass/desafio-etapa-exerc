import json

with open('dados.json', 'r') as f:
    faturamento_diario = json.load(f)

valores_faturamento = [d.get('faturamento', 0) for d in faturamento_diario]

menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)

faturamento_sem_zero = [f for f in valores_faturamento if f != 0]

if len(faturamento_sem_zero) > 0:
    media_faturamento = sum(faturamento_sem_zero) / len(faturamento_sem_zero)
else:
    media_faturamento = 0

dias_acima_da_media = len([f for f in faturamento_sem_zero if f > media_faturamento])

print(f'Menor faturamento diário: R$ {menor_faturamento:.2f}')
print(f'Maior faturamento diário: R$ {maior_faturamento:.2f}')
print(f'Média de faturamento diário: R$ {media_faturamento:.2f}')
print(f'Número de dias acima da média mensal: {dias_acima_da_media}')
