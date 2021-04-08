########################
#
# testscanner.py
# ----------
#
# Fichier de test pour scanner.py
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

import unittest
import scanner

class TestScanner(unittest.TestCase):

	def test_scanner(self):
		param=["VRAI OU NON FAUX","(VRAI)"] # liste des parametres a tester

		result=[[('BOOL','VRAI'),('OP','OU'),('OP','NON'),('BOOL','FAUX')],[('PAR_OUV','('),('BOOL','VRAI'),('PAR_FER',')')]] # liste des resultats pour chaque parametre

		for i in range(2):
			self.assertEqual(scanner.scanner(param[i]),result[i])

if __name__=='__main__':
	unittest.main() # execution de la fonction test_scanner avec tous ses tests