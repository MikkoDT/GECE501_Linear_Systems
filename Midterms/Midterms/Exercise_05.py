# -*- coding: utf-8 -*-
"""
Midterm Exercise #1
 
5. What is the range  of a tilt such that the intersection from a parabolic 
curve lines.
Created on Sat Mar  9 23:22:04 2024

@author: MADT
"""
from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *



fig5=Space3D(title="Figure 05",sz=(8,8)) 

#define the figure

fig5.ax=axes(projection='3d')

fig5.Labels("The a plane Cut parallel to the lateral surface \
generated a parabola.")
fig5.ShowAxes(50)


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
#ncz=outer(ones(res),lnz1)
#fig5.ax.plot_surface(ncx,ncy,ncz,alpha=.2)
ncz=outer(ones(res),lnz2)
fig5.ax.plot_surface(ncx,ncy,ncz,alpha=.2)





"Equation of a circular plane perpendicular to cone height axis."

nHCut=12
nsvcTip=array([0,-nheight, 0])
nsvcTail=array([0, 0, nbase])
nsvc=nsvcTail-nsvcTip
nloc=array([0,5,nHCut])

fig5.PlotVector(nloc,nsvc,color=(1,0,0),base=.5)

ndisk=fig5.GenDisk(nbase*4)
nrotdisk = fig5.QuaternionRotate( ndisk, array([0,0,1]), nsvc)
nmovdisk= fig5.Move(nrotdisk,nloc)
fig5.ax.plot_surface(nmovdisk[0],nmovdisk[1],nmovdisk[2],color=(0,1,1),alpha=.2)

linensvc=fig5.GenLine(nloc,-nsvc*2+nloc)
fig5.ax.plot3D(linensvc[0],linensvc[1],linensvc[2],color=(0,0,0),
                linestyle="dashed")



unsvc=fig5.UnitVector(nsvc)
nuAcart=unsvc[0]
nuBcart=unsvc[1]
nuCcart=unsvc[2]
nuKcart=dot(unsvc,nloc)
plnCart=Eq(nuAcart*x+nuBcart*y+nuCcart*z,nuKcart)

plndistorg=unsvc*nuKcart #plane distance to origin
fig5.PlotVector([0,0,0], plndistorg,color=(0,0,1), base=1)

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




fig5.ax.plot(ndxp,ndy,niz)
fig5.ax.plot(ndxn,ndy,niz)



savefig("Data/fig5.png")

