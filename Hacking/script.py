import os
import sys
import pdb
import time
import random as rand
import datetime
import shutil as sh
import numpy as np
import subprocess as sp
import unicodedata
import argparse
import signal

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

 
def askLogin(username) :


    error_message = 'Login incorrecte, nouvelle tentative :'
    
    ind_choosen   = None
    login_t = input('Login (adresse mail) : ')
    if any([login_t == val for val in username]) :
        goodLogin = True
        ind_choosen = np.where(username == login_t)[0][0]

    else :
        goodLogin = False
        slowprint(error_message,'red')
        time.sleep(0.75)

    return goodLogin,ind_choosen


def askPassword(goodpassword) :


    error_message = 'Mot de passe incorrecte, nouvelle tentative :'
    found         = False
    mdp_t = input('mot de passe : ')
    if mdp_t == goodpassword :
        found = True
    else :
        slowprint(error_message,'red')
        time.sleep(0.75)

    return found
        
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------



def logAsAdmin(goodUsername, goodPassword,indices):

    # !! ne rafraichir que l'heure est pas le jour, puisque de toute facon
    # ca se passe dans le future. !!



    line1 = ' # --------------------------------------------------------------\n'+\
            '        ___                                    ___           \n'+\
            '       // \\\      ! ERREUR DU SYSTEME  !      // \\\       \n'+\
            '      // | \\\                                // | \\\      \n'+\
            '     //  |  \\\    ! ERREUR DU SYSTEME  !    //  |  \\\     \n'+\
            '    //   |   \\\                            //   |   \\\    \n'+\
            '   //    .    \\\  ! ERREUR DU SYSTEME  !  //    .    \\\   \n'+\
            '  //___________\\\                        //___________\\\   \n'+\
            '\n'+\
            '# ---------------------------------------------------------------\n\n'

    line2 = 'Vous avez été piraté '+\
                     'entre le {} et {}.\n'
    line3 = 'Souhaitez-vous tenter une réinitialisation du système ? (Oui/Non)'

    # definning interval of time for the hacking
    # format is year,month,day etc...
    now          = datetime.datetime(2023,4,2,9)      # fictionnal date
    dateInterval = [now - datetime.timedelta(hours=2),\
                    now + datetime.timedelta(hours=2)]

    while True : 
        
        res = 'default'
        while (res.lower() != 'oui' and res.lower() != 'o') :

            sp.call(['clear'])
            time.sleep(0.3)
    
            # use input() for python 3 or raw_input() for python 2.7

            print(colored(line1,'red'))
            slowprint(line2.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold'])
            slowprint(line3,'red')
            res = input()
            res = format_string(res)
            
            
        # -- Asking for logins and Root password
        line = '\nPour trouver la '+\
               'source du problème et réinitialiser le système, '+\
               'entrez le login de  John K. (niveau 3) : \n'
        
        #sp.call(['clear'])
        slowprint(line,'white',attrs=['bold']) 
           
        
    
        goodLogin      = False
        fixed_usernmae = False
        failed_attempt = 0
        
        while not goodLogin :

            if failed_attempt >= 1 :
                sp.call('clear')
                print(colored(line1,'red'))
                print(colored(line2.format(
                    dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                    dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',\
                          attrs=['bold']))
                print(colored(line3,'red'))
                print(colored(line,'white',attrs=['bold']))

            goodLogin,ind = askLogin(goodUsername)

            if not goodLogin :
                failed_attempt += 1


        # When good login
        sp.call('clear')
        print(colored(line1,'red'))
        print(colored(line2.format(
            dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
            dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',\
                      attrs=['bold']))
        print(colored(line3,'red'))
        print(colored(line,'white',attrs=['bold']))

        print(colored('Login (adresse mail) : ')+colored(goodUsername[ind],'green'))


        # asking for MDP
        failed_attempt = 0
        cond           = False
        while not cond :

            if failed_attempt >= 1 :
                sp.call('clear')
                print(colored(line1,'red'))
                print(colored(line2.format(
                    dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                    dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',\
                              attrs=['bold']))
                print(colored(line3,'red'))
                print(colored(line,'white',attrs=['bold']))
                
                print(colored('Login (adresse mail) : ')+\
                      colored(goodUsername[ind],'green'))
                if failed_attempt >= 3 :
                    slowprint(indices[ind],'blue')

            cond = askPassword(goodPassword[ind])

            if not cond :
                failed_attempt += 1


        message  = '\nAccès au compte en cours: \n'
        slowprint(message)
        displayLoadingBar(duration=2)

        break
        
    return None


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def lookForCulprit(culprit, teamNames, teamMembers, chiefs) :

    # second part of the script, where the player tries to find the person responsible
    # for the hacking by looking at the schedule of personns on site
    # and to the recent activity of every team members

    #install_dir = os.environ['EG_DIR']

    
    # definning interval of time for the hacking
    # format is year,month,day etc...
    now          = datetime.datetime(2023,4,2,9)      # fictionnal date
    dateInterval = [now - datetime.timedelta(hours=2),\
                    now + datetime.timedelta(hours=2)]
    sp.call(['clear'])

    line_time_hack = 'Vous avez été piraté '+\
                     'entre le {} et {}.\n'
    print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))

    first_message = "\nCe programme va vous assister pour trouver l'origine "+\
                    "de la défaillance \n"+\
                    "et tenter d'effacer le fichier fautif.\n"+\
                    "Vous allez devoir répondre à plusieurs questions :\n\n"

    team_list_message = "Les 4 équipes à gérer le centre de contrôle sont :\n"+\
                        ' . {}: '.format(teamNames[0])+", ".join(teamMembers[1])+"\n"\
                        ' . {}: '.format(teamNames[1])+", ".join(teamMembers[2])+"\n"\
                        ' . {}: '.format(teamNames[2])+", ".join(teamMembers[3])+"\n"\
                        ' . {}: '.format(teamNames[3])+", ".join(teamMembers[4])+'\n'+\
                        "À chaque roulement un chef différent est en charge de "+\
                        "l'équipe"

    questions = ["\n 1 - Quel était le numéro de l'équipe en poste au moment "+\
                 "de l'attaque ?\n",
                 "\n 2 - Qui était en charge de l'équipe à ce moment ?\n",
                 "\n 3 - Parmi ces personnes, qui possède une accréditation de"+\
                 " niveau 2 (ou plus) nécessaire à la propagation du virus ? \n",
                 "\n 4 - Pensez-vous que {} soit le responsable ? (Oui/Non)\n"]
            
    res = 'Default'
    slowprint(first_message,'red')
    slowprint(team_list_message)


    res = 'default'
    culpritNotFound = True
    
    while culpritNotFound : 

        # ---- question 1 

        condition,failed_once          = False, False
        good_chief_name,good_team_name = False, False
        while not condition :

            if failed_once :
                sp.call(['clear'])
                print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))
                print(colored(first_message,'red'))
                print(team_list_message)
            
            slowprint(questions[0])
            try : 
                teamName_temp = int(input())
            except : 
                teamName_temp = -99
                
            good_team_name = teamName_temp  in teamNames
            
            if not good_team_name :
                slowprint("nom d'équipe incorrecte",'red')
                time.sleep(1)
                failed_once = True

            else : # correct team name, asking who was in charge
                slowprint(questions[1])
                chief_name = ''.join(input().lower().split())
                if chief_name.capitalize() not in chiefs :
                    slowprint("Prénom incorrecte", "red")
                    time.sleep(1)
                    failed_once = True
                else :
                    good_chief_name = True
                    chief_name_display = chief_name.capitalize()
            condition = good_chief_name and good_team_name


        # displaying on screen team members and the chef that was with them
        message_team_list = "\nConfirmez vous que le groupe en poste etait "+\
                            "composé des personnes suivantes ? (oui/non)\n"
        teamName_temp     = teamName_temp
        slowprint(message_team_list.format(teamName_temp))
        slowprint(". {}".format(chief_name_display),"blue",attrs=['bold']) # chief
        slowprint(". {}".format('-'*10),            "blue",attrs=['bold'])
        for val in teamMembers[teamName_temp] :   # rest of the team
            slowprint(". {}".format(val))
        print('')
            
        res         = ''
        failed_once = False
        
        while not isYon(res) :

            if failed_once :
                slowprint('Veuillez répondre par oui ou par non, '+\
                          'nouvelle tentative:','red')
                time.sleep(0.75)
                sp.call(['clear'])
                print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))
                print(colored(first_message,'red'))
                print(message_team_list.format(teamName_temp))
                print(colored(". {}".format(chief_name_display),\
                              "blue",attrs=['bold']))
                print(colored(". {}".format('-'*10),\
                              "blue",attrs=['bold']))
                for val in teamMembers[teamName_temp] :
                    print(". {}".format(val))
                print('')
                
            res = format_string(input())
            if not isYon(res) : failed_once = True
            else : failed_once = False
            
        if res == 'oui' or res == 'o': pass     # just continue the scriot as is
        if res == 'non' or res == 'n':           # looking for new team compostion
            sp.call(['clear'])
            print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))
            print(colored(first_message,'red'))
            print(team_list_message)

            continue

            
        # -- question 3 : qui a les autorisations nécéssaires ? 
        condition2, failed_once = False, False
        while not condition2 :

            if failed_once :
                sp.call(['clear'])
                print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))
                print(colored(first_message,'red'))
                print(message_team_list.format(teamName_temp))
                print(colored(". {}".format(chief_name_display),\
                              "blue",attrs=['bold']))
                print(colored(". {}".format('-'*10),\
                              "blue",attrs=['bold']))
                for val in teamMembers[teamName_temp] :
                    print(". {}".format(val))

            slowprint(questions[2])  # qui a les autorisations nécéssaires ? 
            name_temp         = "".join(input().lower().strip().split())
            name_temp_display = name_temp.capitalize()

            team_in_place = [chief_name_display]+ teamMembers[teamName_temp]
            condition2 = any([name_temp.capitalize() == val for val in \
                                        team_in_place])
            
            if not condition2 :
                failed_once = True
                slowprint('\nNom incorrecte','red')
                time.sleep(1)
            

        # display of log file
        message_activities = "\nVoici les dernieres activitées enregistrées de {} :\n"
        slowprint(message_activities.format(name_temp_display))

        # removing accent + capital first letter to get the correct filename
        sp.call(['head','-30',install_dir+'Log_files/'+\
                 strip_accents(name_temp).capitalize()+'.log'])
        print('')

        # -- question 3 
        res = 'Default'
        while not isYon(res) : 
            slowprint(questions[3].format(name_temp_display))
            res = input()
            
        if res == 'non' :
            sp.call(['clear'])
            print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))
            print(colored(first_message,'red'))
            print(team_list_message)

            continue

        temp = "\n\n Recherche de fichiers sur le compte de {} "+\
               "en cours, veuillez patienter... \n"
        slowprint(temp.format(name_temp_display))
    
        displayLoadingBar(length=40,duration=1)
        
        if name_temp.lower() == culprit.lower() :
            temp = '\nRéussite de la recherche : fichier malveillant detecté '+\
                   'sur le compte de {}'
            slowprint(temp.format(name_temp_display),'green')
            culpritNotFound = False
        else :
            temp = "\nÉchec de la recherche, rien d'inquiétant sur le compte de {}"

            slowprint(temp.format(name_temp_display),'red')
            time.sleep(1.5)
            sp.call(['clear'])
            print(colored(line_time_hack.format(
                dateInterval[0].strftime("%Y-%m-%d %H:%M"),\
                dateInterval[1].strftime("%Y-%m-%d %H:%M")),'white',attrs=['bold']))

            print(colored(first_message,'red'))
            print(team_list_message)

    return None



# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def read_list_of_files(index=None) :

    # if index is none, returns total number of line in the file
    # else returns only the i-th line
    #install_dir = os.environ['EG_DIR']
    
    fname=install_dir+'Files_search/list_of_possible_files.txt'
    with open(fname, 'r') as myFile :

        i = 0 
        for line in myFile :

            line = line.strip()
            line = line.split()

            if len(line) <= 1  : continue
            if line[0]  == '#' : continue


            if not index is None: 
                if index == i :
                    return_line = line
            i += 1

            
    if index is None :
        return i
    else :
        return return_line



# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------

            
    
def makeListFiles(badFileName='reallyBadFile.sh',badFileSize='734Mo',\
                  numberFiles=10) :

    #install_dir = os.environ['EG_DIR']
    
    # making bad file line
    badFileLine = ['drwxrwxrwx','1','soumaya','staff', badFileSize, badFileName]


    # picking random index for selecting files among a list of possible files
    nMaxFiles    = read_list_of_files()
    rand_indexes = rand.sample(list(np.arange(0,nMaxFiles)),numberFiles)


    fileList     = []
    indexBadFile = rand.sample(range(0,numberFiles-1),1)[0]
    
    
    # selecting lines in template files accroding to the random index drawn
    j = 0 
    for i in range(numberFiles) :
        
        
        if i != indexBadFile :
            fileList += [[colored(str(i),'red')]+\
                          read_list_of_files(index=rand_indexes[j])]
            j += 1
        else :
            fileList += [[colored(str(indexBadFile),'red')]+\
                         badFileLine]


    # making and writting fake file
    # getting filenames for comparison of inputs by user later in the code
    
    fname         = install_dir+'Files_search/file_list.txt'
    string_format = "{0[0]:<14}{0[1]:<13}{0[2]:<5}{0[3]:<10}{0[4]:<10}{0[5]:<10}"+\
                    "{0[6]:<30}"
    fnames, index = [], []
    
    with open(fname, 'w') as myFile :

        for i,line in enumerate(fileList) :

            myFile.write(string_format.format(line)+'\n')
            fnames += [line[-1]]
            index  += [i]
        
    return fnames, index


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


def searchForBadFile(culprit) :

    
    #install_dir = os.environ['EG_DIR']

    # randomly select files from a list of possibilities and write a new file
    # listing all files on the "culprit account".
    fnames,index = makeListFiles(numberFiles=34)

    while True :

        sp.call(['clear'])
        first_message = "\nListe des fichiers trouvés sur le compte de {} : \n"
        slowprint(first_message.format(culprit,'red'))

        # display list of files on screen
        sp.call(['head','-40', install_dir+'Files_search/file_list.txt'])

        # which file to inspect ?
        input_fname_num = 99
        failed_once     = False

        message_num = ('\nEntrez le numéro du fichier à inspecter:')
        while not any([input_fname_num == i for i in index]):
            if failed_once :
                slowprint('Numéro incorrect, nouvelle tentative :',color='red')
                time.sleep(0.75)
                sp.call(['clear'])
                print(colored(first_message,'red'))
                sp.call(['head','-40',install_dir+'Files_search/file_list.txt'])
                
            
            slowprint(message_num)
            input_fname_num = input()
            try : 
                input_fname_num = int(input_fname_num)
            except ValueError :
                input_fname_num = str(input_fname_num)
                
   
            if not any([input_fname_num == i for i in index]) :
                failed_once = True
            else : failed_once = False
       

        # show file asked by user
        message = "aperçu de "+colored('{}','red')+":"
        slowprint(message.format(fnames[input_fname_num]))
        print('--'*12)
        sp.call(['head','-30',install_dir+'Files_search/Files/'+\
                 fnames[input_fname_num]])
        print('... \n\n'+'--'*12)
        # ask user if they want to scan the file
        temp = 'None'
        failed_once = False
        while not isYon(temp) :

            if failed_once :
                slowprint('Veuillez répondre par oui ou par non, '+\
                          'nouvelle tentative:','red')
                time.sleep(0.75)
                sp.call(['clear'])
                print(colored(first_message,'red'))
                sp.call(['head','-40', install_dir+'Files_search/file_list.txt'])
                message = "aperçu de "+colored('{}','red')+":"
                print(message.format(fnames[input_fname_num]))
                sp.call(['head','-30',install_dir+'Files_search/Files/'+\
                         fnames[input_fname_num]])
                
            message_scan = '\nSouhaitez-vous scanner le fichier ? (oui/non)'
            slowprint(message_scan)
            temp = format_string(input())

            if not isYon(temp) : failed_once = True
            else : failed_once = False

        if temp.lower() == 'oui' or temp.lower() == 'o' : scan_file = True
        if temp.lower() == 'non' or temp.lower() == 'n' : scan_file = False
        
        if scan_file :
            slowprint('\n scan en cours :\n')
            displayLoadingBar(length=50,duration=2)

            if fnames[input_fname_num] == 'reallyBadFile.sh' :

                temp = 'None'
                failed_once = False
                while not isYon(temp) :

                    if failed_once : 
                        slowprint('Veuillez répondre par oui ou par non, '+\
                                  'nouvelle tentative:','red')
                        time.sleep(0.75)
                        sp.call(['clear'])
                        print(colored(first_message,'red'))
                        sp.call(['head','-30', install_dir+\
                                 'Files_search/file_list.txt'])
                        message = "aperçu de "+colored('{}','red')+":"
                        print(message.format(fnames[input_fname_num]))
                        sp.call(['head','-30',install_dir+'Files_search/Files/'+\
                                 fnames[input_fname_num]])

                    message_bad_file = 'Fichier malveillant identifié : '+\
                                       'souhaitez-vous le supprimer ? (oui/non)'  
                    slowprint(message_bad_file,'red')
                    temp = input()
                    
                    
                    if not isYon(temp) : failed_once = True
                    else : failed_once = False
                    
                    
                if temp.lower() == 'oui' or temp.lower() == 'o': break
                if temp.lower() == 'non' or temp.lower() == 'n': continue
            else :
                message_ok='Rien de suspicieux sur ce fichier \n'
                slowprint(message_ok,'green')
                time.sleep(1.2) # wait one sec

    slowprint('\nfichier effacé !\n','green')

    time.sleep(2)
    
    slowprint('Réinitialisation en cours : ','green')
    displayLoadingBar(duration=20)
    slowprint('SUCCÈS !',time_scale=1,color='green')
    
    return None

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
# ---------------       BEGINNING OF MAIN SCRIPT         ---------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------


parser = argparse.ArgumentParser(description='Some options for the program.')

parser.add_argument('--section','-sec',type=int,default=0, \
                    help='define which section of the script is executed. Usefull '+\
                    'When testing only a specific section')
parser.add_argument('--test','-t',action='store_true',default=False, \
                    help='Use simpler inputs for the login and mdp')
args = parser.parse_args()



global install_dir    # to refer to main directory of the Hacking part
install_dir = './'     # useful to have absolute path designation



# to prevent ctrl + c  ctrl + z
if not args.test : 
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)



# -- first part

# find password and login to lofin as Admin

if args.section == 0 or args.section == 1 : 


    if args.test : 
        goodUsername = np.array(['admin' , 'admin2'])
        goodPassword = np.array(['1234'  , '12345'])

    else : 
        goodUsername = np.array(['john.keller@space.fr'])
        goodPassword = np.array(['Biscotte'])
    
    indices      = np.array(["indice : OUAF OUAF !!"])
    logAsAdmin(goodUsername, goodPassword, indices)
    time.sleep(1)



# -- Second part

# identify the culprit looking at the schedule and recent activities

teamNames   = [1,2,3,4]

teamMembers = {1: ['Kenael', 'Laurent', 'Nicolas'],
               2: ['Thierry', 'Sylvain', 'René'],\
               3: ['Geoffroy', 'Agatha','Lydia'],\
               4: ['Rémi','Tim-long','Julie']}

chiefs      = ['Catherine','Elise','Sacha','Eric','Soumaya','Valentin']
culprit     = "Soumaya"


if args.section == 0 or args.section == 2 : 
    lookForCulprit(culprit,teamNames,teamMembers,chiefs)


time.sleep(1)


# -- Third part

# searching and erasing the file

if args.section == 0 or args.section == 3 :
    searchForBadFile(culprit)


    
# -- Fourth part :
good_angles = [40.,3.]

if args.section == 0 or args.section == 4 : 
    atmospheric_entry(good_angles)
    
            

