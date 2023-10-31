
#number = int(input("qual numero vc quer checar? : "))

#if number % 2 == 0 :
    #print("este é um numero par ou even")
#else :
    #print("este numero é impar ou odds")

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")  # Do you want pepperoni? "Y" or "N"
extra_cheese = input("Do you want extra cheese? Y or N ")  # Do you want extra cheese? "Y" or "N"

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")


    

    


    



