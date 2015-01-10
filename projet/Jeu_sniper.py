# -*- coding: utf-8 -*-
"""
Created on Fri May  9 22:31:32 2014

@author: Nathan
"""
import time
"""
    Conteneurs en bords de terrain, regle rapidement
    nbr_conteneurs fixe à 7
    taille carte fixe a 15
    nombre napolitains fixe a 4
    
    cas special implementation naps a revoir
    
    Tirs naps = OK en X et en Y, reste les diags (panachage)
    
(?? [1] = tirs policiers ?? )
    [2] = policiers
    [3] = tirs napolitain
    [4] = napolitain
    [5] = contener
    
"""


nbr_conteneurs = 10;
n = 15
nbr_nap = 3;

Nap_X = []
Nap_Y = []

def creation_terrain(n):
    return zeros((n, n));
    
def proba_conteneurs(suite, X, Y):            
    if suite<25:
        X2=X+1;
        Y2=Y;
    elif suite<50:
        X2=X-1;
        Y2=Y;
    elif suite<75:
        X2=X;
        Y2=Y-1;
    elif suite<100:
        X2=X;
        Y2=Y+1;

    return (X2, Y2)

def implemente_conteneurs(carte, nbr_conteneurs):
    borne_sup=carte.shape[0];
    for i in range(nbr_conteneurs):
        X=randint(1, borne_sup-1);
        Y=randint(1, borne_sup-1);
        
        suite=randint(0, 100);
        
        carte[X, Y] = 5;
        carte[proba_conteneurs(suite, X, Y)] = 5;    
    return carte
      
def implemente_napolitains(carte, nbr_nap):
    borne_sup=carte.shape[0];
    
    for i in range(nbr_nap):
        X=randint(1, borne_sup);
        Y=randint(1, borne_sup);
        
        if carte[X, Y]==5:
            X=randint(1, borne_sup);
            Y=randint(1, borne_sup); 
            
            carte[X, Y] = 4;
            
            Nap_X.append(X)
            Nap_Y.append(Y)
        else:
            carte[X, Y] = 4;
            Nap_X.append(X)
            Nap_Y.append(Y)
    return carte
          
def implemente_tirs_naps(carte):

    for nbr in range(nbr_nap):
            
            XAct = Nap_X[nbr];
            YAct = Nap_Y[nbr];
            
            #ligne vers la droite            
            for curseur_X in range(1, n):
                
                if XAct + curseur_X > 14:
                    break;
                if carte[XAct + curseur_X, YAct] == 5:
                    break;
                else:
                    if carte[XAct + curseur_X, YAct] == 4:
                        continue;                        
                    else:
                        carte[XAct + curseur_X, YAct] = 3
                        
            #ligne vers la gauche                    
            for curseur_X in range(1, n):
                
                if  XAct - curseur_X < 0:
                    break;      
                if carte[XAct - curseur_X, YAct] == 5:
                    break;
                else:
                    if carte[XAct - curseur_X, YAct] == 4:
                        continue;                         
                    else:
                        carte[XAct - curseur_X, YAct] = 3
                        
            #colonne vers le bas            
            for curseur_Y in range(1, n):
                
                if YAct + curseur_Y > 14:
                    break; 
                if carte[XAct, YAct + curseur_Y] == 5:
                    break;
                else:
                    if carte[XAct, YAct + curseur_Y] == 4:
                        continue;
                    else:
                        carte[XAct, YAct + curseur_Y] = 3
                        
            #colonne vers le haut                    
            for curseur_Y in range(1, n):
                
                if YAct - curseur_Y < 0: 
                    break;    
                if carte[XAct, YAct - curseur_Y] == 5:
                    break;
                else:
                    if carte[XAct, YAct - curseur_Y] == 4:
                        continue;
                    else:
                        carte[XAct, YAct - curseur_Y] = 3 
                        
            ##################################################
                        
            #Diagonale bas droite
            for nbr in range(1, n):
                if YAct + nbr > 14 or XAct + nbr > 14:
                    break;
                if carte[XAct + nbr, YAct + nbr] == 5:
                    break;
                else:
                    if carte[XAct + nbr, YAct + nbr] == 4:
                        continue;
                    else:
                        carte[XAct + nbr, YAct + nbr] = 3  
                        
            #Diagonale bas gauche
            for nbr in range(1, n):
                if YAct - nbr < 0 or XAct + nbr > 14:
                    break;
                if carte[XAct + nbr, YAct - nbr] == 5:
                    break;
                else:
                    if carte[XAct + nbr, YAct - nbr] == 4:
                        continue;
                    else:
                        carte[XAct + nbr, YAct - nbr] = 3
                    
            #Diagonale haut droite
            for nbr in range(1, n):
                if YAct + nbr > 14 or XAct - nbr < 0:
                    break;
                if carte[XAct - nbr, YAct + nbr] == 5:
                    break;
                else:
                    if carte[XAct - nbr, YAct + nbr] == 4:
                        continue;
                    else:
                        carte[XAct - nbr, YAct + nbr] = 3
            
            #Diagonale haut gauche
            for nbr in range(1, n):
                if YAct - nbr < 0 or XAct - nbr < 0:
                    break;
                if carte[XAct - nbr, YAct - nbr] == 5:
                    break;
                else:
                    if carte[XAct - nbr, YAct - nbr] == 4:
                        continue;
                    else:
                        carte[XAct - nbr, YAct - nbr] = 3                        

    return carte
    
   
def balayage(carte, X, Y):
    if carte[X, Y] == 5 or carte[X, Y] == 4 or carte[X, Y] == 3:
        return 0;
    else:
        return 1;


         
def sniper():
    
    tps_debut = time.time()
    
    carte = creation_terrain(n)
    carte = implemente_conteneurs(carte, nbr_conteneurs);
    carte = implemente_napolitains(carte, nbr_nap)
    carte = implemente_tirs_naps(carte)

    imshow(carte, interpolation="nearest") 
    
    tps = time.time() - tps_debut
    return ("Temps d execution : %f secondes" %tps)
    # return balayage(carte, X, Y)
