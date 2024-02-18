# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:19:39 2022

@author: Celso
"""

from sympy import symbols, Function, latex, atan as aTan, Eq, cos as Cos,\
                           sin as Sin

v, uv, mv, vx, vy, vz = symbols("V uV |V| V_x V_y V_z")

x, y, z, mx, bx, mz, bz, my, by, f, t  = symbols("\
x  y  z  m_x b_x m_z b_z m_y b_y f  t          ")

A, B, C, K, Kx, Ky, Kz  = symbols("\
A  B  C  K  K_x K_y K_z           ")

A1, B1, C1, K1, K1x,   K1y,   K1z    = symbols("\
A_1 B_1 C_1 K_1 K_{1x} K_{1y} K_{1z}           ")

x1, x2, y1, y2, z1, z2  = symbols("\
x_1 x_2 y_1 y_2 z_1 z_2           ")

inv           = symbols("\
I_{nverse}              ")

fF  = Function(f)
invF= Function(inv)

def Ml(s):  #Math Latex
    return "$"+latex(s)+"$"

Lx=latex



#fig04.py

a0, a1, a2, a3, a4, an  = symbols("\
a_0 a_1 a_2 a_3 a_4 a_n           ")

b0, b1, b2, b3, b4, bn  = symbols("\
b_0 b_1 b_2 b_3 b_4 b_n           ")

c0, c1, c2, c3, c4, cn  = symbols("\
c_0 c_1 c_2 c_3 c_4 c_n           ")

x0, x1, x2, x3, x4, xn  = symbols("\
x_0 x_1 x_2 x_3 x_4 x_n           ")

y0, y1, y2, y3, y4, yn  = symbols("\
y_0 y_1 y_2 y_3 y_4 y_n           ")

z0, z1, z2, z3, z4, zn  = symbols("\
z_0 z_1 z_2 z_3 z_4 z_n           ")



"cone01.py"

base,   height,   u, rc,      delta,  phi       = symbols("\
b_{ase} h_{eight} u  r_{cone} \\delta \\phi              ")

dots,   cdots,  vdots,  ddots  = symbols("\
\\dots, \\cdots \\vdots \\ddots          ")


"The cone equations"
delta = aTan(height/base)
ecx=Eq(x,(height-u)/height*base*Cos(phi))
ecy=Eq(y,(height-u)/height*base*Sin(phi))
ecz=Eq(z,u)
ecdelta=Eq(delta,2*aTan(rc/height))
ec1=Eq(x**2+y**2,ecy.rhs**2+ecx.rhs**2).simplify()




