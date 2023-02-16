#coding:utf-8

"""
Module pour le joueur 
"""

def parler(perso, message):
	print("{} : {}".format(perso,message))

au_revoir = lambda : print("Au revoir ...")

# POUR TESTER LE MODULE SEULEMENT 
if __name__ == "__main__":
	print("=== Phase de Test ===")

	parler("Koura ", " Fonctionne !")
	au_revoir()