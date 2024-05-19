#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Midterm Exercise #1

3. Formulate the two equations that define the locus of intersection
 points of the upright plane and the disk.
 

"""
#insert libraries
from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *


#define the figure
Fig3=Space3D(title="Figure 03",sz=(8,8));"Disk cut on upright cone."
Fig3.ax=axes(projection='3d');"Plot axes handler."

Fig3.Labels("The upright cone with a disk cutting across upright cone")
Fig3.ShowAxes(30)

"Values of the Cone"
Base=15
Height=25
nTanHalfDelta=Base/Height
delta=2*aTan(nTanHalfDelta)
res=100


"The cone equation in Cartesian Coordinate System"
ec2=ec1.subs(u,z).subs(base,Base).subs(height,Height).simplify()

"The cylindrical axes ."
lnphi = linspace(0,2*npi,res);"One revolution."
lnrho = linspace(0,Base,res);"From center to perimeter of the base."
lnz1  = linspace(0,-Height,res);"Bottom cone from center to negative height."


ncx=outer(cos(lnphi),lnrho); "Catersian meshgrid with cylindrical geometric equivalent cos(lnphi) and lnrho." 
ncy=outer(sin(lnphi),lnrho); "Cartesian meshgrid with cylindrical geometric equivalent sin(lnphi) and lnrho."
ncz1=outer(ones(res),lnz1);  "ncz1 is a Catersian meshgrid with cylindrical equivalent z for bottom cone."

"Plotting of the  cone "
Fig3.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig3.ax.plot_surface(ncx,ncy,ncz1,color=(0,1,0),alpha=.2)


"Plotting of the  cone "
Fig3.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig3.ax.plot_surface(ncx,ncy,ncz1,color=(0,1,0),alpha=.2)


"Equation of a cylindrical circular plane perpendicular to cone height axis."
cDisk=Eq(A*phi+B*rho+C*z,K)
vDiskCoeff=Matrix([A,B,C]);"The [A,B,C] is a vector from origin perpendicular to the disk."

mVecDiskCoeff=Sqrt(A**2+B**2+C**2);"Magnitude of [A,B,C] vector"
uVecDiskCoeff=vDiskCoeff/mVecDiskCoeff;"[A,B,C] unit vector"
Diskxyz=Matrix([x,y,z]);"[x,y,z] is a vector from origin to any point in the disk."

e1VecDisk=Eq(Matrix(dot(Diskxyz.transpose(),vDiskCoeff)),k,evaluate=False);"The dot produc of [x,y,z] and [A,B,C] where $\\theta$ is the angle between them."
e2VecDisk=Eq(Matrix(dot(Diskxyz.transpose(),uVecDiskCoeff)),k/mVecDiskCoeff,evaluate=False);"The projection of [x,y,z] on [A,B,C] that gives the shortest distance from origin \
to the disk. The shortest distance is k/Mag([A,B,C])."

"The disk is perpendicular to z axis and located at z=-12. Hence the disk \
equation is expressed as follows."
nADisk=0;nBDisk=0;nCDisk=1;nKDisk=-12


e1CylDisk=cDisk.subs(A,nADisk).subs(B,nBDisk).subs(C,nCDisk).subs(K,nKDisk)

CaCyD[phi]
CaCyD[rho]


sVecDiskTip=array([0,0,0]);"Coordinate of the tip of nVecDiskCoeff"
sVecDiskTail=array([0,0,nKDisk]);"Coordinate of the tail of nVecDiskCoeff"
sVecDisk=sVecDiskTip-sVecDiskTail;"[0,0,nKDisk] vector"
nloc=array([0,0,nKDisk]);"Location of the disk."
Fig3.PlotVector(nloc,sVecDisk,color=(1,0,0),base=.5)


"The plot algorithm is based on the cylindrical equation of disk. "

"Since the disk is a surface plot, the independent variables were chosen as $\\phi$ \
and $\\rho$ as follows. The dependent varialbe is a constant. Hence z=-12."

nLphi = linspace(0,2*npi,res);"From zero to one complete revolution"
nLrho = linspace(0,Base*2,res);"Trom zero to  radius of the disk"
nLz   = ones(res)*nKDisk;"Constant z=12 for all res data."

mCarx=outer(cos(lnphi),nLrho);"Equivalent Cartesian x meshgrid of $\\phi$ and $\\rho$."
mCary=outer(sin(lnphi),nLrho);"Equivalent Cartesian y meshgrid of $\\phi$ and $\\rho$."
mCarz=outer(ones(res),nLz);"Equivalent Cartesian z meshgrid of z."



Fig3.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig3.PlotVector(nloc,sVecDisk,color=(1,0,0),base=.5)
Fig3.ax.plot_surface(mCarx,mCary,mCarz,alpha=.2)

linensVecDisk=Fig3.GenLine(nloc,-sVecDisk)
Fig3.ax.plot3D(linensVecDisk[0],linensVecDisk[1],linensVecDisk[1],color=(0,0,0),
                linestyle="dashed")


"The equation of disk in Cartesian coordinate system."
eCarDisk=Eq(z,nKDisk);"zd=K"

"The equation of cone in Cartesian Coordinate system."
ec2;"f(xc,yc)=f(zc)"

"Substituting zd=k in f(xc,yc)=f(zc), then f(xc,yc) = f(zd) "
ec3=ec2.subs(z,nKDisk).evalf();"ec3 became f(xc,yc)=f(K)"
"The value of z is constant and is equal to 12. Being a constant it is considred \
dependent variable. Let's consider x as independent variable and y the dependent \
variable. The range of values for x is determined as follows."

sdy2=solve(ec3,y**2)[0]

ec4=Eq(y**2,sdy2)

sdxroots=list(roots(ec4.rhs).keys())

nlineix=linspace(float(sdxroots[0]),float(sdxroots[1]),res)
"x is the independent variable."

ndyp=[];ndyn=[]
"y is the dependent variable."

for i in range(res):
    temp=Sqrt(sdy2.subs(x,nlineix[i]))
    if temp.is_real:
        ndyp.append(temp)    
        ndyn.append(-temp)
    else:
        ndyp.append(0)    
        ndyn.append(0)
                

Fig3.ax.plot3D(nlineix,ndyp,nLz)
Fig3.ax.plot3D(nlineix,ndyn,nLz)

savefig("Data/Fig3.png")