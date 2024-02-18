#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:23:52 2023

@author: cbco
"""
from ccoLib.ccoVector import *
from ccoLib.ccoPlot import *
from Data.variables import *



fgr02=Space3D(title="Figure 02",sz=(10,10)) 

#define the figure

ax2=      [fgr02.Fig3D.add_subplot(2,2,1,projection="3d")]
ax2.append(fgr02.Fig3D.add_subplot(2,2,2,projection="3d"))
ax2.append(fgr02.Fig3D.add_subplot(2,2,3,projection="3d"))
ax2.append(fgr02.Fig3D.add_subplot(2,2,4,projection="3d"))


nbase=2
nheight=20
res=100


lnphi = linspace(0,2*npi,res)
lnr   = linspace(0,nbase,res)
lnh   = linspace(nheight,0,res)
ncx=outer(cos(lnphi),lnr);shape(ncx)
ncy=outer(sin(lnphi),lnr)
ncz=outer(ones(res),lnh)

"ax2[0]"

fgr02.ax=ax2[0]
fgr02.Labels("(a) A Cone ")
fgr02.ShowAxes(2)
fgr02.ax.plot_surface(ncx,ncy,ncz,alpha=.2)



nA=2;nB=-8;nC=5;nK=25
ep1=Eq(A*x+B*y+C*z,K)
ep2=ep1.subs(A,nA).subs(B,nB).subs(C,nC).subs(K,nK)

"Equation of surface requires one dependent variable and 2 independent variablws "

"Let x and y be the independent variables."

"The values of independent variables are assigned. The values of dependent \
 variables are computed or set as given constant."

plnxL = linspace(-4,4,res);shape(plnxL)
plnyL = linspace(-4,4,res);shape(plnyL)

"The meshgrid of plnxL and plnyL are plnxM and plnyM respectively."
plnxM,plnyM=meshgrid(plnxL,plnyL)

#plnxM=outer(plnxL,plnyL)
#plnyM=plnxM.transpose()

"Solving for z=f(x,y)"

sz=solve(ep2,z)[0]

s1z=str(sz).replace("x","plnxM").replace("y","plnyM")
cmdtxt='plnzM = '+s1z
exec(cmdtxt)

"ax2[1]"

fgr02.ax=ax2[1]
fgr02.Labels("(b) A Plane")
fgr02.ShowAxes(2)
fgr02.ax.plot_surface(plnxM,plnyM,plnzM, alpha=.2)


"ax2[2]"

fgr02.ax=ax2[2]
fgr02.Labels("(c) A Plane intersecting a Cone")
fgr02.ShowAxes(2)
fgr02.ax.plot_surface(plnxM,plnyM,plnzM, alpha=.2)
fgr02.ax.plot_surface(ncx,ncy,ncz,alpha=.2)





"Intersection locus of points"

dvx=solve(ep2,x)[0]
dvy=solve(ep2,y)[0]

ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify() 
ec3=ec2.subs(x,dvx)
ec4=ec2.subs(y,dvy)

"Line y dependent variable equation"
dvy11=solve(ec3,y)[0]
dvy12=solve(ec3,y)[1]

zsq=Eq(dvy11.args[1].args[1]**2,0)
rootzsq=solve(zsq,z)

"Line x dependent variable equation"
dvx11=solve(ec4,x)[0]
dvx12=solve(ec4,x)[1]


"z the independent variable for line x and y equations."
linez = linspace(float(rootzsq[0]),float(rootzsq[1]),res)
linex=[];liney=[]
linex1=[];liney1=[]

for i in range(res):
    linex.append(dvx11.subs(z,linez[i]))    
    liney.append(dvy11.subs(z,linez[i]))    
    linex1.append(dvx12.subs(z,linez[i]))    
    liney1.append(dvy12.subs(z,linez[i]))    

"ax2[3]"
    
fgr02.ax=ax2[3]
fgr02.Labels("(d) The locust of points in an Intersection of \n\
a Cone andg a Plane is an elipse in this case.")
fgr02.ShowAxes(2)
fgr02.ax.plot3D(linex, liney, linez)
fgr02.ax.plot3D(linex1, liney1, linez)
fgr02.ax.plot_surface(plnxM,plnyM,plnzM, alpha=.2)
fgr02.ax.plot_surface(ncx,ncy,ncz,alpha=.2)
savefig("Data/fgr02.png")