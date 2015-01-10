# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 17:33:06 2014

@author: Nathan
"""

#### RESSOURCES ####
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

#listeX et liste Y sont donnes

from numpy.lib.polynomial import poly1d
execfile ("Ressources.py")
#from Ressources import tranchettes_x
    
    
def pi_Lagrange(xi, listeX):
    rc=1
    X=poly1d([1, 0])
    for element in listeX:
        
        if element != xi:
            numerateur=(X-element)
            denominateur=(xi-element)
            temp=(numerateur/denominateur)
            rc=rc*temp         
        else:
            continue
    return rc
    
    
#### MAIN ####
def approx_pi_Lagrange(nbr):
    #print "\n", "Approximation la plus fidele : pour 20","\n","au dessus, l'approximation tend vers -inf", "\n"
    #Subdivisions
    tranchX=tranchettes_x(nbr);
    tranchY=[];
    for i in range(nbr+1):
        tranchY.append(fonction(tranchX[i]))
    
    #print tranchX
    #print tranchY
    #Maintenant, Lagrange
    polynome=interpolation_Lagrange(tranchX, tranchY)

    #On le derive
    poly_prim=primitive(polynome)
    
    #Th fondamentale de la derivation:
    approx_pi=poly_prim(1)-poly_prim(-1)
    
    return approx_pi*2 

        
    
