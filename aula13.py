# Toda vez que vir "f" atrás de uma string, significa que é uma formatação: f-strings
nome = 'Renato'
altura = 1.68
peso = 86
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.1f}'

print(linha_1)
print(linha_2)
print(linha_3)