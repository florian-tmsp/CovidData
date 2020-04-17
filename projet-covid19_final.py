# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:51:37 2020

@author: Flo
"""

import pandas as pd
# Documentation : http://eric.univ-lyon2.fr/~ricco/tanagra/fichiers/fr_Tanagra_Data_Manipulation_Pandas.pdf
import datetime
import numpy as np
import matplotlib.pyplot as plt

def rechercher(mot, caractere):
	"""Cette fonction prend en entrée un mot et un caractère et renvoie en sortie une liste.
		Cette liste contient la position du caractère dans la chaine de caractère.
	"""
	Positions = []
	for k in range(len(mot)) :
		if mot[k] == caractere :
			Positions.append(k)
	return Positions


"""Reccuperation de l'information utile : ici l'information concernant la France."""
url_death = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_confirmed = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

dataset_death = pd.read_csv(url_death, error_bad_lines=False )
dataset_confirmed = pd.read_csv(url_confirmed, error_bad_lines=False)

France_Zone_death = dataset_death.loc[dataset_death['Country/Region']=="France",:]     
France_Zone_confirmed = dataset_confirmed.loc[dataset_confirmed['Country/Region']=="France",:]  

FranceAllzone_death = France_Zone_death.iloc[:, 4:]
FranceAllzone_confirmed = France_Zone_confirmed.iloc[:, 4:]

FranceAll_death = FranceAllzone_death.sum(axis = 0)
FranceAll_confirmed = FranceAllzone_confirmed.sum(axis = 0)




""" Création d'un liste contenant les dates sans le /20 pour dire 2020 par soucis de visibilité sur le graphe """
Dates = np.array(FranceAll_death.index)
for k in range (len(Dates)):
	positions = rechercher(Dates[k],"/")
	Dates[k] = Dates[k][:positions[1]]


"""Conversion des données en array"""
Case_death = np.array(FranceAll_death) # en France
Case_confirmed = np.array(FranceAll_confirmed) #en France

"""Figure nombre de morts"""
plt.xlabel('Dates')
plt.ylabel('Morts')
plt.title('Nombre de morts en france en 2020')
plt.plot(Dates, Case_death, 'ro')
plt.show()


"""Figure nombre de cas"""
plt.xlabel('Dates')
plt.ylabel('Cas confirmés')
plt.title('Nombre de cas confirmés en france en 2020')
plt.plot(Dates, Case_confirmed, 'ro')
plt.show()

