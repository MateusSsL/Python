#====================================== TUPLAS =====================================
# #Listas é prepresentada por colchetes
# lista=['Maria','Helena','Luiz']
# #Podemos mudar qualquer nome dentro de uma lista
# lista[1]='Mateus'
# print(lista)
# #Tuplas não aceitam modificar oque tem dentro dela
# #podemos modificar lista para tupla utilizando:
# tupla=tuple(lista)  #ou vice versa/ lista=list(tupla)
# #====================================== TUPLAS =====================================
# #Tupla é uma lista imutável(não aceita mudar seus itens)
# #Tupla é representada por Parênteses ou sem nada
# nomes= 'Maria','Helena','Luiz','Pedro'
# nome= ('Maria','Helena','Luiz','Pedro')
# # Quando temos muitos itens em uma lista podemos adicionar em uma variavel
# # UNDERLINE(*_) que é uma convenção entre os DEV's que é uma variavel "descartavel"
# # EXEMPLO: nome1, nome2, --> *_ =['Maria','Helena','Luiz','Pedro']
# #a variavel UNDERLINE recebe todo o resto da lista
# # o nome 'Luiz' e 'Pedro' serão guardados na variavel _
# # Asterisco significa que ele pode armazenar mais de 1 item(empacotar)
# print(nomes)
#==================================================================
lista=['Maria','Helena','Luiz']
lista.append('Mateus')

# lista_enumerada= enumerate(lista)
# for item in lista_enumerada:
#     print(item)

for indice,nome in enumerate(lista):
    print(indice,nome)