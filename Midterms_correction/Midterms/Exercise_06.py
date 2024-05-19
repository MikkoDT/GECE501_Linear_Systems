# -*- coding: utf-8 -*-
"""


@author: MADT

6. What is the disk angle of tilt such that the intersection
 from a hyperbolic curve lines.
"""

from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *

# Defining the figure
Fig6 = Space3D(title="Figure 06", sz=(8, 8))  # Handler of Figure 6
Fig6.ax = axes(projection='3d')
Fig6.Labels("The disk cuts upright and inverted cones at an angle.")
Fig6.ShowAxes(30)

# Values of the Cone
Base = 8
Height = 25
nTanHalfDelta = Base / Height
delta = 2 * aTan(nTanHalfDelta)
res = 100

# The cone equation in Cartesian Coordinate System
# ec2 = ec1.subs(u, z).subs(base, Base).subs(height, Height).simplify()  # No definition for ec1

# The cylindrical axes
lnphi = linspace(0, 2 * npi, res)  # One revolution.
lnrho = linspace(0, Base, res)  # From center to perimeter of the base.
lnz1 = linspace(0, -Height, res)  # Bottom cone from center to negative height.
lnz2 = linspace(0, Height, res)  # Top cone from center to positive height.

ncx = outer(cos(lnphi), lnrho)  # Cartesian meshgrid with cylindrical geometric equivalent cos(lnphi) and lnrho.
ncy = outer(sin(lnphi), lnrho)  # Cartesian meshgrid with cylindrical geometric equivalent sin(lnphi) and lnrho.
ncz1 = outer(ones(res), lnz1)  # ncz1 is a Cartesian meshgrid with cylindrical equivalent z for bottom cone.
ncz2 = outer(ones(res), lnz2)  # ncz2 is a Cartesian meshgrid with cylindrical equivalent z for top cone.

# Plotting both upright and inverted cones
Fig6.ax.plot_surface(ncx, ncy, ncz1, alpha=.2)
Fig6.ax.plot_surface(ncx, ncy, ncz2, alpha=.2)

# Disk parameters
nKDisk = -15
nConeAngle = aTan(Base / Height)
n1ConeAngle = nConeAngle * 180 / npi
nDiskTilt = nConeAngle
nDiskVectorTilt = npi / 2 - nDiskTilt

nsVecTip = array([Height, 0, nKDisk])
nsVecTail = array([0, 0, nKDisk])
nsVec = nsVecTip - nsVecTail
nloc = array([0, 0, nKDisk])

# Plotting the vector
Fig6.PlotVector([5, 0, nKDisk], nsVec, color=(1, 0, 0), base=.5)
nDisk = Fig6.GenDisk(Base * 4)
nrotDisk = Fig6.QuaternionRotate(nDisk, nloc, nsVec)
nmovDisk = Fig6.Move(nrotDisk, [5, 0, nKDisk])
Fig6.ax.plot_surface(nmovDisk[0], nmovDisk[1], nmovDisk[2], alpha=.2)

linensVec = Fig6.GenLine([5, 0, nKDisk], -nsVec + nloc)
Fig6.ax.plot3D(linensVec[0], linensVec[1], linensVec[2], color=(0, 0, 0), linestyle="dashed")

# Cone equations in Cartesian coordinates
e1ConeCar = Eq(x**2 + y**2, (Base * z / Height)**2)

# Disk plane equation
unsVec = Fig6.UnitVector(nsVec)
nuAcar = unsVec[0]
nuBcar = unsVec[1]
nuCcar = unsVec[2]
nuKcar = dot(unsVec, [5, 0, nKDisk])
e1PlaneCar = Eq(nuAcar * x + nuBcar * y + nuCcar * z, nuKcar)

# Solving for intersections
sdx = solve(e1PlaneCar, x)[0]
sr2 = e1ConeCar.rhs
e3ConeCar = Eq(y**2, sr2 - sdx**2)
sizroots = solve(Eq(e3ConeCar.rhs, 0), z)[0]

# Computing intersection points
niz = linspace(float(sizroots), -float(Height), res)
ndyn = []
ndyp = []
ndx = []

for i in range(res):
    temp1 = e3ConeCar.rhs.subs(z, niz[i])
    temp2 = sdx.subs(z, niz[i])
    if Ge(temp1, 0):
        ndyp.append(Sqrt(temp1))
        ndyn.append(-Sqrt(temp1))
    else:
        ndyp.append(0)
        ndyn.append(0)
    ndx.append(temp2)

Fig6.ax.plot(ndx, ndyp, niz)
Fig6.ax.plot(ndx, ndyn, niz)

# Computing intersection points for the upright cone
niz = linspace(-float(sizroots), float(Height), res)
ndyn = []
ndyp = []
ndx = []

for i in range(res):
    temp1 = e3ConeCar.rhs.subs(z, niz[i])
    temp2 = sdx.subs(z, niz[i])
    if Ge(temp1, 0):
        ndyp.append(Sqrt(temp1))
        ndyn.append(-Sqrt(temp1))
    else:
        ndyp.append(0)
        ndyn.append(0)
    ndx.append(temp2)

Fig6.ax.plot(ndx, ndyp, niz)
Fig6.ax.plot(ndx, ndyn, niz)

savefig("Data/Fig6.png")