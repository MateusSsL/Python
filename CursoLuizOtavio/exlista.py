import os
'''
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir,apagar e listar valores da sua lista
não permita que o programa quebra com erros
de índices inexistentes na lista.
'''
listaatual=[]
def linha():
    print('~~'*20)
def inserir(item):
    '''colocando o 'item' na lista atual'''
    if item is str:
        listaatual.append(item)
        limpar_terminal()
        print(f'{item} foi adicionado a lista com sucesso.')
    else:
        limpar_terminal()
        print('Digite nomes de produtos')
        print(f'{item} não pode ser adicionado a lista')
def listar():
    '''listando listaatual'''
    if len(listaatual)>=1:
        limpar_terminal()
        linha()
        print('{:_^40}'.format('Lista de Compra'))
        linha()
        for indice,item in enumerate(listaatual):
            print(f'{indice:<5}{item:>5}')
        linha()
    else:
        print('A lista ainda não possui nenhum item')
def apagar(indice):
    '''Apagar um item pop(indice)'''
    if len(listaatual)>=1 or indice>len(listaatual):
        try:
            indice=int(indice)
            listaatual[indice]
        except Exception:
            print('Digite um número valido de indice')
        else:
            print(f'{listaatual[indice]} foi Removido')
            listaatual.pop(indice)
    else:
        limpar_terminal()
        print('A lista não possui items ainda')
def limpar_terminal():
    '''Use a função para limpar o terminal no vscode'''
    os.system('cls' if os.name == 'nt' else 'clear')
sair=False
while sair is not True:
    resp=input('Selecione uma Opção \n[i]nserir [a]pagar [l]istar [s]sair\nOpção: ').strip().lower()
    if len(resp)>1:
        print('Escolha apenas UMA opção')
    if resp in 'lias':
        if resp == 'i':
            inserir(input('Item: '))
        elif resp == 'a':
            apagar(input(f'Digite o indice do item que deseja remover: '))
        elif resp == 'l':
            listar()
        elif resp == 's':
            print('Volte Sempre')
            sair=True
    else:
        print('Digite uma opção válida')