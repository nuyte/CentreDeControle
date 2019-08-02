#!/bin/bash
###############################################################################
# Nom du fichier : pcCommunication.sh
# Date : 08/05/2019
# Auteur : Sylvain Nion
# Description : Scrit permettant de se connecter à PC de monitoring afin
#               d'établir la communication avec l'ISS
# Requis : printf, server.sh
###############################################################################

#Variables d'environnement
motDePasse="4594"
adrIPSrv="192.168.1.109"
portSrv="9999"


#Fonction qui affiche une barre de progression
barreprogression() {
    p=0
    nbCar=1
    nbSpc=71
    echo -en "\r"
    echo -en "\r"
    while [ $p -lt 100 ]; do
        chaine=""
        for i in `seq 1 $nbCar` ; do
            chaine="$chaine="
        done
        espace=""
        for i in `seq 1 $nbSpc` ; do
            if [ $nbSpc != 1 ] ; then
                espace="${espace}."
            else
                espace="${espace}=]"
            fi
        done

        if [ $nbCar != 72 ] ; then
            chaine="$chaine$espace"
        else
            chaine="$chaine="
        fi

        if [ $p != 99 ] ; then
            echo -en "["$chaine"]($p%)\r"
        else
            echo -en "["$chaine"(100%)\r"
        fi

        valAlea=$((0+3+RANDOM*(1+3-0)/32767))
        p=$(echo "scale=0;$p + $valAlea"|bc -l)
        if [ $p -gt 100 ] ; then
            echo "[========================================================================](100%)"
            break
        fi
        nbCar=$(echo "scale=0;$p * 72 / 100"|bc -l)
        nbSpc=$(echo "scale=0;72 - $nbCar"|bc -l)
        sleep 0.10
    done
}


#Programme principal
clear
echo "==============================================================================="
echo "                               PC de communication"
echo "==============================================================================="
echo ""
printf "\033[33mLa tentative de hacking du centre de contrôle a bloqué le canal de communication avec l'ISS.\033[0m\n"
echo "Veuillez entrer le mot de passe (4 chiffres) afin de déverouiller le canal"
echo ""

M2P=0

while test $M2P != $motDePasse
do
    #Afficher le mesage ci-dessous lorsqu'un mot de passe est saisi est erroné
    if [ $M2P != 0 ] ; then
        printf '\033[31mErreur\033[0m saisie mot de passe\n'
    fi

    echo -e "Saisir le mot de passe : \c"
    read M2P

    #On défini une valeur si aucune valeur saisie
    if test -z $M2P ; then
        M2P=0
    fi

done
printf '\033[32mOK\033[0m : Mot de passe valide\n'

echo "Etablissement de la liaison en cours..."
barreprogression
echo -en '\r'
printf "Canal de communication avec l'ISS \033[32mouvert\033[0m\n"

nc $adrIPSrv $portSrv
