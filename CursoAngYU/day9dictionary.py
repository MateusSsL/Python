# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program,
# you should have a new dictionary called student_grades that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.
#========================================= Exercicio ==========================================
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# student_grades=dict()
# for score in student_scores:
#     k = student_scores[score]
#     if  k > 90:
#         student_grades[score] = "Outstanding"
#     elif  k > 80:
#         student_grades[score] = "Exceeds Expectations"
#     elif  k > 70:
#         student_grades[score] = "Acceptable"
#     else:
#         student_grades[score] = "Fail"  
# #Scores 91 - 100: Grade = "Outstanding"
# # Scores 81 - 90: Grade = "Exceeds Expectations"
# # Scores 71 - 80: Grade = "Acceptable"
# # Scores 70 or lower: Grade = "Fail"
# for x,k in student_grades.items():
#   print(f'{x} is {k} !')
#   if k == 'Fail':
#     print(f'DAMN {x} você deveria estudar mais')
#========================================= Nesting/Aninhamento ==========================================
# You are going to write a program that adds to a travel_log.
# You can see a travel_log which is a List that contains 2 Dictionaries.
# Your job is to create a function that can add new countries to this list.
# Write a function that will work with the following line of code on line 21
# to add the entry for Brazil to the travel_log.
# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
#=========================================#=========================================
# country = input('Qual o nome do Pais que você visitou? ') # Add country name EX= Brazil
# visits = int(input(f'Numero de visitas ao {country}: ')) # Number of visits EX= 2
# list_of_cities = eval(input('Nome das cidades que você visitou? \nEX= ["Sao Paulo", "Rio de Janeiro"]')) # create list from formatted string EX= ["Sao Paulo", "Rio de Janeiro"]
# travel_log = [
#   {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
#   },
#   {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
#   },
# ]
# def add_new_country(name,total_cities_visit,cities_visit):
#     new_country={}
#     new_country['country']= name
#     new_country['visits']=total_cities_visit
#     new_country['cities']=cities_visit
#     travel_log.append(new_country.copy())

# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")
#=========================================#=========================================
import os
from art import logo
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
maior=0
dados=list()
regist=dict()
print(logo)
print("-="*20)
print("{:-^40}".format(' Leilão online/Auction House '))
print("-="*20)
fim=False
while not fim:
    regist['Nome']=str(input("Digite seu nome/What's your name? ").title())
    regist['Oferta']=float(input("Qual será o valor do seu lance?/Bid "))   
    if regist['Oferta']> maior :
        maior=regist['Oferta']
        regist['Vencedor']=regist['Nome']
    dados.append(regist.copy())
    while True:
        resp=str(input("Mais alguem?/Another one to join?[S/N]").upper())
        if resp not in 'SN':
            resp=str(input("Tem outra pessoa para participar?[S/N]").strip().upper())
        elif resp =='S':  
            limpar_terminal()
            break
        elif resp == 'N':
            print(f"O vencedor é foi(winner) {regist['Vencedor']} !! \nCom um lance de(bid) {maior:.2f} $ !")
            fim=True
            break
        

