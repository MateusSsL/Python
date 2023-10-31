from cev115 import mensagem
import corescev as cor
def arqExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo{nome}')
    else:
        print(f'Arquivo {nome} , Criado com sucesso!')

def lerAqv(nome):
    try:
        a=open(nome,'rt')
    except:
        print('Não foi possivel ler o arquivo')
    else:
        mensagem(f'{cor.GREEN}Pessoas Cadastradas{cor.RESET}')
        #print(f'{cor.CYAN}{a.read()}{cor.RESET}')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado [1].replace('\n','')
            print(f'{cor.CYAN}{dado[0]:<20}{dado[1]:>10} anos{cor.RESET}')
    finally:
        a.close()


def cadastrar(arq,nome='desconhecido',idade='nao_declarou'):
    try:
        a=open(arq,'at')
    except:
        print(f'{cor.RED}Não foi possivel abrir o arquivo{cor.RESET}')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'{cor.RED}Houve um erro ao escrever os dados!{cor.RESET}')
        else:
            print(f'Novo registro de {cor.CYAN}{nome}{cor.RESET} foi cadastrado com sucesso')
            a.close()
