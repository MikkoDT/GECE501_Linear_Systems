# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:48:07 2024

@author: MADT
"""

from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *



Fig1=Space3D(title="Figure 1",sz=(8,8)) 

#define the figure

Fig1.ax=axes(projection='3d')

Fig1.Labels("Inverted and Upright Cones")
Fig1.ShowAxes(30)

"Given value for cone equations"
abase=30
aheight=30
aTanHalfDelta=abase/aheight
delta=2*aTan(aTanHalfDelta)
res=100


"The cone equation"
ec2=ec1.subs(u,z).subs(base,abase).subs(height,aheight).simplify()

"Plotting the cone"
lnphi = linspace(0,2*npi,res)
lnrho = linspace(0,abase,res)
lnz1  = linspace(0,-aheight,res)
lnz2  = linspace(0,aheight,res)

ncx=outer(cos(lnphi),lnrho)
ncy=outer(sin(lnphi),lnrho)
ncz=outer(ones(res),lnz1)
Fig1.ax.plot_surface(ncx,ncy,ncz,alpha=.2)
ncz=outer(ones(res),lnz2)
Fig1.ax.plot_surface(ncx,ncy,ncz,alpha=.2)



savefig("Data/Fig1.png")