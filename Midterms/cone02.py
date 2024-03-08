#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: conio02.py
Created on Thu Nov  9 19:23:52 2023

@author: cbco
"""
from ccoLib.ccoVector import *
from ccoLib.ccoPlot import *
from Data.variables import *



fgr02=Space3D(title="Figure 02",sz=(10,10)) 

#define the figure

"ax2 is a list of subfigure handlers of fgr02."

ax2=      [fgr02.Fig3D.add_subplot(2,2,1,projection="3d")];"handler of (a)"
ax2.append(fgr02.Fig3D.add_subplot(2,2,2,projection="3d"));"handler of (b)"
ax2.append(fgr02.Fig3D.add_subplot(2,2,3,projection="3d"));"handler of (c)"
ax2.append(fgr02.Fig3D.add_subplot(2,2,4,projection="3d"));"handler of (d)"

srho=base*(height-z)/height
eConeCyl=Eq(rho,srho)
szCyl=solve(eConeCyl,z)[0]

nbase=2;"The radius of the base of the cone." 
nheight=20;"The height of the cone."
res=100;"The resolution of a plot or number of data in a variable list."


nlphi = linspace(0,2*npi,res);"One complete revolution of phi"
nlrh0   = linspace(0,nbase,res);"res points of rho from center to the perimeter \
of base of cone"
nlz   = linspace(nheight,0,res);"res points of z from bottom of cone to its tip"
"The prefix nl means numerical list."
mcx=outer(cos(nlphi),nlrh0);"Direct conversion of cylindrical mesgrid phi and \
rho to x Cartesian meshgrid."
mcy=outer(sin(nlphi),nlrh0);"Direct conversion of cylindrical mesgrid phi and \
rho to y Cartesian meshgrid."
mcz=outer(ones(res),nlz);"Direct conversion of cylindrical mesgrid z to z \
Cartesian meshgrid."


fgr02.ax=ax2[0];"Set (a) subfigure."
fgr02.Labels("(a) A Cone ")
fgr02.ShowAxes(2)
fgr02.ax.plot_surface(mcx,mcy,mcz,alpha=.2);"The cone surface plot."


nA=2;nB=-8;nC=5;nK=25;"Constant coefficients of plane equation"
ep1=Eq(A*x+B*y+C*z,K);"Plane symbolic math equation"
ep2=ep1.subs(A,nA).subs(B,nB).subs(C,nC).subs(K,nK);"Plane equation with numerical \
coefficients"

"Equation of surface requires one dependent variable and 2 independent variablws "
"Let x and y be the independent variables."

"The values of independent variables are assigned. The values of dependent \
 variables are computed or set as given constant."

plnxL = linspace(-4,4,res);shape(plnxL);"x independent variable data list"
plnyL = linspace(-4,4,res);shape(plnyL);"y independent variable data list"

"The meshgrid of plnxL and plnyL are plnxM and plnyM respectively."
plnxM,plnyM=meshgrid(plnxL,plnyL);"x and y independent mesh variable data list"

#plnxM=outer(plnxL,plnyL)
#plnyM=plnxM.transpose()

"Solving for z=f(x,y)"

sz=solve(ep2,z)[0];"z solution from plane equation ep2"

s1z=str(sz).replace("x","plnxM").replace("y","plnyM")
"z solution with x and y meshgrid variable data list"
cmdtxt='plnzM = '+s1z;"command text to create z meshgrid."
exec(cmdtxt)

"ax2[1]"

fgr02.ax=ax2[1];"set handler for (b) subfigure"
fgr02.Labels("(b) A Plane")
fgr02.ShowAxes(2)
fgr02.ax.plot_surface(plnxM,plnyM,plnzM, alpha=.2)



"ax2[2]"

fgr02.ax=ax2[2];"set handler for (c) subfigure."
fgr02.Labels("(c) A Plane intersecting a Cone")
fgr02.ShowAxes(2)
fgr02.ax.plot_surface(plnxM,plnyM,plnzM, alpha=.2);"Plot of the cone"
fgr02.ax.plot_surface(mcx,mcy,mcz,alpha=.2);"Plot of the plane"




"The surface equations are expressed as z = f(x,y) or x=f(z,y) or y=f(x,z). \
The rhs has the independent variables. The lhs has the dependent variable. \
Consider the surface plots of a cone and a plane with z as the dependent \
variable and x and y as the independent variables. Thus,"

ezc=Eq(zc,fF(xc,yc)); "cone equation"
ezp=Eq(zp,fF(xp,yp)); "plane equation"


"A line in 3D space where the cone and the plane intersected could be drawn \
and plotted. The locus of points must be the common points of the cone and the \
plane. Hence, x=xc=xp; y=yc=yp; and z=zc=zp"

"The equations of the cone with xc a dependent variable and yc and zc as \
independent vatiable is expressed as follows."

exc=Eq(xc,fF(yc,zc))

"The equations of the plane with yp a dependent variable and xp and zp as \
independent vatiable is expressed as follows."
eyp=Eq(yp,fF(xp,zp))

"Substituting yp in yc,"

e1xc=Eq(xc,fF(fF(xp,zp),zc))

"Since the locus of points of intersection must be the seame for both cone \
and plane, thus, "

ex=Eq(x,fF(fF(x,z),z))

"Solving for x,"

e1x=Eq(x,fF(z))

"In like process,"

e1y=Eq(y,fF(z))


"Given a set of values of z, the x and y are computed. The values of x, y, \
and z forms the locus of points common to both the cone and plane."


"""
object      no of equations  no of dependent variables no of independent variables
surface     1                1                         2
line        2                2                         1           
point       0                0                         3      

"""





"Intersection locus of points"

dvx=solve(ep2,x)[0]; "xc =  f(yc,zc)"
dvy=solve(ep2,y)[0]; "yc =  f(xc,zc)"

ec2=ec1.subs(u,z).subs(base,nbase).subs(height,nheight).simplify(); "f(xc,yc)=f(zc)" 
ec3=ec2.subs(x,dvx); "f(yc)=f(zc)"
ec4=ec2.subs(y,dvy); "f(xc)=f(zc)"

"Line y dependent variable equation"
dvy11=solve(ec3,y)[0]; "yc = f0(zc)" 
dvy12=solve(ec3,y)[1]; "yc = f1(zc)"

dvy11.args[1].args[1]**2; "f(zc)" 

zsq=Eq(dvy11.args[1].args[1]**2,0); "f(zc)"
rootzsq=solve(zsq,z)           

"Line x dependent variable equation"
dvx11=solve(ec4,x)[0]; "f0(zc)"
dvx12=solve(ec4,x)[1]; "f1(zc)"


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
    
fgr02.ax=ax2[3]; "Handler for subplot (d)"
fgr02.Labels("(d) The locust of points in an Intersection of \n\
a Cone andg a Plane is an elipse in this case.")
fgr02.ShowAxes(2)
fgr02.ax.plot3D(linex, liney, linez)
fgr02.ax.plot3D(linex1, liney1, linez)
fgr02.ax.plot_surface(plnxM,plnyM,plnzM, alpha=.2)
fgr02.ax.plot_surface(mcx,mcy,mcz,alpha=.2)
savefig("Data/fgr02.png")