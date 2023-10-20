line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# Loop principal do jogo
while True: 
    print("Esse é o jogo de escolher a posição do tesouro.\n")
    print(f"{line1}\n{line2}\n{line3}")
    
    position = input("Digite as position do tesouro (por exemplo, A1 a C3): ").upper()
    # Verificar se as position são válidas
    if len(position) != 2 or position[0] not in "ABC" or position[1] not in "123":
        print("Coordenadas inválidas. Tente novamente.")
        continue
    # Obter as coordenadas em índices da matriz
    linha = "ABC".index(position[0])
    coluna = int(position[1]) - 1
    #Criando um lugar para colocar o tesouro
    if linha == 1 and coluna == 2:  # B3

        print(''' 
         __________
        /\____;;___
       | /         /
       `. ())oo() .
        |\(%()*^^()^
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
              ''')
        
        print("Você encontrou o tesouro! Parabéns!")
        break
    elif linha == 2 and coluna == 1:  # C2
        print("""
        {}          {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
mts 97     / HHH \\ 
          /  \_/  \\
        {}         {}
""")
        break
    else:
        map[coluna][linha] = "X"
        print(f"{line1}\n{line2}\n{line3}")
    resposta = input("Deseja continuar? (S para sim, qualquer outra tecla para sair): ").upper()
    if resposta != "S":
        break
print("Fim do jogo.")
 