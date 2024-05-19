# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:48:07 2024

@author: MADT
"""

from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *


#define the figure
Fig1=Space3D(title="Figure 1",sz=(8,8)) 
Fig1.ax=axes(projection='3d')
Fig1.Labels("Inverted and Upright Cones")
Fig1.ShowAxes(30)

"Values for Cone Equations"
Base=10
Height=50
TanHalfDelta=Base/Height
delta=2*Tan(TanHalfDelta)
res=100

"The cone equation in the Cartesian Coordinates"
ec2=ec1.subs(u,z).subs(base,Base).subs(height,Base).simplify()
"Plotting the Cone"

phi = linspace(0,2*npi,res);"1 revolution"
rho = linspace(0,Base,res);"From center to perimeter of the base."
z1  = linspace(0,-Height,res);"The bottom cone from center to negative height."
z2  = linspace(0,Height,res);"The top cone from center to positive height."

cx=outer(cos(phi),rho);"Cartesian Meshgrid of geometic equivalent equal to cosine phi and rho"
cy=outer(sin(phi),rho);"Cartesian Meshgrid of geometric equivalent equal to sine phi and rho"
cz=outer(ones(res),z1);"Cartesian Meshgrid of bottom cyclindral equal to z"

#Plotting of Figure in 3D space model
Fig1.ax.plot_surface(cx,cy,cz,color = (0,0,1),alpha=.2)
cz=outer(ones(res),z2)
Fig1.ax.plot_surface(cx,cy,cz,color = (1,0,0),alpha=.2)


#Saving the Figure
savefig("Data/Fig1.png")