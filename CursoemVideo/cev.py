#Curso Em Video modulo
def mensagem(titulo):
    '''
    escreve 3 linhas , e uma mensagem centralizada na segunda'''
    print("-="*20)
    print("{:-^40}".format(titulo))
    print("-="*20)

def lin():
    '''quebra linha com '''
    print("-="*20)

def centralizando(msg):
    '''centraliza uma mensagem com 40 espaços'''
    print("{:-^40}".format(msg))

# def contador(*num): #criar uma tupla com valores
#     print(num) # num(1, 2, 3, 4, 5)
#     # [1, 2, 3, 4, 5]

# def dobra(lst):
#     pos=0
#     while pos<len(lst):
#         lst[pos] *= 2
#         pos+=1
#         # valores = [2,4,3,5,6] criar lista
#         # print(valores)
#         # dobra(valores)
#         # print(valores)

# def soma(* valores):  #crie um lista para colocar em valores
#     s=0  #s vai receber a soma dos itens dentro da lista
#     for n in valores:  #num=[4,8,9,2]
#         s +=n
#     print(f"Somando os {valores} temos {s}")
#     #soma(*num)

def aumentar(p=0.0, porc=0.0, formato=False):
    res = p + (p*porc/100)
    return res if formato is False else moeda(res)

def diminuir(p=0.0 , porc=0.0, formato=False):
    res=p-(p* porc/100 )
    return res if formato is False else moeda(res)

def dobro(p=0.0, formato=False):

    res=p*2
    return res if not formato else moeda(res)

def metade(p=0.0, formato=False):
    res=p / 2
    return res if not formato else moeda(res)

def moeda(p=0.0 , moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.' , ',')

def resumo(p,aumen,demin):
    
