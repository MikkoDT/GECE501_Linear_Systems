# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:40:17 2023

@author: Celso
"""
from numpy import array, sqrt, arccos
from sympy import symbols, latex, Function, Matrix, sqrt as Sqrt,\
                  acos as aCos, Heaviside, Sum, oo, DiracDelta, factorial,\
                  numer, denom, factor, Float    

from sympy import symbols, Function, latex, var, Ge, log as Ln, re, im 
from sympy import laplace_transform, inverse_laplace_transform, gamma 
from sympy import LaplaceTransform, InverseLaplaceTransform  #unevaluated

from sympy     import abc, oo, numer, denom, integrate, diff, roots, exp as Exp
from sympy.abc import delta, phi, theta

sigfig=4

Lx   = latex
fn   = Function
LTu  = LaplaceTransform           #unevaluated
LTe  = laplace_transform          #evaluated
ILTu = InverseLaplaceTransform    #unevaluated
ILTe = inverse_laplace_transform  #evaluated

t, s, zeroN, fP, mathcalL   = symbols("\
t  s  0^{-}  f'  \\mathcal{L}           ")

F, f, s, t, T, u, U, a, b, k, w,      lc,         invlc,           n =symbols("\
F  f  s  t  T  u  U  a  b  k  \\omega \mathcal{L} \mathcal{L}^{-1} n        ")


FF, F1F, F2F, fF, f1F, f2F, uF, UF, lcF, invlcF, fPF = symbols("\
F,  F_1  F_2   f,  f_1  f_2   u,  U,  lc,  invlc f'          ",cls=Function)

fF(t)

LTu(fF(t),t,s)

LTe(fF(t),t,s)

LTu(t,t,s)

LTe(t,t,s)[0]

LTu(t**n,t,s)

LTe(t**n,t,s)

LTu(t**4,t,s)

LTe(t**4,t,s)[0]

Lx(LTu(t**4,t,s))


y, yP, yPP, Y = symbols("\
y  y'  y{\"}  Y         ")

yF, YF, yPF, yPPF = symbols("\
y   Y   y'   y{\"}          ",cls=Function)


A, B, C, K, x, y, z   = symbols("\
A  B  C  K  x  y  z       ")





"""
sloc, sTail,  sTip,  smid,   stheta, sMag, sUnit, sDot, sCross   =symbols("\
loc   T_{ail} T_{ip} m_{id} \\theta Mag   Unit   Dot   Cross        ")

sx,  sy,    sz                        =symbols("\
x    y      z                                  ")

A, B, C, K, x, y, z   = symbols("\
A  B  C  K  x  y  z       ")

sv, svx,  svy,  svz,              =symbols("\
v   v_{x} v_{y} v_{z}                      ")



sv1, sv1x,  sv1y,  sv1z,              =symbols("\
v_1  v_{1x} v_{1y} v_{1z}                      ")


sv2, sv2x,  sv2y,  sv2z,               =symbols("\
v_2  v_{2x} v_{2y} v_{2z}                       ")


sv3, sv3x,  sv3y,  sv3z,               =symbols("\
v_3  v_{3x} v_{3y} v_{3z}                       ")




sax,                   say,                   saz                   =symbols("\
\\overrightarrow{a_x}  \\overrightarrow{a_y}  \\overrightarrow{a_z}          ")

sthetax,  sthetay,   sthetaz     = symbols("\
\\theta_x \\theta_y  \\theta_z             ")


A1, B1, C1, K1, A2, B2, C2, K2 = symbols("\
A_1 B_1 C_1 K_1 A_2 B_2 C_2 K_2          ") 

V1, V2,  V3       = symbols("\
V_1 V_2  V_3              ")

sTipf   = Function(sTip)   #avoidance univocal 
sTailf  = Function(sTail)
slocf   = Function(sloc)
sMagf   = Function(sMag)
sUnitf  = Function(sUnit)
smidf   = Function(smid)
sDotf   = Function(sDot)
sCrossf = Function(sCross)

Lx=latex

def Ml(s):return "$"+latex(s)+"$"


class cbcoVector():
    def __init__(self,value,loc=[0,0,0]):
        self.Value=array(value)
        self.Loc=array(loc)
        self.Tail=array(loc)
        self.Tip=array(loc)+array(value)
        self.Mid=(self.Tail+self.Tip)/2
        self.Magnitude=Sqrt(value[0]**2+value[1]**2+value[2]**2)
        if self.Magnitude > 0 :
            self.Unit=self.Value/self.Magnitude
        self.DirectionalAngles=array([\
            aCos(self.Unit[0]),aCos(self.Unit[1]),aCos(self.Unit[2])])

    def reloc(self,loc):
        self.Loc=array(loc)
        self.Tail=loc
        self.Tip=loc+self.Value
        self.Mid=(self.Tail+self.Tip)/2
      
    def revalue(self,value):
        self.Value=array(value)
        self.Tail=self.Loc
        self.Tip=self.Loc+self.Value
        self.Mid=(self.Tail+self.Tip)/2
        
    def mag(self,v=""):
        if v=="":
            temp = Sqrt(self.value[0]**2+self.value[1]**2+self.value[2]**2)
            self.Magnitude = temp
            return temp
            
        else:
            return Sqrt(v[0]**2+v[1]**2+v[2]**2)
        
    def unit(self,v=""):
        if v=="":
            if self.Magnitude > 0 :
                temp = self.Value/self.Magnitude
                self.Unit = temp
                return temp
            else:
                return oo
        else:
            return  array(v)/sqrt(v[0]**2+v[1]**2+v[2]**2)
                
        
r, e, ym, y, yfrd, u, Ao, Ac, s, G, G0, Gc, Gp, H, Hp   = symbols("\
r  e  ym  y  y_f   u  A_o A_c s  G  G_0 G_c G_p H  H_p           ")        

rf  = Function(r)
ef  = Function(e)
ymf = Function(ym)
yf  = Function(y)
yfrdf = Function(yfrd)
uf  = Function(u)
Aof = Function(Ao)
Acf = Function(Ac)
Gcf = Function(Gc)
Gpf = Function(Gp)
Hf  = Function(H)
Hpf = Function(Hp)
Gf  = Function(G)


z, Z, zeta,  omega,  omegan,   R, E,  E1, E1a,   C, F,  T, Gprm = symbols("\
z  Z, \\zeta \\omega \\omega_n R  E  E_1  E_{1*} C  F   T  G'             ")


zf    =  Function(z)
Zf    =  Function(Z)
Rf    =  Function(R)
Ef    =  Function(E)
E1f   =  Function(E1)
E1af  =  Function(E1a)
Cf    =  Function(C)
Ff    =  Function(F)
Gprmf =  Function(Gprm)


diracdelta, k, us = symbols("\
\\delta     k  u      ")

diracdeltaf = Function(diracdelta)
usf         = Function(us)






"""