# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import itertools
import random
import numpy as np

from charactersClass import Character
from armyClass import Army

characters_list = []

with open('characters.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in itertools.islice(spamreader,1,spamreader.__sizeof__()):
        characters_list.append(Character(row[0],row[1],row[2],row[3],row[4]))

rouge = Army(characters_list[0], random.uniform(20, 100))
bleu = Army(characters_list[1], random.uniform(20, 100))
vert = Army(characters_list[2], random.uniform(20, 100))
jaune = Army(characters_list[3], random.uniform(20, 100))
orange = Army(characters_list[4], random.uniform(20, 100))

def total_morale():
    res = rouge.get_total_morale() + bleu.get_total_morale() + vert.get_total_morale() + jaune.get_total_morale() + orange.get_total_morale()
    return res

print(total_morale())

morale_armee = np.array([random.uniform(20, 100),random.uniform(20, 100),random.uniform(20, 100),random.uniform(20, 100),random.uniform(20, 100)])
boostMorale_char = np.array([float(characters_list[0].get_boostMorale()),float(characters_list[1].get_boostMorale()),float(characters_list[2].get_boostMorale()),float(characters_list[3].get_boostMorale()),float(characters_list[4].get_boostMorale())])
total = np.sum(morale_armee*boostMorale_char)

print(total)

input_a = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
sortie_y = np.array([0, 0, 0, 1])

column, row = 10, 10
valeur_erreur = [[0]*row for _ in range(column)]


for w1 in range(-5, 5):
    for w2 in range(-5, 5):
        for a in range(0, 3):
            sortie_T = input_a[a, 0] * w1 + input_a[a, 1] * w2
            if sortie_T <= 0:
                y = 0
            if sortie_T > 1:
                y = 1
            valeur_erreur[w1 ,w2] = 1/2 * ((y * sortie_T)**2)


print (valeur_erreur)

# si T <=0 -> 0
# si T >0 -> 1
