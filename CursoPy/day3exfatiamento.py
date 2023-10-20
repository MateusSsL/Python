#fatiamento e procura de dados em variavel=====
frase = "curso python em video"
print(frase[9]) #oq tem na posição 9
print(frase[0:10]) #oq tem entre 0 a 9 na frase
print(frase[:9]) #oq tem antes da posição 9 
print(frase[8:]) #oq tem na posição 9 pra frente
print(frase[8:2:15]) #oq tem entre 8 a 15 pulando de 2 em 2

#analise========================================
#use r para achar coisas no extemo direito frase.rfind()
#use l para achar coisas na extrema esquerda frase.lfind()
print(len(frase)) #saber o tamanho da variavel frase
print(frase.count['o',0,13]) #quantas letras 'o' tem do 0 a 12
print(frase.find['deo']) # quantas vezes ele encontrou a palavra 'deo' e onde ela começou (posição incial)
print('video' in frase) # vai dizer se existe ou nao a palavra 'video' na variavel frase (sim ou n)
print(frase.rfind['x']) #usado para achar a ultima posição de 'x' ou extrema direita
#transformação========================================
frase.replace('python', 'Android')#vai substituir python por Android
frase.upper()#vai deixar a frase toda em maiusculo
frase.lower()#vai deixar tudo em minusculo
frase.capitalize()#vai deixar só a primeira Letra da frase em Maiusculo o restante da frase em minusculo
frase.title()#deixa todas as primeiras letras de todas as palavras maiuscula
frase.strip()#remove todas as linhas de espaço inuteis da frase (começo e fim)
frase.rstrip()#remove as linhas de espaço na extrema direita(fim da frase)
frase.lstrip()#remove as linhas de espaço do começo
#divisao==============================================
frase.split()#vai dividir a frase entre os espaços das palavras(gera uma lista)
'-'.join(frase)#vai juntar a lista com o elemto entre aspas (traço) ex curso-python
lista = ['12','25','4','6']
lista.sort()#vai colocar uma lista em ordem crescente
lista.append('15')#Adiciona alguma coisa no final da lista
lista.insert(0, 40) #adiciona um numero 40 na posição 0