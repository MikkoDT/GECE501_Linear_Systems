# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:59:27 2024

@author: MADT
"""

"""
2.Create your own plane disk perpendicular to the z axis
and cut the upright cone below the origin.Choose your own 
distance value below the origin.Formulate the disk equation."

"""

#define the figure
Fig2=Space3D(title="Figure 02",sz=(8,8));"Disk cut on upright cone." 
Fig2.ax=axes(projection='3d');"Plot axes handler."

Fig2.Labels("The upright cone with a diskcutting across upright cone")
Fig2.ShowAxes(30)

"Values of the Cone"
Base=10
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
Fig2.ax.plot_surface(ncx,ncy,ncz1,color=(1,0,0),alpha=.2)
Fig2.ax.plot_surface(ncx,ncy,ncz1,color=(0,1,0),alpha=.2)


"Equation of a cylindrical circular plane perpendicular to cone height axis."
cDisk=Eq(A*phi+B*rho+C*z,K)
vDiskCoeff=Matrix([A,B,C]);"The [A,B,C] is a vector from origin perpendicular to the disk."

mVecDiskCoeff=Sqrt(A**2+B**2+C**2);"Magnitude of [A,B,C] vector"
uVecDiskCoeff=vDiskCoeff/mVecDiskCoeff;"[A,B,C] unit vector"
Diskxyz=Matrix([x,y,z]);"[x,y,z] is a vector from origin to any point in the disk."

e1VecDisk=Eq(Matrix(dot(Diskxyz.transpose(),vDiskCoeff)),k,evaluate=False);"The dot produc of [x,y,z] and [A,B,C] where $\\theta$ is the angle between them."
e2VecDisk=Eq(Matrix(dot(Diskxyz.transpose(),uVecDiskCoeff)),k/mVecDiskCoeff,evaluate=False);"The projection of [x,y,z] on [A,B,C] that gives the shortest distance from origin \
to the disk. The shortest distance is k/Mag([A,B,C])."

"The disk is perpendicular to z axis and located at z=-12. Hence the disk \
equation is expressed as follows."
nADisk=0;nBDisk=0;nCDisk=1;nKDisk=-12


e1CylDisk=cDisk.subs(A,nADisk).subs(B,nBDisk).subs(C,nCDisk).subs(K,nKDisk)

CaCyD[phi]
CaCyD[rho]


sVecDiskTip=array([0,0,0]);"Coordinate of the tip of nVecDiskCoeff"
sVecDiskTail=array([0,0,nKDisk]);"Coordinate of the tail of nVecDiskCoeff"
sVecDisk=sVecDiskTip-sVecDiskTail;"[0,0,nKDisk] vector"
nloc=array([0,0,nKDisk]);"Location of the disk."
Fig2.PlotVector(nloc,sVecDisk,color=(1,0,0),base=.5)


"The plot algorithm is based on the cylindrical equation of disk. "

"Since the disk is a surface plot, the independent variables were chosen as $\\phi$ \
and $\\rho$ as follows. The dependent varialbe is a constant. Hence z=-12."

nLphi = linspace(0,2*npi,res);"From zero to one complete revolution"
nLrho = linspace(0,Base*2,res);"Trom zero to  radius of the disk"
nLz   = ones(res)*nKDisk;"Constant z=12 for all res data."

mCarx=outer(cos(lnphi),nLrho);"Equivalent Cartesian x meshgrid of $\\phi$ and $\\rho$."
mCary=outer(sin(lnphi),nLrho);"Equivalent Cartesian y meshgrid of $\\phi$ and $\\rho$."
mCarz=outer(ones(res),nLz);"Equivalent Cartesian z meshgrid of z."

Fig2.ax.plot_surface(mCarx,mCary,mCarz,alpha=.2)


"Draw dashed line from point [0,0,nKDisk] to point [0,0,-nKDisk]"
linensVecDisk=Fig2.GenLine(nloc,-sVecDisk)
Fig2.ax.plot3D(linensVecDisk[0],linensVecDisk[1],linensVecDisk[2],color=(0,0,0),
                linestyle="dashed")
savefig("Data/Fig2.png")