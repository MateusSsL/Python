print("seja bem vindo a calculadora de taxa!")

compra = float(input("qual o total da compra? $ ") )

taxa = int(input("qual a porcentagem que vc gostaria de pagar? 10 , 12 ou 15? ") )

pessoas = int(input("quantas pessoas iram dividor a compra com vc ?") )

#calculo da compra com taxa
taxa_calc = (taxa / 100) * compra + compra
div_compra = taxa_calc / pessoas
#usar round para separar até 2 casa decimais apenas
total_final = round(div_compra, 2)
#para transformar 82.5 em 82.50 precisamos formatar com: "{:.2f}".format(variavel)
total_final = "{:.2f}".format(total_final)
#usar f-string para transformar em string tudo de uma vez
print(f"total para cada: {total_final} reais.")
