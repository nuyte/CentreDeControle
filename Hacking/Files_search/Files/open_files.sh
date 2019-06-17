#!/bin/bash

# call the function like this :
# open_plots 00, open_plots 35 etc...
# all the function are called in the same way

function open_plots(){
    evince LF_${1}/Lf.pdf &
    evince LF_${1}/iterations_lf.pdf &
    }

function open_fits(){
    evince LF_${1}/Lf_fit_1.pdf &
    evince LF_${1}/Lf_fit_2.pdf &
}

function d_info(){
    more LF_${1}/info.txt
    }

function d_sinfo(){
    more LF_${1}/source_info.txt
    }

function open_info(){
    em LF_${1}/info.txt &
    }

function open_sinfo(){
    em LF_${1}/source_info.txt &
    }
