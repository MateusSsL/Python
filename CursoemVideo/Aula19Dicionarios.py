#=============================== DICIONARIOS ===================================
# Listas []
# tuplas ()
# Dicionarios {}
# filme=dict()
# filme= {'titulo':'Stars Wars',
#         'ano':1977,
#         'diretor':'George Lucas'
#         }
#print(filme.values())  # Stars Wars.1997,George Lucas
#print(filme.keys())  #titulo , ano , diretor
#print(filme.items())  # tudo
# for k,v in filme.items():
#     print(f"O {k} é {v}")  # O {keys} é {values}
#O titulo é Stars Wars      
#O ano é 1977
#O diretor é George Lucas
#===============================  ===================================
# pessoas = {'nome':'Gustavo',
#            'sexo':'M',
#            'idade':22
#            }
# print(f" O {pessoas['nome']} tem {pessoas['idade']} anos.")
# print(pessoas.items())

# estado= dict()
# brasil=list()
# for c in range(0,3):
#     estado['uf']= str(input('Unidade Federativa: '))
#     estado['sigla']=str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for e in brasil:
#     for v in e.values():
#         print(v, end=" ")
#     print()

#=============================== 090 ===================================
# https://youtu.be/ZWj8o692qGY?si=XmHcqA67dHQdBhZ1&t=1822
# print('=-'*20)
# print("{:-^40}".format(" Teste de Aprovação "))
# print('=-'*20)
# dici=dict()
# # perguntar nome e média
# dici['Nome']=str(input("Digite seu nome: ").strip().title())
# dici['Media']=float(input(f"Média de {dici['Nome']}: "))
# print('=-'*20)
# #verificar se a media é maior ou igual a 6
# if dici['Media']>=6 :
#     dici['Situacao'] = 'Aprovado'
# else:
#     dici['Situacao'] = 'Reprovado'
# #para cada key e value in dici items() printar 
# for k, v in dici.items():
#     print(f'{k} é igual a {v}')
#     # Nome é igual a :
#     # Media é igual a :
#     # Situação é igual a :
#=============================== 091 ===================================
# print('=-'*20)
# print("{:-^40}".format(" Ranking de Dados Aleatorios"))
# print('=-'*20)
# from random import randint
# from time import sleep
# from operator import itemgetter
# jogo={'jogador1': randint(1, 6),
# 'jogador2': randint(1, 6),
# 'jogador3': randint(1, 6),
# 'jogador4': randint(1, 6)
# }
# rank=list()
# print("{:-^40}".format('Sorteando'))
# for k,v in jogo.items():
#     print(f'{k} tirou {v} no dado.')
#     sleep(1)
# rank = sorted(jogo.items(), key=itemgetter(1),reverse=True)
# print('=-'*20)
# print("{:-^40}".format(" Ranking dos vencedores"))
# for i , v in enumerate(rank):
#     print(f'{i+1} lugar: {v[0]} com {v[1]}')
#     sleep(1)
#=============================== 092 ===================================
# from datetime import datetime
# print('=-'*20)
# print("{:-^40}".format(" Registro Aposentadoria "))
# print('=-'*20)
# dados=dict()
# dados['nome']=str(input("Digite seu nome: "))
# nas=int(input("Ano de nascimento: "))
# dados['idade']= datetime.now().year - nas
# dados['ctps']=int(input("Carteira de Trabalho(0 não tem): "))
# dados['sexo']=str(input('Digite seu Sexo [M/F]').strip().upper())
# if dados['ctps'] != 0 and dados['sexo'] == 'M':
#     dados['contrato']=int(input("Digite o ano de Contratação: "))
#     dados['salario']=float(input("Digite o seu Salario: "))
#     dados['aposentadoria']= dados['idade'] + ((dados['contrato'] + 35) - datetime.now().year)
# elif dados['ctps'] != 0 and dados['sexo'] == 'F':
#     dados['contrato']=int(input("Digite o ano de Contratação: "))
#     dados['salario']=float(input("Digite o seu Salario: "))
#     dados['aposentadoria']=dados['idade'] + ((dados['contrato'] + 30) - datetime.now().year)
# for k,v in dados.items():
#     print(f'{k} tem o valor : {v}')
# =============================== 093 ===================================
# print('=-'*20)
# print("{:-^40}".format(" Jogador de Futebol "))
# print('=-'*20)
# total = 0
# dados=dict()
# partidas=list()
# dados['nome']=str(input("Digite seu nome: ").strip().title())
# dados['partidas']=int(input(f"Quantas Partidas {dados['nome']} jogou: "))
# for x in range(0,dados['partidas']):
#     partidas.append(int(input(f"Digite Quantos gols foram feitos no {x}º jogo? ")))
# dados['gols']=partidas[:]
# dados['totalgols']= sum(partidas)
# print('=-'*20)
# for k, v in dados.items():
#     print(f"O campo {k} tem o valor {v} !")
# print('=-'*20)
# for i,v in enumerate(dados['gols']):
#     print(f"    => Na {i+1}ª Partida - {dados['nome']}, fez {v} Gol's")
# print('=-'*20)
# print(f'Essa é a carreira de {dados["nome"]} !')
# =============================== 094 ===================================
# print('=-'*20)
# print("{:-^40}".format(" Dicionario "))
# print('=-'*20)
# dados=dict()
# dadosfinal=dict()
# listados=list()
# mulheres=list()
# maiores=list()
# total=somaid= 0
# while True:
#     dados['nome']=str(input("Digite seu nome: ").title())
#     dados['sexo']=str(input("Qual seu SEXO [M/F] ").upper())
#     if dados['sexo'] not in 'FM' :
#         dados['sexo']=str(input("Qual seu SEXO [M/F] ").upper())
#     if dados['sexo'] in 'F':
#         mulheres.append(dados['nome'])
#     dados['idade']=int(input("Digite sua Idade: "))
#     somaid += dados['idade']
#     if dados['idade'] >= 21:
#         maiores.append(dados['nome'])
#     total+=1
#     listados.append(dados.copy())
#     resp=str(input('Quer continuar? [S/N]').strip().upper())
#     if resp in 'N':
#         break
# media=somaid/total
# print(dados)
# print(listados)
# print(f'A média de idade dos cadastrados é {media:,.2f} anos!')
# print(f'Mulheres cadastradas: {mulheres}')
# print(f'Os maiores de idade são : {maiores}')
# print (f'Total cadastrados {total}')
# =============================== 095 ===================================
print('=-'*20)
print("{:-^40}".format(" Jogador de Futebol "))
print('=-'*20)
total = 0
dados=dict()
partidas=list()
while True:
    dados['nome']=str(input("Digite seu nome: ").strip().title())
    dados['partidas']=int(input(f"Quantas Partidas {dados['nome']} jogou: "))
    for x in range(0,dados['partidas']):
        partidas.append(int(input(f"Digite Quantos gols foram feitos no {x}º jogo? ")))
    dados['gols']=partidas[:]
    dados['totalgols']= sum(partidas)
    dados['aproveitamento']=(dados['totalgols']/ dados['partidas'])
    print('=-'*20)
    resp=str(input("Quer Continuar? [S/N]").strip().upper())
    if resp not in 'NS':
        resp=str(input("Quer Continuar? [S/N]").strip().upper())
    for k, v in dados.items():
        print(f"O campo {k} tem o valor {v} !")
    print('=-'*20)
    for i,v in enumerate(dados['gols']):
        print(f"    => Na {i+1}ª Partida - {dados['nome']}, fez {v} Gol's")
    print('=-'*20)
    print(f'Essa é a carreira de {dados["nome"]} com {dados["aproveitamento"]} gols por jogo!')
    if resp in 'N':
        break