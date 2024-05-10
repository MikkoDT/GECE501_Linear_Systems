"""
@author: Engr_Mikko

Exercise #1 
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

"1.1"

Y1s= Eq(YF(s),s/(s+2))
Y1s1=Y1s.rhs.apart()
Y1s2=Y1s1.args[0]
Y1s3=Y1s1.args[1]

y1t1=ILTe(Y1s2,s,t)
y1t2=ILTe(Y1s3,s,t)
y1t=y1t1+y1t2

"1.2"

Y2s=Eq(YF(s),(3*s-5)/(s**2 + 4*s +2))
Y2numer=numer(Y2s.rhs)
Y2denom=denom(Y2s.rhs)
Y2roots=list(roots(Y2denom))
Y2denom1=(s-Y2roots[0])
Y2denom2=(s-Y2roots[1])
Y2s1=Eq(Y2numer/(Y2denom1*Y2denom2),A/Y2denom1 + B/Y2denom2)
Y2s2=Eq(Y2numer/(Y2denom2),A+B*Y2denom1/Y2denom2)
Y2s3=Y2s2.subs(s,Y2roots[0])
nA=solve(Y2s3,A)[0]
Y2s4=Eq(Y2numer/(Y2denom1),A*Y2denom2/Y2denom1+B)
nB=solve(Y2s4.subs(s,Y2roots[1]),B)[0]
Y2s5=Y2s1.subs(A,nA).subs(B,nB)

y2t1=ILTe(nA/Y2denom1,s,t)
y2t2=ILTe(nA/Y2denom2,s,t)
y2t=y2t1+y2t2
y2t3=y2t.evalf()

"1.3"
Y3denom1=s+2
Y3denom2=s+3
Y3s=Eq(YF(s),3/(Y3denom1*Y3denom2)-6*Exp(-2*s)/(Y3denom1*Y3denom2))

y3t1=ILTe(3/(Y3denom1*Y3denom2),s,t)
y3t2=ILTe(-6*Exp(-2*s)/(Y3denom1*Y3denom2),s,t)
y3t=y3t1+y3t2

"1.4"
Y4s=Eq(YF(s),10/(s**3+2*s**2+5*s))
y4t=ILTe(Y4s.rhs,s,t)

"1.5"
Y5numer=4*(s+1)
Y5denom1=(s+2)
Y5denom2=(s+3)
Y5denom3=(s+3)**2
Y5s=Eq(YF(s),Y5numer/(Y5denom1*Y5denom3))

y5t=ILTe(Y5s.rhs,s,t)