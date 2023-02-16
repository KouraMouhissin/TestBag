#coding:utf-8

print("\n===== Comparateur d'Age =====\n")

nomPerso = input("Votre Nom # ")

age = input("Age> ")
age = int(age)

if 0 < age < 18:
	print(nomPerso, ", Vous etes un gamin !")
elif age==18:
	print(nomPerso, ", Majeur Novice !")
elif 18 < age < 40:
	print(nomPerso, ", Vous etes Jeune !")
elif age==40:
	print(nomPerso, ", Bonjour la Vieillèsse !")
elif 40 < age < 80:
	print(nomPerso, ", Vous etes Vieux !")
elif 80 < age < 100:
	print(nomPerso, ", Vous etes chanceux !")
elif age == 100:
	print(nomPerso, ", Vous avez vécu un siècle !")
else:
	print(nomPerso, ", Vous n'etes pas Humain !")


