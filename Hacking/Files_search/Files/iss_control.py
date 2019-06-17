import os
import sys
import iss_utils as issu
import numpy as np



# defining initial state of ISS and showing control commands

params = {'weight' : 450 , 'velocity' : 27500, 'loads' : 21 , 'spec' : 10.3,\
          'alt' : 408    , 'n_people' : 4.   , 'lffp' : None }

init = issu.intializise_state(params=params,t0=0,use_true_val=True,spec=None)

for param in init :
    param.set_confidence(use_defaults = True)

    
sim = issu.make_simulations(params = params, spec=None)

isOk = True
while isOk : 

    sim.display_live_parameters(monitor='all',cond=2)
    sim.track_live_position(monitor=1)
    sim.make_prediction(monitor=2)
    sim.display_controls(monitor='control panel')
    
    isOk = sim.get_status(time='current')

else : 

    sim.show_emergency_display(priority=1)

    issu.launch_emergency_process()
