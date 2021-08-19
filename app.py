'''
name = input("What is your name? ")
color = input(f"and what is your favorite color {name}? ")
print(f"{name} likes the color {color}!")

kg_weight = input("How much do you weight in kilos? ")
in_pounds = float(kg_weight) * 2.20462262185
print("Your weight in pounds is "+str(in_pounds))

#Se usar [] para definir a variável string, retorna um array excluindo o último index
print(name[0:3])
#deve retonar NEV, se a variável for Nevile str[nevile]=array[012345]

#A index 0 do array será sempre a primeira letra.
#Se o index for negativo, é de trás para frente com o 0 sendo a primeira letra ainda
print(name[1:-1])
#deve retornar EVIL
'''
'''
#Next is IF STATEMENTS
is_hot = True
is_cold = True

if is_hot:
    print("Drink lot's of water.")
elif is_cold:
    print("Waer warm clothes.")
else:
    print("It's a lovely day.")
print("Have a lovely day")
'''
'''
price = 1000000
is_good = False

if is_good:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
    print(f"Down Payment is going to be ${down_payment}.")
'''
'''
name = input("What is your name?")

if len(name) < 3:
    print("Name must be at least 3 characters length, let's try again.")
    name = input("What is your name?")
elif len(name) > 50:
    print("Name can be a maximum 50 characters length, let's try again.")
    name = input("What is your name?")
else:
    print("Beautiful name!")
'''
weight = int(input("Weight:"))
unit = input("(K)g or (L)bs:")

if unit.upper() == "K":
    converted_weight = weight * 2.204623
    print(f"You weight {converted_weight} pounds")
else:
    converted_weight = weight * 0.4535924
    print(f"You weight {converted_weight} kilos")