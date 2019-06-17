import os
import sys
import iss_utils as issu
import numpy as np

# script to transfer iss to automated control 


level_security = 1
spec           = False
dev            = 14.5
emergency_num  = '+331 33 43 56 79'

usual_parms    = 


res = input('Are you sure you want to continue ? : (y/n)')

if res.lower() == 'y' :
    print('Shiffting to cruise control ...')
if res.lower() == 'n' :
    print('Exiting script')
    sys.exit()
    
issu.shift_to_automated(level_sec=level_security,spec=spec,
                        dev=dev,emergency_num,other_params=usual_params)

list_war = issu.get_list_warning

for val in list_war :
    if val.state == 'good' : continue
    else :
        issu.make_alarm()

        
