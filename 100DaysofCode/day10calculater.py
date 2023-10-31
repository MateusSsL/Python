from art import logo
print(logo)


def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2
 

operations={
'+': add,
'-': subtract,
'*': multiply,
'/': divide,
}
status=True 
while status is True:
    num1=int(input('Enter your first number: '))
    for symbols in operations:
        print(symbols)
    operations_symbol=input('choose an operation from the line above: ')
    num2=int(input('Enter the second number: '))
    calculation_function = operations[operations_symbol]
    first_answer= calculation_function(num1,num2)

    print(f'{num1} {operations_symbol} {num2} = {first_answer}')

    while True:
        resp1= input('Do you want to continue?[Y/N]').upper()
        if resp1 in 'YES':
            print(f'Resume = {first_answer} ')
            resp2=input('Want to clear?[Y/N]').upper()
            if resp2 in 'YES':
                first_answer=0
                break

            operations_symbol=input('pick another operation: ')
            num3=int(input("What's the next number: "))
            calculation_function = operations[operations_symbol]
            second_answer=calculation_function(first_answer,num3)

            print(f'{first_answer} {operations_symbol} {num3} = {second_answer}')
        if resp1 in 'NO':
            print('Fim')
            status=False
            break


  
