from ppy import ADC #Importation du module ADC
from lib import afficheurWEBAPP #Importation de la lib AfficheurGrosChiffre


A0 = ADC('A0') #Initialisation du module ADC (ici A0)
unit = "Â°C" # Initialisation de l'unité envoyé a l'application web (ici °C)
id = "2" 
afficheur = afficheurWEBAPP.afficheursWEBAPP() # Initialisation de l'afficheur gros chiffre
value = 0
m= A0.read() #Initialisation de la variable de lecture sur le port A0, elle contiendra la donnée lue
m=m/4095 # Normalisation de la valeur entre 0 et 1
temperature=235.27*m*m*m-346.75*m*m+267.28*m-50.898 # Multiplication de la normalisation avec la fonction de transfert de la température
value="{:.1f}".format(temperature) # Format de la valeur avec un chiffre dérrière la virgule
afficheur.envoyer(valeur=value,identifier=id,unit=unit) # Envoie de la valeur à l'application Web

