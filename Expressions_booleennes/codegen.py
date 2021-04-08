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
		fichier.write("#!/usr/bin/python\n")
		for el in ch:
			if(el[1]=="VRAI"):
				fichier.write("t"+str(i)+"=True"+"\n")
				i+=1
			elif(el[1]=="FAUX"):
				fichier.write("t"+str(i)+"=False"+"\n")
				i+=1
			elif(el[1]=="ET"):
				fichier.write("t"+str(i-2)+"="+"t"+str(i-2)+" and "+"t"+str(i-1)+"\n")
				i-=1
			elif(el[1]=="OU"):
				fichier.write("t"+str(i-2)+"="+"t"+str(i-2)+" or "+"t"+str(i-1)+"\n")
				i-=1
			elif(el[1]=="NON"):
				fichier.write("t"+str(i-1)+"=not "+"t"+str(i-1)+"\n")
		os.chmod("a.out", stat.S_IRWXU)# On donne les droits d'execution au proprietaire
		fichier.write("print(t0)\n")

if __name__=='__main__':

	'''
		Exemple d'execution de la fonction prod,
		Un fichier executable est cree, le resultat sera stocké dans t0, donc le code affiche t0.
	'''

	example_ch=[('BOOL', 'VRAI'), ('BOOL', 'FAUX'),('OP', 'OU')]
	prod(example_ch)

	os.system("echo 'Resultat : '")
	os.system("./a.out")
