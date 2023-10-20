from forcaapi import stages
from forcaapi import logo
from forcaapi import deflistas
import random

fim = False
vidas=6

forca = random.choice(deflistas).upper() #ESCOLHA ALEATORIA
tamanho = len(forca)#MEDINDO QUANTAS LETRAS TEM

print(logo)
print(f'A Palavra tem {tamanho} Letras')
print(forca)

display = []
for _ in range(tamanho):
    display += "_"
print(display)
while not fim:

    testar = input('Digite uma Letra : ').upper().strip()
    for posit in range(tamanho):
        letra = forca[posit]
        if letra == testar:
            display[posit] = letra

    if testar not in forca:
        vidas -= 1
        print(f"A letra: {testar} não existe na palavra, vc agora tem {vidas}! ")
        if vidas == 0:
            print('Você perdeu')
            fim = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        fim = True
        print("Você Venceu!.")

    print(stages[vidas])
        
        

    
    





