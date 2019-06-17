import os
import sys
import iss_utils as issu
import numpy as np

Astronauts_names = ['Arnaud B', 'John S.', 'Vladimir K.' , 'Ellena B.']
Astronaut_names  = issu.create_astrinaut_list()

i = 0 
for astronaut in Astronauts_names :

    astronaut.display_vital(monitor_num = i, language='Russian')
    
    i += 1
