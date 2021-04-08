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
		param=["5- (9+2 *3)","56"] # liste des paramaetres a tester

		result=[[('NOMBRE', '5'),('OP', '-'),('PAR_OUV', '('),
				('NOMBRE', '9'),('OP', '+'), ('NOMBRE', '2'),
				('OP', '*'), ('NOMBRE', '3'), ('PAR_FER', ')')],[("NOMBRE",'56')]] # liste des resultats pour chaque parametre

		for i in range(2):
			self.assertEqual(scanner.scanner(param[i]),result[i])

if __name__=='__main__':
	unittest.main() # execution de la fonction test_scanner avec tous ses tests