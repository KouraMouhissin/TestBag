#coding:utf-8

print("\n===== Table de Multiplication =====")

programme = True

while programme:
	a = input("\nMultiplicateur > ")
	a=int(a)

	if a == 0:
		choix=input("\nVoulez vous quitter le programme ? (o/n) > ")
		if choix=="o" or choix=="O":
			print("Au revoir ...")
			break
		elif choix=="n" or choix=="N":
			print("Merci ...")
			continue

	i=0
	while i<=12:
		print(a, " X ", i ," = ", a*i)
		i=i+1

