# -*- coding: utf-8 -*-
"""
Created on Sat Apr 06 08:02 2024

@author: MADT


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


from sympy                     import GreaterThan, StrictGreaterThan
from sympy                     import LessThan,    StrictLessThan, LambertW
from sympy                     import And, Or, Ge, Gt, Le, Lt, Rel, S, Ne
from sympy.abc                 import x, y, z
from sympy.core.relational     import Relational
from sympy                     import laplace_transform, inverse_laplace_transform
from sympy                     import roots, Poly, Heaviside, numer, denom, gamma

import sys
import string

from sympy                      import Piecewise, piecewise_fold, And, Or, Function
from sympy                      import latex, var, symbols, solve, sqrt, dsolve, exp, log
from sympy                      import integrate, Integral, diff, preview, pi, Derivative
from sympy                      import asin, acos, atan, sin, cos, tan, oo, sinc, S
from sympy                      import summation, Sum, solve, dsolve,factorial
from sympy.matrices             import Matrix, eye, zeros, ones, diag
from mpmath                     import fourier
from sympy.abc                  import omega, tau, phi
from sympy.core.relational      import Eq, Ne, Le, Gt, Ge, Rel
from sympy.core.function        import Lambda

from sympy.polys.partfrac       import apart
from sympy.polys.polyerrors     import PolynomialError

from sympy.functions.elementary.complexes import arg, im, re, sign, Abs, conjugate

from numpy           import linspace
import numpy as np

from matplotlib.collections import PatchCollection
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# MatPlot Library
from matplotlib.axes import Axes
from matplotlib.backend_bases import FigureCanvasBase
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.axis import Axis

from matplotlib.pyplot import figure, show, axes, text, cla, draw, annotate
from matplotlib.pyplot import subplots_adjust, plot, subplot, gca, axis
from matplotlib.pyplot import show, stem, setp, hist, savefig

from matplotlib.text import Text
from matplotlib.pyplot import polar
"""



from numpy            import linspace, meshgrid, dot, cross, cos, sin, ones,\
                             arccos, arctan, arcsin, array, pi as npi, size, \
                             sqrt, outer, inner, abs, zeros, mat, matrix, exp

from sympy            import latex, solve, symbols, pi, Eq, Matrix, Function,\
                             var, Abs, cos as Cos, sin as Sin, atan as aTan, \
                             sqrt as Sqrt, acos as aCos, Inverse, tan as Tan,\
                             dsolve, I, exp as Exp, Lt, And, Or, Piecewise,  \
                             Integral, Derivative, latex, Float, Ge, Gt, Le, \
                             Lt, Ne

                
#CC Library

class PyLatex():
    '''
    This is the class for building the file for Latex format. See Latex
    manual for customization purposes.
    '''
    
    def Math_Latex(self,s): #adjust sympy LaTex for matplot latex
        tx='$'+latex(s)+'$'
        #adjustment on sympy Latex for compatibility with pyplot
        return tx

    def Text(self,s,before="\\noindent ",after="\n \par \ \par"):  #Append text 
        return before+s+after

    def Expression(self,s,p="",c="",n=""):
        #Append equation to eQ variable and return its latex format
        self.eQ.append(s)
        
        temp=  "\\begin{equation"+n+"}\n \\begin{minipage}{250pt}\n\
                \\begin{flushleft} "+p+"$\\displaystyle "+s+"$  "+c + \
               "\\end{flushleft}\n \\end{minipage}\n \\end{equation"+n+"}\n"
        return temp

    def Equation(self,lhs,rhs,e=False,p="",c="",n=""):
        #Append equation to TxData variable
        #n = "*" equation without number
        #lhs for left hand side
        #rhs for right hand side
        #p for prior text
        #c for condition or comment thereafter
        s=Eq(lhs,rhs,evaluate=e)
        self.eQ.append(s)
        temp=  "\\begin{equation"+n+"}\n \\begin{minipage}{250pt}\n\
                \\begin{flushleft} "+p+"$\\displaystyle "+latex(s)+"$  "+c + \
               "\\end{flushleft}\n \\end{minipage}\n \\end{equation"+n+"}\n"
        return temp
    
    

    def Relation(self,lhs,rhs,e=False,p="",c="",r="Le",n=""):
        #Append equation to TxData variable
        #lhs for left hand side
        #rhs for right hand side
        #p for prior text
        #c for condition or comment thereafter
        #t for type of relations namely Le Lt Ge Gt
        if   r== "Le":s=latex(Le(lhs,rhs,evaluate=e))
        elif r== "Lt":s=latex(Lt(lhs,rhs,evaluate=e))
        elif r== "Ge":s=latex(Ge(lhs,rhs,evaluate=e))
        elif r== "Gt":s=latex(Gt(lhs,rhs,evaluate=e))
        elif r== "Ne":s=latex(Ne(lhs,rhs,evaluate=e))
        elif r== "Ap":s=str(lhs)+" \\approx "+str(rhs) 
        else:return("") 
        self.eQ.append(s)
        self.rE.append([s,len(self.eQ)-1])
        temp=  "\\begin{equation"+n+"}\n \\begin{minipage}{250pt}\n"+p+ \
               "\\begin{flushleft} $\\displaystyle "+s+"$  "+c + \
               "\\end{flushleft}\n \\end{minipage}\n \\end{equation"+n+"}\n"
        return temp


    def Figure(self,filename,place="H",width=1,height=.7,caption='',
                      end="\\end{figure}\n\n"):
                      #insert fig in Frame variable
        if place != "":
            tx="\\begin{figure}["+place+"]\n"
        else: tx="\\begin{figure}\n"
        return tx+"\\centering\\includegraphics[width="  +str(width)+\
               "\\linewidth,height=" +str(height)+ \
               "\\textheight]{"+filename+"}\n\\caption{"+\
               caption+"}\n\\label{fig:"+filename+"}\n"+end

    def Build(self,Filename="PyLatex"):
        self.TxData.append('\\end{document}')
        #Creating Latex File
        f=open(Filename,'w',encoding='utf-8')
        for i in self.TxData:f.write(i)
        f.close()
        print(Filename+" Build Completed.")
        

    def Append_Var_Dictionary(self,key=""):
        neq=len(self.eQ)-1
        
        if key=="":
            try:
                k=self.eQ[neq].lhs
            except AttributeError:
                return "Not an equation but expression. key needed"
            else:
                rhs=self.eQ[neq].rhs
        else:
            k=key
            rhs=self.eQ[neq]
        
        try:
            self.vD[k]
        except KeyError:     
            self.vD[k]=[[neq,"("+str(neq)+")",rhs]]
                
        else:
            self.vD[k].append([neq,"("+str(neq)+")",rhs])        
        
        


class PyBeamer(PyLatex):
    '''
    This is the class for building the file for Latex format. See Latex
    manual for customization purposes. This is for beamer format.
    '''

    def __init__(self,Headers='',authors='',title='',subtitle='',institute='',
                      date='',  logo='', subject=''):

        if Headers != '':
            self.Headers=Headers
        else:
            self.Headers='\
\\documentclass[11pt]{beamer}\n\
\\usetheme{default}\n\
\\usepackage[ascii]{inputenc}\n\
\\usepackage[T1]{fontenc}\n\
\\usepackage{amsmath,esint}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{xcolor}\n\
\\usepackage{graphicx}\n\
\\author{'+authors+'}\n\
\\title{'+title+'}\n\
\\subtitle{'+subtitle+'}\n\
\\logo{'+logo+'}\n\
\\institute{'+institute+'}\n\
\\date{'+date+'}\n\
\\subject{'+subject+'}\n\
\\setbeamercovered{transparent}\n\
\\setbeamertemplate{navigation symbols}{}\n\
\\newcommand*\VF[1]{\mathbf{#1}}\n\
\\newcommand*\dif{\mathop{}\!\mathrm{d}}\n\
\\begin{document}\n\
\\maketitle\n\n'

        self.TxData=[self.Headers]
        self.FrameData=[]
        self.Frame=[]
        self.eQ=[title]   #variable for equation
        self.rE=[title]   #variable for relation
        self.vD={}        #variable dictionary       
   

    def Append_Text(self,s,before="\\noindent ",after="\n \par \ \par"):   #Append text to Frame variable
        self.Frame.append(self.Text(s,before,after))

    def Create_Frame(self,title=''): #Create Frame
        Number=str(len(self.FrameData)+1)+" "
        self.FrameData.append(self.Frame)
        self.TxData.append('\\begin{frame}\n')
        self.TxData.append('\\frametitle{'+Number+title+'}\n')
        for i in self.Frame:self.TxData.append(i)
        self.TxData.append('\n\\end{frame}\n\n')
        self.Frame=[]
        print("Frame no.",Number," done.")

    def Append_Relation(self,lhs,rhs,e=False,p="",c="",r="Le",n=""):
        #Append equation to TxData variable
        #lhs for left hand side
        #rhs for right hand side
        #p for prior text
        #c for condition or comment thereafter
        #t for type of relations namely Le Lt Ge Gt
        self.TxData.append(self.Relation(lhs,rhs, e=e,p=p,c=c,r=r,n=n))
    
    def Append_Expression(self,s,p="",c="",n=""):
        #s is the symbolic expression
        #x is the latex expression of s formatted to desired display
        #p is text before the expression s
        #c is condition
        self.Frame.append(self.Expression(s,p=p,c=c,n=n))

    def Append_Equation(self,lhs,rhs,e=False,p="",c="",n=""):
        #lhs and rhs are the left and righ hands of equation
        #x is the latex expression of equation formatted to desired display
        #p is text before the expression s
        #c is condition
        self.Frame.append(self.Equation(lhs,rhs,e=e,p=p,c=c,n=n))

    def Append_Figure(self,filename,place="H",width=1,height=.7,caption='',
                      end="\\end{figure}\n\n"):
        self.Frame.append(self.Figure(filename,place=place, width=width,
                                      height=height,caption=caption,end=end))
     
            

class PyArticle(PyLatex):

    '''
    This is the class for building the file for Latex format. See Latex
    manual for customization purposes. This is for beamer format.
    '''
    def __init__(self,Headers='',authors='',title='',institute='',date=''):
        if Headers != '':
            self.Headers=Headers
        else:
            self.Headers=\
"\\documentclass[10pt,a4paper]{article}\n\
\\usepackage[latin1]{inputenc}\n\
\\usepackage[T1]{fontenc}\n\
\\usepackage{amsmath,esint}\n\
\\usepackage{amsfonts}\n\
\\usepackage{amssymb}\n\
\\usepackage{xcolor}\n\
\\usepackage{mathrsfs}\n\
\\usepackage{makeidx}\n\
\\usepackage{graphicx}\n\
\\usepackage{float}\n\
\\usepackage{gensymb}\n\
\\usepackage{ifpdf}\n\
\\usepackage{tikz}                            \n\
\\usetikzlibrary{shapes,arrows}               \n\
%\\usepackage{tgothic}\n\
\\ifpdf\n\
\\usepackage[breaklinks,hidelinks]{hyperref}\n\
\\else \n\
\\usepackage{url}\n\
\\fi\n\
\\newcommand*\VF[1]{\mathbf{#1}}\n\
\\newcommand*\dif{\mathop{}\!\mathrm{d}}\n\
\\author{"+authors+"}\n\
\\title{"+title+"}\n\
\\begin{document}\n\
\\maketitle\n\n"
        self.TxData=[self.Headers]   #storage for latex text
        self.eQ=[title]              #storage variable for equation
        self.rE=[title]              #storage variable for relation
        self.vD={}                   #starage dictionary of variables            
        
   
    def Append_Text(self,s,before="\\noindent ",after="\n \par \ \par"):   #Append text to Frame variable
        self.TxData.append(self.Text(s,before,after))
    

    def Append_Expression(self,s,p="",c="",n=""):
        #s is the symbolic expression
        #p is text before the expression s
        #c is condition
        self.TxData.append(self.Expression(s,p=p,c=c,n=n))
    

    def Append_Equation(self,lhs,rhs,e=False,p="",c="",n=""):
        #lhs and rhs are the left and righ hands of equation
        #x is the latex expression of equation formatted to desired display
        #p is text before the expression s
        #c is condition
        #with \\\ the next line.
        self.TxData.append(self.Equation(lhs,rhs, e=e,p=p,c=c,n=n))

    def Append_Relation(self,lhs,rhs,e=False,p="",c="",r="Le",n=""):
        #Append equation to TxData variable
        #lhs for left hand side
        #rhs for right hand side
        #p for prior text
        #c for condition or comment thereafter
        #t for type of relations namely Le Lt Ge Gt
        self.TxData.append(self.Relation(lhs,rhs, e=e,p=p,c=c,r=r,n=n))

    def Append_Figure(self,filename,place="H",width=1,height=.7,caption='',
                      end="\\end{figure}\n\n"):
        self.TxData.append(self.Figure(filename,place=place, width=width,
                                       height=height,caption=caption,end=end))

 
    
        
            



