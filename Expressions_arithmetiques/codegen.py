########################
#
# codegen.py
# ----------
#
# Producteur de code a trois adresses
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

import os,stat

def prod(ch):
	'''
	Produit un fichier executable python nommé a.out, a partir de la liste d'unites lexicales en notation postfixee <ch>
	prise en entree
	'''
	i=0
	with open("a.out", "w") as fichier:
		fichier.write("#!/usr/bin/python3\n")
		for el in ch:
			if(el[0]=="NOMBRE"): # Si c'est un nombre, on empile
				fichier.write("t"+str(i)+"="+el[1]+"\n")
				i+=1
			elif(el[0]=="OP"): # Si c'est un operateur, on depile 2 fois
				fichier.write("t"+str(i-2)+"="+"t"+str(i-2)+el[1]+"t"+str(i-1)+"\n")
				i-=1
		os.chmod("a.out", stat.S_IRWXU) # On donne les droits d'execution au proprietaire
		fichier.write("print(t0)\n")

if __name__=='__main__':

	'''
		Exemple d'execution de la fonction prod,
		Un fichier executable est cree, le resultat sera stocké dans t0, donc le code affiche t0.
	'''

	example_ch=[('NOMBRE', '4'),('NOMBRE', '2'), ('OP', '+')]
	prod(example_ch)

	os.system("echo 'Resultat : '")
	os.system("./a.out")