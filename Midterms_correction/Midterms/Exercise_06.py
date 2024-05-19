# -*- coding: utf-8 -*-
"""


@author: MADT

6. What is the disk angle of tilt such that the intersection
 from a hyperbolic curve lines.
"""

from madLib.madVector import *
from madLib.madPlot import *
from Data.variables import *

# defining the figure
Fig6 = Space3D(title="Figure 06", sz=(8, 8)); "Handler of Figure 6"
Fig6.ax = axes(projection='3d')
Fig6.Labels("The disk cuts the upright and inverted cones at an angle.")
Fig6.ShowAxes(30)

# Values of the Cone
Base = 8
Height = 25
nTanHalfDelta = Base / Height
delta = 2 * aTan(nTanHalfDelta)
res = 100

# The cone equation in Cartesian Coordinate System
ec2 = ec1.subs(u, z).subs(base, Base).subs(height, Height).simplify()

# The cylindrical axes
lnphi = linspace(0, 2 * npi, res); "One revolution."
lnrho = linspace(0, Base, res); "From center to perimeter of the base."
lnz1 = linspace(0, -Height, res); "Bottom cone from center to negative height."

ncx = outer(cos(lnphi), lnrho); "Cartesian meshgrid with cylindrical geometric equivalent cos(lnphi) and lnrho."
ncy = outer(sin(lnphi), lnrho); "Cartesian meshgrid with cylindrical geometric equivalent sin(lnphi) and lnrho."
ncz1 = outer(ones(res), lnz1); "ncz1 is a Cartesian meshgrid with cylindrical equivalent z for bottom cone."

# Plotting of the inverted cone
Fig6.ax.plot_surface(ncx, ncy, ncz1, alpha=.2)

# Tilt angle to create hyperbolic intersection
nConeAngle = aTan(Base / Height)
nDiskTilt = nConeAngle + 0.1  # Slightly greater than the cone angle for hyperbolic intersection
nDiskVectorTilt = npi / 2 - nDiskTilt

nsVecTip = array([Height, 0, -Height])
nsVecTail = array([0, 0, -Height])
nsVec = nsVecTip - nsVecTail
nloc = array([0, 0, -Height])

Fig6.PlotVector([5, 0, -Height], nsVec, color=(1, 0, 0), base=.5)
nDisk = Fig6.GenDisk(Base * 4)
nrotDisk = Fig6.QuaternionRotate(nDisk, nloc, nsVec)
nmovDisk = Fig6.Move(nrotDisk, [5, 0, -Height])
Fig6.ax.plot_surface(nmovDisk[0], nmovDisk[1], nmovDisk[2], alpha=.2)

linensVec = Fig6.GenLine([5, 0, -Height], -nsVec + nloc)
Fig6.ax.plot3D(linensVec[0], linensVec[1], linensVec[2], color=(0, 0, 0), linestyle="dashed")

e1ConeCyl = Eq(rho, base * (z) / height); "$\\rho$=f(z)"
exc = Eq(x, base * z / height * Cos(phi)); "x=f(z,$\\phi$)"
eyc = Eq(y, base * z / height * Sin(phi)); "x=f(z,$\\phi$)"
e1ConeCar = Eq(x**2 + y**2, (exc.rhs**2 + eyc.rhs**2).simplify()); "f(x,y)=f(z)"
e2ConeCar = e1ConeCar.subs(base, Base).subs(height, Height)

"Cartesian System cone equation"
e2ConeCyl = Eq(rho**2, e2ConeCar.rhs)

unsVec = Fig6.UnitVector(nsVec)
nuAcar = unsVec[0]
nuBcar = unsVec[1]
nuCcar = unsVec[2]
nuKcar = dot(unsVec, [5, 0, -Height])

"Cartesian system disk equation."
e1PlaneCar = Eq(nuAcar * x + nuBcar * y + nuCcar * z, nuKcar)

sdx = solve(e1PlaneCar, x)[0]
sr2 = e2ConeCar.rhs
e3ConeCar = Eq(y**2, -sdx**2 + sr2)
sdy2 = e3ConeCar.rhs
sizroots = solve(Eq(sdy2, 0), z)[0]
niz = linspace(float(sizroots), -float(Height), res)

ndyn = []
ndyp = []
ndx = []
ndxn = []

for i in range(res):
    temp1 = sdy2.subs(z, niz[i])
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

niz = linspace(-float(sizroots), float(Height), res)
ndyn = []
ndyp = []
ndx = []
ndxn = []

savefig("Data/Fig6.png")