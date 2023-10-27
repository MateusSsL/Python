#https://youtu.be/etjJ_4Eqrk8?si=PGP06-DVS7RzKpqw&t=2840
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

