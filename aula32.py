


"""
Faça um programa que pergunte a hora do usuário e, baseando-se no horário descrito,
 exita a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e boa noite 17-23
"""

entrada = input('Digite um número inteiro: ')

try:
    entrada_int = int(entrada)
    if entrada_int % 2 == 0:
       print('Número par!')
    else:
       print('Número par!')

except:
    print('Não é inteiro.')   

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro
"""

hora_pergunta = input('Por favor, me informar as horas: \n ')
# nome_nome = input('Qual o seu nome? \n ')
# hora_resp = int(hora_pergunta)


try:
    hora_resp = int(hora_pergunta)
    bom_dia = hora_resp >= 0 and hora_resp <= 11 
    boa_tarde = hora_resp >= 12 and hora_resp <= 17 
    boa_noite = hora_resp >= 18 and hora_resp <= 23
    nome_nome = input('Qual o seu nome? \n ')
    if bom_dia:
        print(f'Bom dia {nome_nome}, tenha um dia produtivo!\n')
    elif boa_tarde:
        print(f'Boa tarde {nome_nome}, tenha uma tarde produtivo!\n')
    elif boa_noite:
        print(f'Boa noite {nome_nome}, tenha uma noite produtivo!\n')
    else:
        print(f'Não conheço essa hora {nome_nome}')
except:
    print('Você não digitou um número inteiro!')

"""
Faça um programa que peça o primeiro nome do usuário. 
Se o nome tiver 4 letras ou nemos escreva "Seu nome é curto"; 
se tuver entre 5 e 6 letras, escreva "Seu nome é normal"; 
maior que 6 escreva "Seu nome é muito grande"

"""

pri_nome = input ('Me fale seu primeiro nome: ')
resp_nome = str(pri_nome)

if len(resp_nome) <= 4:
    print("Seu nome é curto.")
if len(resp_nome) >= 5 and len(resp_nome) <=6:
    print("Seu nome é normal.")
if len(resp_nome) > 6:
    print("Seu nome é muito grande.")


      