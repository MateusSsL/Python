# Crie um dicionário para armazenar os lances com os nomes das pessoas
lances = {}

# Solicite ao usuário que insira lances até que eles não queiram mais participar
while True:
    nome = input("Digite o nome da pessoa (ou 'fim' para encerrar): ")
    
    if nome.lower() == 'fim':
        break
    
    lance = float(input("Digite o lance: "))
    
    lances[nome] = lance

# Verifique e determine o vencedor com o lance mais alto
if lances:
    vencedor = max(lances, key=lances.get)
    lance_vencedor = lances[vencedor]
    print(f"O vencedor do leilão é {vencedor} com um lance de R${lance_vencedor:.2f}")
else:
    print("Nenhum lance foi dado no leilão.")