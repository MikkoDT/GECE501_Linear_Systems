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
from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *

# Define the figure
Fig2 = Space3D(title="Figure 02", sz=(8, 8)); "Disk cut on inverted cone."
Fig2.ax = axes(projection='3d'); "Plot axes handler."

Fig2.Labels("The inverted cone with a disk cutting across inverted cone")
Fig2.ShowAxes(30)

# Values of the Cone
Base = 10
Height = 25
nTanHalfDelta = Base / Height
delta = 2 * aTan(nTanHalfDelta)
res = 100

# The cone equation in Cartesian Coordinate System
# Assuming ec1 is defined elsewhere
ec2 = ec1.subs(u, z).subs(base, Base).subs(height, Height).simplify()

# The cylindrical axes
lnphi = linspace(0, 2 * npi, res); "One revolution."
lnrho = linspace(0, Base, res); "From center to perimeter of the base."
lnz1 = linspace(0, Height, res); "Inverted cone from center to positive height."

ncx = outer(cos(lnphi), lnrho); "Cartesian meshgrid with cylindrical geometric equivalent cos(lnphi) and lnrho."
ncy = outer(sin(lnphi), lnrho); "Cartesian meshgrid with cylindrical geometric equivalent sin(lnphi) and lnrho."
ncz1 = outer(ones(res), lnz1); "ncz1 is a Cartesian meshgrid with cylindrical equivalent z for inverted cone."

# Plotting of the inverted cone
Fig2.ax.plot_surface(ncx, ncy, ncz1, color=(1, 0, 0), alpha=.2)

# Equation of a cylindrical circular plane perpendicular to cone height axis.
# Assuming cDisk is defined elsewhere
cDisk = Eq(A * phi + B * rho + C * z, K)
vDiskCoeff = Matrix([A, B, C]); "The [A, B, C] is a vector from origin perpendicular to the disk."

mVecDiskCoeff = Sqrt(A**2 + B**2 + C**2); "Magnitude of [A, B, C] vector"
uVecDiskCoeff = vDiskCoeff / mVecDiskCoeff; "[A, B, C] unit vector"
Diskxyz = Matrix([x, y, z]); "[x, y, z] is a vector from origin to any point in the disk."

e1VecDisk = Eq(Matrix(dot(Diskxyz.transpose(), vDiskCoeff)), k, evaluate=False); "The dot product of [x, y, z] and [A, B, C] where θ is the angle between them."
e2VecDisk = Eq(Matrix(dot(Diskxyz.transpose(), uVecDiskCoeff)), k / mVecDiskCoeff, evaluate=False); "The projection of [x, y, z] on [A, B, C] that gives the shortest distance from origin to the disk. The shortest distance is k/Mag([A, B, C])."

# The disk is perpendicular to z-axis and located at z=12. Hence the disk equation is expressed as follows.
nADisk = 0; nBDisk = 0; nCDisk = 1; nKDisk = 12

e1CylDisk = cDisk.subs(A, nADisk).subs(B, nBDisk).subs(C, nCDisk).subs(K, nKDisk)

CaCyD[phi]
CaCyD[rho]

sVecDiskTip = array([0, 0, 0]); "Coordinate of the tip of nVecDiskCoeff"
sVecDiskTail = array([0, 0, nKDisk]); "Coordinate of the tail of nVecDiskCoeff"
sVecDisk = sVecDiskTip - sVecDiskTail; "[0, 0, nKDisk] vector"
nloc = array([0, 0, nKDisk]); "Location of the disk."
Fig2.PlotVector(nloc, sVecDisk, color=(1, 0, 0), base=.5)

# The plot algorithm is based on the cylindrical equation of disk.
# Since the disk is a surface plot, the independent variables were chosen as φ and ρ as follows. The dependent variable is a constant. Hence z=12.
nLphi = linspace(0, 2 * npi, res); "From zero to one complete revolution"
nLrho = linspace(0, Base * 2, res); "From zero to radius of the disk"
nLz = ones(res) * nKDisk; "Constant z=12 for all res data."

mCarx = outer(cos(lnphi), nLrho); "Equivalent Cartesian x meshgrid of φ and ρ."
mCary = outer(sin(lnphi), nLrho); "Equivalent Cartesian y meshgrid of φ and ρ."
mCarz = outer(ones(res), nLz); "Equivalent Cartesian z meshgrid of z."

Fig2.ax.plot_surface(mCarx, mCary, mCarz, alpha=.2)

# Draw dashed line from point [0,0,nKDisk] to point [0,0,-nKDisk]
linensVecDisk = Fig2.GenLine(nloc, -sVecDisk)
Fig2.ax.plot3D(linensVecDisk[0], linensVecDisk[1], linensVecDisk[2], color=(0, 0, 0), linestyle="dashed")

savefig("Data/Fig2.png")