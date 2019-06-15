#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# include the package used for shell and time
import os, sys, time, datetime

from module.structure import *

path = "."

# 整理出所有圖的list
PlotsList = [p for p in os.listdir(path+"/plots") if "lin.pdf" in p] # lin and log
PlotsList.sort()
# print_r(PlotsList)

# summarize all the cut stages and variables
Cuts = []
Vars = []

for x in PlotsList:
#assuming followin name convention Channel-Cut-Var-lin(log).pdf
        CutStart = x.find("-")+1
        CutEnd = x.find("-",CutStart)
        VarStart = CutEnd+1
        VarEnd = x.find("-",VarStart)
        Cut = x[CutStart:CutEnd]
        Var = x[VarStart:VarEnd]
        if not Cut in Cuts: Cuts.append(Cut)
        if not Var in Vars: Vars.append(Var)

print(x)
print_g(Cuts)
print(Vars)
# FindPlots(path)

here = os.getcwd() #where are you now
# if os.path.isfile("Validation.tex")): print_g("The file exists")
# else: os.mkdir("slides")


outF = open(here+"/Validation.tex","w+")


make_general_structure(outF, here)


# for cut in Cuts:
#     print(cut)
#     for var

OneChannel(path, outF, Cuts, Vars, PlotsList)


# for Var in Vars:
#     print(Var)
#     nCount=0
#
#     # outF.write("\n\n\\subsection{Channel, Var: "+x[0:x.find("-")]+", "+Var+"}\n")
#     for x in PlotsList:
#         print("prefix = {}, var = {}".format(x[0:x.find("-")], Var))
        # outF.write("\\begin{frame}{Channel, Var: "+x[0:x.find("-")]+", "+Var+"}\n")
        # outF.write("\\vspace{-0.5cm}\n")
        # if x.find("-"+Var+"-")>=0:
        #     outF.write("\\begin{figure}\n\\centering\n")
        #     # if validation:
        #     #     outF.write("\\includegraphics[width = 0.5\\textwidth]{old/plots/"+x+"}")
        #     # else:
        #     # outF.write("\\includegraphics[width = 0.5\\textwidth]{plots/"+x.replace("-log","-lin")+"}")
        #     outF.write("\n\\includegraphics[width = 0.5\\textwidth]{plots/"+x+"}")
        #     outF.write("\n\\vspace{-1.0cm}\\caption{"+ x[0:x.find(Var)-1].replace("_","\\_") +".}\n")
        #     outF.write("\\end{figure}\n")
        #     nCount+=1
        #     if nCount%6==0:
        #         outF.write("\\end{frame}\n")

outF.write("\n\end{document}\n")
outF.close()

print(here+"/slides/Validation.tex")
os.system("pdflatex "+here+"/Validation.tex")
