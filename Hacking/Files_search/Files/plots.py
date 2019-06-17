import matplotlib.pyplot as plt
import matplotlib 
import cPickle as pck
from matplotlib import gridspec
import matplotlib.colors as colors
import numpy as np
import mpdaf
import pdb
import sys
import os


sys.path.append(os.environ['MAINDIR'])
import functions as f
import annex_functions as af
import functions as f



def bp_vs_flux(flux,bp) :

    # plots the flux of each sources versus the value of the brightest pixel
    # of the source


    fig,ax = plt.subplots()
    ax.set_title('brightest pixel versus flux')
    ax.set_xlabel('Flux')
    ax.set_ylabel('Brightest pixel')
    ax.set_xscale('log')
    ax.set_yscale('log')
    
    xflux = []
    ybp   = []
    for key in flux :
        xflux += [flux[key][0]]
        ybp   += [bp[key]]

    ax.plot(xflux,ybp,c='r',marker='.',ls='')
    fig.savefig('bp_vs_flux.pdf')
    plt.close(fig)



def plot_rms_levels(conf,rlevel,median,cname,output_dir,\
                    oplot_wav_sample=False,wav_sample=[]) :

    # function that plots the evolution of the rms level with wavelength in the
    # the datacube.
    # The rms level should reflect the presence of sky lines in the cubes
    # as the sky substraction introduces a lot of errror in the data cube
    # the pdfs are produced in output_dir

    # rlevel, dict with key set to slice index
    # median, spatial value of the median rms image used to
    # determine the rms level of each slice

    # if oplot wav_sample is set to true, the wav sample keyword is also plotted
    # over the rms plot

    # rebuilding entire wav array of the original cube
    
    cube           = mpdaf.obj.Cube(conf.path2Cubes(cname))
    cube_wav_range = cube.get_range()
    cube_wav_range = [cube_wav_range[0],cube_wav_range[3]]
    cube_wav       = cube_wav_range[0] + np.arange(cube.shape[0]) * cube.get_step()[0]
    
    wav,rl = [],[]
    for key in rlevel :

        wav += [key]
        rl  += [rlevel[key]]

    wav, rl = np.asarray(wav), np.asarray(rl)
    wav     = cube_wav[np.array(wav)]
         
    fig,ax = plt.subplots(figsize=(10,5))

    
    #ax.set_title('Evolution of RMS level with wavelength')
    ax.set_xlabel('wavelength [A]',fontsize=20)
    ax.set_ylabel('Noise level',fontsize=20)
    #ax.set_yscale('log')

    ax.plot(wav,rl,ls='-',marker='',color='r',linewidth=0.5,alpha=1)
    #ax.axhline(y=median,ls='--',color='k',linewidth=0.7,\
    #           label='Median of median image')

    if oplot_wav_sample :
        for i,wav_val in enumerate(np.nditer(wav_sample)) :
            if i == 0 : 
                ax.axvline(x=wav_val,color='c',ls='--',linewidth=1,alpha=0.5,\
                           label='wavelength sample')
            else :
                ax.axvline(x=wav_val,color='c',ls='--',linewidth=1,alpha=0.5)
                
   
    
    ax.legend()
    ax.tick_params(direction='in',which='both',labelsize=15)
    fig.savefig(output_dir+cname+'_rms_level_with_wav.pdf')
    plt.close(fig)
    
    
    return None
