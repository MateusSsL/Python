#from cev import mensagem
# #DOCSTRING'S para quando o programador usar o help(contador),
# #Uma lista de instruções da função criada entre 3 aspas
# def contador (i,f,p):
#     """
#     :param f : fim da contagem
#     :param i : inicio da contagem
#     :param p : passo da contagem
#     """
# help(contador)


# # VALROES PADRÃO OU OPCIONAIS =0 (para caso não receba nenhum valor,evitar bugs)
# def somar(a=0,b=0,c=0):
#     s=a+b+c
#     print(f"O valor somado é : {s} !")
# somar(1,2)

#ESCOPO DE VARIAVEL
# def votos(a):
#     a+=4
#     b=7 #VARIAVEL LOCAL
#     print(a)
#     print(b)

# votos(4)
# print(b)#Nao é possivel printar o valor b porquê ele esta fora de Escopo

#================================ PRATICA ==============================
# def fatorial(num=1):
#     f=1
#     for c in range(num, 0 ,-1):
#         f *= c
#     return f


# f1= fatorial(5)
# f2=fatorial(4)
# f3=fatorial(6)
# print(f"o fatorial de {f1} {f2} {f3}")

#================================ EXERCICIOS ==============================
#================================ 101 ==============================
'''
CRIE UM PROGRAMA QUE TENHA UMA função CHAMADA voto() QUE VAI RECEBER parâmetro
ANO DE NASCIMENTO DE UMA PESSOA , RETORNANDO UM VALOR LITERAL INDICANDO SE UMA
PESSOA TEM VOTO NEGADO,OPCIONAL OU OBRIGATORIO NAS ELEIÇÕES
'''
# def voto(idade=0):
#     '''
#     Idade >= 18 : OBRIGATÓRIO
#     Idade >=16 and >60 : OPCIONAL
#     idade <16 : NEGADO
#     '''
#     if idade < 16:
#         return 'NEGADO'
#     if idade >=16 and idade<18 or idade>=60:
#         return 'OPCIONAL'
#     if idade>=18 and idade<60:
#         return 'OBRIGATÓRIO'


# mensagem('Eleições 2023')
# id=int(input("Digite sua idade: "))
# print(f"Seu voto nessas eleições é : {voto(id)} !")
# lin()
#================================ 102 ==============================
'''
CRIE UM PROGRAMA QUE TENHA UMA função CHAMADA fatorial() QUE VAI RECEBER 2 parâmetros
O PRIMEIRO QUE INDIQUE O numero A CALCULAR
E O OUTRO CHAMADO show,QUE SERÁ UM VALOR LÓGICO(opcional) INDICANDO SE SERÁ MOSTRADO OU NÃO
NA TELA O PROCESSO DE CÁLCULO DO FATORIAL
'''

# def fatorial(num=1,logic=False):
#     f=1
#     print(f"Fatorando {num} ",end='')
#     for c in range(num-1,0,-1):
#         f *= c
#         if logic == True:
#             print(f"x {c} ",end='')
#     if logic == False:
#         print(f"= {f}")
#     if logic != False:
#         print(f"= {f}")
        
# fatorial(4,True)

#================================ 103 ==============================
'''
CRIE UM PROGRAMA QUE TENHA UMA função CHAMADA ficha() QUE VAI RECEBER 2 parâmetros
O PRIMEIRO QUE INDIQUE O nome DE UM JOGADOR ,E O OUTRO CHAMADO gols,QUE O JOGADOR MARCOU
O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAS A FICHA DO JOGADOR, MESMO QUE ALGUM DADO NÃO TENHA
SIDO INFORMADO CORRETAMENTE.
'''
# def ficha(nome='<Desconhecido>',gols=0):
#     mensagem('Ficha do jogador')
#     print(f'Nome do jogador: {nome:^12}')
#     print(f'Numero de Gols: {gols:^12}')
#     lin()


# nom=str(input("Nome do jogador: ").strip().title())
# gol=str(input("Numero de Gols: "))

# if gol.isnumeric():
#     g=int(gol)
# else:
#     gol=0
# if nom == '':
#     ficha(gols=gol)
# else:
#     ficha(nom,gol)
#================================ 104 ==============================
'''
CRIE UM PROGRAMA QUE TENHA UMA função CHAMADA leiaint() QUE VAI FUNCIONAR SEMELHANTE
À FUNÇÃO input() DO PYTHON , SÓ QUE FAZENDO A validação PARA ACEITAR APENAS UM VALOR
NUMERICO.
'''
# def leiaint(msg):
#     ok=False
#     valor= 0
#     while True:
#         n=str(input(msg))
#         if n.isnumeric():
#             valor=int(n)
#             ok=True
#         else:
#             print('\033[31mERRO! Digite um número inteiro válido.\033[0ml')
#         if ok:
#             break
#     return valor
# # PROGRAMA PRINCIPAL
# n = leiaint('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')
#================================ 105 ==============================
'''
CRIE UM PROGRAMA QUE TENHA UMA função CHAMADA notas() QUE PODE RECEBER VÁRIAS NOTAS
DE ALUNOS E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:
- QUANTIDADE DE NOTAS
- MAIOR NOTA
- MENOR NOTA
- A MÉDIA DA TURMA
- A SITUAÇÃO DE CADA ALUNO(APROVADO,REPROVADO)
ADICIONE DOCSTRINGS NA FUNÇÃO
'''
# def notas(*n,sit=False):
#     """
#     => Função para analisar notas e situações de vários alunos.
#     :param n: Uma ou mais notas dos alunos(aceita várias).
#     :param sit: Valor opcional,indicando se deve ou não adicionar a situação.
#     """
#     r = dict()
#     r['total'] = len(n)
#     r['maior']=  max(n)
#     r['menor']=  min(n)
#     r['média']=  sum(n)/len(n)
#     if sit:
#         if r['média']>=7:
#             r['situação']='APROVADO'
#         elif 7>r['média']>=5:
#             r['situação']='RECUPERAÇÃO'
#         else:
#             r['situação']="REPROVADO"
#     return r


# #PROGRAMA PRINCIPAL
# resp= notas (5.5,2.4,9,8,sit=True)
# print(f"\033[31m{resp}")

#https://youtu.be/etjJ_4Eqrk8?si=PGP06-DVS7RzKpqw&t=2840
#================================ 106 ==============================
'''
FAÇA UM MINI-SISTEMA QUE UTILIZE O interactive Help DO PYTHON.O USUÁRIO VAI
DIGITAR O COMANDO E O MANUAL VAI APARECER. QUANDO O USUÁRIO DIGITAR A PALAVRA
'FIM' O PROGRAMA SE ENCERRARÁ.
USE CORES
'''

from time import sleep
# Cores de fundo
BG_ROXO = "\033[44m"
BG_ROSA = "\033[45m"
BG_CYAN = "\033[46m"
# Códigos ANSI para cores e estilo
RESET = "\033[0m" #Reset
BOLD = "\033[1m" #Negrito

def mensagem(titulo,cor):
    print(f"{cor}")
    print("{:-^40}".format('~~'*20))
    print("{:-^40}".format(titulo))
    print("~~"*20,)
    print(f"{RESET}")
    sleep(1)


def ajuda(com):
    mensagem(f'Acessando o manual do comando {comando}',BG_CYAN)
    sleep(1)
    help(com)
    print('Digite FIM para Sair')
 
print('Digite FIM para Sair')
mensagem(f'SISTEMA DE AJUDA PyHelp',BG_ROXO)
while True:
    comando=str(input(f"{RESET}{BOLD}Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        mensagem(f'  ATÉ LOGO  ',BG_ROSA)
        break
    else:
        ajuda(comando)