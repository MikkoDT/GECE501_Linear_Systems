#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: Assessment.py

Created on Fri Jun 24 21:06:57 2022

@author: celso
"""   


from ccoLib.ccoLatex import *  
"The library for python interface with latex It is in the folder ccoLib. \
 与乳胶的蟒蛇接口的库 它位于文件夹 ccoLib 中。   "
from ccoLib.ccoPlot  import *
"The library for python plots and symbolic math. It is in the folder ccoLib. \
 用于蟒蛇图和符号数学的库。它位于文件夹 ccoLib 中。   "

title="Symbolic Math of Python"
author="CBCO"

Preamble="\
\\documentclass[10pt,a4paper,leqno]{article}         \n\
\\usepackage{CJKutf8}                          \n\
\\usepackage{inputenc}                         \n\
\\usepackage[T1]{fontenc}                      \n\
\\usepackage{amsmath,esint}                    \n\
\\usepackage{amsfonts}                         \n\
\\usepackage{amssymb}                          \n\
\\usepackage{xcolor}                           \n\
\\usepackage{mathrsfs}                         \n\
\\usepackage{makeidx}                          \n\
\\usepackage{graphicx}                         \n\
\\usepackage{float}                            \n\
\\usepackage{textcomp}                         \n\
\\usepackage{gensymb}                          \n\
\\usepackage{ifpdf}                            \n\
\\usepackage{tikz}                             \n\
\\usepackage[siunitx]{circuitikz}              \n\
\\usetikzlibrary{shapes,arrows,positioning}    \n\
%\\usepackage{tgothic}                         \n\
\\ifpdf                                        \n\
\\usepackage[breaklinks,hidelinks]{hyperref}   \n\
\\else                                         \n\
\\usepackage{url}                              \n\
\\fi                                           \n\
%\\newcommand*\VF[1]{\mathbf{#1}}              \n\
%\\newcommand*\dif{\mathop{}\!\mathrm{d}}      \n\
\\begin{document}                              \n\
\\author{"+author+"}                           \n\
\\title{"+title+"}                             \n\
\\maketitle\n\n"

"The preamble is the list of packages and certain commands for latex operation. \
 The interface library is ccoLatex.py. \
 前导码是用于乳胶操作的包和某些命令的列表。 接口库已 ccoLatex.py。    "
       

PyArt=PyArticle(Headers=Preamble)
       
#Shortcut Handlers 
At=PyArt.Append_Text            #Append text to tD variable 
Ae=PyArt.Append_Expression      #Append expression to eQ variable and to tD as latex
Ce=PyArt.Append_Equation        #Append equation to eQ variable and to tD as latex
Pb=PyArt.Build                  #Build Latex File *.tex out of tD variable
Af=PyArt.Append_Figure          #Insert figure in tD variable
Ad=PyArt.Append_Var_Dictionary  #Append an equation or expression to Dictionary variable
Ml=PyArt.Math_Latex             #Convertion to text to Math format latex   
eQ=PyArt.eQ                     #Equation variable List
vD=PyArt.vD                     #Dictionary Variable List
tD=PyArt.TxData                 #Latex variable list
Lx=latex                        #Latex function

At("\\begin{CJK*}{UTF8}{gbsn}")


#Links to latex drawing and circuit schematics
#乳胶图纸和电路原理图的链接
tikz="https://tex.stackexchange.com/questions/175969/block-diagrams-using-tikz"
circuitikz="https://texdoc.org/serve/circuitikzmanual.pdf/0"



Reference="Urs Graf, \"Applied Laplace Transforms and z-Transforms for \
    Scientists and Engineers \", Copyrights \\copyright 2004 Springer \
    Basel AG, ISBN 978-3-0348-9593-4  "

from Data.variables import *



At("\\section{Exercises 1}" )

At("Find y(t) of the following Laplace transforms for $t \\ge 0$")

Ce(YF(s),s/(s+2),n="*",p="1\quad")

Ce(YF(s),(3*s-5)/(s**2+4*s+2),n="*",p="2\quad")

Ce(YF(s),(3-6*Exp(-2*s))/((s+2)*(s+3)),n="*",p="3\quad")

Ce(YF(s),10/(s**3+2*s**2+5*s),n="*",p="4\quad")

Ce(YF(s),4*(s+1)/((s+2)*(s+3)**2),n="*",p="5\quad")



At("\\section{Exercises 2}" )

At("Solve the following differential equation using Laplace transform for \n\
   $t \\ge 0$ with the given initial condition")

Ce(yF(t).diff(t)+4*y,6*Exp(-2*t),n="*",p="1\quad")
Ce(yF(zeroN),3,n="*")

Ce(yF(t).diff(t)+y,3*Cos(2*t),n="*",p="2\quad")
Ce(yF(zeroN),0,n="*")

Ce(yF(t).diff(t,t)+7*yF(t).diff(t)+12*y,4,n="*",p="3\quad")
Ce(yF(zeroN),3,n="*")
Ce(yPF(zeroN),0,n="*")


Ce(yF(t).diff(t,t)+4*yF(t).diff(t)+20*y,4,n="*",p="4\quad")
Ce(yF(zeroN),-2,n="*")
Ce(yPF(zeroN),0,n="*")

Ce(yF(t).diff(t,t,t)+5*yF(t).diff(t,t)+6*yF(t).diff(t),0,n="*",p="5\quad")
Ce(yF(zeroN),3,n="*")
Ce(yPF(zeroN),-2,n="*")
Ce(yPPF(zeroN),7,n="*")



At("\\end{CJK*}")   
Pb(Filename="Assessment.tex")
