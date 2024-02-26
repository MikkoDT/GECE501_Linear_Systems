#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:23:52 2023

@author: cbco
"""
from ccoLib.ccoVector import *
from ccoLib.ccoPlot import *
from Data.variables import *



fgr05=Space3D(title="Figure 05",sz=(8,8)) 

#define the figure

fgr05.ax=axes(projection='3d')

fgr05.Labels("The a plane Cut parallel to the lateral surface \
generated a parabola.")
fgr05.ShowAxes(50)


nbase=10
nheight=40
nTanHalfDelta=nbase/nheight
delta=2*aTan(nTanHalfDelta)
res=100


"The cone equation"
ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify()


lnphi = linspace(0,2*npi,res)
lnrho = linspace(0,nbase,res)
lnz1  = linspace(0,-nheight,res)
lnz2  = linspace(0,nheight,res)

ncx=outer(cos(lnphi),lnrho)
ncy=outer(sin(lnphi),lnrho)
ncz=outer(ones(res),lnz1)
fgr05.ax.plot_surface(ncx,ncy,ncz,alpha=.2)
ncz=outer(ones(res),lnz2)
fgr05.ax.plot_surface(ncx,ncy,ncz,alpha=.2)





"Equation of a circular plane perpendicular to cone height axis."

nHCut=12
nsvcTip=array([0,-nheight, 0])
nsvcTail=array([0, 0, nbase])
nsvc=nsvcTip-nsvcTail
nloc=array([0,5,nHCut])

fgr05.PlotVector(nloc,nsvc,color=(1,0,0),base=.5)

ndisk=fgr05.GenDisk(nbase*4)
nrotdisk = fgr05.QuaternionRotate( ndisk, array([0,0,1]), nsvc)
nmovdisk= fgr05.Move(nrotdisk,nloc)
fgr05.ax.plot_surface(nmovdisk[0],nmovdisk[1],nmovdisk[2],color=(0,1,1),alpha=.2)

linensvc=fgr05.GenLine(nloc,-nsvc)
fgr05.ax.plot3D(linensvc[0],linensvc[1],linensvc[2],color=(0,0,0),
                linestyle="dashed")



unsvc=fgr05.UnitVector(nsvc)
nuAcart=unsvc[0]
nuBcart=unsvc[1]
nuCcart=unsvc[2]
nuKcart=dot(unsvc,nloc)
plnCart=Eq(nuAcart*x+nuBcart*y+nuCcart*z,nuKcart)

plndistorg=unsvc*nuKcart #plane distance to origin
fgr05.PlotVector([0,0,0], plndistorg,color=(0,0,1), base=1)

sdy=solve(plnCart,y)[0]


ec4=Eq(x**2+y**2,base**2*z**2/height**2)
ec5=ec4.subs(base,nbase).subs(height,nheight)

sdy=solve(plnCart,y)[0]
ec6=Eq(x**2,-(sdy**2).expand()+ec5.rhs)

sdx2=ec6.rhs
sdx2roots=float(list(roots(sdx2).keys())[0])

niz=linspace(sdx2roots,nheight,res)


ndy=[];ndxp=[];ndxn=[]

for i in range(res):
    ndy.append(sdy.subs(z,niz[i]))  
    ndxp.append(Sqrt(sdx2.subs(z,niz[i])))
    ndxn.append(-ndxp[i])




fgr05.ax.plot(ndxp,ndy,niz)
fgr05.ax.plot(ndxn,ndy,niz)



savefig("Data/fgr05.png")

