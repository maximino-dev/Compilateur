BOGADO GARCIA Maximino
L3 Informatique

TP 2 - I53 | Compilation et théorie des langages

2 dossiers présents, Expressions_arithmetiques/ et Expressions_booleennes/
Dans chaque dossier se trouvent les fichiers scanner.py, parser.py, codegen.py et compilo.py, data.txt,
ainsi que les fichiers de test, testscanner.py et testparser.py.

Les grammaires sont decrites dans les fichiers parser.py.

scanner.py:
	Une fonction principale scanner(), qui prend en paramètre une chaine de caractères,
	et qui renvoie une liste de tuples représentant cette chaine sous forme d'unités lexicales,
	Ex: scanner("3*4+2") renvoie [("NOMBRE",3),("OP",*),("NOMBRE",4),("OP",+),("NOMBRE",2)]

parser.py:
	Une fonction principale parser(), qui prend en parametre une liste d'unités lexicales (donnée par scanner())
	et renvoie une liste contenant ces unités lexicales mais en notation postifxée,
	La fonction renvoie une erreur si la syntaxe en entrée est incorrecte.
	Ex: parser([("NOMBRE",3),("OP",*),("NOMBRE",4)]) renvoie [("NOMBRE",3), ("NOMBRE",4), ("OP",*)]
	
codegen.py:
	Une fonction principale prod(), qui prend en parametre une expression d'unités lexicales 
	en notation Postfixée (donnée par parser()),
	et écrit dans un fichier nommé a.out un programme python qui affichera la valeur finale de l'expression en entrée.
	La fonction utilise les librairies os et stat pour rendre le fichier a.out exécutable.

compilo.py:
	Programme python qui prend en argument un nom de fichier à lire, fait appel aux 3 modules précédents, puis qui affiche
	le résultat de la donnée du fichier d'entrée en exécutant "a.out".

data.txt:
	Fichier contenant une expression (arithmetique ou boléeenne), qui sera lu par compilo.py

Les fichiers testscanner.py et testparser.py utilisent la librairie unittest,
mais les fonctions peuvent également être testées en les exécutant normalement:
Ex: 
Pour tester scanner.py, on ecrit sur le terminal:
	- python3 scanner.py
	OU
	- python3 testscanner.py