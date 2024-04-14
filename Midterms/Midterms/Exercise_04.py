# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:20:10 2024

@author: MADT

4. What is the range of disk tilt angle such that the intersection
forms circular  and/or eleptical curve lines.
"""
#insert libraries
from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *


#define the figure
Fig4=Space3D(title="Figure 04",sz=(8,8));
Fig4.ax=axes(projection='3d')
Fig4.Labels("The plane cuts the cone at an angle.")
Fig4.ShowAxes(30)

"Values of the Cone"
Base=15
Height=25
nTanHalfDelta=Base/Height
delta=2*aTan(nTanHalfDelta)
res=100


"The cone equation in Cartesian Coordinate System"
ec2=ec1.subs(u,z).subs(base,Base).subs(height,Height).simplify()

"The cylindrical axes ."
lnphi = linspace(0,2*npi,res);"One revolution."
lnrho = linspace(0,Base,res);"From center to perimeter of the base."
lnz1  = linspace(0,-Height,res);"Bottom cone from center to negative height."


ncx=outer(cos(lnphi),lnrho); "Catersian meshgrid with cylindrical geometric equivalent cos(lnphi) and lnrho." 
ncy=outer(sin(lnphi),lnrho); "Cartesian meshgrid with cylindrical geometric equivalent sin(lnphi) and lnrho."
ncz1=outer(ones(res),lnz1);  "ncz1 is a Catersian meshgrid with cylindrical equivalent z for bottom cone."

"Plotting of the  cone "
Fig4.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig4.ax.plot_surface(ncx,ncy,ncz1,color=(0,1,0),alpha=.2)

ncz=outer(ones(res),lnz1);"For Lower cone"
Fig4.ax.plot_surface(ncx,ncy,ncz,alpha=.4)


nKDisk=-12
nConeAngle=aTan(Base/Height)
n1ConeAngle=nConeAngle*180/npi
"let tilt angle be .25 less than "+str(nConeAngle)
nTiltAngle=npi/2-nConeAngle*1.2
nDiskTilt=aTan(Base/(Height+nKDisk))
nDiskVectorTilt=npi/2-nDiskTilt



nsVecTip=array([0,0,0])
nsVecTail=array([Tan(nDiskVectorTilt)*nKDisk,0,nKDisk])
nsVec=nsVecTip-nsVecTail
nloc=array([0,0,nKDisk])

Fig4.PlotVector(nloc,nsVec,color=(1,0,0),base=.5)
nDisk=Fig4.GenDisk(Base*4)

nrotDisk = Fig4.QuaternionRotate( nDisk, nloc, nsVec)

nmovDisk= Fig4.Move(nrotDisk,nloc)
Fig4.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.2)


linensVec=Fig4.GenLine(nloc,-nsVec*2+nloc)
Fig4.ax.plot3D(linensVec[0],linensVec[1],linensVec[2],color=(0,0,0),
                linestyle="dashed")


e1ConeCyl=Eq(rho,base*(z)/height);"$\\rho$=f(z)"

exc=Eq(x,base*z/height*Cos(phi));"x=f(z,$\\phi$)"
eyc=Eq(y,base*z/height*Sin(phi));"x=f(z,$\\phi$)"
e1ConeCar=Eq(x**2+y**2,(exc.rhs**2+eyc.rhs**2).simplify());"f(x,y)=f(z)"
e2ConeCar=e1ConeCar.subs(base,Base).subs(height,Height);



"Cartesian System cone equation"
e2ConeCyl=Eq(rho**2,e2ConeCar.rhs);"Cylindrical System cone equation "
unsVec=Fig4.UnitVector(nsVec)
nuAcar=unsVec[0]
nuBcar=unsVec[1]
nuCcar=unsVec[2]
nuKcar=dot(unsVec,nloc)
e1PlaneCar=Eq(nuAcar*x+nuBcar*y+nuCcar*z,nuKcar);"Cartesian system disk equation."

sdxp=solve(e1PlaneCar,x)[0]
sdyc2=solve(e2ConeCar,y**2)[0].subs(x,sdxp).expand()
sdzroots=list(roots(sdyc2).keys())
niz=linspace(float(sdzroots[0]),float(sdzroots[1]),res)

ndyn=[];ndyp=[];ndx=[]
for i in range(res):
     tempc=Sqrt(sdyc2.subs(z,niz[i]))
     if tempc.is_real:
         ndyn.append(-float(tempc))        
         ndyp.append( float(tempc))
     else:
         ndyn.append(0)
         ndyp.append(0)
     ndx.append(float(sdxp.subs(z,niz[i])))
     
Fig4.ax.plot3D(ndx,ndyp,niz)
Fig4.ax.plot3D(ndx,ndyn,niz)

savefig("Data/Fig4.png")             

 
