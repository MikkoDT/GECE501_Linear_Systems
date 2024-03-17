#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Midterm Exercise #1

3. Formulate the two equations that define the locus of intersection
 points of the upright plane and the disk.
 

"""
#insert libraries
from amrLib.amrVector import *
from amrLib.amrPlot import *
from Data.variables import *


#define the figure
Fig3=Space3D(title="Figure 04",sz=(8,8)) 
Fig3.ax=axes(projection='3d')

Fig3.Labels(" The locus intersection of the upright plane and the disk. ")
Fig3.ShowAxes(30)

#defining the values
nbase=10
nheight=25
nTanHalfDelta=nbase/nheight
delta=2*aTan(nTanHalfDelta)
res=100

#The cone equation
ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify()


lnphi = linspace(0,2*npi,res)
lnrho = linspace(0,nbase,res)
lnz1  = linspace(0,-nheight,res)

ncx=outer(cos(lnphi),lnrho)
ncy=outer(sin(lnphi),lnrho)
ncz=outer(ones(res),lnz1)
Fig3.ax.plot_surface(ncx,ncy,ncz,alpha=.4)

#position of circular disk
nHCut=-12
nsvcTip=array([0,0,nheight])
nrhoCut=(nheight-nHCut)*nTanHalfDelta
nsvcTail=array([nrhoCut,0,nHCut])
nsvc=nsvcTip-nsvcTail
nloc=array([0,0,nHCut])

Fig3.PlotVector(nloc,nsvc,color=(1,0,0),base=.5)
ndisk=Fig3.GenDisk(nbase*4)
nrotDisk = Fig3.QuaternionRotate( ndisk, nloc, nsvc)
nmovDisk= Fig3.Move(nrotDisk,nloc)
Fig3.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.4)


ecx1=Eq(x,base*z/height*Cos(phi))
ecy1=Eq(y,base*z/height*Sin(phi))
ecz1=Eq(z,z)
ec4=Eq(x**2+y**2,(ecx1.rhs**2+ecy1.rhs**2).simplify())
ec5=ec4.subs(base,nbase).subs(height,nheight)
ec6=Eq(rho**2,ec5.rhs)


unsvc=Fig3.UnitVector(nsvc)
nuAcart=unsvc[0]
nuBcart=unsvc[1]
nuCcart=unsvc[2]
nuKcart=dot(unsvc,nloc)
plnCart=Eq(nuAcart*x+nuBcart*y+nuCcart*z,nuKcart)

sdx=solve(plnCart,x)[0]

sdy2=solve(ec5,y**2)[0].subs(x,sdx)
sdzroots=list(roots(sdy2).keys())

niz=linspace(float(sdzroots[0]),float(sdzroots[1]),res)
sdy2.subs(z,niz[0])
sdy2.subs(z,niz[res-1])

ndyn=[];ndyp=[];ndx=[]
for i in range(res):
     ndyn.append(-float(Sqrt(sdy2.subs(z,niz[i]))))        
     ndyp.append( float(Sqrt(sdy2.subs(z,niz[i]))))        
     ndx.append(sdx.subs(z,niz[i]))

Fig3.ax.plot3D(ndx,ndyp,niz)
Fig3.ax.plot3D(ndx,ndyn,niz)


savefig("Data/Fig3.png")             

 
