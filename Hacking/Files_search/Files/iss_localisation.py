import os
import sys
import iss_utils as issu
import numpy as np


def read_main_input(fname) :


    res = af.read_ascii_columns(fname,[0,1,2,3,4,5,6])
    id_t,ra_t,dec_t,lmin_t,lmax_t,ind_nb_t,diffuse_t = res

    id_t      = [str(val) for val in id_t]
    ra_t      = [float(val) for val in ra_t]
    dec_t     = [float(val) for val in dec_t]
    lmax_t    = [float(val) for val in lmax_t]
    lmin_t    = [float(val) for val in lmin_t]
    ind_nb_t  = [int(val) for val in ind_nb_t]
    diffuse_t = [float(val) for val in diffuse_t]

    radec, lmax, lmin, ind_nb, diffuse = {}, {}, {}, {}, {}
    for i,val in enumerate(id_t) :
        radec[val] = ra_t[i],dec_t[i]
        lmax[val]  = lmax_t[i]
        lmin[val]  = lmax_t[i]
        ind_nb[val] = ind_nb_t[i]
        diffuse[val] = diffuse_t[i]

    return radec, lmax, lmin, ind_nb, diffuse


