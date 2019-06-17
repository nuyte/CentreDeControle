import os
import sys
import Cpickle as pck
import iss_utils as issu
import numpy as np


state = issu.initialize_power_system(params='Default',simu=True)
state = initialize_water_distribution_system(params='Default',simu=True)
state = initialize_air_filtering_system(params='Default',simu=True)
state = initialize_water_filtering_system(params='Default',simu=True)
state = initialize_sport_room(params='Default',simu=True)
state = initialize_lights(params='Default',simu=True)
state = initialize_rooms(which='all',params='Default',simu=True)

res = issu.make_simulation(state,resolutio = 0.1, activate_pal=False, t=2500)

pck.dumop(res,open('results.pck','wb'))


res.make_results(output_channel=2,show=False,save=True)
