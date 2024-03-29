# -*- coding: utf-8 -*-
"""
Filename: FreeBodyDiagram.py

Created on Fri Mar 22 12:48:20 2024

@author: Celso Co
"""
#Library

from ccoLib.ccoLatex import *  #This is the library for Python-Tex coding.
from ccoLib.ccoPlot  import *
from Data.variables  import *

title="Mechanical System Diagram in LaTeX Tikz"
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
\\usetikzlibrary{shapes,arrows,positioning,    \n\
calc,patterns,decorations.pathmorphing,        \n\
decorations.markings}                          \n\
%\\usepackage{tgothic}                         \n\
\\ifpdf                                        \n\
\\usepackage[breaklinks,hidelinks]{hyperref}   \n\
\\else                                         \n\
\\usepackage{url}                              \n\
\\fi                                           \n\
%\\newcommand*\VF[1]{\mathbf{#1}}              \n\
%\\newcommand*\dif{\mathop{}\!\mathrm{d}}      \n\
\\author{"+author+"}                           \n\
\\title{"+title+"}                             \n\
\\begin{document}                              \n\
\\maketitle\n\n"


       
#initialize the PyLx as class PyLatex


#\\documentclass[10pt,a4paper]{article}\n\

PyArt=PyArticle(Headers=Preamble)
       
#Shortcut Handlers 

At=PyArt.Append_Text            #Append Frame variable
Ae=PyArt.Append_Expression      #Short cut for Atf(Ae(s,n='',c-''))
Ce=PyArt.Append_Equation        #Short cut for At(Ae(Eq(left,right),n="",c=""))
Pb=PyArt.Build                  #Build Latex File
Af=PyArt.Append_Figure          #Insert figure
Ad=PyArt.Append_Var_Dictionary  #Append Variable Dictionary
Ml=PyArt.Math_Latex             #Convertion to Math format latex    
eQ=PyArt.eQ                     #Equation List
vD=PyArt.vD                     #Variable List
tD=PyArt.TxData                 #Latex variable list
Lx=latex

At("\\newcommand\\CWht[1][2.5]{\\tikz[baseline=-#1]{\\draw[thick](0,0) \
    circle[radius=1.5mm];}}")
#CBlk is circle with black fill
At("\\newcommand\\CBlk[1][2.5]{\\tikz[baseline=-#1]{\\draw[thick,\
    fill=black!](0,0) circle[radius=1.5mm];}}")


At("\\begin{CJK*}{UTF8}{gbsn}")

tikz="https://tex.stackexchange.com/questions/175969/block-diagrams-using-tikz"

circuitikz="https://texdoc.org/serve/circuitikzmanual.pdf/0"

At("Given the mechanical system free body diagrams as shown in Figure 1, \
(a) Draw the free body diagram and write the equation for Figure 1 (a) and \
(b) Draw the free body diagram and write the equation for Figure 1 (b) ") 

At("\\begin{figure}[H]\\centering \n")
At("\\begin{tikzpicture}[every node/.style={outer sep=0pt,thick}]              \n\
\\tikzstyle{spring}=[thick,decorate,decoration={zigzag,pre length=0.3cm,post   \n\
length=0.3cm,segment length=6}]                                                \n\
\\tikzstyle{damper}=[thick,decoration={markings,mark connection node=dmp,      \n\
mark=at position 0.5 with                                                      \n\
{                                                                              \n\
\\node (dmp) [thick,inner sep=0pt,transform shape,rotate=-90,minimum           \n\
width=15pt,minimum height=3pt,draw=none] {};                                   \n\
\\draw [thick] ($(dmp.north east)+(2pt,0)$) -- (dmp.south east) --             \n\
(dmp.south west) -- ($(dmp.north west)+(2pt,0)$);                              \n\
\\draw [thick] ($(dmp.north)+(0,-5pt)$) -- ($(dmp.north)+(0,5pt)$);            \n\
}                                                                              \n\
}, decorate]                                                                   \n\
\\tikzstyle{ground}=[fill,pattern=north east lines,draw=none,minimum           \n\
width=0.75cm,minimum height=0.3cm]                                             \n\
\\node (M) [draw,minimum width=3.5cm,minimum height=2cm] {mass, $m1$};         \n\
\\node (ground1) at (M.south) [ground,yshift=-1.5cm,xshift=-1.25cm,            \n\
anchor=north] {};                                                              \n\
\\draw (ground1.north west) -- (ground1.north east);                           \n\
\\draw [spring] (ground1.north) -- node[left=.25]{s1}($(M.south east)!         \n\
(ground1.north)!(M.south west)$);                                              \n\
\\node (ground2) at (M.south) [ground,yshift=-1.5cm,anchor=north] {};          \n\
\\draw (ground2.north west) -- (ground2.north east);                           \n\
\\draw [damper] (ground2.north) -- node[left=.3]{d1}($(M.south east)!          \n\
(ground2.north)!(M.south west)$);                                              \n\
\\node (ground3) at (M.south) [ground,yshift=-1.5cm,xshift=1.25cm,             \n\
anchor=north] {};                                                              \n\
\\draw (ground3.north west) -- (ground3.north east);                           \n\
\\draw [spring] (ground3.north) -- node[left=.25]{s2}($(M.south east)!         \n\
(ground3.north)!(M.south west)$);                                              \n\
\\draw [-latex,ultra thick] (M.north) ++(0,0.2cm) -- +(0,1cm);                  \n\
%                                                                              \n\
\\begin{scope}[xshift=7cm]                                                     \n\
\\node (M) [draw,minimum width=1cm, minimum height=2.5cm] {$m$};               \n\
\\node (ground) [ground,anchor=north,yshift=-0.25cm,minimum width=1.5cm] at    \n\
(M.south) {};                                                                  \n\
\\draw (ground.north east) -- (ground.north west);                             \n\
\\draw [thick] (M.south west) ++ (0.2cm,-0.125cm) circle (0.125cm)             \n\
(M.south east) ++ (-0.2cm,-0.125cm) circle (0.125cm);                          \n\
\\node (wall) [ground, rotate=-90, minimum width=3cm,yshift=-3cm] {};          \n\
\\draw (wall.north east) -- (wall.north west);                                 \n\
\\draw [spring] (wall.170) -- node[above=.25]{s}($(M.north west)!(wall.170)!   \n\
(M.south west)$);                                                              \n\
\\draw [damper] (wall.10) -- node[above=.35]{d}($(M.north west)!(wall.10)!     \n\
(M.south west)$);                                                              \n\
\\draw [-latex,ultra thick] (M.east) ++ (0.2cm,0) -- +(1cm,0);                 \n\
\\end{scope}                                                                   \n\
%                                                                              \n\
\\draw (0cm,-4cm) node{(a)}++(5.5cm,0cm)node{(b)};                             \n\
\\end{tikzpicture}")              
At("\\caption{Mechanical System Diagram} \\end{figure}")


At("The mechanical system in Figure 1 (a) is converted into free body diagram \
as shown in Figure 2.")

At("\\begin{figure}[H]\\centering \n")
At("\\begin{tikzpicture}[every node/.style={outer sep=0pt,thick}]              \n\
\\draw (0cm,0cm) -- (0cm,0cm);                                                 \n\
\\node (M) [draw,minimum width=3.5cm,minimum height=2cm] at (5cm,0cm)          \n\
{mass, $m1$};                                                                  \n\
\\draw [-latex,ultra thick] (M.north) ++(0cm,0.1cm) -- +(0cm,1cm);             \n\
\\draw (5cm,2.4cm) node(){$r(t)\n$};                                       \n\
\\draw [-latex,ultra thick] (M.south) ++(1cm,-0.1cm) -- +(0cm,-1cm);           \n\
\\draw (4cm,-2.5cm) node(){$F_{s1}$};    \n\
\\draw [-latex,ultra thick] (M.south) ++(0cm,-0.1cm) -- +(0cm,-1cm);    \n\
\\draw (5cm,-2.5cm) node(){$F_{d1}$};    \n\
\\draw [-latex,ultra thick] (5cm,-2.75cm)--(5cm,-4cm);        \n\
\\draw (5cm,-4.25cm) node(){$F_{mass}$};    \n\
\\draw [-latex,ultra thick] (M.south) ++(-1cm,-0.1cm) -- +(0cm,-1cm);    \n\
\\draw (6cm,-2.5cm) node(){$F_{s2}$};    \n\
\\end{tikzpicture}")              
At("\\caption{Mechanical System Free Body Diagram of Figure 1 (a)} \\end{figure}")

At("Out of the free diagram in Figure 2, the system equation is generated as follows.")

Ce(Fs1+Fd1+Fs2+Fmass,rF(t))                                                    #eQ[1]   

At("where")

Ce(Fmass,m1*yF(t).diff(t,t))                                                   #eQ[2]
Ce(Fs1,k1*yF(t))                                                               #eQ[3]
Ce(Fs2,k2*yF(t))                                                               #eQ[4]
Ce(Fd1,b1*yF(t).diff(t))                                                       #eQ[5]

At("Substituting (2), (3), (4), and (5),")

Ce(m1*yF(t).diff(t,t)+b1*yF(t).diff(t)+k1*yF(t)+k2*yF(t),rF(t))                #eQ[6]

At("The equation (6) could be arranged for control system block diagram.")

Ce(rF(t)-(k1+k2)*yF(t)-b1*yF(t).diff(t),m1*yF(t).diff(t,t))                    #eQ[7]

At("\\begin{figure}[H]\\centering \n")
At("\
\\tikzstyle{block} = [draw, fill=white, rectangle,                           \n\
    minimum height=3em, minimum width=6em]                                   \n\
\\tikzstyle{sum} = [draw, fill=white, circle, node distance=1cm]             \n\
\\tikzstyle{input} = [coordinate]                                            \n\
\\tikzstyle{output} = [coordinate]                                           \n\
\\tikzstyle{pinstyle} = [pin edge={to-,thin,black}]                          \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                       \n\
\\node [input, name=input] {};                                               \n\
\\node [sum, right of=input] (sum1) {+};                                     \n\
\\node [sum, below of=sum1, node distance = 2 cm] (sum2) {+};                \n\
\\node [block, right of=sum1, node distance = 3 cm] (int1)                   \n\
    {$\\frac{1}{m1 s}$};                                                     \n\
\\node [block, right of=int1, pin={[pinstyle]above:D},                       \n\
            node distance=4cm] (int2) {$\\frac{1}{s}$};                      \n\
\\node [block, below of=int1] (dfb) {$-b_1$};                                \n\
\\draw [->] (int1) -- node[midway](u) {$\\frac{dy(t)}{dt}$} (int2);          \n\
\\node [output, right of=int2] (output) {};                                  \n\
\\node [block, below of=dfb] (fb) {$-(K_1+K_2)$};                            \n\
\\draw [draw,->] (input) -- node {$r(t)$} (sum1);                            \n\
\\draw [->] (u) |- (dfb.east);                                               \n\
\\draw [->] (sum1) -- node {$\\frac{m1d^2y(t)}{d^2t}$} (int1);               \n\
\\draw [->] (int2) -- node [name=y] {$y(t)$}(output);                        \n\
\\draw [->] (y) |- (fb);                                                     \n\
\\draw [->] (fb) -| node[below]{$-(K_1+K_2)y(t)$} (sum2)--(sum1) ;           \n\
\\draw [->] (dfb) -- node[above]{$-b_1\\frac{dy(t)}{dt}$}(sum2);             \n\
\\end{tikzpicture} ")
At("\\caption{Control System Block Diagram} \\end{figure}")

At("Exercise")
At("Use latex for all your drawing. See latex codes above for your referenc." )
At("1. Draw the free body diagram of mechanical system shown in Figure 1 (b).")
At("2. From your free body diagram, derive the equation of the mechanical \
system.")
At("3. Rearrange your equation for control system block diagram. Generate the \
control system block diagram.")

At("\\nocite{2}")
At("\\nocite{201}")
At("\\nocite{202}")
At("\\nocite{301}")
At("\\nocite{310}")

#At("\\bibliographystyle{plain} \n \\bibliography{ccoLib/ccoBook,ccoLib/ccoArticle}")
At("\\bibliographystyle{plain} \n \\bibliography{ccoLib/ccobib}")



At("\\end{CJK*}")    

Pb(Filename="FreeBodyDiagrams.tex")