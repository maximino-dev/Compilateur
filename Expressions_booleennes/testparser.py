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
		param=[('BOOL','FAUX'),('OP','ET'),('OP','NON'),('BOOL','VRAI')] # liste des parametres a tester

		result=[('BOOL', 'FAUX'), ('BOOL', 'VRAI'), ('OP', 'NON'), ('OP', 'ET')] # liste des resultats pour chaque parametre

		self.assertEqual(parser.parser(param),result)

if __name__=='__main__':
	unittest.main() # execution de la fonction test_parser