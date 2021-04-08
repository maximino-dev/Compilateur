########################
#
# scanner.py
# ----------
#
# Analyseur lexical d'expression arithmetique
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

'''
On utilise le lexique suivant:
(MAXINT=9223372036854775807)
NOMBRE --> [0-MAXINT]
OP --> + | - | * | /
PAR_OUV  --> (
PAR_FER  --> )
'''

def scanner(ch):
	'''
	Convertit une chaine de caracters en liste d'unites lexicales, 
	retourne 0 et le caractere fautif si celui-ci n'est pas reconnu.

	'''
	liste=[] # contiendra les unites lexicales
	nb="" # pour etendre l'ecriture aux nombres entiers quelconques
	i=0
	while i < len(ch):
		if ch[i].isdigit():
			nb=""
			while(i<len(ch) and ch[i].isdigit()):
				nb+=ch[i]
				i+=1
			i-=1
			liste+=[("NOMBRE",nb)]
		elif(ch[i] in ["+","-","*","/"]):
			liste+=[("OP",ch[i])]
		elif(ch[i]=="("):
			liste+=[("PAR_OUV",ch[i])]
		elif(ch[i]==")"):
			liste+=[("PAR_FER",ch[i])]
		elif(ch[i] != " "):
			print("Erreur, caractere inconnu : "+ch[i])
			return(0)
		i+=1
	return(liste)


if __name__=='__main__':
	import sys
	if(len(sys.argv)!=2):
		print("Utilisation: python3 'expression arithmetique'")
		exit()

	ch = sys.argv[1]
	print(scanner(ch))