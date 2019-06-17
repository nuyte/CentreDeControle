import os
import sys
import iss_utils as issu
import numpy as np

def plot_evolution_path(key,cname,sn_arr,slice_index,figure_dir,\
                      selected_sn_val=[],wav_sample=[],\
                      Lya_position=None,sn_threshold= None) :


    if not os.path.isdir(figure_dir) :
        os.makedirs(figure_dir)
    
    fig,ax = plt.subplots()
    ax.set_title('Evolution of path for '+str(key[0])+','+str(key[1])+' in '+cname)

    ax.set_xlabel('Slice index in '+cname+' cube')
    ax.set_ylabel('SN')
    ax.set_yscale('log')

    ax.plot(slice_index,sn_arr,color='b',linewidth=0.7,label='sn')

    try : 
        ax.plot(wav_sample,selected_sn_val,c='r',marker='.',markersize=4,ls='',\
                label='SN values selected for masks')
    except ValueError : # cause by Bps set to np.nan
        pass

    if not Lya_position is None : 
        ax.axvline(x=Lya_position,ls='--',c='c',alpha=0.6,linewidth=2,\
                   label='Expected coord')

    if not sn_threshold is None :
        ax.axhline(y=sn_threshold[0],ls=':',linewidth=0.5,color='k',\
                   label='Covering fraction = 1')
        ax.axhline(y=sn_threshold[1],ls='--',linewidth=0.5,color='k',\
                   label='Covering fraction = 0')
    ax.legend()
    ax.tick_params(direction='in')
    fig.savefig(figure_dir+key[0]+'_'+key[1]+'_path_evolution_for_'+cname+'.pdf')
    plt.close(fig)

    return None
