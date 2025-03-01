"""
Exercicio
Peça ao usuário para digitar seu nome
peça ao usuário para digitar sua idade
Se nome e idade dorem digitados:
   Exiba:
         Seu nome é {nome}
         Seu nome invertido é {nome invertido}
         Se nome contém (ou não) espaços
         Seu nome tem {n} letras
         A primeira letra do seu nome é {letra}
         A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
   exiba "Desculpas, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    contem_n = 'n' or 'N'

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome contém "{len(nome)}" letras')

    print(f'A primeira letra do seu nome é "{nome[0]}"')
    print(f'A útima letra do seu nome é "{nome[-1]}"')

else:
    print('Desculpe, você deixou campos varios')