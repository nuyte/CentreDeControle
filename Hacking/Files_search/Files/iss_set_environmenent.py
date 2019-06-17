import os
import sys
import iss_utils as issu
import numpy as np


issu.set_temperature(params='Default')

res = issu.check_pressure(params='Default')
issu.adjust_pressure(res, params='Default')


hum = issu.check_humidity(params='Default')
issu.adjust_humidity(hum, params='Default')

issu.initialize_power_system(params='Default')
issu.initialize_water_distribution_system(params='Default')
issu.initialize_air_filtering_system(params='Default')
issu.initialize_water_filtering_system(params='Default')
issu.initialize_sport_room(params='Default')
issu.initialize_lights(params='Default')
issu.initialize_rooms(which='all',params='Default')

