########################
#
# parser.py
# ----------
#
# Analyseur syntaxique d'expression arithmetique
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

'''
Grammaire :
	(MAXINT=9223372036854775807)
	(NOMBRE->[0-MAXINT])
	T: {NOMBRE,+,-,/,*,(,)}
	N: {Exp,Teme,Rste,Reste2,Facteur,Chiffre}
	S: Exp
	P:  Exp -> TermeReste
		Terme -> FacteurReste2
		Reste -> +TermeReste | -TermeReste | epsilon
		Reste2 -> *FacteurReste2 | /FacteurReste2 | epsilon
		Facteur -> (Exp) | Chiffre
		Chiffre -> NOMBRE
'''

import sys,os,stat

ch = [] # la chaine des unites lexicales prise en entree
pc = 0 # pointeur sur les elements de ch
liste=[] # Cette liste contiendra l'expression postfixee des unites lexicales

def parser(ul):
	'''
	Fonction principale qui convertit la liste d'unites lexicales <ul> en une autre liste <liste> mais en notation postifxee.
	Retourne 0 en cas d'erreur et affiche le caractere fautif, ou erreur syntaxique.

	'''
	global ch
	ch = ul
	if(Exp() and len(ul)==pc):
		print("chaine valide")
		return(liste)
	else:
		print("erreur syntaxique")
		exit()
		return(0)

def Exp():
	global pc

	save=pc
	if(Terme() and Reste()):
		return(1)
	pc=save
	return(0)

def Terme():
	return(Facteur() and Reste2())

def Reste():
	global liste

	if(pc==len(ch)): # S'il ne reste plus d'element a lire, il n'y a pas d'erreur donc return(1)
		return(1)
	cc=ch[pc]
	if(Reconnaitre("+")):
		if(Terme()):
			liste.append(cc)
			if(Reste()):
				return(1)
		Erreur()
		return(0)
	elif(Reconnaitre("-")):
		if(Terme()):
			liste.append(cc)
			if(Reste()):
				return(1)
		Erreur()
		return(0)
	return(1)

def Reste2():
	global liste

	if(pc==len(ch)): # S'il ne reste plus d'element a lire, il n'y a pas d'erreur donc return(1)
		return(1)
	cc=ch[pc]
	if(Reconnaitre("*")):
		if(Facteur()):
			if(Reste2()):
				liste.append(cc)
				return(1)
		Erreur()
		return(0)
	elif(Reconnaitre("/")):
		if(Facteur()):
			if(Reste2()):
				liste.append(cc)
				return(1)
		Erreur()
		return(0)
	return(1)

def Facteur():
	if(Chiffre()):
		return(1)
	elif(Reconnaitre("(") and Exp() and Reconnaitre(")")):
		return(1)
	return(0)

def Chiffre():
	global pc,liste
	if(pc < len(ch)):
		if(ch[pc][0]=="NOMBRE"):
			liste.append(ch[pc])
			pc+=1
			return(1)
		return(0)
	return(0)

def Reconnaitre(c):
	global pc

	if(pc==len(ch)):
		return(0)
	if(c==ch[pc][1]):
		pc+=1
		return(1)
	return(0)

def Erreur():
	print("Erreur, caractere : "+ str(pc))
	return(0)

if __name__=='__main__':
	param=[('NOMBRE', '32'), ('OP', '/'), ('NOMBRE', '2'),('OP', '+'),('NOMBRE', '21')]

	print(parser(param))


