#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 19:23:52 2023

@author: cbco
"""

from ccoLib.ccoVector import *
from ccoLib.ccoPlot   import *
from Data.variables   import *

fgr01=Space3D(title="Figure 01",sz=(16,8)) 

#define the figure
#Cn1.Labels(title="Cone Plot in Cartersian System")
#Cn1.ShowAxes(4)
#ax=Cn1.Fig3D.subplots(2,1)
ax1=[fgr01.Fig3D.add_subplot(1,2,1,projection="3d")]
ax1.append(fgr01.Fig3D.add_subplot(1,2,2,projection="3d"))

nbase=2
nheight=8
res=100

ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify()

"Cone plot 1"
cphi=linspace(0,2*npi,res)
cz=linspace(0,nheight,res)
crho=(nheight-cz)/nheight*nbase

cx=nbase*cos(cphi)
cy=nbase*sin(cphi)

z1=solve(ec2,z)[0]

mcx,mcy = meshgrid(cx,cy)
cmdtext="mcz="+str(z1).replace("x","mcx").replace("y","mcy")
exec(cmdtext)
#mcz=2.0-2.0*sqrt(mcx**2+mcy**2)
fgr01.ax=ax1[0]
fgr01.ax.plot_surface(mcx,mcy,mcz, alpha=.3)
fgr01.Labels(title="(a) Cone Equations using Cartesian Meshgrid")
fgr01.ShowAxes(4)


"Cone plot 2"
nphiL = linspace(0,2*npi,res)
nrhoL = linspace(nbase,0,res)
nzL   = linspace(0,nheight,res)

nphiM,nrhoM = meshgrid(nphiL,nrhoL)

XM,YM = nrhoM*cos(nphiM), nrhoM*sin(nphiM)
#ZM =8-4*nrhoM
#ZM=8-4*sqrt(XM**2+YM**2)
cmdtxt="ZM="+str(z1).replace("x","XM").replace("y","YM")
exec(cmdtxt)
fgr01.ax=ax1[1]
fgr01.ax.plot_surface(XM,YM,ZM,alpha=.2)
fgr01.Labels(title="(b) Cone Equations using Polar Meshgrid")
fgr01.ShowAxes(4)

savefig("Data/fgr01.png")


