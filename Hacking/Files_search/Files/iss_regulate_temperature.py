import os
import sys
import iss_utils as issu
import numpy as np



rooms = ['Columbus', 'Cupola', 'Destiny', 'Harmony', 'Kibo', 'Leonardo',\
         'Nauka', 'Pirs', 'Poisk', 'Quest', 'Rassvet', 'Tranquility',\
         'Unity', 'Zarya','Zveda']


i = 0 
for r in rooms :
    isus.display_temperature(monitor = i,units='celsius')
    i += 1



While True :
    for r in rooms :

        res = r.adjust_temperature(target=20,units='celsius')


        if res.stat == ok :
            continue
        else :
            res.investigate()
