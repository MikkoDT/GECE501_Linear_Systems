# -*- coding: utf-8 -*-
"""

@author: Engr_Mikko

Exercise #2

"""
from numpy  import sqrt, real, imag

from sympy import laplace_transform as LTe, im, re, \
                  LaplaceTransform as LTu, \
                  inverse_laplace_transform as ILTe, together, apart, factor, \
                  InverseLaplaceTransform as ILTu, Heaviside, DiracDelta
                      
from sympy import diff, symbols, Eq, exp as Exp, sin as Sin, numer, denom, \
                  cos as Cos, pi, Function, solve, dsolve, latex as Lx, roots

y, t, s, Y, A, B, C    = symbols("\
y  t  s  Y  A  B  C        ")

yF, YF    = symbols("\
y   Y              ",cls=Function)

"Drill #1"
Deq1=Eq(4*yF(t) + yF(t).diff(t) - 6*Exp(2*t),0)
Y1s=LTe(yF(t),t,s)[0]
Y1s1 = LTe(Deq1.lhs, t, s, noconds=True)
Y1s2=solve(Y1s1,Y1s)[0]
Y1s3=Y1s2.subs(yF(0),3)
soln_1=Eq(yF(t),ILTe(Y1s3,s,t))

"Drill #2"
Deq2 = Eq(yF(t) + yF(t).diff(t), 3*Cos(2*t))
Y2s=LTe(yF(t),t,s)[0]
Y2s2=LTe(Deq2.lhs-Deq2.rhs,t,s)[0]
Y2s3=solve(Y2s2,Y2s)[0]
Y2s4=Y2s3.subs(yF(0),0)
soln_2=Eq(yF(t),ILTe(Y2s4,s,t))


"Drill #3"
Deq3 = Eq(12*yF(t) + 7*yF(t).diff(t) + yF(t).diff(t, t), 10)
Y3s=LTe(yF(t),t,s)[0]
Y3s1=LTe(yF(t).diff(t),t,s)[0]
Y3s2=LTe(yF(t).diff(t,t),t,s)[0]
Y3s3=Y3s2.args[0]
Y3s4=LTe(Deq3.lhs- Deq3.rhs,t,s)[0]
Y3s5=solve(Y3s4,Y3s)[0]
Y3s6=Y3s5.subs(-Y3s3,0).subs(t,0).subs(yF(0),3)
soln_3=Eq(yF(t),ILTe(Y3s6,s,t))


"Drill #4"
Deq4= Eq(20*yF(t) + 4*yF(t).diff(t) + yF(t).diff(t, t) , 4)
Y4s=LTe(yF(t),t,s)[0]
Y4s1=LTe(yF(t).diff(t),t,s)[0]
Y4s2=LTe(yF(t).diff(t,t),t,s)[0]
Y4s3=-Y4s2.args[0]
Y4s4=LTe(Deq4.lhs-Deq4.rhs,t,s)[0]
Y4s5=solve(Y4s4,Y4s)[0]
Y4s6=Y4s5.subs(Y4s3,0).subs(t,0).subs(yF(0),-2)
soln_4=Eq(yF(t),ILTe(Y4s6,s,t))


"Drill #5"
Deq= Eq(6*yF(t).diff(t) + 5*yF(t).diff(t, t) + yF(t).diff(t, t, t),0)
Y_s=LTe(yF(t),t,s)[0]
Y_s1=LTe(yF(t).diff(t),t,s)[0]
Y_s2=LTe(yF(t).diff(t,t),t,s)[0]
Y_s3=Y_s2.args[0]
Y_s4=LTe(yF(t).diff(t,t,t),t,s)[0]
Y_s5=Y_s4.args[0]
Y_s6=LTe(Deq.lhs-Deq.rhs,t,s)[0]
Y_s7=solve(Y_s6,Y_s)[0]
Y_s8=Y_s7.subs(-Y_s3,-2).subs(-Y_s5,7).subs(t,0).subs(yF(0),3)
soln_5=Eq(yF(t),ILTe(Y_s8,s,t))