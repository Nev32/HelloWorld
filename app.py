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

#Next is IF STATEMENTS

is_hot = True

if is_hot:
    print("Drink lot's of water.")
print("Have a lovely day")



