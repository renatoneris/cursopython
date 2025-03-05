"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
loop infinito -> quanto um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome?  ')
    print(f'Seu nom é {nome}')
    
    if nome == 'sair':
        break

print('ACABOU')