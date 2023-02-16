#coding:utf-8

print("\n===== Calculatrice v2 =====")
print("\n 1. Addition\n 2. Soustraction\n 3. Multiplication\n 4. Division\n\n 00. Quitter\n")

ouvert = True 
while ouvert:
	choix=input("Choix > ")
	choix=int(choix)

	if choix==1:
		addition(int(input("\na = ")),int(input("b = ")))
	elif choix==2:
		soustraction(int(input("\na = ")),int(input("b = ")))
	elif choix==3:
		multiplicateur(int(input("\na = ")),int(input("b = ")))
	elif choix==4:
		division(int(input("\na = ")),int(input("b = ")))
		
	elif choix==00:
		choix_q=input("Voulez vous Quitter ? (o/n) ")
		if choix_q=="o" or choix_q=="O":
			print("Au revoir...")
			break
		if choix_q=="n" or choix_q=="N":
			continue