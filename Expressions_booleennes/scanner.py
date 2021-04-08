########################
#
# scanner.py
# ----------
#
# Analyseur lexical d'expression booleene
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

'''
On utilise le lexique suivant:
BOOL --> VRAI | FAUX
OP --> OU | ET | NON
PAR_OUV  --> (
PAR_FER  --> )
'''

def scanner(ch):
	'''
	Convertit une chaine de caracters en liste d'unites lexicales, 
	retourne 0 et le caractere fautif si celui-ci n'est pas reconnu.

	'''
	liste=[]
	nb=""
	i=0
	if(len(ch) < 4):
		print("Saisir au moins une valeur booleenne")
		return(0)
	while i < len(ch):
		if(ch[i]=="("):
			liste+=[("PAR_OUV",ch[i])]
		elif(ch[i]==")"):
			liste+=[("PAR_FER",ch[i])]
		elif(i < len(ch) - 1):
			if(ch[i:i+2]=="ET"):
				liste+=[("OP","ET")]
				i+=1
			elif(ch[i:i+2]=="OU"):
				liste+=[("OP","OU")]
				i+=1
			elif(i < len(ch) - 2):
				if(ch[i:i+3]=="NON"):
					liste+=[("OP","NON")]
					i+=2
				elif(i < len(ch) - 3):
					if(ch[i:i+4]=="VRAI"):
						liste+=[("BOOL","VRAI")]
						i+=3
					elif(ch[i:i+4]=="FAUX"):
						liste+=[("BOOL","FAUX")]
						i+=3
					elif(ch[i] != " "):
						print("Erreur, caractere",i,"inconnu")
						return(0)
		elif(ch[i] != " "):
			print("Erreur, caractere ",i," inconnu")
			return(0)
		i+=1
	return(liste)

if __name__=='__main__':
	import sys
	if(len(sys.argv)!=2):
		print("Utilisation: python3 'expression booleene'")
		exit()

	ch = sys.argv[1]
	print(scanner(ch))
