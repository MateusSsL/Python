# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] [::]
# Obs.: a função len retorna a qtd 
# de caracteres da str
# """
# variavel = 'Olá mundo'
# print(variavel[::-1])

nome=str(input("Seu nome: ") or 'nada')
idade=int(input("Sua idade: ") or 0)
if not nome or not idade or nome=='nada' or idade == False :
    print("Desculpe, você deixou campos vazios.")
else:
    if ' ' in nome:
        esp = 'Contem'
    else:
        esp = 'Não Contem'
    print(f"A ultima letra do seu nome é {nome[-1]} .")
    print(f"Seu nome {esp}  espaços.")
    print(f"Seu nome tem {len(nome)} letras.")
    print(f'Seu nome é : {nome}')
    print(f"Nome invertido = {nome[-1::-1]}")
    print("Seu nome é: %s e sua idade é: %i "%(nome,idade))
    
