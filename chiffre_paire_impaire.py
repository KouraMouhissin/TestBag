#coding:utf-8

ouvert = True

while ouvert:
	nombre = input("Terminal# ")
	nombre = int(nombre)

	test = nombre % 2
	test = bool(test)

	if nombre==0 or nombre==1 or nombre==2 or nombre==3 or nombre==4 or nombre==5 or nombre==6 or nombre==7 or nombre==8 or nombre==9:
		if not test:
			print("Le chiffre ", nombre ," est paire.")
			continue
		else:
			print("Le chiffre ", nombre ," est impaire.")
			continue

	elif nombre == 999:
		print("Vous quittez l'interface...")		
		break

	else:
		if not test:
			print("Le nombre ", nombre ," est paire.")
			continue
		else:
			print("Le nombre ", nombre ," est impaire.")
			continue
