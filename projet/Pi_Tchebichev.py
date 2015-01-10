# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 17:18:29 2014

@author: nathan
"""

from numpy.lib.polynomial import poly1d

#### Ressources ####
from numpy.lib.polynomial import poly1d
from matplotlib.pyplot import plot

    
def fonction(x):
    return(1.0/(1.0+x**2))

def tranchettes_x(nbr):
    abscisse=[];
    taille=2.0/nbr
    for i in range(nbr+1):
        abscisse.append(-1+(i*taille))
    return abscisse
    
def primitive(polynome):
    polynome_primitive=poly1d([])
    p=1
    for i in range (0, polynome.order+1): 
        temp=polynome[i]*1/p
        polynome_primitive[i+1]=temp

        p=p+1
        
    return polynome_primitive
    
def interpolation_Lagrange(listeX, listeY):
    rc=poly1d([])
    nbr=0;
    for i in (listeX):       
        temp=pi_Lagrange(i, listeX)
        #print "temp =", temp
        #print "Y act =", listeY[nbr]
        rc=rc+(listeY[nbr]*temp);
        nbr=nbr+1
    return rc    
    #### FIN RESSOURCES ####



def Tchebichev_coeffs(ordre):
    #Avec des dictionnaires !    
    dico_T={}
    
    dico_T[0]=poly1d([1])
    dico_T[1]=poly1d([1, 0])
    
    x=poly1d([1, 0])
    
    for i in range(2, ordre+1):
        dico_T[i] = (2*x*dico_T[i-1])-(dico_T[i-2])

    return dico_T
    #return dico_T   

def Tchebichev_roots(ordre):
    dico=Tchebichev_coeffs(ordre)
    rc=[] #il faut envoyer a Lagrange une liste    
    for element in dico[ordre].roots:
        rc.append(element)
    return rc
    
### MAIN ###
def approx_pi_Tchebichev(nbr):
    
    tranchX=Tchebichev_roots(nbr+1)
    tranchY=[]
    
    for i in range(nbr+1):
        tranchY.append(fonction(tranchX[i]))    
    #print tranchX
    #print tranchY
    
    polynome=interpolation_Lagrange(tranchX, tranchY)
    #print polynome

    #On le derive
    poly_prim=primitive(polynome)
    
    #Th fondamentale de la derivation:
    approx_pi=poly_prim(1)-poly_prim(-1)
    
    #print "\n", poly_prim(1)
    #print poly_prim(-1), "\n"
    
    return approx_pi*2 
