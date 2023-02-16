#coding:utf-8




ouvert = True
print("\n==== CHOISISSER LE TYPE D'OPERATION ====\n\n 1- Addition\n 2- Soustraction\n 3- Multiplication\n 4- Division\n 5- Modulo\n\n 00- QUITTER\n")

while ouvert:
	choixMenu = input("Calculatrice# ")
	choixMenu = int(choixMenu)

	if choixMenu == 1:
		print("Vous avez choisi l'Addition !")
		a = input("Premier nombre : ")
		a = int(a)
		b = input("Second nombre : ")
		b = int(b)
		print("Résultat : ", a+b,"\n")

	elif choixMenu == 2:
		print("Vous avez choisi la Soustraction !")
		a = input("Premier nombre : ")
		a = int(a)
		b = input("Second nombre : ")
		b = int(b)
		print("Résultat : ", a-b,"\n")

	elif choixMenu == 3:
		print("Vous avez choisi la Multiplication !")
		a = input("Premier nombre : ")
		a = int(a)
		b = input("Second nombre : ")
		b = int(b)
		print("Résultat : ", a*b,"\n")

	elif choixMenu == 4:
		print("Vous avez choisi la Division !")
		a = input("Premier nombre : ")
		a = int(a)
		b = input("Second nombre : ")
		b = int(b)
		print("Résultat : ", a/b,"\n")

	elif choixMenu == 5:
		print("Vous avez choisi le Modulo !")
		a = input("Premier nombre : ")
		a = int(a)
		b = input("Second nombre : ")
		b = int(b)
		print("Résultat : ", a%b,"\n")

	elif choixMenu == 00:
		choix_quit = input("Voulez vous Quitter ? (o/n) ")
		if choix_quit=="o" or choix_quit=="O":
			print("Au Revoir...")
			break
		elif choix_quit=="n" or choix_quit=="N":
			pass
		else:
			print("Choisissez Oui (o/O) ou Nom (n/N) !")
	else:
		print("Tapez un chiffre de 1 à 5 ou 00 !")