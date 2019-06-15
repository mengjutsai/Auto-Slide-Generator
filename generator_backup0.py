#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# include the package used for shell and time
import os, sys, time, datetime

# 從自訂的strucutre導入所有function
from module.structure import *


if __name__ == '__main__':
    initial()
    # LoadDir(".")
    path = "./"

    PlotsList = [p for p in os.listdir(path+"plots") if "lin.pdf" in p]
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

    print_g(Cuts)
    print(Vars)
    # FindPlots(path)
