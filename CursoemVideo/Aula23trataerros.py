from cev import leiafloat,leiaint
import urllib.request
#=============================== Tratamento de erros e exceções ===================================
# try:
#     p=int(input("Digite o Numerador: "))
#     d=int(input("Digite o Divisor: "))
#     r=p/d
# except (ValueError,TypeError):
#     print(f'Tivemos um problema com o tipo de dado que você digitou.')
# except ZeroDivisionError:
#     print(f'Não é possivel dividir por Zero.')
# except KeyboardInterrupt:
#     print('O Usuário preferiu não informar os dados.')
# except Exception as error:
#     print(f"Tivemos um problema com {error.__cause__}")
# else:
#     print(f'resultado {r:.1f}')
# finally:
#     print('Volte sempre!')
#=============================== 113 ===================================
#reescreva o desafio 104 para evitar erros e adicione o leia float
#escreva no arquivo cev.py

# PROGRAMA PRINCIPAL
# n = leiafloat('Digite um número: ')
# print(f'Você acabou de digitar o número {n}')

#=============================== 114 ===================================
#Verifique se o site X está online ou não
# try:
#     site=urllib.request.urlopen('https://github.com/MateusSsL')
# except urllib.error.URLError:
#     print('O site não está acessível no momento!')
# else:
#     print('Tudo OK!')
#=============================== 115 ===================================
