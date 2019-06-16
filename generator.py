#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

# include the package used for shell and time
import os, sys, time, datetime, argparse

# 在Python中，为了解决内存泄露问题，采用了对象引用计数，并基于引用计数实现自动垃圾回收。
import gc

# import functions from module/sturcture.py
from module.structure import *


def main(args):

    # path = "."

    path = args.input

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
    if args.compile:
        if args.quiet:
            # the command should be installed before using
            os.system("pdflatex-quiet "+here+"/Validation.tex")
        else:
            os.system("pdflatex "+here+"/Validation.tex")




if __name__ == "__main__":
  # parse the CLI arguments
  parser = argparse.ArgumentParser(description='Create slides by Python')

  parser.add_argument('-i', metavar='INPUT', type=str, dest="input", default=".", help='Comparison plot with input 1')

  parser.add_argument('--compile', '-c', dest="compile", action="store_const", const=True, default=False, help='Will compile the Latex file')
  parser.add_argument('--quiet', '-q', dest="quiet", action="store_const", const=True, default=False, help='Suppress the compilation from latex. Please the command pdflatex-quiet from https://gitlab.com/jirislav/pdftex-quiet')

  # For the flat mode
  # parser.add_argument('--flat', '-f', dest="flat", action="store_const", const=True, default=False, help='Only run with one root file and create flat plot')
  # parser.add_argument('--input', '-i', metavar='INPUT', type=str, dest="inputfile", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='ROOT file with input sample folder')
  # parser.add_argument('--normalize', '-n', dest="normalize", action="store_const", const=True, default=False, help='Normalize the plot to unit area')
  # parser.add_argument('--outputfolder', '-o', metavar='OUTPUT', type=str, dest="outputfolder", default="results/tmp/", help='outputfolder for plots')
  #
  # parser.add_argument('--compare', '-c', dest="compare", action="store_const", const=True, default=False, help='Run with two root files and make the comparison plots')
  # parser.add_argument('--i1', metavar='INPUT', type=str, dest="compare_inputfileUp", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 1')
  # parser.add_argument('--i2', metavar='INPUT', type=str, dest="compare_inputfileDown", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 2')
  #
  # parser.add_argument('--diffprocess', '-d', dest="diffprocess", action="store_const", const=True, default=False, help='Compare with diff processes')
  # parser.add_argument('--p1', metavar='INPUT', type=str, dest="compare_ProcessUp", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 1')
  # parser.add_argument('--p2', metavar='INPUT', type=str, dest="compare_ProcessDown", default="input/20180618_R21_mc16a_p3387_w_PRW_UpdateLumi_v1.root", help='Comparison plot with input 2')
  #
  #
  # parser.add_argument('--info', metavar='info', type=str, dest="info", default="", help='Adding addtional string on the plot')
  # parser.add_argument('--sublegendname', '--sln', metavar='sublegendname', type=str, dest="sublegendname", default="", help='Adding legend name of subplot')
  # parser.add_argument('--printHist', '--ph', dest="printHist", action="store_const", const=True, default=False, help='Print list of histograms')
  #
  # # parser.add_argument('--rd', dest="rd", action="store_const", const=True, default=False, help='Check TQSampleDataReader to see the plots in the sample folder')
  #
  #
  # # parser.add_argument('--cuts', '-c', metavar='*CUT*', type=str, dest="cuts", default=["CutGGF_TopoDPhill_0jet","CutGGF_TopoDPhill_1jet"], nargs='+', help='filter for cuts to plot distributions')
  # parser.add_argument('--samplename', '-s', metavar='NAME', type=str, dest="samplename", default=["ggf","Vgamma/Wgamma","diboson/NonWW/qq/WZgammaStar","Wjets","WjetsCompB"], nargs='+', help='list of the processes for plotting')
  # parser.add_argument('--append', dest="append", action="store_const", const=True, default=False,help='append to the output file (instead of overwriting)')
  # parser.add_argument('--observable', metavar='obs', type=str, dest="observable", default=["Mll_3", "subleadLepPt_3"], nargs='+', help='list of the 1D observables to be plotted')

  args = parser.parse_args()

  import timeit
  import time

  # disable garbage collection
  gc.disable()

  # call the main function
  main(args);
