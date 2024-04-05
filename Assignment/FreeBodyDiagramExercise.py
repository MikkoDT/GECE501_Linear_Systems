# -*- coding: utf-8 -*-
"""
Filename: FreeBodyDiagramExercise.py

Created on Sun Mar 31 15:12:42 2024

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


At("Exercise")
At("Use latex for all your drawing. See latex codes above for your referenc." )
At("1. Draw the free body diagram of mechanical system shown in Figure 1 (b).")
At("2. From your free body diagram, derive the equation of the mechanical \
system.")
At("3. Rearrange your equation for control system block diagram. Generate the \
control system block diagram.")

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
            \n\
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
                  \n\
\\end{tikzpicture}")              
At("\\caption{(b) Mechanical System Diagram} \\end{figure}")






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
\\begin{scope}[xshift=7cm]                                                     \n\
\\node (M) [draw,minimum width=1cm, minimum height=2.5cm] {$m$};               \n\
\\draw [-latex,ultra thick] (M.east) ++ (0.1cm,0) -- +(1cm,0)node[right=.05cm]{r};                 \n\
\\draw [-latex,ultra thick] (-2cm,.6cm) node[left=.05cm]{$F_s$} -- (-.5cm,.6cm); \n\
\\draw [-latex,ultra thick] (-2cm,0cm) node[left=.05cm]{$F_m$}-- (-.5cm,0cm); \n\
\\draw [-latex,ultra thick] (-2cm,-.6cm)node[left=.05cm]{$F_d$} -- (-.5cm,-.6cm); \n\
\\end{scope}                                                                   \n\
\\end{tikzpicture}")              
At("\\caption{(b) Free Body Diagram} \\end{figure}")


At("Alternative Drawing.")
Af("Data/ExerciseFig.png",caption="Drawn using Paint Brush",height=.25)









At("\\nocite{2}")
At("\\nocite{201}")
At("\\nocite{202}")
At("\\nocite{301}")
At("\\nocite{310}")

#At("\\bibliographystyle{plain} \n \\bibliography{ccoLib/ccoBook,ccoLib/ccoArticle}")
At("\\bibliographystyle{plain} \n \\bibliography{ccoLib/ccobib}")



At("\\end{CJK*}")    

Pb(Filename="FreeBodyDiagramsExercises.tex")