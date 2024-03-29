# -*- coding: utf-8 -*-
"""
Filename: BlockDiagrams.py

Created on Sat Aug 27 00:11:47 2022
Rev1    on Wed Sep 27 10:17:50 2023

@author: CBCO
"""


#Library

from ccoLib.ccoLatex import      *  #This is the library for Python-Tex coding.
from ccoLib.ccoPlot import *


title="Block Diagram in LaTeX Tikz"
author="CBCO"

Preamble="\
\\documentclass[10pt,a4paper]{article}                                         \n\
\\usepackage{CJKutf8}                                                          \n\
\\usepackage{inputenc}                                                         \n\
\\usepackage[T1]{fontenc}                                                      \n\
\\usepackage{amsmath,esint}                                                    \n\
\\usepackage{amsfonts}                                                         \n\
\\usepackage{amssymb}                                                          \n\
\\usepackage{xcolor}                                                           \n\
\\usepackage{mathrsfs}                                                         \n\
\\usepackage{makeidx}                                                          \n\
\\usepackage{graphicx}                                                         \n\
\\usepackage{float}                                                            \n\
\\usepackage{textcomp}                                                         \n\
\\usepackage{gensymb}                                                          \n\
\\usepackage{ifpdf}                                                            \n\
\\usepackage{tikz}                                                             \n\
\\usepackage[siunitx]{circuitikz}                                              \n\
\\usetikzlibrary{shapes,arrows,positioning}                                    \n\
%\\usepackage{tgothic}                                                         \n\
\\ifpdf                                                                        \n\
\\usepackage[breaklinks,hidelinks]{hyperref}                                   \n\
\\else                                                                         \n\
\\usepackage{url}                                                              \n\
\\fi                                                                           \n\
%\\newcommand*\VF[1]{\mathbf{#1}}                                              \n\
%\\newcommand*\dif{\mathop{}\!\mathrm{d}}                                      \n\
\\author{"+author+"}                                                           \n\
\\title{"+title+"}                                                             \n\
\\begin{document}                                                              \n\
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

 


At("\\section{Block Diagrams }")

At("The typical control system diagram in Figure 1 was drawn using \\href{ "+
tikz+"}{Tikz}. The Figure 1 (a) was basic control system. The Figure 1 (b) \
was the simplification of Figure 1 (a). \n")


#Figure 1

At("\\begin{figure}[H] \\centering \n")

At("\
\\tikzstyle{block}=[draw, fill=white, rectangle,                             \n\
minimum height=3em,minimum width=6em]                                        \n\
\\tikzstyle{sum} = [draw, fill=white, circle, node distance=1cm]             \n\
\\tikzstyle{input} = [coordinate]                                            \n\
\\tikzstyle{output} = [coordinate]                                           \n\
\\tikzstyle{pinstyle} = [pin edge={to-,thin,black}]                          \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                       \n\
%(a)                                                                         \n\
\\node [input, name=input] {};                                               \n\
\\node [sum, right of=input] (sum) {};                                       \n\
\\node [block, right of=sum] (controller) {Controller};                      \n\
\\node [block, right of=controller, pin={[pinstyle]above:D},                 \n\
            node distance=3cm] (system) {System};                            \n\
\\draw [->] (controller) -- node[name=u] {$u$} (system);                     \n\
\\node [output, right of=system] (output) {};                                \n\
\\node [block, below of=u] (measurements) {Measurements};                    \n\
\\draw [draw,->] (input) -- node {$r$} (sum);                                \n\
\\draw [->] (sum) -- node {$e$} (controller);                                \n\
\\draw [->] (system) -- node [name=y] {$y$}(output);                         \n\
\\draw [->] (y) |- (measurements);                                           \n\
\\draw [->] (measurements) node [below=1cm ]{$(a)$} -| node[pos=0.99] {$-$}  \n\
        node [near end] {$y_m$} (sum) ;                                      \n\
%(b)                                                                         \n\
\\node [input, below of =input, node distance = 5cm](input1) {};             \n\
\\node [sum, right of=input1] (sum1) {};                                     \n\
\\node [block, right of=sum1, node distance = 3.5cm]                         \n\
    (feedforward) {Feedforward=Ff};                                          \n\
\\node [output, right of=feedforward, node distance = 3cm] (output1) {};     \n\
\\node [block, below of=feedforward] (feedback) {Feedback=Fb};               \n\
\\draw [draw,->] (input1) -- node {$r$} (sum1);                              \n\
\\draw [->] (sum1) -- node {$e$} (feedforward)                               \n\
    -- node [name=y1] {$y$}(output1);                                        \n\
\\draw [->] (output1) |- (feedback);                                         \n\
\\draw [->] (feedback) node [below=1cm ]{$(b)$} -| node[pos=0.99] {$-$}      \n\
        node [near end] {$y_m$} (sum1) ;                                     \n\
\\node [input, below of =input, node distance = 5cm](input1) {};             \n\
\\node [sum, right of=input1] (sum1) {};                                     \n\
\\node [block, right of=sum1, node distance = 3.5cm]                         \n\
    (feedforward) {Feedforward=Ff};                                          \n\
\\node [output, right of=feedforward, node distance = 3cm] (output1) {};     \n\
\\node [block, below of=feedforward] (feedback) {Feedback=Fb};               \n\
\\draw [draw,->] (input1) -- node {$r$} (sum1);                              \n\
\\draw [->] (sum1) -- node {$e$} (feedforward)                               \n\
    -- node [name=y1] {$y$}(output1);                                        \n\
\\draw [->] (output1) |- (feedback);                                         \n\
\\draw [->] (feedback) node [below=1cm ]{$(b)$} -| node[pos=0.99] {$-$}      \n\
        node [near end] {$y_m$} (sum1) ;                                     \n\
\\end{tikzpicture} ")

At("\\caption{Block diagram}\n\
    \\end{figure}\n")

At("\par \ \par")

r, e, ym, y, Ff, Fb, iin,   iout,   vin,   vout,   R, C, L, t= symbols("\
r  e  y_m y  F_f F_b i_{in} i_{out} v_{in} v_{out} R  C  L t ")

iinF  = Function(iin)
voutF = Function(vout)

At("Consider Figure 1 (b). The following equations were noted. Note that the \
   negative sign in sum means negative feedback. ")

Ce(e, r - ym)                                                                  #1
Ce(ym,Fb*y)                                                                    #2 
Ce(y,Ff*e)                                                                     #3

At("Eliminating e, and ym ")

Ce(y,Ff*(r-Fb*y))                                                              #4
Ce(y*(1+Fb*Ff),Ff*r)                                                           #5
Ce(y,Eq(Ff/(1+Fb*Ff)*r,1/(1/Ff+Fb)*r))                                         #6

Ae("y \\approx \\frac{1}{F_b}r \\quad for 1 << F_f")                           #7

At("The open loop gain was feedforward. The close loop gain was reciprocal of \
   feedback. If Fb = 1, then y=r. It was called unity feedback. Current mirrors \
   made used of unity feedback. ")

 
At("\\section{Block Diagrams of Schematic Passive Circuit Components}")   

#Figure 2 Resistor Circuit and Block Diagram

At("\\subsection{Resistor}")

At("\\begin{figure}[H] \\centering \n")

At("\\begin{circuitikz}[american]   \n\
\draw (0,0) to[isource, l=$I_{in}$] (0,3) -- (2,3) \n\
to[R=$R$, v=$V_{out}$, i=$i_{in}$] (2,0) -- (0,0) \n\
node[left, below=2cm]{$\hspace{2cm}(a)$}; \n\
\draw (0,0) -- (0,-1 )node[ground]{};\n\
\end{circuitikz}")


At("\\begin{circuitikz}[american]   \n\
\draw (0,0) to[vsource, V=$V_{in}$] (0,3) -- \n\
(2,3) \n\
to[R=$R$, v=$V_{in}$, i=$i_{out}$] (2,0) -- (0,0)\n\
node[left, below=2cm]{$\hspace{2cm}(c)$}; \n\    ; \n\
\draw (0,0) -- (0,-1 )node[ground]{};\n\
\end{circuitikz}")


At("\par \ \par")




At("\\hspace{.5cm}\n\
\\tikzstyle{block} = [draw, fill=white, rectangle,                             \n\
    minimum height=3em, minimum width=6em]                                     \n\
\\tikzstyle{input} = [coordinate]                                              \n\
\\tikzstyle{output} = [coordinate]                                             \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                         \n\
\\node [input, above = 2cm,  name=in] {};                                      \n\
\\node [block, right of=in] (iv) {$v_{out}=R*i_{in}$};                         \n\
\\node [output, right of=iv] (out) {$v_{out}$};                                \n\
\\draw [->] (in)  -- node {$i_{in}$} (iv);                                     \n\
\\draw [->] (iv) node[below=.75cm]{$(b)$}-- node [name=v] {$v_{out}$}(out);    \n\
\\end{tikzpicture}\\hspace{.5cm}")              

At("\
\\tikzstyle{block} = [draw, fill=white, rectangle,                             \n\
    minimum height=3em, minimum width=6em]                                     \n\
\\tikzstyle{input} = [coordinate]                                              \n\
\\tikzstyle{output} = [coordinate]                                             \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                         \n\
\\node [input, above = 2cm,  name=in] {};                                      \n\
\\node [block, right of=in] (iv) {$i_{out}=R^{-1}*v_{in}$};                    \n\
\\node [output, right of=iv] (out) {$i_{out}$};                                \n\
\\draw [->] (in)  -- node {$v_{in}$} (iv);                                     \n\
\\draw [->] (iv) node[below=.75cm]{$(d)$}-- node [name=i] {$i_{out}$}(out);    \n\
\\end{tikzpicture}")                                                   


At("\\caption{Resistor Circuits schematic to Resistor blocks diagram}          \n\
    \\end{figure}\n")

At("\par \ \par")

At("The resistor schematic circuit diagram was shown in Figure 2 (a). It had a \
    current source as input. Its block diagram was shown in Figure 2 (b). The \
    resistor schematic circuit diagram with voltage source as input was shown \
    in Figure 2 (c). ")

At("The equations of Resistor in time domain were the following." )

Ce(voutF(t),R*iinF(t))                                                         #8
Ce(iinF(t),R**-1*voutF(t))                                                     #9

#Figure 3 Capacitor Circuit and Block Diagram

At("\\subsection{Capacitor}")

At("\\begin{figure}[H] \\centering \n")


At("\\begin{circuitikz}[american]                                              \n\
\draw (0,0) to[isource, l=$I_{in}$] (0,3) --(2,3) \n\
to[C=$C$, v=$V_{out}$, i=$i_{in}$] (2,0) -- (0,0) \n\
node[left, below=2cm]{$\hspace{2cm}(a)$}; \n\
\draw (0,0) -- (0,-1 )node[ground]{};\n\
\end{circuitikz}")


At("\\begin{circuitikz}[american]   \n\
\draw (0,0) to[vsource, V=$V_{in}$] (0,3) -- \n\
(2,3) \n\
to[C=$C$, v=$V_{in}$, i=$i_{out}$] (2,0) -- (0,0)\n\
node[left, below=2cm]{$\hspace{2cm}(a)$}; \n\
\draw (0,0) -- (0,-1 )node[ground]{};\n\
\end{circuitikz}")


At("\par \ \par")

At("\\hspace{.5cm}\n\
\\tikzstyle{block} = [draw, fill=white, rectangle,                           \n\
    minimum height=3em, minimum width=6em]                                   \n\
\\tikzstyle{input} = [coordinate]                                            \n\
\\tikzstyle{output} = [coordinate]                                           \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                       \n\
\\node [input, above = 2cm,  name=in] {};              \n\
\\node [block, right of=in] (iv) {$v_{out}=C^{-1}\\int{i_{in}dt}$};                               \n\
\\node [output, right of=iv] (out) {$v_{out}$};                                 \n\
\\draw [->] (in)  -- node {$i_{in}$} (iv);                                      \n\
\\draw [->] (iv) node[below=.75cm]{$(b)$}-- node [name=v] {$\\hspace{.5cm}v_{out}$}(out);                                  \n\
\\end{tikzpicture}\\hspace{.5cm}")              



At("\
\\tikzstyle{block} = [draw, fill=white, rectangle,                             \n\
    minimum height=3em, minimum width=6em]                                     \n\
\\tikzstyle{input} = [coordinate]                                              \n\
\\tikzstyle{output} = [coordinate]                                             \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                         \n\
\\node [input, above = 2cm,  name=in] {};                                      \n\
\\node [block, right of=in] (iv) {$i_{out}=C\\frac{dv_{in}}{dt}$};             \n\
\\node [output, right of=iv] (out) {$i_{out}$};                                \n\
\\draw [->] (in)  -- node {$v_{in}$} (iv);                                     \n\
\\draw [->] (iv) node[below=.75cm]{$(d)$}-- node [name=i] {$i_{out}$}(out);    \n\
\\end{tikzpicture}")                                                   

At("\\caption{Capacitor Circuits schematic to Capacitor blocks diagram}\n\
    \\end{figure}\n")

At("\par \ \par")

At("The schematic circuit diagram of capacitor with current source as input \
    was shown in Figure 3 (a). Its block diagram was shown in Figure 3 (b). \
    Its schematic circuit diagram with voltage source as input was shown in \
    Figure 3 (c). Its block diagram was shown in Figure 3 (d). The capacitor \
    equations were expressed as follows.")

Ce(voutF(t),1/C*iinF(t).integrate(t))                                          #10
Ce(iinF(t),C*voutF(t).diff(t))                                                 #11   

#Figure 4 Inductor Circuit and Block Diagram

At("\\subsection{Inductor}")

At("\\begin{figure}[H] \\centering \n")

At("\\begin{circuitikz}[american]                                              \n\
\draw (0,0) to[isource, l=$I_{in}$] (0,3) -- (2,3)                             \n\
to[L=$L$, v=$V_{out}$, i=$i_{in}$] (2,0) -- (0,0)                              \n\
node[left, below=2cm]{$\hspace{2cm}(a)$};                                      \n\
\draw (0,0) -- (0,-1 )node[ground]{};                                          \n\
\end{circuitikz}")


At("\\begin{circuitikz}[american]                                              \n\
\draw (0,0) to[vsource, V=$V_{in}$] (0,3) -- (2,3)                             \n\
to[L=$L$, v=$V_{in}$, i=$i_{out}$] (2,0) -- (0,0)                              \n\
node[left, below=2cm]{$\hspace{2cm}(a)$};                                      \n\
\draw (0,0) -- (0,-1 )node[ground]{};                                          \n\
\end{circuitikz}")


At("\par \ \par")


At("\\hspace{.5cm}\n\
\\tikzstyle{block} = [draw, fill=white, rectangle,                             \n\
    minimum height=3em, minimum width=6em]                                     \n\
\\tikzstyle{input} = [coordinate]                                              \n\
\\tikzstyle{output} = [coordinate]                                             \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                         \n\
\\node [input, above = 2cm,  name=in] {};                                      \n\
\\node [block, right of=in] (iv) {$v_{out}=L\\frac{i_{in}}{dt}$};              \n\
\\node [output, right of=iv] (out) {$v_{out}$};                                \n\
\\draw [->] (in)  -- node {$i_{in}$} (iv);                                     \n\
\\draw [->] (iv) node[below=.75cm]{$(b)$}-- node [name=v] \
    {$\\hspace{.5cm}v_{out}$}(out);                                            \n\
\\end{tikzpicture}\\hspace{.5cm}")              


At("\
\\tikzstyle{block} = [draw, fill=white, rectangle,                             \n\
    minimum height=3em, minimum width=6em]                                     \n\
\\tikzstyle{input} = [coordinate]                                              \n\
\\tikzstyle{output} = [coordinate]                                             \n\
\\begin{tikzpicture}[auto, node distance=2cm,>=latex']                         \n\
\\node [input, above = 2cm,  name=in] {};                                      \n\
\\node [block, right of=in] (iv) {$i_{out}=L\\int{dv_{in}}{dt}$};              \n\
\\node [output, right of=iv] (out) {$i_{out}$};                                \n\
\\draw [->] (in)  -- node {$v_{in}$} (iv);                                     \n\
\\draw [->] (iv) node[below=.75cm]{$(d)$}-- node [name=i] {$i_{out}$}(out);    \n\
\\end{tikzpicture}")                                                   

At("\\caption{Inductor Circuits schematic to Inductor blocks diagram}\n\
    \\end{figure}\n")




At("\par \ \par")


At("The schematic circuit diagram of inductor with current source as input \
    was shown in Figure 3 (a). Its block diagram was shown in Figure 3 (b). \
    Its schematic circuit diagram with voltage source as input was shown in \
    Figure 3 (c). Its block diagram was shown in Figure 3 (d). The inductor \
    equations were expressed as follows.")

Ce(voutF(t),L*iinF(t).diff(t))                                                 #12
Ce(iinF(t),1/L*voutF(t).diff(t))                                               #13


At("\\section{Emitter Follower}")


At("\\begin{figure}[H] \\centering \n")
At("\\begin{circuitikz}[american]                                              \n\
\draw (0,0) to[vsource=$V_{ref}$](0,3);                                        \n\
\draw (4,0) to[R=$R_e$](4,3);                                                  \n\
\draw (0,0) --(0,-.5) node[ground]{};                                          \n\
\draw (4,0) --(4,-.5) node[ground]{};                                          \n\
\draw (4,4) node[npn](npn1){Q1};                                               \n\
\draw (4,5) to[R=$R_c$](4,8);                                                  \n\
\draw (7,9) to[vsource=$V_{cc}$](7,5);                                         \n\
\draw (7,5) --(7, 5) node[ground]{};                                           \n\
\draw (4,8) |- (7,9);                                                          \n\
\draw [->] (npn1.C) -- (4,5) node[midway]{}--(5,5)node[]{$\\hspace{.5cm} V_c$};\n\
\draw (npn1.E) -- (4,3) -- (5,3) node[]{$\hspace{.5cm}V_e$};                   \n\
\draw (npn1.B) -| (0,3)node[left]{$V_{ref}$};                                  \n\
\draw (3.5,3.5) node[]{$V_{be}$};                                              \n\
\\end{circuitikz}")
At("\\caption{Schematic Circuit diagram of emitter follower}                   \n\
    \\end{figure}\n")


At("\\begin{figure}[H] \\centering \n")
At("\\begin{tikzpicture}                                                       \n\
\\node[draw, circle, minimum size=0.5cm] (sum1){+};                            \n\
\\node [draw,  minimum width=1cm, minimum height=1cm,                          \n\
    right=2cm of sum1] (Q1e) {$I_e=I_se^{\\frac{V_{be}}{V_T}}$};               \n\
\\node [draw,  minimum width=1cm, minimum height=1cm,                          \n\
    below= of Q1e] (Re) {$-V_{re}=-I_eR_e$};                                   \n\
\\node [draw,  minimum width=1cm, minimum height=1cm,                          \n\
    right= 2cm of Q1e] (Q1c) {$I_{c}=I_e\\frac{h_{fe1}}{h_{fe1}+1}$};          \n\
\\node [draw, minimum width=1cm, minimum height =1cm,                          \n\
    below = of Q1c](Rc){$V_c = I_c Rc$};                                       \n\
\\draw[->] ++(-1.5,0) --  (sum1.west) node[midway,above]{$V_{ref}$};           \n\
\\draw [->] (sum1) -- (Q1e)node[midway,above ]{$V_{be}$};                      \n\
\\draw [->] (Q1e)-- (Q1c)node[midway,above](m1){$I_e$};                        \n\
\\draw [->] (m1) |-(Re) -| (sum1.south) node[midway,below]{$-V_{R_e}$};        \n\
\\draw [->] (Q1c) -- (Rc)node[right]{$I_c$} -- (9cm,-2cm)node[above]{$V_c$};   \n\
\\end{tikzpicture}")


At("\\caption{Control System Block Diagram of Emitter Follower Circuit of \
    Figure 8} \\end{figure}\n")



At("\\section{Block Diagram of current Mirrors}")

At("\\subsection{Widlar Current Mirror}")

At("\\begin{figure}[H] \\centering \n")
At("\\begin{circuitikz}[american]                                              \n\
\draw (2,0) node[npn,xscale=-1](npn1){Q1};                                     \n\
\draw (npn1.E) --(2,-.5) node[ground]{};                                       \n\
\draw (npn1.C) -| (npn1.B);                                                    \n\
\draw (2,4) to[isource, ](2,2)--node[left]{$I_{in}$}(npn1.C);                  \n\
\draw (2,4) -|  (3,3.5)node[ground]{};                                         \n\
\draw (4,0) node[npn](npn2){Q2};                                               \n\
\draw (npn1.B) --node[below]{$V_{be}$} (npn2.B);                               \n\
\draw (npn2.E) --(4,-.5) node[ground]{};                                       \n\
\draw (npn2.C) to[R=$R1$,](4,3) -|(6,2) to[vsource](6,0)--                     \n\
      (6,-.5) node[ground]{};                                                  \n\
\\end{circuitikz}")

At("\\caption{Widlar current mirror schematic diagram}                         \n\
    \\end{figure}\n")




At("\\subsection{Wilson Current Mirror}")

At("\\begin{figure}[H] \\centering \n")
At("\\begin{circuitikz}[american]                                              \n\
\draw (2,0) node[npn,xscale=-1](npn1){Q1};                                     \n\
\draw (npn1.E) --(2,-.5) node[ground]{};                                       \n\
\draw (2,6) to[isource, ](2,4)--node[left]{$I_{in}$}(npn1.C);                  \n\
\draw (2,6) -|  (3,5.5)node[ground]{};                                         \n\
\draw (4,0) node[npn](npn2){Q2};                                               \n\
\draw (npn1.B) --node[below]{$V_{be}$} (npn2.B);                               \n\
\draw (npn2.E) --(4,-.5) node[ground]{};                                       \n\
\draw (4,2) node[npn](npn3){Q3};                                               \n\
\draw (npn2.C) -| (npn2.B);                                                    \n\
\draw (npn3.C) to[R=$R1$,](4,6) -|(6,2) to[vsource](6,0)--                     \n\
      (6,-.5) node[ground]{};                                                  \n\
\draw (npn3.E)-- (npn2.C);                                                     \n\
\draw (2,2) -- (npn3.B);                                                       \n\
\\end{circuitikz}")

At("\\caption{Wilson current mirror schematic diagram}\n\
    \\end{figure}\n")


At("\\section{Exercises}")

At("1. Write the Equations of Widlar current mirror. (5)")
At("2. Draw the Widlar block diagram. (5) ")
At("3. Write the equations of Wilson current mirror. (5)")
At("4. Draw the block diagram of Wilson current mirror. (5)")
At("5.There is a portion of Wilson current mirror that is Widlar current \
mirror. Draw the block diagram of Wilson current mirror incorporating a block \
that is the Widlar currrent mirror. (5)")


At("\\nocite{2}")
At("\\nocite{201}")
At("\\nocite{202}")
At("\\nocite{301}")
At("\\nocite{310}")

#At("\\bibliographystyle{plain} \n \\bibliography{ccoLib/ccoBook,ccoLib/ccoArticle}")
At("\\bibliographystyle{plain} \n \\bibliography{ccoLib/ccobib}")



At("\\end{CJK*}")    

Pb(Filename="BlockDiagrams.tex")