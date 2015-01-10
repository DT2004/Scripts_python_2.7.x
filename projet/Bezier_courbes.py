# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 15:52:37 2014

@author: Nathan
"""
from matplotlib import *

def factorielle(n):
    rc=1
    for i in range(n):
        rc=rc+i*rc;
    return rc

def combinaison(i, n):
    return factorielle(n)/(factorielle(i)*factorielle(n-i))
    
def Bi_n(i, n, t):
    return combinaison(i, n)*(t**i)*(1.-t)**(n-i)
    
def multiplication(liste, scalaire):
    liste_fin=[]
    for element in liste:
        liste_fin.append(element*scalaire)
    return liste_fin

def OM_t(P0, P1, P2, t):
    fin=[0.0, 0.0]

    temp_1=multiplication(P0, t**2)
    temp_2=multiplication(P1, 2*t*(1-t))
    temp_3=multiplication(P2, (1-t)**2)
    
    fin[0]=temp_1[0]+temp_2[0]+temp_3[0]
    fin[1]=temp_1[1]+temp_2[1]+temp_3[1]
    return fin


def Bernstein(P0, P1, P2, pas):
    x=[]
    y=[]
    curseur=0;
    while curseur<=1:
        
        x_actuel=OM_t(P0, P1, P2, curseur)
        x.append(x_actuel[0])
        
        y_actuel=OM_t(P0, P1, P2, curseur)
        y.append(y_actuel[1])
        curseur=curseur+pas;
    plot(x, y)
    #return((x, y))
        
    
def e_bezier(pas):
    X=[]
    Y=[]
    P0=[3, 8]
    P1=[2, 6]
    P2=[5.5, 6]
    P3=[6.5, 6]
    P4=[6.5, 7]
    P5=[6.5, 8]
    P6=[5.5, 8]
    P7=[4, 8]
    P8=[4, 5]
    P9=[4, 4]
    P10=[5, 3.5]
    P11=[6, 3]
    P12=[7, 4]
    X.append(Bernstein(P0, P1, P2, pas))
    X.append(Bernstein(P2, P3, P4, pas))
    X.append(Bernstein(P4, P5, P6, pas))
    X.append(Bernstein(P6, P7, P8, pas))
    X.append(Bernstein(P8, P9, P10, 0.1))
    X.append(Bernstein(P10, P11, P12, 0.1))
    
    Y.append(Bernstein(P0, P1, P2, 0.1))
    Y.append(Bernstein(P2, P3, P4, 0.1))
    Y.append(Bernstein(P4, P5, P6, 0.1))
    Y.append(Bernstein(P6, P7, P8, 0.1))
    Y.append(Bernstein(P8, P9, P10, 0.1))
    Y.append(Bernstein(P10, P11, P12, 0.1))
    
    plot(X, Y)
    

    

