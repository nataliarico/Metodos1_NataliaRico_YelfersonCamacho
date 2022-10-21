import numpy as np
import sympy as sym
from scipy import integrate


#x_0 = 0 
def p_0(x,h):
    return ((x-h)/-h)((x-2h)/-2h)((x-3h)/-3h)
def p_1(x,h): 
    return (((x+1)-h)/-h)(((x+1)-2h)/-2h)(((x+1)-3h)/-3h)
def p_2(x,h):
    return (((x+2)-h)/-h)(((x+2)-2h)/-2h)(((x+2)-3h)/-3h)
def p_3(x,h):
    return (((x+3)-h)/-h)(((x+3)-2h)/-2h)(((x+3)-3h)/-3h)

resultado= (integrate(p_0(x,h))+integrate(p_1(x,h)) +integrate(p_2(x,h))+integrate(p_3(x,h)))

    
#Se resuelve sumando las integrales de cada polinomio, desde 0 hasta 3. se usa h que representa el paso. 
