########################
#
# testparser.py
# ----------
#
# Fichier de test pour parser.py
#
# BOGADO GARCIA Maximino
# L3 Informatique
#
########################

import unittest
import parser

class TestParser(unittest.TestCase):

	def test_parser(self):
		param=[('NOMBRE', '32'), ('OP', '/'), ('NOMBRE', '2'),('OP', '+'),('NOMBRE', '21')] # liste des parametres a tester

		result=[('NOMBRE', '32'), ('NOMBRE', '2'), ('OP', '/'), ('NOMBRE', '21'), ('OP', '+')] # liste des resultats pour chaque parametre

		self.assertEqual(parser.parser(param),result)

if __name__=='__main__':
	unittest.main() # execution de la fonction test_parser