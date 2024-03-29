# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:40:17 2023

@author: Celso
"""
from numpy import array, sqrt, arccos
from sympy import symbols, latex, Function, Matrix, sqrt as Sqrt,\
                  acos as aCos
from sympy import oo                  

r, Fs1,   Fs2,   Fd1,   Fmass,   t, y, b1,  m1, k1, k2     = symbols("\
r  F_{s1} F_{s2} F_{d1} F_{mass} t  y  b_1, m_1 K_1 K_2              ") 


rF  = Function(r)
yF  = Function(y)