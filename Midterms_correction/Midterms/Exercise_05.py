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


# defining the figure
Fig5=Space3D(title="Figure 05",sz=(8,8));"Handler of Figure 5" 
Fig5.ax=axes(projection='3d')
Fig5.Labels("The disk cuts the cone at an angle parallel to the lateral surface. ")
Fig5.ShowAxes(30)


"Values of the Cone"
Base=8
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
Fig5.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig5.ax.plot_surface(ncx,ncy,ncz1,color=(0,1,0),alpha=.2)


"Plotting of the  cone "
Fig5.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig5.ax.plot_surface(ncx,ncy,ncz1,color=(0,1,0),alpha=.2)


ncz=outer(ones(res),lnz1);"Lower cone"
Fig5.ax.plot_surface(ncx,ncy,ncz,alpha=.2)


nKDisk=-15
nConeAngle=aTan(Base/Height)
n1ConeAngle=nConeAngle*180/npi


"let tilt angle be .25 less than "+str(nConeAngle)
#nTiltAngle=npi/2-nConeAngle*1.2
nDiskTilt=aTan(Base/Height)
nDiskVectorTilt=npi/2-nDiskTilt


nsVecTip=array([0,0,0])
nsVecTail=array([Tan(nDiskVectorTilt)*nKDisk,0,nKDisk])
nsVec=nsVecTip-nsVecTail
nloc=array([0,0,nKDisk])

Fig5.PlotVector(nloc,nsVec,color=(0,1,0),base=.5)
nDisk=Fig5.GenDisk(Base*4)
#fgr04.ax.plot_surface(ndisk[0],ndisk[1],ndisk[2],alpha=.2)
nrotDisk = Fig5.QuaternionRotate( nDisk, nloc, nsVec)
#fgr04.ax.plot_surface(nrotDisk[0],nrotDisk[1],nrotDisk[2],alpha=.2)
nmovDisk= Fig5.Move(nrotDisk,nloc)
Fig5.ax.plot_surface(nmovDisk[0],nmovDisk[1],nmovDisk[2],alpha=.2)


linensVec=Fig5.GenLine(nloc,-nsVec+nloc)
Fig5.ax.plot3D(linensVec[0],linensVec[1],linensVec[2],color=(0,0,0),
                linestyle="dashed")


e1ConeCyl=Eq(rho,base*(z)/height);"$\\rho$=f(z)"

exc=Eq(x,base*z/height*Cos(phi));"x=f(z,$\\phi$)"
eyc=Eq(y,base*z/height*Sin(phi));"x=f(z,$\\phi$)"
e1ConeCar=Eq(x**2+y**2,(exc.rhs**2+eyc.rhs**2).simplify());"f(x,y)=f(z)"
e2ConeCar=e1ConeCar.subs(base,Base).subs(height,Height)
"Cartesian System cone equation"
e2ConeCyl=Eq(rho**2,e2ConeCar.rhs);"Cylindrical System cone equation "



unsVec=Fig5.UnitVector(nsVec)
nuAcar=unsVec[0]
nuBcar=unsVec[1]
nuCcar=unsVec[2]
nuKcar=dot(unsVec,nloc)
e1PlaneCar=Eq(nuAcar*x+nuBcar*y+nuCcar*z,nuKcar);"Cartesian system disk equation."

sdx=solve(e1PlaneCar,x)[0]

sr2=e2ConeCar.rhs

e3ConeCar=Eq(y**2,-sdx**2+sr2)
sdy2=e3ConeCar.rhs

sizroots=solve(Eq(sdy2,0),z)[0]

niz=linspace(float(sizroots),-float(Height),res)

        
ndyn=[];ndyp=[];ndx=[];ndxn=[]


for i in range(res):
    temp1=sdy2.subs(z,niz[i])
    temp2=sdx.subs(z,niz[i])
    if Ge(temp1,0):
        ndyp.append(Sqrt(temp1))
        ndyn.append(-Sqrt(temp1))
    else:
        ndyp.append(0)
        ndyn.append(0)
    ndx.append(temp2)  
    #print(ndyp[i]**2+ndx[i]**2,sr2.subs(z,niz[i]))    

Fig5.ax.plot(ndx,ndyp,niz)
Fig5.ax.plot(ndx,ndyn,niz)



savefig("Data/Fig5.png")
