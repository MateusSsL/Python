import corescev as cor

def leiaint(msg):
    ok=False
    while True:
        try:
            n=int(input(msg))
            ok=True
        except Exception as erro:
            print(f'{cor.RED}ERRO! Encontramos o Erro {erro.__class__}.{cor.RESET}')
        if ok:
            break
    return n

#Curso Em Video modulo
def lin(tam=20):
    '''quebra linha com '''
    return '-=' * 20

def mensagem(titulo):
    '''
    escreve 3 linhas , e uma mensagem centralizada na segunda'''
    #print("{:-^40}".format(titulo))
    print(lin())
    print(titulo.center(50))
    print(lin())

def menu(lista):
    mensagem(f'{cor.YELLOW}MENU PRINCIPAL{cor.RESET}')
    c=1
    for item in lista:
        print(f'{cor.BLUE}{c}{cor.RESET} - {cor.MAGENTA}{item}{cor.RESET}')
        c += 1
    print(lin())
    opc= leiaint(f'{cor.BOLD}Sua Opção: {cor.RESET}')
    return opc

def centralizando(msg):
    '''centraliza uma mensagem com 40 espaços'''
    print(lin())
    print(msg.center(40))