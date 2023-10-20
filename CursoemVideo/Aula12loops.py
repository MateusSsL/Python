# O Curso de Python está de volta no seu Mundo 2 e vai falar sobre
# Estruturas de Controle da linguagem:
# if.. elif.. else, for e while.

# valdc = int(input("Qual o valor da casa? ").format('{:.2f}'))
# salario = int(input("Qual o seu salario? ").format('{:.2f}'))
# anos = int(input("Em quantos anos você deseja pagar? "))
# parcela = valdc / (anos * 12)
# parcela= round(parcela)
# salariomin = salario * 0.3
# if parcela > salariomin :
#     print("Financiamento Negado. Valor muito alto : {:.2f} ".format(parcela) )
# else:
#     print("Financiamento Aprovado. O valor da parcela será de {:.2f} ")

# numero =int(input("Digite um numero: "))

# binario = bin(numero)
# dec = oct(numero)
# hexa = hex(numero)

# escolha = input('Escolha se quer transformar em 1 binario,2 decimal ou 3 hexadecimal: ')
# if escolha == '1':
#     print(binario)
# if escolha =='2':
#     print(dec)
# if escolha == '3':
#     print(hexa)

# idade = int(input("Digite sua Idade : ").strip())
# tf = 18 - idade
# ts = idade - 18
# if idade < 18:
#     print('Ainda falta {} anos para vc se alistar fique atento!'.format(tf))
# elif idade == 18:
#     print('Você precisa se apresentar na junta militar mais proxima a sua casa para o serviço de alistamento obrigatorio! ')
# elif idade > 18:
#     print("Você passou {} anos do servço de alistamento obrigatorio!".format(ts))idade = int(input("Digite sua Idade : ").strip())

# idade = int(input("Digite sua Idade : ").strip())

# if idade <= 9:
#     print('Nadador MIRIM')
# elif idade <= 14:
#     print('Nadador: INFANTIL')
# elif idade <= 19:
#     print("Nadador: JUNIOR")
# elif idade == 20:
#     print("Nadador: SENIOR")
# elif idade > 20:
#     print("Nadador: MASTER")

def verificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c :
            print("Esse é um triangulo equilatero")
        elif a == b or b == c or c == a:
            print ('Esse é um triangulo isósceles')
        if a != b and b != c:
            print("Esse é um triangulo escaleno")
        return 'Consigo formar um Triangulo !'
    
    else:
        return 'Impossivel formar um tringualo com esses numeros!'
    
numeros =input("Digite 3 numeros para formar um triangulo: ").strip().split()
numero = [int(transforma) for transforma in numeros]
a = numero[0]
b = numero[1]
c = numero[2]
print(a + b)
resultado = verificar_triangulo(a,b,c)
print(resultado)
