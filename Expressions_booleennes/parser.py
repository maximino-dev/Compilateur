########################
#
# parser.py
# ----------
#
# Analyseur syntaxique d'expression booleenne
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

'''
Grammaire :
	T: {VRAI,FAUX,OU,ET,NON,(,)}
	N: {Exp,Teme,Rste,Reste2,Facteur,Valeur}
	S: Exp
	P:  Exp -> TermeReste
		Terme -> FacteurReste2
		Reste -> OU TermeReste | epsilon
		Reste2 -> ET FacteurReste2 | epsilon
		Facteur -> NON Facteur | (Exp) | Valeur
		Valeur -> VRAI | FAUX
'''

ch = [] # la chaine des unites lexicales prise en entree
pc = 0 # pointeur sur les elements de ch
liste=[] # Cette liste contiendra l'expression postfixee de ch

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
	save = pc
	if(Terme()):
		if(Reste()):
			return(1)
	pc = save
	return(0)

def Terme():
	if(Facteur()):
		if(Reste2()):
			return(1)
	return(0)

def Reste():
	global liste

	if(pc==len(ch)): # S'il ne reste plus d'element a lire, il n'y a pas d'erreur donc return(1)
		return(1)
	cc=ch[pc]
	if(Reconnaitre("OU")):
		if(Terme()):
			liste.append(cc)
			if(Reste()):
				return(1)
		Erreur()
		return(0)
	return(1)

def Reste2():
	if(pc==len(ch)): # S'il ne reste plus d'element a lire, il n'y a pas d'erreur donc return(1)
		return(1)
	cc=ch[pc]
	if(Reconnaitre("ET")):
		if(Terme()):
			liste.append(cc)
			if(Reste2()):
				return(1)
		Erreur()
		return(0)
	return(1)

def Facteur():
	global liste

	if(pc==len(ch)): # Pour eviter un out of range avec par exemple la chaine : VRAI OU
		return(0)

	cc=ch[pc]
	if(Reconnaitre("NON")):
		if(Facteur()):
			liste.append(cc)
			return(1)
	elif(Valeur()):
		return(1)
	elif(Reconnaitre("(") and Exp() and Reconnaitre(")")):
		return(1)
	return(0)

def Valeur():
	global pc,liste
	if(pc < len(ch)):
		if(ch[pc][0]=="BOOL"):
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
	print("erreur, caractere : "+ ch[pc-1][1])
	return(0)

if __name__=='__main__':
	param=[('BOOL','FAUX'),('OP','OU'),('BOOL','VRAI'),('OP','ET'),('OP','NON'),('BOOL','FAUX')]
	print(param)
	print("Resultat : ")
	print(parser(param))
