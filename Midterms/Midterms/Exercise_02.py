# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:59:27 2024

@author: Lenovo
"""

"""
2.Create your own plane disk perpendicular to the z axis
and cut the upright cone below the origin.Choose your own 
distance value below the origin.Formulate the disk equation."

"""

from amrLib.amrVector import *
from amrLib.amrPlot import *
from Data.variables import *



Fig2=Space3D(title="Figure 2",sz=(8,8)) 

#define the figure

Fig2.ax=axes(projection='3d')

Fig2.Labels("Inverted and Upright Cones with Disk Perpedicular to Z axis")
Fig2.ShowAxes(30)

nbase=10
nheight=25
nTanHalfDelta=nbase/nheight
delta=2*aTan(nTanHalfDelta)
res=100


"The upright cone equation"
#ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify()
ec2 = x**2 + y**2 - (nbase / nheight)**2 * z**2


lnphi = linspace(0,2*npi,res)
lnrho = linspace(0,nbase,res)
lnz1  = linspace(0,-nheight,res)
lnz2  = linspace(0,nheight,res)

ncx=outer(cos(lnphi),lnrho)
ncy=outer(sin(lnphi),lnrho)
ncz=outer(ones(res),lnz1)
Fig2.ax.plot_surface(ncx,ncy,ncz,alpha=.2)
ncz=outer(ones(res),lnz2)
Fig2.ax.plot_surface(ncx,ncy,ncz,alpha=.2)





"Equation of a circular plane perpendicular to upright cone."

cCut=-12 ;"is the height at which the circular disk is cut along the cone's height axis"
nsvcTip=array([0,0,nheight]); "define vectors that determine the orientation of the circular disk'"
nsvcTail=array([0,0,0]);"define vectors that determine the orientation of the circular disk"
nsvc=nsvcTip-nsvcTail;
nloc=array([0,0,cCut]) ;"is the location where the disk is positioned within the cone"

Fig2.PlotVector(nloc,nsvc,color=(1,0,0),base=.5)


"Equation of the Circular Disk"
ndisk=Fig2.GenDisk(nbase*4)
#nrotDisk = Fig3.QuaternionRotate( ndisk, nloc, nsvc)
nmovDisk= Fig2.Move(ndisk,nloc)
Fig2.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.2)

linensvc=Fig2.GenLine(nloc,-nsvc)
Fig2.ax.plot3D(linensvc[0],linensvc[1],linensvc[2],color=(0,0,0),
                linestyle="dashed")

ec3=ec2.subs(z,cCut).evalf()
 
sdy2=solve(ec2,y**2)[0]

unsvc=Fig2.UnitVector(nsvc)
nuAcart=unsvc[0]
nuBcart=unsvc[1]
nuCcart=unsvc[2]
nuKcart=dot(unsvc,nloc)

"This equation represents the intersection of the upright cone and the disk "
plnCart=Eq(nuAcart*x+nuBcart*y+nuCcart*z,nuKcart)



sdy2=solve(ec3,y**2)[0]
sdxroots=list(roots(sdy2).keys())
nix=linspace(float(sdxroots[0]),float(sdxroots[1]),res)
ndz=ones(res)*cCut

ndyp=[];ndyn=[]

for i in range(res):
    ndyp.append( Sqrt(sdy2.subs(x,nix[i])))    
    ndyn.append(-Sqrt(sdy2.subs(x,nix[i])))    

ndyp[0]=0;ndyp[res-1]=0  
ndyn[0]=0;ndyn[res-1]=0  

Fig2.ax.plot3D(nix,ndyp,ndz)
Fig2.ax.plot3D(nix,ndyn,ndz)

savefig("Data/Fig2.png")