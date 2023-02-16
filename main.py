#coding:utf-8

"""

Nommer une variable : doit commencer par une lettre 
					  ne pas contenir de caractère spé
					  ne pas contenir d'espace
					  utiliser des underscore


Fonction : 		print() -> afficher à l'écran
				input() -> lire au clavier
				type()  -> retourne le type d'une donnée, variable etc.
				int(), float(), str() -> caster une donnée
				str.format() -> formater une chaine
Opérateur de comparaison : == (égal à)
						   != (différent de ) comme dans c++

Condition mutiple : and (ET)
					or (ou)
					in/not in (Dans / Pas Dans)
	Mot Clé : IF (Si)/ ELIF(Sinon Si)/ ELSE(Sinon)

Les Boucle :
			While ET For
	Mot clés : break (casse la boucle) /continue (revient au debut)

"""
"""
+++++++++CREATION DE PROMPT++++++++
jeu_lance = True

print("")
while jeu_lance:
	choixMenu = input("> ")

	if choixMenu == "encore":
		continue
	elif choixMenu == "quitter" or choixMenu == "q":
		break
	else:
		print("Commande introuvable !")

print("sortie de la boucle...") 


def surface(x,y):
	print("La surface est : ", x*y)

surface(x=int(input("\nTapez a : ")),y=int(input("\nTapez b : ")))

Si on précise les paramètres à l'appelle de la fonction, 
on n'est pas obliger de respecter l'ordre !

def show_inventory(*list_items): #Pour avoir un nombre infini d'argument
	for item in list_items:
		print(item) 


show_inventory("épée", "arc", "potion de mana", "cap")

ttc = lambda prixHT:prixHT + (prixHT * 20 / 100)
#les fonction lambda pour executer une seul instruction
print(ttc(24))

"""
"""
Liste des Modules : 
				import os
				import math

Importation du module :
						import nom_module
						from nom_module import *
						from nom_module import nom_fonction
						import dossier.nom_module as nom_module
"""
from player import *


parler("Koura","Je suis fort !")

au_revoir()
au_revoir()