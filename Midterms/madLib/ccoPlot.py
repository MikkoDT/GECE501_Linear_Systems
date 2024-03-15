# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 08:52:47 2014
@author: CBCO
cbco rev 1 Dec 8, 2017
cbco rev 2 Tue Apr 19 7:37:00 2022
cbco rev 3 Wed May 31 20:45:14 2023
cbco rev 4 Thu Jun 15 16:22:27 2023
cbco rev 5 Wed Jan 10 02:40:22 2024
cbco rev 6 Sat Feb 10 17:24:20 2024
cbco rev 7 Wed Feb 21 00:42:17 2024

"""

"""
Software

Installing Anaconda
1. Visit https://www.anaconda.com/download/
2. Download Python 3.6 version. Choose 64 bit for computer with 64 bit hardware.
3. Register in Anaconda Cloud.

From anaconda, access Spyder editor. Its website is https://spyder-ide.github.io


Installing ProTeXt

1. Visit http://tug.org/protext/
2. click  download the self-extracting protext.exe file  and it will bring \
you to http://mirror.pregi.net/tex-archive/systems/windows/protext/
Download ProTeXt-3.1.8-051917.exe or protext.exe This file is 2.5 GB

From ProTeXt run set up, install MikText first then install TexStudio.
MikText Website is https://miktex.org.
TexStudio Website is at https://www.texstudio.org


Library

import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import scipy as sp  # SciPy (signal and image processing library)

import matplotlib as mpl          # Matplotlib (2D/3D plotting library)
import matplotlib.pyplot as plt   # Matplotlib's pyplot: MATLAB-like syntax
from pylab import *               # Matplotlib's pylab interface
ion()                             # Turned on Matplotlib's interactive mode

import guidata                    # GUI generation for easy dataset editing and display

import guiqwt                     # Efficient 2D data-plotting features
import guiqwt.pyplot as plt_      # guiqwt's pyplot: MATLAB-like syntax
plt_.ion()                        # Turned on guiqwt's interactive mode


Within Spyder, this interpreter also provides:
    * special commands (e.g. %ls, %pwd, %clear)
    * system commands, i.e. all commands starting with '!' are subprocessed
      (e.g. !dir on Windows or !ls on Linux, and so on)

@Article{Hunter:2007,
  Author    = {Hunter, J. D.},
  Title     = {Matplotlib: A 2D graphics environment},
  Journal   = {Computing In Science \& Engineering},
  Volume    = {9},
  Number    = {3},
  Pages     = {90--95},
  abstract  = {Matplotlib is a 2D graphics package used for Python
  for application development, interactive scripting, and
  publication-quality image generation across user
  interfaces and operating systems.},
  publisher = {IEEE COMPUTER SOC},
  year      = 2007
}

"""


import sys
import string

import numpy as np  # NumPy (multidimensional arrays, linear algebra, ...)
import scipy as sp  # SciPy (signal and image processing library)
import sympy as sym

from numpy   import linspace, meshgrid, dot, cross, cos, sin, ones,\
                    arccos, arctan, arcsin, array, pi as npi, size, \
                    sqrt, outer, inner, abs, zeros, mat, matrix, exp,\
                    log10, shape    
from sympy   import latex, solve, symbols, pi, Eq, Matrix, Function,\
                    var, Abs, cos as Cos, sin as Sin, atan as aTan, \
                    sqrt as Sqrt, Le, acos as aCos, Inverse, tan as Tan,\
                    dsolve, I, exp as Exp, Lt, And, Or, Piecewise, Ne, \
                    Integral, Derivative, Float, det, roots, Gt, Ge
                                        
from sympy.codegen.cfunctions import log10 as Log10

from matplotlib.collections   import PatchCollection

import matplotlib.path             as    mpath
import matplotlib.patches          as    mpatches
import matplotlib.lines            as    mlines

# MatPlot Library

import matplotlib.pyplot                           as     plt
from   matplotlib.axes                             import Axes
from   matplotlib.backend_bases                    import FigureCanvasBase
from   mpl_toolkits.mplot3d.axes3d                 import Axes3D
from   matplotlib.axis                             import Axis


from   matplotlib.pyplot import figure, show, axes, text, cla, draw, annotate
from   matplotlib.pyplot import subplots_adjust, plot, subplot, subplots, gca, axis
from   matplotlib.pyplot import show, stem, setp, hist, savefig, close, fill

from   matplotlib.text   import Text
from   matplotlib.pyplot import polar





def OnClickAction(self,event):
    if event.inaxes != None:
        
        print( "\n\nMouse event\n")
        print( "2D Coordinates: (X2D,Y2D) = (",Float(event.xdata,3),
          ",",Float(event.ydata,3),")")
        self.x=event.xdata;self.y=event.ydata
        s=self.ax.format_coord(event.xdata, event.ydata).replace("−","-")
        if event.button ==3:
            s=s.replace('=','').replace('x','').replace('y','').replace('z','')
        print('3D Coordinates Information: ',s)
        print('Event button = ',event.button)
        self.data=s

def PressKeyAction(self,event):
    print( "\n\nKeyboard event\n")
    self.x=Float(event.xdata,3);self.y=Float(event.ydata,3)
    print( "2D Coordinates: X2D = ",self.x,", Y2D = ",self.y)
   
    print ("key = ", event.key, " \n")
    self.key=event.key
   

#CC Library

class Space2D:


    def __init__(self,click=OnClickAction,press=PressKeyAction,
                 title="2D Figure",sz=(10,8),fc='w'):

        self.title=title
        self.sz   =sz
        self.fc   =fc
        self.Fig2D=figure(
            self.title,figsize=self.sz,
            facecolor=self.fc)           #define the figure
      
        
  
        self.ev= [
            'resize_event',      'draw_event',          'key_press_event',
            'key_release_event', 'button_press_event',  'button_release_event',
            'scroll_event',      'motion_notify_event', 'pick_event',
            'idle_event',        'figure_enter_event',  'figure_leave_event',
            'axes_enter_event',  'axes_leave_event',    'close_event']
        self.handleOnClick  = self.Fig2D.canvas.mpl_connect(self.ev[4], self.OnClick)
        self.handleClose    = self.Fig2D.canvas.mpl_connect(self.ev[14],self.Disconnect)
        self.handlePressKey = self.Fig2D.canvas.mpl_connect(self.ev[2], self.PressKey)
        self.x=0;self.y=0;
        self.key=''
        self.button=0
        self.CountButton=[0,0,0]  #CountButton[0] for button 1
                                  #CountButton[1] for button 2
                                  #CountButton[2] for button 3
        self.cmd=''               #command buffer
        self.OnClickAction=click
        self.PressKeyAction=press

    def OnClick(self,event):
        self.OnClickAction(self,event)
        draw()

    def PressKey(self,event):
        self.PressKeyAction(self,event)
        draw()

    def Disconnect(self,event):
        self.Fig2D.canvas.mpl_disconnect(self.handleOnClick)
        self.Fig2D.canvas.mpl_disconnect(self.handleClose)
        self.Fig2D.canvas.mpl_disconnect(self.handlePressKey)

    def Labels(self,title="",x="x",y="y"):
        ax=gca()
        ax.set_title(title)
        ax.set_xlabel(x)
        ax.set_ylabel(y)
   
    def Annotate(self,x,y,s,color=[0,0,0]):
        self.ax.text(x,y,s,color=color)

    def Fill(self,x,y,color=[0,1,0]):
        self.ax.fill(x,y,color=color)


class Space3D:

    def __init__(self,click=OnClickAction,press=PressKeyAction,
                 title="3D Figure",sz=(6,8),fc='w',clear=True):

        self.title=title
        self.sz   =sz
        self.fc   =fc
        self.Fig3D=figure(self.title,figsize=self.sz,facecolor=self.fc) 
                                 #define the figure
        #self.ax = axes(projection='3d')
        #self.Labels()
        self.x=0;self.y=0;self.z=0;self.data=""
        self.PointSize=0.2
        self.key=''
        self.button=0
        self.CountButton=[0,0,0]  #CountButton[0] for button 1
                                  #CountButton[1] for button 2
                                  #CountButton[2] for button 3
        self.cmd=''               #command buffer
        self.segment=10
        #self.Plot3D=self.ax.plot3D
        #self.PlotSurface=self.ax.plot_surface 
        #surface = self.PlotSurface(Xm, Ym, Zm,color=(1,0,0),linewidth=0,
        #                          antialiased=False, alpha=.1)  
        #alpha is a measure of transparency
       
        self.SaveFigure=self.Fig3D.savefig
        self.OnClickAction=click
        self.PressKeyAction=press
        self.ev= [
            'resize_event',      'draw_event',          'key_press_event',
            'key_release_event', 'button_press_event',  'button_release_event',
            'scroll_event',      'motion_notify_event', 'pick_event',
            'idle_event',        'figure_enter_event',  'figure_leave_event',
            'axes_enter_event',  'axes_leave_event',    'close_event']
        self.handleOnClick  = self.Fig3D.canvas.mpl_connect(self.ev[4], self.OnClick)
        self.handleClose    = self.Fig3D.canvas.mpl_connect(self.ev[14],self.Close)
        self.handlePressKey = self.Fig3D.canvas.mpl_connect(self.ev[2], self.PressKey)

    def Annotate(self,pt,s=""):
        if s=="":
            s=str(pt)
        self.ax.text(pt[0],pt[1],pt[2],s)

    def Labels(self,title="",x="x",y="y",z="z"):
        self.ax.set_title(title)
        self.ax.set_xlabel(x)
        self.ax.set_ylabel(y)
        self.ax.set_zlabel(z)
       

    def OnClick(self,event):
        self.OnClickAction(self,event)
        self.event=event
        draw()

    def PressKey(self,event):
        self.key=event.key
        print("key ", event.key)
        if event.key.isalnum:
            self.PressKeyAction(self,event)
        self.event=event    
        draw()

    def Close(self,event):
        self.Fig3D.canvas.mpl_disconnect(self.handleOnClick)
        self.Fig3D.canvas.mpl_disconnect(self.handleClose)
        self.Fig3D.canvas.mpl_disconnect(self.handlePressKey)



    def ShowAxes(self,seg,at=[0,0,0]):
        if at ==[0,0,0]:self.ax.text(0,0,0," 0")
        self.PlotLine([-seg+at[0],     at[1],     at[2]],
                      [ seg+at[0],     at[1],     at[2]],color='y') 
        self.PlotLine([     at[0],-seg+at[1],     at[2]],
                      [    at[0],  seg+at[1],     at[2]],color='y')  
        self.PlotLine([     at[0],     at[1],-seg+at[2]],
                      [    at[0],     at[1],  seg+at[2]],color='y')  
        self.ax.text(  seg+at[0],    at[1],    at[2],  '  x')
        self.ax.text(      at[0],seg+at[1],    at[2],  '  y')
        self.ax.text(      at[0],    at[1],seg+at[2],  '  z')
        self.ax.text( -seg+at[0],    at[1],    at[2],  ' -x')
        self.ax.text(     at[0],-seg+at[1],    at[2],  ' -y')
        self.ax.text(     at[0],    at[1],-seg+at[2],  ' -z')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')
        draw()
    
    def ShowPoints(self,coordinates):
        l=len(coordinates)
        for i in range(l):
            self.ax.text(coordinates[i][0],coordinates[i][1],coordinates[i][2],
                   '('+str(round(coordinates[i][0],2))+
                   ','+str(round(coordinates[i][1],2))+
                   ','+str(round(coordinates[i][2],2))+')')         
        
    def GenArc(self, At, From, To, Radius, res=100):
    
        FromUnit=self.UnitVector(From)
        ToUnit=self.UnitVector(To)
        
        #angle betwee From and To
        angleFromTo=arccos(dot(FromUnit,ToUnit))
        #vector perpendicular to both From and To direction by right hand rule
        crossFromUnitToUnit=cross(FromUnit,ToUnit) 
   
        #The crossFromUnitToUnit oriented along z axis that is [0,0,1]
        #The FromUnit is the object rotated by such orientation
        RotFrom = self.QuaternionRotate(FromUnit,crossFromUnitToUnit,[0,0,1])
        RotFromUnit=self.UnitVector(RotFrom) 
    
        
        AngleFrom=arccos(RotFromUnit[0])
        if RotFromUnit[1] < 0 :AngleFrom=-AngleFrom
        
        lnphi = linspace(AngleFrom,AngleFrom+angleFromTo,res)
        lnz=ones(res)
        lnr=Radius
        x=cos(lnphi)*lnr
        y=sin(lnphi)*lnr
        z=lnz*0

        Arc=[x,y,z]  
   
        RotArc = self.QuaternionRotate( Arc, [0,0,1], crossFromUnitToUnit)
        MovRotArc=self.Move(RotArc,At)
   
        return MovRotArc

    def GenLine(self,From=[0,0,0],To=[0,0,1]):
        X=[From[0],To[0]]
        Y=[From[1],To[1]]
        Z=[From[2],To[2]]
        return [X,Y,Z]

    def GenPoints(self,coordinates):
        x=[];y=[];z=[]
        for i in range(len(coordinates)):
            x.append(coordinates[i][0]);
            y.append(coordinates[i][1]);
            z.append(coordinates[i][2])
        return x, y ,z



    def GenSphere(self,radius,at=[0,0,0],res=100):    
        phi   = linspace(0, 2 * np.pi, res)
        theta = linspace(0, np.pi, res)
        x = radius*outer(cos(phi), sin(theta))+at[0]
        y = radius*outer(sin(phi), sin(theta))+at[1]
        z = radius*outer(ones(res), cos(theta))+at[2]
        return x, y, z
    
    def GenCone(self,base, height,at=[0,0,0],res=100):
        lnphi = linspace(0,2*npi,res)
        lnr   = linspace(0,base,res)
        lnh   = linspace(height,0,res)
        x=outer(cos(lnphi),lnr)+at[0]
        y=outer(sin(lnphi),lnr)+at[1]
        z=outer(ones(res),lnh)+at[2]
        return x, y, z



    def GenDisk(self,radius, at=[0,0,0], res=100):
        lnphi = linspace(0,2*npi,res)
        lnr=linspace(0,radius,res)
        x=outer(cos(lnphi),lnr)+at[0]
        y=outer(sin(lnphi),lnr)+at[1]
        z=0*outer(ones(res),lnr)+at[2]

        return x, y, z

    def GenCoordinates(self, v, at=[0,0,0]):
        x=[at[0], v[0]+at[0]]
        y=[at[1], v[1]+at[1]]
        z=[at[2], v[2]+at[2]]
        return x, y, z

    def GenVector(self, v, at=[0,0,0]):
        x=[at[0], v[0]+at[0]]
        y=[at[1], v[1]+at[1]]
        z=[at[2], v[2]+at[2]]
        return x, y, z

    def Gen3DCoord(self,event):
        xd=event.xdata;yd=event.ydata
        s=self.ax.format_coord(xd, yd);print('s = ',s)
        return s.replace('−','-')
    
          
    def Magnitude(self, v):
        temp=float(v[0]**2+v[1]**2+v[2]**2)
        return sqrt(temp)
             
    def FloatVector(self,v):
        return array([float(v[0]),float(v[1]),float(v[2])])
     
    
    def UnitVector(self, v):
        m=self.Magnitude(v)
        if m !=0:
            return array([float(v[0]/m),float(v[1]/m),float(v[2]/m)])
        else:
            return v
        
    def DirectionalAngles(self, v):
        u=self.UnitVect(v)
        return  [arccos(u[0]),np.arccos(u[1]),np.arccos(u[2])]
    
      
    def QuaternionMultiply(self,a,b):
        sa=a[0];sb=b[0];va=array(a[1]);vb=array(b[1]) 
        return [sa*sb-dot(va,vb),sa*vb+sb*va+cross(va,vb)]

    def QuaternionRotate(self, obj, From, To, res=100):
        lnshp=len(shape(obj)) #lnshp=3 for surface, 2 for curve line, 1 for vector
        x=obj[0];y=obj[1];z=obj[2]
        uFrom=self.UnitVector(From)
        #Generate quaternion rotation coordinates for cone
        uTo=self.UnitVector(To)
        if uFrom[0]==uTo[0] and uFrom[1]==uTo[1] and uFrom[2]==uTo[2]:
            return obj
        cosTheta=float(dot(uFrom,uTo))
        theta=arccos(cosTheta)
        norm=cross(uFrom,uTo)
        unorm=self.UnitVector(norm)
        xh=[];yh=[];zh=[]
        Qn=[cos(theta/2),sin(theta/2)*unorm]    # Quaternion for unorm
        Qnc=[cos(theta/2),sin(theta/2)*-unorm]  # Complement Quaternion of unorm 
      
        if lnshp == 3:
            for i in range(res):
                x1=[];y1=[];z1=[]
                for j in range(res):
                    Qv=[0,array([x[i][j],y[i][j],z[i][j]])] #vector for rotation
                    QvQnc=self.QuaternionMultiply(Qv,Qnc)       
                    QnQvQnc=self.QuaternionMultiply(Qn,QvQnc)
                    x1.append(QnQvQnc[1][0])
                    y1.append(QnQvQnc[1][1])
                    z1.append(QnQvQnc[1][2])
                xh.append(x1)
                yh.append(y1)
                zh.append(z1)
        #Generate coordinates for placement of cone on vector tip  
            xh=np.array(xh)
            yh=np.array(yh)
            zh=np.array(zh)
            return [xh,yh,zh]
        elif lnshp == 2:
            for i in range(res):
                Qv=[0,array([x[i],y[i],z[i]])] #vector for rotation
                QvQnc=self.QuaternionMultiply(Qv,Qnc)       
                QnQvQnc=self.QuaternionMultiply(Qn,QvQnc)
                xh.append(QnQvQnc[1][0])
                yh.append(QnQvQnc[1][1])
                zh.append(QnQvQnc[1][2])
            xh=np.array(xh)
            yh=np.array(yh)
            zh=np.array(zh)
            return [xh,yh,zh]
        elif lnshp == 1:
            Qv=[0,array([x,y,z])] #vector for rotation
            QvQnc=self.QuaternionMultiply(Qv,Qnc)       
            QnQvQnc=self.QuaternionMultiply(Qn,QvQnc)
            xh=QnQvQnc[1][0]
            yh=QnQvQnc[1][1]
            zh=QnQvQnc[1][2]
            return array([xh,yh,zh])
        else:
            return "The object is not a vector nor a line nor surface."
        
    def Move(self,obj, To=[0,0,0]):
        x=obj[0]+To[0]
        y=obj[1]+To[1]
        z=obj[2]+To[2]
        return [x,y,z]

    def PutCone(self,at, vector, base=.5, height=1 ):
        #Generate coordinates for vector plot
        pv = self.GenVector(vector,at=at)
        #Generate coordinates for cone plot
        cone = self.GenCone(base,height,at=[0,0,-height])
        rcone=self.QuaternionRotate(cone,[0,0,1], vector)
        mrcone=self.Move(rcone,[pv[0][1],pv[1][1],pv[2][1]])
        return mrcone

    def PutDisk(self,at, vector, radius=.5 ):
        #Generate coordinates for vector plot
        pv = self.GenVector(vector,at)
        #Generate coordinates for cone plot
        disk = self.GenDisk(radius,[0,0,0],res=100)
        rdisk=self.QuaternionRotate(disk, [0,0,1], vector)
        mrdisk=self.Move(rdisk,[pv[0][0],pv[1][0],pv[2][0]])
        return mrdisk

    def PutPlane(self,at, vector, w=1, l=1 ):
        #Generate coordinates for vector plot
        pv = self.GenVector(vector,at)
        #Generate coordinates for cone plot
        plane = self.GenPlane(w,l,[0,0,0],res=100)
        rplane=self.QuartenionRotate(plane, [0,0,1], vector)
        mrplane=self.Move(rplane,[pv[0][0],pv[1][0],pv[2][0]])
        return mrplane

    
    def PlotPoint(self, pt, nm='', size=.2,alpha=.5,res=100,color=(0,0,0)):
        u = np.linspace(0, 2 * np.pi, res)
        v = np.linspace(0, np.pi, res)
        x = size * np.outer(np.cos(u), np.sin(v))+pt[0]
        y = size * np.outer(np.sin(u), np.sin(v))+pt[1]
        z = size * np.outer(np.ones(np.size(u)), np.cos(v))+pt[2]
        self.ax.plot_surface(x, y, z,  rstride=4, cstride=4, color=color,alpha=alpha)
        if nm != "":
            self.ax.text(pt[0],pt[1],pt[2],nm)
     
    
    def PlotLine(self,From=[0,0,0],To=[0,0,1],color=(0,0,0),linestyle='solid'):
        X=[From[0],To[0]]
        Y=[From[1],To[1]]
        Z=[From[2],To[2]]
        self.ax.plot(X,Y,Z,color=color,linestyle=linestyle)
    
    def PlotVector(self,loc,vect,color=(0,0,0), base=.05, height=.1):
        Height=self.Magnitude(vect)*height;Base=Height*base
        loc=self.FloatVector(loc);vect=self.FloatVector(vect) 
        cone = self.PutCone(loc,vect,base=Base,height=Height) 
        #cone is the sets of points for cone plotN
        #vplot is the sets of points for vector plot  
        pv = self.GenVector(vect,at=loc)
        self.ax.plot3D(pv[0],pv[1],pv[2],color=color)
        self.ax.plot_surface(cone[0],cone[1],cone[2],color=color)
        return pv
    
    

    def SphericalLinePlot(self,vr,vtheta,vphi,color=(0,0,0),linestyle='solid'):
        lnz=cos(vtheta)*vr
        lnx=cos(vphi)*sin(vtheta)*vr
        lny=sin(vphi)*sin(vtheta)*vr
        self.ax.plot3D(lnx,lny,lnz,linestyle=linestyle,color=color)
        return lnx, lny, lnz

    def CylindricalLinePlot(self,vrho,vphi,vz,color=(0,0,0),linestyle='solid'):
        lnz=vz
        lnx=cos(vphi)*vrho
        lny=sin(vphi)*vrho
        self.ax.plot3D(lnx,lny,lnz,linestyle=linestyle,color=color)
        return lnx, lny, lnz

            
    def Note(self,at,s):   #Nota Bene
        self.ax.text(at[0],at[1],at[2],s)




