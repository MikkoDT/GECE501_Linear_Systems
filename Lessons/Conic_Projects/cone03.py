#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:23:52 2023

@author: cbco
"""
from ccoLib.ccoVector import *
from ccoLib.ccoPlot import *
from Data.variables import *



fgr03=Space3D(title="Figure 03",sz=(8,8)) 

#define the figure

fgr03.ax=axes(projection='3d')

fgr03.Labels("The mirrored cones with a plane Cut perpendicular to the height.")
fgr03.ShowAxes(30)


nbase=10
nheight=25
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
fgr03.ax.plot_surface(ncx,ncy,ncz,alpha=.2)
ncz=outer(ones(res),lnz2)
fgr03.ax.plot_surface(ncx,ncy,ncz,alpha=.2)





"Equation of a circular plane perpendicular to cone height axis."

nHCut=12
nsvcTip=array([0,0,nheight])
nsvcTail=array([0,0,0])
nsvc=nsvcTip-nsvcTail
nloc=array([0,0,nHCut])

fgr03.PlotVector(nloc,nsvc,color=(1,0,0),base=.5)

ndisk=fgr03.GenDisk(nbase*4)
#nrotDisk = fgr03.QuaternionRotate( ndisk, nloc, nsvc)
nmovDisk= fgr03.Move(ndisk,nloc)
fgr03.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.2)

linensvc=fgr03.GenLine(nloc,-nsvc)
fgr03.ax.plot3D(linensvc[0],linensvc[1],linensvc[2],color=(0,0,0),
                linestyle="dashed")

ec3=ec2.subs(z,nHCut).evalf()
 
sdy2=solve(ec2,y**2)[0]

unsvc=fgr03.UnitVector(nsvc)
nuAcart=unsvc[0]
nuBcart=unsvc[1]
nuCcart=unsvc[2]
nuKcart=dot(unsvc,nloc)
plnCart=Eq(nuAcart*x+nuBcart*y+nuCcart*z,nuKcart)



sdy2=solve(ec3,y**2)[0]
sdxroots=list(roots(sdy2).keys())
nix=linspace(float(sdxroots[0]),float(sdxroots[1]),res)
ndz=ones(res)*nHCut

ndyp=[];ndyn=[]

for i in range(res):
    ndyp.append( Sqrt(sdy2.subs(x,nix[i])))    
    ndyn.append(-Sqrt(sdy2.subs(x,nix[i])))    

ndyp[0]=0;ndyp[res-1]=0  
ndyn[0]=0;ndyn[res-1]=0  

fgr03.ax.plot3D(nix,ndyp,ndz)
fgr03.ax.plot3D(nix,ndyn,ndz)




savefig("Data/fgr03.png")











fgr04=Space3D(title="Figure 04",sz=(8,8)) 

#define the figure

fgr04.ax=axes(projection='3d')

fgr04.Labels("The plane cut is at an angle. ")
fgr04.ShowAxes(30)



ncz=outer(ones(res),lnz1)
fgr04.ax.plot_surface(ncx,ncy,ncz,alpha=.4)
ncz=outer(ones(res),lnz2)
fgr04.ax.plot_surface(ncx,ncy,ncz,alpha=.4)



nHCut=12
nsvcTip=array([0,0,nheight])
nrhoCut=(nheight-nHCut)*nTanHalfDelta
nsvcTail=array([nrhoCut,0,nHCut])
nsvc=nsvcTip-nsvcTail
nloc=array([0,0,nHCut])

fgr04.PlotVector(nloc,nsvc,color=(1,0,0),base=.5)
ndisk=fgr04.GenDisk(nbase*4)
nrotDisk = fgr04.QuaternionRotate( ndisk, nloc, nsvc)
nmovDisk= fgr04.Move(nrotDisk,nloc)
fgr04.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.2)
linensvc=fgr04.GenLine(nloc,-nsvc*2)
fgr04.ax.plot3D(linensvc[0],linensvc[1],linensvc[2],color=(0,0,0),
                linestyle="dashed")




ecx1=Eq(x,base*z/height*Cos(phi))
ecy1=Eq(y,base*z/height*Sin(phi))
ecz1=Eq(z,z)
ec4=Eq(x**2+y**2,(ecx1.rhs**2+ecy1.rhs**2).simplify())
ec5=ec4.subs(base,nbase).subs(height,nheight)
ec6=Eq(rho**2,ec5.rhs)


unsvc=fgr04.UnitVector(nsvc)
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

fgr04.ax.plot3D(ndx,ndyp,niz)
fgr04.ax.plot3D(ndx,ndyn,niz)




savefig("Data/fgr04.png")             

