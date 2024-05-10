# -*- coding: utf-8 -*-
"""
File: consultancy.py
Created on Wed Feb 23 09:08:52 2022

@author: Celso Co
"""

#Consultancy Template


import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Abanilla, Mico M.",
            "Cao, Michael Angelo R.",
            "Alano, Alyssa B.",
            "Catapang, Ashley J.",
            "Canaling, Daniella P." 
        ],
        "WT Ct": [2, 4, 3, 1, 3],
        "WT Ce": [5, 3, 1, 0, 2],
        "WS Ct": [4, 2, 3, 2, 3],
        "WS Ce": [3, 1, 2, 2, 3],
        "OS Ct": [0, 0, 0, 0, 0],
        "OS Ce": [0, 0, 0, 0, 0],
    }
)
    
print(df)
  

consultancy_table='\\begin{table}[H]\\centering \\caption{Consultant/Consultee}\n\
       \\scriptsize \\begin{tabular}\n\
       {|p{.5cm}|p{3.5cm}|p{1.42cm}|p{1.42cm}|p{1.42cm}|}\n\
       \\hline Nos &SamSan Tech & Within Team & Within Section & Outside Section  \n\
       \\end{tabular}\n\
       \\scriptsize \\begin{tabular}\n\
       {|p{.5cm}|p{3.5cm}|p{.5cm}|p{.5cm}|p{.5cm}|p{.5cm}|p{.5cm}|p{.5cm}|}\n\
       \\hline Nos &Name &Ct &Ce   &Ct   &Ce  &Ct  & Ce \\\ \n'
for i in range(len(df['Name'])):
    consultancy_table+='\\hline '+str(i+1)+'&'+df['Name'][i]+'&'+str(df['WT Ct'][i])+'&'+str(df['WT Ce'][i])+\
           '&'+str(df['WS Ct'][i])+'&'+str(df['WS Ce'][i])+'&'+str(df['OS Ct'][i])+\
           '&'+str(df['OS Ce'][i])+'\\\ \n'
consultancy_table+='\\hline \\end{tabular} \\end{table}\n'
