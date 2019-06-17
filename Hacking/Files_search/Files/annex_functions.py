
import astropy
import cPickle as pck
import random as rand
import matplotlib.pyplot as plt
import pdb
import numpy as np
import shutil
import types
import mpdaf
import pdb
import sys
import os
import re

'''
# ---------------------------------------------------------------------------------


 This file contains usual functions that are often in use 


# ----------------------------------------------------------------------------------
'''



def write_ds9_catalog(radec,colors,fname='default.reg',radius=2) :

   
    
    if not isinstance(colors,dict) :
        color_temp = str(colors)  # copy initial value
        colors     = {}
        for key in radec :
            colors[key] = color_temp

    if not isinstance(radius,dict) :
        radius_dict, radius_val = {}, radius
        for key in radec :
            radius_dict[key] = radius_val
    else :
        radius_dict = dict(radius)
        
    with open(fname, 'w') as myfile :
        for key  in radec : 
            
            color = colors[key]
            radius = radius_dict[key]
            line  = 'Circle('+str(radec[key][0])+'d,'+str(radec[key][1])+'d,'+\
                    str(radius)+'") # text={'+str(key)+'},color='+color
            myfile.write(line +'\n')

    return None
                                                    
def alignDictionnaries(collection, ref={}) :

    for i in range(len(collection)) :
        
        copy_temp = dict(collection[i])
        
        for key in copy_temp :
            if key not in ref.keys() :
                
                del collection[i][key]

    return collection


def display_counter(count,loop_number,message) :


    if not loop_number is None : 
        sys.stdout.write('\r'+str(count)+'/'+str(loop_number)+' '+message)
    else :
        sys.stdout.write('\r'+str(count)+' '+message)
        
    sys.stdout.flush()

    if count == loop_number :
        print('')

    return None

