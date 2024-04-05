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

y, y0, y1, y2, y3, yn             = symbols("\
y  y_0 y_1 y_2 y_3 y_n                      ")

x, x0, x1, x2, x3, xn             = symbols("\
x  x_0 x_1 x_2 x_3 x_n                      ")

u, u0, u1, u2, u3, un             = symbols("\
u  u_0 u_1 u_2 u_3 u_n                      ")



yF, y0F, y1F, y2F, y3F, ynF      = symbols("\
y  y_0 y_1 y_2 y_3 y_n                     ",cls=Function)

xF, x0F, x1F, x2F, x3F, xnF      = symbols("\
x  x_0 x_1 x_2 x_3 x_n                     ",cls=Function)

uF, u0f, u1F, u2F, u3F, unF      = symbols("\
u  u_0 u_1 u_2 u_3 u_n                      ",cls=Function)

dotx,    dotx1,     dotx2,     dotx3,     dotxn          = symbols("\
\\dot{x} \\dot{x_1} \\dot{x_2} \\dot{x_3} \\dot{x_n}                ")

ddotx,    ddotx1,     ddotx2,     ddotx3,     ddotxn          = symbols("\
\\ddot{x} \\ddot{x_1} \\ddot{x_2} \\ddot{x_3} \\ddot{x_n}                ")

A, B, C, D     =symbols("\
A  B  C  D              ")



rF  = Function(r)
yF  = Function(y)