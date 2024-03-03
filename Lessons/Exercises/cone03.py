#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:23:52 2023

@author: cbco
"""
from ccoLib.ccoVector import *
from ccoLib.ccoPlot import *
from Data.variables import *



fgr03=Space3D(title="Figure 03",sz=(8,8));"Handler for Figure 3" 

#define the figure

fgr03.ax=axes(projection='3d');"Plot axes handler."

fgr03.Labels("The mirrored cones with a plane Cut perpendicular to the height.")
fgr03.ShowAxes(30)


nbase=10
nheight=25
nTanHalfDelta=nbase/nheight
delta=2*aTan(nTanHalfDelta)
res=100


"The cone equation in Cartesian Coordinate System"
ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify()

"The cylindrical axes $\\phi$, $\\rho$, and z data."
lnphi = linspace(0,2*npi,res);"One revolution."
lnrho = linspace(0,nbase,res);"From center to perimeter of the base."
lnz1  = linspace(0,-nheight,res);"Bottom cone from center to negative height."
lnz2  = linspace(0,nheight,res);"Top cone from center to positive height."

ncx=outer(cos(lnphi),lnrho) 
"ncx is a Catersian meshgrid with cylindrical geometric equivalent cos(lnphi) and lnrho." 
ncy=outer(sin(lnphi),lnrho)
"ncy is a Cartesian meshgrid with cylindrical geometric equivalent sin(lnphi) and lnrho."
ncz1=outer(ones(res),lnz1)
"ncz1 is a Catersian meshgrid with cylindrical equivalent z for bottom cone. \
The ones(res) made ncz1 assumed shape=2  "
fgr03.ax.plot_surface(ncx,ncy,ncz1,alpha=.2)
ncz2=outer(ones(res),lnz2)
"ncz2 is a Catersian meshgrid with cylindrical equivalent z for top cone. \
The ones(res) made ncz1 assumed shape=2.  "
fgr03.ax.plot_surface(ncx,ncy,ncz2,alpha=.2)



"Equation of a cylindrical circular plane perpendicular to cone height axis."
eCylDisk=Eq(A*phi+B*rho+C*z,K)

sVecDiskCoeff=Matrix([A,B,C]);
"The [A,B,C] is a vector from origin perpendicular to the disk."
sMagVecDiskCoeff=Sqrt(A**2+B**2+C**2);"Magnitude of [A,B,C] vector"
sUnitVecDiskCoeff=sVecDiskCoeff/sMagVecDiskCoeff;"[A,B,C] unit vector"
sVecDiskxyz=Matrix([x,y,z]);"[x,y,z] is a vector from origin to any point in the \
disk."

e1VecDisk=Eq(Matrix(dot(sVecDiskxyz.transpose(),sVecDiskCoeff)),k,evaluate=False)
"The dot produc of [x,y,z] and [A,B,C] where $\\theta$ is the angle between them."
e2VecDisk=Eq(Matrix(dot(sVecDiskxyz.transpose(),sUnitVecDiskCoeff)),k/sMagVecDiskCoeff,evaluate=False)
"The projection of [x,y,z] on [A,B,C] that gives the shortest distance from origin \
to the disk. The shortest distance is k/Mag([A,B,C])."

"The disk is perpendicular to z axis and located at z=12. Hence the disk \
equation is expressed as follows."
nADisk=0;nBDisk=0;nCDisk=1;nKDisk=12
e1CylDisk=eCylDisk.subs(A,nADisk).subs(B,nBDisk).subs(C,nCDisk).subs(K,nKDisk)

CaCyD[phi]
CaCyD[rho]


nsVecDiskTip=array([0,0,nKDisk]);"Coordinate of the tip of nVecDiskCoeff"
nsVecDiskTail=array([0,0,0]);"Coordinate of the tail of nVecDiskCoeff"
nsVecDisk=nsVecDiskTip-nsVecDiskTail;"[0,0,nKDisk] vector"
nloc=array([0,0,nKDisk]);"Location of the disk."
fgr03.PlotVector(nloc,nsVecDisk,color=(1,0,0),base=.5)


"The plot algorithm is based on the cylindrical equation of disk. "

"Since the disk is a surface plot, the independent variables were chosen as $\\phi$ \
and $\\rho$ as follows. The dependent varialbe is a constant. Hence z=12."

nLphi = linspace(0,2*npi,res);"From zero to one complete revolution"
nLrho = linspace(0,nbase*2,res);"Trom zero to  radius of the disk"
nLz   = ones(res)*nKDisk;"Constant z=12 for all res data."

mCarx=outer(cos(lnphi),nLrho);"Equivalent Cartesian x meshgrid of $\\phi$ and $\\rho$."
mCary=outer(sin(lnphi),nLrho);"Equivalent Cartesian y meshgrid of $\\phi$ and $\\rho$."
mCarz=outer(ones(res),nLz);"Equivalent Cartesian z meshgrid of z."

fgr03.ax.plot_surface(mCarx,mCary,mCarz,alpha=.2)


"Draw dashed line from point [0,0,nKDisk] to point [0,0,-nKDisk]"
linensVecDisk=fgr03.GenLine(nloc,-nsVecDisk)
fgr03.ax.plot3D(linensVecDisk[0],linensVecDisk[1],linensVecDisk[2],color=(0,0,0),
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

ec4=Eq(y**2,27.04-x**2)

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
                

fgr03.ax.plot3D(nlineix,ndyp,nLz)
fgr03.ax.plot3D(nlineix,ndyn,nLz)

savefig("Data/fgr03.png")







fgr04=Space3D(title="Figure 04",sz=(8,8));"Handler of Figure 4" 

fgr04.ax=axes(projection='3d')
fgr04.Labels("The plane cut is at an angle. ")
fgr04.ShowAxes(30)


ncz=outer(ones(res),lnz1);"Lower cone"
fgr04.ax.plot_surface(ncx,ncy,ncz,alpha=.4)
ncz=outer(ones(res),lnz2);"Upper cone"
fgr04.ax.plot_surface(ncx,ncy,ncz,alpha=.4)



nKDisk=12
nsVecTip=array([0,0,nheight])
nsVecTail=array([nbase,0,nKDisk])
nsVec=nsVecTip-nsVecTail
nloc=array([0,0,nKDisk])

fgr04.PlotVector(nloc,nsVec,color=(1,0,0),base=.5)
nDisk=fgr04.GenDisk(nbase*4)
#fgr04.ax.plot_surface(ndisk[0],ndisk[1],ndisk[2],alpha=.2)
nrotDisk = fgr04.QuaternionRotate( nDisk, nloc, nsVec)
#fgr04.ax.plot_surface(nrotDisk[0],nrotDisk[1],nrotDisk[2],alpha=.2)
nmovDisk= fgr04.Move(nrotDisk,nloc)
fgr04.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.2)

linensVec=fgr04.GenLine(nloc,-nsVec*2+nloc)
fgr04.ax.plot3D(linensVec[0],linensVec[1],linensVec[2],color=(0,0,0),
                linestyle="dashed")


e1Cyl=Eq(rho,base*(height-z)/height);"$\\rho$=f(z)"

exc=Eq(x,base*z/height*Cos(phi));"x=f(z,$\\phi$)"
eyc=Eq(y,base*z/height*Sin(phi));"x=f(z,$\\phi$)"
e1ConeCar=Eq(x**2+y**2,(exc.rhs**2+eyc.rhs**2).simplify());"f(x,y)=f(z)"
e2ConeCar=e1ConeCar.subs(base,nbase).subs(height,nheight);
"Cartesian System cone equation"
e3ConeCar=Eq(rho**2,e2ConeCar.rhs);"Cylindrical System cone equation "


unsVec=fgr04.UnitVector(nsVec)
nuAcar=unsVec[0]
nuBcar=unsVec[1]
nuCcar=unsVec[2]
nuKcar=dot(unsVec,nloc)
e1PlaneCar=Eq(nuAcar*x+nuBcar*y+nuCcar*z,nuKcar);"Cartesian system disk equation."

sdxp=solve(e1PlaneCar,x)[0]

 
sdyc2=solve(e2ConeCar,y**2)[0].subs(x,sdxp).expand()
sdzroots=list(roots(sdyc2).keys())

niz=linspace(float(sdzroots[0]),float(sdzroots[1]),res)

ndyn=[];ndyp=[];ndx=[]
for i in range(res):
     tempc=Sqrt(sdyc2.subs(z,niz[i]))
     if tempc.is_real:
         ndyn.append(-float(tempc))        
         ndyp.append( float(tempc))
     else:
         ndyn.append(0)
         ndyp.append(0)
     ndx.append(float(sdxp.subs(z,niz[i])))
     
fgr04.ax.plot3D(ndx,ndyp,niz)
fgr04.ax.plot3D(ndx,ndyn,niz)




savefig("Data/fgr04.png")             

