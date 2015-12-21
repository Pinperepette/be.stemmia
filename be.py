# -*- coding: utf-8 -*-

from random import randrange
import time

def singola_bestemmia():

	
	bestemmia = ['dio porco ', 'cristo la madonna ', 'madunassa ',
'gesù inchiodato sulla croce ', 'madonna puttanaccia ','dio culo infiammato ',
'dio can ', 'Ave Maria piena di Merda ', 'Dio, Madonna e tutti gli angeli in colonna ','Gesù scalzo in una valle di chiodi ', 'Gesù cieco in una valle di spigoli ',
'Porco Dio e Padre Pio ', 'Bastardo il clero ', 'Madonna cagna ', 'Dio cantante, Madonna musicante, Giuseppe batterista e Cristo in autopista ',
'Maria putrefatta ', 'Dio bastardo ', 'Madonna inculata da cristo, quel bastardo']


	random_bestemmia = randrange(0,len(bestemmia))
	print bestemmia[random_bestemmia]

def stemmia(numero=1):
	cristoni = range(0,numero)
	for count in cristoni:
		singola_bestemmia()
		time.sleep(1)
