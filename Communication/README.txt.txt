# Escape Game communication
Ce système permet la mise en place d'un système de chat entre le centre de contrôle et le PC du médiateur.


## Description
Un premier programme est lancé sur le PC du médiateur qui va ouvrir un espace de chat à destination d'un raspberry pi du centre de contrôle.
Un autre programme sera executé à partir d'un raspberry pi du centre de contrôle. Ce dernier nécessite la saisie du mot de passe ciel afin d'établir la connexion avec le PC du médiateur. Une fois le mot de trouvé la connexion chat est établie et les deux protagoniste peuvent communiquer via le chat


## Prérequis
Le système est composé de 2 équipements à partir desquels une communication chat sera établie.
Les deux équipements réseaux doivent être obligatoirement connecté au même réseau.
Le système d'exploitation pour lequel le système a été testé est basé sur raspbian.


## Installation
1) Extraire le fichier "server.sh" et le charger sur le PC du médiateur.
2) Après chargement, rendre ce fichier executable à l'aide de la commande  : chmod +x server.sh
3) Noter l'adresse ip utilisée en executant la commande "ifconfig".
4) Extraire le fichier "pcCommunication.sh" et le charger sur un raspberry pi du centre de contrôle.
5) Après chargement, rendre ce fichier executable à l'aide de la commande  : chmod +x pcCommunication.sh
6) Modifier le fichier pcCommunication.sh afin de saisir la bonne adresse IP dans l'attribut "adrIPSrv"


## Utilisation
1)Executer le programe "server.sh" à partir du PC du médiateur à l'aide de la commande suivante : ./server.sh
2)Saisir le nom que l'on souhaite utiliser pour être identifié dans le chat.
3) Executer le programme "pcCommunication.sh" à partir du raspberry pi du centre de contrôle à l'aide de la commande suivante : ./pcCommunication.sh


## Problème(s) rencontré(s)
  - Le programme de communication ne se connecte pas à l'espace de chat
    1) Vérifier que les deux appareils sont bien connectés sur le même réseau
    2) Vérifier que le serveur est bien executé sur le PC de monitoring (consulter paragraphe 1) du chap. Utilisation)
	3) Vérifier que la configuration de l'adresse IP du serveur est correctement définie (consulter 6) du chap. Installation)
	4) Redémarrer le serveur de chat sur le PC du médiateur
	5) Redémarrer le programme de communication sur le raspberry pi
	6) Procéder  de nouveau à l'installation des deux applicatifs