from time import sleep
from cev115 import menu,centralizando,leiaint
from arquivo115 import arqExiste,criarArq,lerAqv,cadastrar
import corescev as cor
#=============================== 115 ===================================
arq = 'usuarios.txt'
if not arqExiste(arq):
    criarArq(arq)


while True:
    resposta = menu([f'Cadastrar Pessoas','Listar Pessoas','Sair do Sistema'])
    if resposta ==1:
        centralizando('Novo Cadastro!')
        nome=str(input('Nome: '))
        idade=leiaint('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 2:
        lerAqv(arq)
    elif resposta == 3:
        centralizando(f'{cor.GREEN}Saindo do Sistema...Até logo!{cor.RESET}')
        break
    else:
        centralizando(f'{cor.RED}Erro digite uma opção Válida{cor.RESET}')
    sleep(2)
    