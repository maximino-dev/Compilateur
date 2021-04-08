########################
#
# compilo.py
# ----------
#
# Regroupement et test des modules parser.py, scanner.py et codegen.py
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################
import scanner
import parser
import codegen
import sys,os

if __name__=="__main__":
	'''
	On prend en argument une chaine contenant le chemin du fichier a lire,
	puis le resultat de l'expression arithmetique dans ce fichier est affiché.
	'''
	if(len(sys.argv)!=2):
		print("Utilisation: python3 'nom du fichier a lire'")
		exit()

	fichier = open(sys.argv[1], "r")
	ch = fichier.read().rstrip()
	print("Chaine : ", ch)
	ul = scanner.scanner(ch)
	if(ul):
		postfix = parser.parser(ul)
		for el in postfix:
			print(el[1],end=' ')
		codegen.prod(postfix)
		os.system("echo 'Resultat : '")
		os.system("python3 a.out")
	fichier.close()
