# -*- coding: utf-8 -*-

from random import randrange
import time

def singola_bestemmia():

	
	bestemmia = ['dio porco ', 'cristo la madonna ', 'madunassa ',
'gesù inchiodato sulla croce ', 'madonna puttanaccia ','dio culo infiammato ',
'dio can ', 'Ave Maria piena di Merda ', 'Dio, Madonna e tutti gli angeli in colonna ']


	random_bestemmia = randrange(0,len(bestemmia))
	print bestemmia[random_bestemmia]

def stemmia(numero=2):
	cristoni = range(1,numero)
	for count in cristoni:
		singola_bestemmia()
		time.sleep(1)
