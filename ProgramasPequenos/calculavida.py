#calculadora de semanas restante de vida, idade max 90.
age = input("Quantos anos vc tem?")
#Diferenca entre idade final e atual
final = 90 - int(age)
#um ano tem 52 semanas
weeks = final * 52

print(f"Voce ainda tem {weeks} Semanas de vida.")
