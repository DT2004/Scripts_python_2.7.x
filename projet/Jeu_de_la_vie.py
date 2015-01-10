# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 17:46:02 2014

@author: Nathan
"""

import random
import numpy as np
from pylab import *
import time
import pylab


def afficher_matrice(M): 
    #fig.set_size_inches(3,2)
    plt.clf()
    plt.imshow(M, interpolation='nearest', );
    #cmap = plt.get_cmap('gray')
    plt.pause(0.05)
    plt.show();
    #plt.pause(0.1)
    pylab.show()
    
def egalite_matrices(A, B):
    
    test=[]
    for ligne in range(B.shape[0]):
        for colonne in range(B.shape[1]):
            if A[ligne, colonne]!=B[ligne, colonne]:
                  test.append(1)
            else:
                  test.append(0);
        
    if test.count(0)==len(test):
        return True;
    else:
        return False;            
                    
def jeu_de_la_vie():
    #Matrice 15x15 aleatoire, de depart
    import random
    compteur=0
    Z=zeros((10, 10));
    temoin=zeros((10, 10));
    
    
    for ligne in range(Z.shape[0]):
        for colonne in range(Z.shape[1]):
            Z[ligne,colonne]=random.randint(0,1);
    #OK
    afficher_matrice(Z)
    #clf()
    #imshow(Z, interpolation='nearest') # Par défaut : quadratique
    limite=1
    Y=zeros(Z.shape)
    
    a=0
    while limite==1:

        if a%2==0:
            if a%4==0:
                Z_temp=Z;                 
                   
        for ligne in range(Z.shape[0]):
            for colonne in range (Z.shape[1]):
                ligne_avant=(ligne-1)%100;
                ligne_apres=(ligne+1)%100;
                colonne_avant=(colonne-1)%100;
                colonne_apres=(colonne+1)%100;
            
                couronne=[]
                vie=0
                mort=0
                
                couronne.append(Z[ligne_avant,colonne_avant])
                couronne.append(Z[ligne_avant, colonne])
                couronne.append(Z[ligne_avant, colonne_apres])
                
                couronne.append(Z[ligne, colonne_avant]);
                couronne.append(Z[ligne, colonne_apres]);
                
                couronne.append(Z[ligne_apres, colonne_avant]);
                couronne.append(Z[ligne_apres, colonne]);
                couronne.append(Z[ligne_apres, colonne_apres]);
                     
                for element in couronne:
                    if element==1:
                        vie=vie+1
                    else:
                        mort=mort+1
          
                
                if vie<2:
                    Y[ligne, colonne]=0;
                    
                if vie>3:
                    Y[ligne, colonne]=0;
                    
                if vie==2:
                    if Z[ligne, colonne]==1:
                        Y[ligne, colonne]=1;
                    else:
                        Y[ligne, colonne]=0;
                
                if vie==3:
                    if Z[ligne, colonne]==1:
                        Y[ligne, colonne]=1;
                    else:
                        Y[ligne, colonne]=1;
                                       
        afficher_matrice(Z)        
        
        if Z.any()==temoin.any():
            print "Plus aucun signe de vie !"            
            limite=50 
            continue;
        
        if a%2==0:
            if a%4!=0:
                if egalite_matrices(Z, Z_temp)==True:
                    print "boucle !";
                    limite=50;
                    continue;               
        
        #print"Y=", Y
        #inutile, juste pour la precision
        if egalite_matrices(Z, Y)==True:
            print "etat stable";
            limite=50
            continue;
        
        Z=Y                        
        Y=zeros(Y.shape)
        
        a=a+1    
        print "passe numero", a        
        
        print "Z=", Z
        
        if a>200:
            continuer = input("Continuer ? (+100 passes) True/False ?")
            if continuer==True:
                
                a=a-100;
                compteur=compteur+1            
            #limite=50
        
        time.sleep(0)

    #On sort de la boucle    
    afficher_matrice(Z)
    print ("Nombre de passes :"), (a+100*compteur)
