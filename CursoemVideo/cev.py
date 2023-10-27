
def mensagem(titulo):
    print("-="*20)
    print("{:-^40}".format(titulo))
    print("-="*20)

def lin():
    print("-="*20)

def centralizando(msg):
    print("{:-^40}".format(msg))

def contador(*num): #criar uma tupla com valores
    print(num) # num(1, 2, 3, 4, 5)
    # [1, 2, 3, 4, 5]

def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos] *= 2
        pos+=1
        # valores = [2,4,3,5,6] criar lista
        # print(valores)
        # dobra(valores)
        # print(valores)

def soma(* valores):  #crie um lista para colocar em valores
    s=0  #s vai receber a soma dos itens dentro da lista
    for n in valores:  #num=[4,8,9,2]
        s +=n
    print(f"Somando os {valores} temos {s}")
    #soma(*num)
    


