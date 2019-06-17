import os
import sys
import pdb
import time
import numpy as np
import shutil as sh
import unicodedata
import argparse
import signal
import subprocess as sp
import random as rand

from termcolor import colored




def strip_accents(s):

    # to remove accent from a string
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')

def format_string(s) :
    s = strip_accents(s)
    return "".join(s.lower().strip().split())


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def isYon(string) :

    # function that checks if the input string is 'oui' or 'non'
    s = ''.join(string.lower().strip().split())
    if s  == 'oui' or s == 'non' or \
       s  == 'o'   or s == 'n':
        return True
    else :
        return False

    
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def slowprint(s,color=None,attrs=None,time_scale=0.02):

    # time scale is in sec :
    for c in s + '\n':
        if not color is None: 
            sys.stdout.write(colored(c,color,attrs=attrs))
        else  :
            # This case allows to use color for single word in a sentence..
            sys.stdout.write(c)
            
        sys.stdout.flush() # defeat buffering
        time.sleep(rand.random() * time_scale)

    return None


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------



def displayLoadingBar(length=40,duration=5,color=None) :

    # prints a fake loading bar on the terminal
    # length defines the length of the loading var in number of characters
    # duration defines how much time it will take for the bar to load (in sec)
    
    sys.stdout.write(colored("|%s|" % ("-" * length),color))
    sys.stdout.flush()
    sys.stdout.write(colored("\b" * (length+1),color)) # return to start of line,
                                                       # after '['
    
    dt = float(duration/length)
    
    for i in np.arange(length):
        time.sleep(dt)
        sys.stdout.write(colored("#",color))
        sys.stdout.flush()
        
    sys.stdout.write("\n\n")

    return None


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------



def atmospheric_entry(good_angles) :

    # asking coordinate for the atmospheric re-entry :

    
    sp.call(['clear'])
    message = "Ce programme a pour but d'établir les trajectoires du Soyouz "+\
              "pour rentrer sur Terre en sécurité.\n\n"
           
    slowprint(message,'red')
    
    questions = ["Angle d'entrée de Soyouz dans l'atmosphere (a1):",\
                 'Angle de descente du Soyouz vers la Terre (a2):']
    
    ok_angles = False


    while not ok_angles :

        try :
            angle1 = input(questions[0]).lower()
            angle1 = float(angle1)  
        except ValueError  :
            slowprint('Veuillez entrer un nombre','red')
            time.sleep(1)

            sp.call(['clear'])
            print(colored(message,'red'))
            
            continue

        try : 
            angle2 = input(questions[1]).lower()
            angle2 = float(angle2)
        except ValueError :
            slowprint('Veuillez entrer un nombre','red')
            time.sleep(1)

            sp.call(['clear'])
            print(colored(message,'red'))

            continue

        slowprint('\n Simulation en cours:')
        displayLoadingBar(duration=3)
        
        if angle1 == good_angles[0] and angle2 == good_angles[1] :
            ok_angles = True
            success_message = 'Trajectoire correcte, entrée atmospherique OK\n' 
            slowprint(success_message,'green')
            slowprint('Envoi des informations de vol vers le Soyouz:')
            displayLoadingBar(duration=7)
            slowprint('Transfert terminé, paré au décollage.')

            # to quit the script at the end
            # Merci au beau Babak pour cette excellente idée !!
            res = input()
            while format_string(res) != format_string('quit script hacking') :
                res = input()
                

        else :
            ok_angles = False
            error_message = "Paramètres incorrects, désintégration dans l'atmosphère"
            slowprint(error_message, 'red')
            time.sleep(1)        

            sp.call(['clear'])
            print(colored(message,'red'))






# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------



parser = argparse.ArgumentParser(description='Some options for the program.')

parser.add_argument('--test','-t',action='store_true',default=False, \
                    help='Use simpler inputs for the login and mdp')

args = parser.parse_args()



# to prevent ctrl + c  ctrl + z
if not args.test : 
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)



# locked by password

mdp     = 4594 # NGC code of sombrero galaxy, cf galaxy poster in the room
message = "Ordinateur bloqué à la suite d'une attaque. \n"+\
          "Veuillez entrer le mot de passe (4  chiffres) pour démarer la "+\
          "réinitialisation: "
res     = "0"



if args.test:
    mdp = 0

while True:
    sp.call('clear')
    slowprint(message, 'white',attrs=['bold'])
    res = input("Mot de passe :")

    if int(res) != mdp :
        slowprint('Mot de passe incorect','red')
        time.sleep(1)
    else :
        slowprint('\nReinitialisation en cours:\n','green')
        duration = 10
        if args.test : duration = 1
        displayLoadingBar(duration=duration)
        time.sleep(1)

        break

if args.test:
    good_angles = [0.,0.]
else : 
    good_angles = [40.,3.]

atmospheric_entry(good_angles)
    
            
