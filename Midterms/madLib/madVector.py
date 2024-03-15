# -*- coding: utf-8 -*-
"""
Filename: madVector.py

Rev 1 Wed Feb 14 07:00:24 2024
Rev 2 Fri Mar 15 13:25:00 2024

@author: MADT

"""

import os               #See https://www.pitt.edu/~naraehan/python3/file_path_cwd.html
import sympy as sym

import numpy as num

import sys
sys.path.insert(0, '/Python/Library')

from numpy   import linspace, meshgrid, dot, cross, cos, sin, ones,\
                    arccos, arctan, arcsin, array, pi as npi, size, \
                    sqrt, outer, inner, abs, zeros, mat, matrix, exp,\
                    log10, shape    
from sympy   import latex, solve, symbols, pi, Eq, Matrix, Function,\
                    var, Abs, cos as Cos, sin as Sin, atan as aTan, atan2 as aTan2,\
                    sqrt as Sqrt, Le, acos as aCos, Inverse, tan as Tan,\
                    dsolve, I, exp as Exp, Lt, And, Or, Piecewise, Ne, \
                    Integral, Derivative, Float

from sympy.physics.vector import cross as Cross, dot as Dot, ReferenceFrame
from sympy.vector         import CoordSys3D

from sympy.algebras.quaternion import Quaternion

#Coordinate Systems and Transformation
u=CoordSys3D('u')                                     #Cartesian as parent coordinate system 
Sph=u.create_new('u',transformation='spherical')      #Spherical as derived from parent        

SphToCrt=Sph.transformation_to_parent();#print(SphToCrt)   #Spherical to Cartesian transformation           
CrtToSph=Sph.transformation_from_parent();#print(CrtToSph) #Cartesian to Spherical transformation

Cyl=u.create_new('u',transformation='cylindrical')    #Cylindrical as derived from parent
CylToCrt=Cyl.transformation_to_parent();#print(CylToCrt)   #Cylindrical to Cartesian transformation    
CrtToCyl=Cyl.transformation_from_parent();#print(CrtToCyl) #Cartesian to Cylindrical transformation

uref=(u.i,u.j,u.k)        #unit vector reference

v, uv, mv, vx, vy, vz = sym.symbols("V uV |V| V_x V_y V_z")

x, y, z, f, a, b, c, k, r, rho,  phi,  theta,  res, s0   = sym.symbols("\
x  y  z  f  A  B  C  K  R  \\rho \\phi \\theta res, 0                  ")    

v,      pl,      uv,      up,       mv,       mp,        theta  = sym.symbols("\
V_{xyz} P_{lane} uV_{xyz} uP_{lane} |V_{xyz}| |P_{lane}| \\theta               ")



acart, ax, ay, az =symbols('\
\\stackrel{\\rightarrow}{a}_{Cart}  \
\\stackrel{\\rightarrow}{a}_{x}     \
\\stackrel{\\rightarrow}{a}_{y}     \
\\stackrel{\\rightarrow}{a}_{z}') 

A,  Ax,  Ay,  Az,  Arho,     Aphi,     Ar,  Atheta = symbols('\
A   A_x  A_y  A_z  A_{}\\rho A_{\\phi} A_r  A_{theta}')

B,  Bx,  By,  Bz,  Brho,     Bphi,     Br,  Btheta = symbols('\
B   B_x  B_y  B_z  B_{}\\rho B_{\\phi} B_r  B_{theta}')

P, T = symbols('P_{itch} T_{urns}' )


car, ax, ay, az =symbols('\
\\stackrel{\\rightarrow}{a}_{car}  \
\\stackrel{\\rightarrow}{a}_{x}      \
\\stackrel{\\rightarrow}{a}_{y}      \
\\stackrel{\\rightarrow}{a}_{z}') 


cyl, arho, aphi, az =symbols('\
\\stackrel{\\rightarrow}{a}_{cyl}  \
\\stackrel{\\rightarrow}{a}_{\\rho}      \
\\stackrel{\\rightarrow}{a}_{\\phi}      \
\\stackrel{\\rightarrow}{a}_{z}') 


asph, ar, aphi, atheta =symbols('\
\\stackrel{\\rightarrow}{a_{sph}}        \
\\stackrel{\\rightarrow}{a_r}            \
\\stackrel{\\rightarrow}{a_{\\phi}}      \
\\stackrel{\\rightarrow}{a_{\\theta}}') 


fz = Function('Z')
ff = Function('f')
facos=Function('cos^{-1}')
fatan=Function('tan^{-1}')
fasin=Function('sin^{-1}')
fouter = Function('Outer')
fones  = Function('Ones')
fdot   = Function('Dot')
fcross = Function('Cross')



Vcart,  Vcyl,  Vsph = symbols('V_{cart} V_{cyl} V_{sph}')

uVcart, uVcyl, uVsph = symbols('uV_{cart} uV_{cyl} uV_{sph}')


mVcart=Matrix([Ax,Ay,Az]).transpose()
muVcart=Matrix([ax,ay,az])
mVcyl=Matrix([Arho,Aphi,Az]).transpose()
muVcyl=Matrix([arho,aphi,az])
mVsph =Matrix([Ar,Atheta,Aphi]).transpose()
muVsph=Matrix([ar,atheta,aphi])

CaToCy = symbols('C_{art}T_oC_{yl}')                                            
CyToCa = symbols('C_{yl}T_oC_{art}')                                            
mCyToCa = (muVcart*muVcyl.transpose())
mCaToCy = (muVcyl*muVcart.transpose())
CaSph = symbols('C_{art}T_oS_{ph}')                                            
SphCa = symbols('S_{ph}T_oC_{art}')                                            
mSphToCa = (muVcart*muVsph.transpose())
mCaToSph = (muVsph*muVcart.transpose())




CaCyD={}
CaCyD[x]=Cos(phi)*rho
CaCyD[y]=Sin(phi)*rho
CaCyD[z] = z
CaCyD[rho]=Sqrt(x**2+y**2)
CaCyD[phi]=aTan(y/x)
CaCyD[Cos(phi)]=x/Sqrt(x**2+y**2)
CaCyD[Sin(phi)]=y/Sqrt(x**2+y**2)

mCyToCa= Matrix([[Cos(phi),-Sin(phi),0     ],
                 [Sin(phi), Cos(phi),0     ],
                 [0       , 0       ,1     ]] )
m1CyToCa=mCyToCa.subs(Cos(phi),CaCyD[Cos(phi)]).subs(Sin(phi),CaCyD[Sin(phi)])
m1CaToCy=mCyToCa.transpose()

def CartesianToCylindrical(vCart):
    if shape(vCart)!=(3,1):vCart=vCart.transpose()
    vCylCart=vCart.subs(x,CaCyD[x]).subs(y,CaCyD[y]).subs(z,CaCyD[z])
    temp=m1CaToCy*vCylCart
    vCyl=[]
    for i in range(len(temp)):
        vCyl.append(temp[i].expand().simplify())
    vCyl=Matrix(vCyl)               
    return vCyl


def CylindricalToCartesian(vCyl):
    if shape(vCyl)!=(3,1):vCyl=vCyl.transpose()
    vCartCyl=vCyl.subs(phi,CaCyD[phi]).subs(rho,CaCyD[rho]).subs(z,CaCyD[z])
    temp=m1CyToCa*vCartCyl
    vCart=[]
    for i in range(len(temp)):
        vCart.append(temp[i].expand().simplify())
    vCart=Matrix(vCart)               
    
    return vCart

CaSphD={}
CaSphD[x]=r*Sin(theta)*Cos(phi)
CaSphD[y]=r*Sin(theta)*Sin(phi)
CaSphD[z]=r*Cos(theta)
CaSphD[r]=Sqrt(x**2+y**2+z**2)
CaSphD[theta]=aCos(z/Sqrt(x**2+y**2+z**2))
CaSphD[Sin(theta)]=Sqrt(x**2+y**2)/Sqrt(x**2+y**2+z**2)
CaSphD[Cos(theta)]=z/Sqrt(x**2+y**2+z**2)
CaSphD[phi]=aTan(y/x)
CaSphD[Cos(phi)]=x/Sqrt(x**2+y**2)
CaSphD[Sin(phi)]=y/Sqrt(x**2+y**2)

mSphToCa= Matrix([[Sin(theta)*Cos(phi), Cos(theta)*Cos(phi),-Sin(phi)],
                  [Sin(theta)*Sin(phi), Cos(theta)*Sin(phi), Cos(phi)],
                  [Cos(theta)         ,-Sin(theta)           , 0       ]])

m1SphToCa=mSphToCa.subs(Cos(theta),CaSphD[Cos(theta)]).subs(Sin(theta),CaSphD[Sin(theta)])\
              .subs(Cos(phi),CaSphD[Cos(phi)]).subs(Sin(phi),CaSphD[Sin(phi)])
m1CaToSph=mSphToCa.transpose()

def CartesianToSpherical(vCart):
    if shape(vCart)!=(3,1):vCart=vCart.transpose()
    vSphCart=vCart.subs(x,CaSphD[x]).subs(y,CaSphD[y]).subs(z,CaSphD[z])
    temp=m1CaToSph*vSphCart
    vSph=[]
    for i in range(len(temp)):
        vSph.append(temp[i].expand().simplify())
    vSph=Matrix(vSph)               
    return vSph

def SphericalToCartesian(vSph):
    if shape(vSph)!=(3,1):vSph=vSph.transpose()
    vCartSph=vSph.subs(Cos(theta),CaSphD[Cos(theta)]).subs(Sin(theta),CaSphD[Sin(theta)]).\
                  subs(Cos(phi),CaSphD[Cos(phi)]).subs(Sin(phi),CaSphD[Sin(phi)]).\
                  subs(r,CaSphD[r]).subs(phi,CaSphD[phi]).subs(theta,CaSphD[theta])
    temp=m1SphToCa*vCartSph
    vCart=[]
    for i in range(len(temp)):
        vCart.append(temp[i].expand().simplify())
    vCart=Matrix(vCart)               
    return vCart

def Magnitude(v):
    return Sqrt((v[0]**2+v[1]**2+v[2]**2)).evalf()
    
             
def UnitVector(v):
    m=Magnitude(v)
    return array([float(v[0]/m),float(v[1]/m),float(v[2]/m)])

def FloatVector(v):
    return array([float(v[0]),float(v[1]),float(v[2])])
    
    
def DirectionalAngles(v):
    u=UnitVect(v)
    return  [arccos(u[0]),np.arccos(u[1]),np.arccos(u[2])]


def VectorCoefficient(v,sigfig=4):
    vc=[]
    for i in range(3):
        vc.append(Float(v.args[i].args[0],sigfig))
    return vc

def SigFigVector(v,sigfig=4):
    sfv=[]
    for i in range(len(v)):
        sfv.append(Float(v[i],sigfig))
   
    return sfv



    
def GenPlaneEquation(pts):
    x, y, z, A, B, C, K =symbols('x y z A B C K')
    nzpts=[];zpts=[];eq=[]
    for i in range(3):
        if pts[i] != [0,0,0]:nzpts.append(pts[i])
        else:zpts.append(pts[i])
    lnzpts=len(nzpts);lzpts=len(zpts)
    eq1=Eq(A*x+B*y+C*z,K)
    for i in range(3):
        eq.append(eq1.subs(x,pts[i][0]).subs(y,pts[i][1]).subs(z,pts[i][2]))
    if lnzpts == 3:
        eq.append(Eq(K,1))
        soln=solve(tuple(eq),(A,B,C,K))
    elif And(lnzpts == 2, lzpts == 1):
        eq.append(Eq(C,1))
        soln=solve(tuple(eq),(A,B,C,K))
        if soln == []:
            eq[3]=Eq(B,1)
            soln=solve(tuple(eq),(A,B,C,K))
        if soln == []:
            eq[3]=Eq(A,1)
            soln=solve(tuple(eq),(A,B,C,K))
    nA = soln[A]
    nB = soln[B]
    nC = soln[C]    
    nK = soln[K]
    eq2=eq1.subs(A,nA).subs(B,nB).subs(C,nC).subs(K,nK)
    return eq2
   

def GenPlaneCoordinates(eq, w, l ):
    x,y,z = symbols('x y z')
    lx=linspace(-w/2,w/2,10)
    ly=linspace(-l/2,l/2,10)
    soln=solve(eq,z)[0]
    cx=float(soln.coeff(x))
    cy=float(soln.coeff(y))
    c =float(soln.coeff(x,n=0).coeff(y,n=0))
    Xm, Ym = meshgrid(lx,ly)
    Zm=cx*Xm+cy*Ym+c
    return Xm, Ym, Zm


def GenLineEquations(From, To):
    #x, y are the dependent variables
    #z is the independent variables
    x, y, z, mx, bx, my, by = symbols('x y z Mx Bx My By')
    eq1=Eq(x,z*mx+bx)
    eq2=Eq(y,z*my+by)
    eq3=eq1.subs(x,From[0]).subs(z,From[2])
    eq4=eq2.subs(y,From[1]).subs(z,From[2])
    eq5=eq1.subs(x,To[0]).subs(z,To[2])
    eq6=eq2.subs(y,To[1]).subs(z,To[2])
    soln=solve((eq3,eq4,eq5,eq6),(bx, mx, by, my))
    eq1=eq1.subs(bx,soln[bx]).subs(mx,soln[mx])
    eq2=eq2.subs(by,soln[by]).subs(my,soln[my])
    return eq1, eq2


def GenLineCoordinates(eq1,eq2,From,To,res=100):
    z=symbols('z')
    lz=linspace(From[2],To[2],res);lx=[];ly=[]
    for i in range(res):
        lx.append(eq1.rhs.subs(z,lz[i]))
        ly.append(eq2.rhs.subs(z,lz[i]))
    return lx, ly, lz


def GenPathEquations(path):
    x, y, z = symbols('x y z')
    deg=len(path)
    kx=[];ky=[];kz=[];ivx=[];ivy=[];ivz=[]      
         
    for i in range(deg):
        kx.append(var('k_{x'+str(i)+'}'))
        ky.append(var('k_{y'+str(i)+'}'))
        kz.append(var('k_{z'+str(i)+'}'))
        ivx.append(x**i)
        ivy.append(y**i)
        ivz.append(z**i)

    ivX=[];ivY=[];ivZ=[];lx=[];ly=[];lz=[] 
    for i in range(deg):
        ivX.append(list(Matrix(ivx).transpose().subs(x,path[i][0])))    
        ivY.append(list(Matrix(ivy).transpose().subs(y,path[i][1])))    
        ivZ.append(list(Matrix(ivz).transpose().subs(z,path[i][2])))    
        lx.append(path[i][0])
        ly.append(path[i][1])
        lz.append(path[i][2])
   
    mivX=Matrix(ivX)
    mivY=Matrix(ivY)
    mivZ=Matrix(ivZ)
    mlx=Matrix(lx)
    mly=Matrix(ly)
    mlz=Matrix(lz)
    
    eqx=[];eqy=[];eqz=[]
    if mivX.det() !=0:
        nkyx=mivX**-1*mly
        nkzx=mivX**-1*mlz
        eqx.append(Eq(y,(nkyx.transpose()*Matrix(ivx))[0],evaluate=False))
        eqx.append(Eq(z,(nkzx.transpose()*Matrix(ivx))[0],evaluate=False))
    if mivY.det() !=0:
        nkxy=mivY**-1*mlx
        nkzy=mivY**-1*mlz
        eqy.append(Eq(x,(nkxy.transpose()*Matrix(ivy))[0],evaluate=False))
        eqy.append(Eq(z,(nkzy.transpose()*Matrix(ivy))[0],evaluate=False))
    if mivZ.det() !=0:
        nkxz=mivZ**-1*mlx
        nkyz=mivZ**-1*mly
        eqz.append(Eq(x,(nkxz.transpose()*Matrix(ivz))[0],evaluate=False))
        eqz.append(Eq(y,(nkyz.transpose()*Matrix(ivz))[0],evaluate=False))

    return eqx,eqy,eqz



def GenPathCoordinates(eq, From, To, iv='z', res=100):
    x,y,z = symbols('x y z')
    if iv == 'z':
        lz=linspace(float(From[2]),float(To[2]),res)
        lx=[]
        ly=[]
        for i in lz:
            lx.append(eq[0].rhs.subs(z,i))
            ly.append(eq[1].rhs.subs(z,i))
    
    if iv == 'y':
        ly=linspace(float(From[1]),float(To[1]),res)
        lz=[]
        lx=[]
        for i in ly:
            lx.append(eq[0].rhs.subs(y,i))
            lz.append(eq[1].rhs.subs(y,i))
    
    if iv == 'x':
        lx=linspace(float(From[0]),float(To[0]),res)
        ly=[]
        lz=[]
        for i in lx:
            ly.append(eq[0].rhs.subs(x,i))
            lz.append(eq[1].rhs.subs(x,i))
    
    return lx,ly,lz


def QuaternionMultiply(a,b):
    sa=a[0];sb=b[0];va=array(a[1]);vb=array(b[1]) 
    return [sa*sb-dot(va,vb),sa*vb+sb*va+cross(va,vb)]

def QuaternionRotate(self, obj, From, To, res=100):
    lnshp=len(shape(obj)) #lnshp=3 for surface, 2 for curve line, 1 for vector
    x=obj[0];y=obj[1];z=obj[2]
    uFrom=self.UnitVector(From)
    #Generate quaternion rotation coordinates for cone
    uTo=self.UnitVector(To)
    if uFrom[0]==uTo[0] and uFrom[1]==uTo[1] and uFrom[2]==uTo[2]:
        return obj
    cosTheta=float(dot(uFrom,uTo))
    theta=arccos(cosTheta)
    norm=cross(uFrom,uTo)
    unorm=self.UnitVector(norm)
    xh=[];yh=[];zh=[]
    Qn=[cos(theta/2),sin(theta/2)*unorm]    # Quaternion for unorm
    Qnc=[cos(theta/2),sin(theta/2)*-unorm]  # Complement Quaternion of unorm 
  
    if lnshp == 3:
        for i in range(res):
            x1=[];y1=[];z1=[]
            for j in range(res):
                Qv=[0,array([x[i][j],y[i][j],z[i][j]])] #vector for rotation
                QvQnc=self.QuaternionMultiply(Qv,Qnc)       
                QnQvQnc=self.QuaternionMultiply(Qn,QvQnc)
                x1.append(QnQvQnc[1][0])
                y1.append(QnQvQnc[1][1])
                z1.append(QnQvQnc[1][2])
            xh.append(x1)
            yh.append(y1)
            zh.append(z1)
    #Generate coordinates for placement of cone on vector tip  
        xh=np.array(xh)
        yh=np.array(yh)
        zh=np.array(zh)
        return [xh,yh,zh]
    elif lnshp == 2:
        for i in range(res):
            Qv=[0,array([x[i],y[i],z[i]])] #vector for rotation
            QvQnc=self.QuaternionMultiply(Qv,Qnc)       
            QnQvQnc=self.QuaternionMultiply(Qn,QvQnc)
            xh.append(QnQvQnc[1][0])
            yh.append(QnQvQnc[1][1])
            zh.append(QnQvQnc[1][2])
        xh=np.array(xh)
        yh=np.array(yh)
        zh=np.array(zh)
        return [xh,yh,zh]
    elif lnshp == 1:
        Qv=[0,array([x,y,z])] #vector for rotation
        QvQnc=self.QuaternionMultiply(Qv,Qnc)       
        QnQvQnc=self.QuaternionMultiply(Qn,QvQnc)
        xh=QnQvQnc[1][0]
        yh=QnQvQnc[1][1]
        zh=QnQvQnc[1][2]
        return array([xh,yh,zh])
    else:
        return "The object is not a vector nor a line nor surface."
        
    def Move(self,Surface, To):
        x=Surface[0]+To[0]
        y=Surface[1]+To[1]
        z=Surface[2]+To[2]
        return [x,y,z]


def RotateVector(v,From,To):
    uFrom=UnitVector(From)
    #Generate quaternion rotation coordinates for cone
    uTo=UnitVector(To)
    if uFrom[0]==uTo[0] and uFrom[1]==uTo[1] and uFrom[2]==uTo[2]:return v
    cosTheta=float(dot(uFrom,uTo))
    theta=arccos(cosTheta)
    norm=cross(uFrom,uTo)
    unorm=UnitVector(norm)
    Qn =[cos(theta/2),sin(theta/2)* unorm]    # Quaternion for unorm
    Qnc=[cos(theta/2),sin(theta/2)*-unorm]    # Complement Quaternion of unorm 
    Qv=[0,array([v[0],v[1],v[2]])] #vector for rotation
    QvQnc=QuaternionMultiply(Qv,Qnc)       
    QnQvQnc=QuaternionMultiply(Qn,QvQnc)
    return QnQvQnc[1]


def RotateVectorAbout(v, axis, angle):
    uaxis=UnitVector(axis)
    Qn =[cos(angle/2),sin(angle/2)* uaxis]    # Quaternion for unorm
    Qnc=[cos(angle/2),sin(angle/2)*-uaxis]    # Complement Quaternion of unorm 
    Qv=[0,array([v[0],v[1],v[2]])] #vector for rotation
    QvQnc=QuaternionMultiply(Qv,Qnc)       
    QnQvQnc=QuaternionMultiply(Qn,QvQnc)
    return QnQvQnc[1]


def RotatePath(path, From, To,res=100):
    x=path[0];y=path[1];z=path[2]
    uFrom=UnitVector(From)
    #Generate quaternion rotation coordinates for cone
    uTo=UnitVector(To)
    if uFrom[0]==uTo[0] and uFrom[1]==uTo[1] and uFrom[2]==uTo[2]:
        return arc
    cosTheta=float(dot(uFrom,uTo))
    theta=arccos(cosTheta)
    norm=cross(uFrom,uTo)
   
    unorm=UnitVector(norm)
    xh=[];yh=[];zh=[]
    Qn =[cos(theta/2),sin(theta/2)* unorm]    # Quaternion for unorm
    Qnc=[cos(theta/2),sin(theta/2)*-unorm]    # Complement Quaternion of unorm 

    x1=[];y1=[];z1=[]
    for j in range(res):
        Qv=[0,array([x[j],y[j],z[j]])] #vector for rotation
        QvQnc=QuaternionMultiply(Qv,Qnc)       
        QnQvQnc=QuaternionMultiply(Qn,QvQnc)
        x1.append(QnQvQnc[1][0])
        y1.append(QnQvQnc[1][1])
        z1.append(QnQvQnc[1][2])
    

    return [x1,y1,z1]

def GenArc(at, From, To, Length,res=100):
    uFrom=UnitVector(From)
    uTo=UnitVector(To)
    theta=arccos(dot(uFrom,uTo))
    ltheta=linspace(0,theta,res)
    nu=UnitVector(cross(uFrom,uTo))
    arc=[]
    for i in range(res):
        arc.append((cos(ltheta[i])*uFrom+sin(ltheta[i])*cross(nu,uFrom))*Length)
    
    arcx=[];arcy=[];arcz=[]
    for i in range(res):
        arcx.append(arc[i][0])                 
        arcy.append(arc[i][1])              
        arcz.append(arc[i][2])
    x=list(array(arcx)+array(at[0]))
    y=list(array(arcy)+array(at[1]))
    z=list(array(arcz)+array(at[2]))

    return x, y ,z

#Test
'''
mBcart = Matrix([y,-x,z])
mBcyl = CartesianToCylindrical(mBcart);print(mBcyl)
m1Bcart= CylindricalToCartesian(mBcyl);print(m1Bcart)

print('mBcart = m1Bcart',Eq(mBcart,m1Bcart))

mGcart = Matrix([x*z/y,0,0]);print(mGcart)
vSph = CartesianToSpherical(mGcart);print(vSph)  
vCart = SphericalToCartesian(vSph);print(vCart)

print('mGcart = vCart', Eq(mGcart,vCart))
'''                           
