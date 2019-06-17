#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import os, sys, time, datetime

# initialize the slides
def initial():
    print_g("\033[1;32mNow is {}\033[0;m".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


# get the path of the file directory
def LoadDir(file_path):
    Absolute_Path = os.path.abspath(file_path)
    print_g(Absolute_Path)

def FindPlots(path, sort=True):
    PlotsList = [p for p in os.listdir(path+"plots") if "lin.pdf" in p]
    if sort: PlotsList.sort()
    print_r(PlotsList)
    return PlotsList




def make_general_structure(outF, workdir = ".", File_title = "Recent Work"):
    #write the tex file
    outF.write("\\documentclass[pdf]{beamer}\n")
    outF.write("\\usepackage{tikz}\n")
    outF.write("\\usepackage[utf8]{inputenc}\n")
    outF.write("\\usepackage{graphicx}\n")
    outF.write("\\usepackage{color}\n")
    outF.write("\\usepackage{lscape}\n")
    outF.write("\\usepackage{subfig}\n")
    outF.write("\\usepackage[skip=0.1cm]{caption}\n")
    # outF.write("\\usepackage[hidelinks]{hyperref}\n")
    outF.write("\\usepackage{standalone}\n")
    outF.write("\\usepackage{tikz}\n")
    # outF.write("%\\usepackage{underscore}\n")#this package seems not working
    outF.write("\\usepackage{hyperref}\n")
    outF.write("\\captionsetup[subfloat]{captionskip=0.1pt, labelformat=empty, position=top}\n")
    # outF.write("\\captionsetup[figure]{captionskip=1.pt, labelformat=empty}\n")
    outF.write("\\captionsetup{labelformat=empty,labelsep=none}\n")
    outF.write("\\usetikzlibrary{positioning,arrows}\n")
    outF.write("\\mode<presentation>{\n")
    outF.write("    \\usetheme{Warsaw}\n")
    outF.write("    \\usecolortheme{default}\n")
    outF.write("    \\usefonttheme{serif}\n")
    outF.write("    \\setbeamertemplate{navigation symbols}{}\n")
    outF.write("    \\setbeamertemplate{caption}[numbered]\n")
    outF.write("    \\setbeamertemplate{footline}[frame number]{}\n")
    outF.write("}\n")
    outF.write("\\title[Recent Work]{"+File_title+"}\n")
    outF.write("\\author{%\n")
    outF.write("\\textsc{\\scriptsize{\\underline{Meng-Ju Tsai}, Pai-hsien Jennifer Hsu, YunJu Lu, Ya-Feng Lo}}\\\\}\n")
    outF.write("\\date{\\today}\n")
    outF.write("\\titlegraphic{\n")
    outF.write("    \\centering\n")
    outF.write("    \\includegraphics[width=2cm]{"+workdir+"/logos/nthu_logo.png}\n")
    outF.write("    \\hspace{1cm}\n")
    outF.write("    \\includegraphics[width=2cm]{"+workdir+"/logos/ATLAS-Logo1}\n")
    outF.write("}\n")
    outF.write("\\begin{document}\n")
    outF.write("\\setbeamertemplate{caption}{\\raggedright\\insertcaption\\par}\n")
    outF.write("\\begin{frame}\n")
    outF.write("\\titlepage\n")
    outF.write("\\end{frame}\n")
    outF.write("\\begin{frame}{Introduction}\n")
    outF.write("\\tableofcontents\n")
    outF.write("\\end{frame}\n")




def OneChannel(path, outF, Cuts, Vars, PlotsList):
    print_r("Run for one channel.")
    for cut in Cuts:
        print_g(cut)
        nCount = 0
        RevPlotList = []

        for x in PlotsList:
            if x.find("-"+cut+"-")>=0:
                RevPlotList.append(x)

        print(RevPlotList)
        List_Length = len(RevPlotList)
        Quotient = List_Length/6
        Remainder = List_Length%6
        print_r("Quotient = {}, Remainder = {}".format(Quotient, Remainder))
        nCount = 0
        nTime = 0
        xTime = 0

        for plot in RevPlotList:
            # print_r("cut = {}, plot = {}, find? = {}".format(cut, plot, plot.find("-"+cut+"-")))
            if nTime < Quotient:
                if nCount%6 == 0:
                    outF.write("\\begin{frame}{Cut stage = "+cut.replace("_", "\\_")+"}\n")
                    outF.write("\\vspace{-1cm}\n")

                    # print_r("\\begin{frame}{Cut stage = "+cut.replace("_", "\\_")+"}\n")

                if nCount%3 == 0:
                    outF.write("\\begin{figure}\n\\centering\n")
                    # print_r("\\begin{figure}\n\\centering\n")

                outF.write("    \subfloat["+plot.replace("-"+cut+"-"," ").replace("_", "\\_").replace("-lin.pdf", "")+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+path+"/plots/"+plot+"}}\n")
                # print("cut = {}, plot = {}, find? = {}".format(cut, plot, plot.find("-"+cut+"-")))
                nCount = nCount + 1


                if nCount%3 == 0:
                    outF.write("\\end{figure}\n")
                    if nCount/3%2 == 1:
                        outF.write("\\vspace{-0.8cm}\n")
                    # print_y("\\end{figure}\n")

                if nCount%6 == 0:
                    outF.write("\\end{frame}\n")
                    # print_y("\\end{frame}\n")
                    nTime+=1
                    if nTime == Quotient and Remainder == 0:
                        nTime = nTime - 1

                    # print("nCount = {}, nTime = {}".format(nCount, nTime))

            else:
                if Remainder > 3:

                    if xTime == 0:
                        print(nCount)
                        if nCount%3 == 0:
                            outF.write("\\begin{frame}{Cut stage = "+cut.replace("_", "\\_")+"}\n")
                            outF.write("\\vspace{-1cm}\n")
                            outF.write("\\begin{figure}\n\\centering\n")
                            # print_r("\\begin{frame}{Cut stage = "+cut.replace("_", "\\_")+"}\n")
                            # print_r("\\begin{figure}\n\\centering\n")

                        outF.write("    \subfloat["+plot.replace("-"+cut+"-"," ").replace("_", "\\_").replace("-lin.pdf", "")+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+path+"/plots/"+plot+"}}\n")
                        print("cut = {}, plot = {}, find? = {}".format(cut, plot, plot.find("-"+cut+"-")))
                        nCount = nCount + 1

                        if nCount%3 == 0:
                            outF.write("\\end{figure}\n")
                            # print_y("\\end{figure}\n")
                            xTime = xTime + 1
                            print("xTime", xTime)
                            if nCount/3%2 == 1:
                                outF.write("\\vspace{-0.8cm}\n")
                    else:
                        if nCount%3 == 0:
                            outF.write("\\begin{figure}\n\\centering\n")
                            # print_r("\\begin{figure}\n\\centering\n")

                        outF.write("    \subfloat["+plot.replace("-"+cut+"-"," ").replace("_", "\\_").replace("-lin.pdf", "")+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+path+"/plots/"+plot+"}}\n")
                        # print("cut = {}, plot = {}, find? = {}".format(cut, plot, plot.find("-"+cut+"-")))
                        nCount = nCount + 1

                        if nCount%3 == Remainder%3:
                            outF.write("\\end{figure}\n")
                            if nCount/3%2 == 1:
                                outF.write("\\vspace{-0.8cm}\n")
                            outF.write("\\end{frame}\n")
                            # print_y("\\end{figure}\n")
                            # print_y("\\end{frame}\n")
                else:
                    print("eiofjewoijfoiwj ============== {}".format(nCount))
                    if nCount%3 == 0:
                        outF.write("\\begin{frame}{Cut stage = "+cut.replace("_", "\\_")+"}\n")
                        outF.write("\\begin{figure}\n\\centering\n")
                        # print_r("\\begin{figure}\n\\centering\n")

                    outF.write("    \subfloat["+plot.replace("-"+cut+"-"," ").replace("_", "\\_").replace("-lin.pdf", "")+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+path+"/plots/"+plot+"}}\n")
                    # print("cut = {}, plot = {}, find? = {}".format(cut, plot, plot.find("-"+cut+"-")))
                    nCount = nCount + 1


                    if nCount%3 == Remainder%3:
                        outF.write("\\end{figure}\n")
                        if nCount/3%2 == 1:
                            outF.write("\\vspace{-0.8cm}\n")
                        outF.write("\\end{frame}\n")
                        # print_y("\\end{figure}\n")
                        # print_y("\\end{frame}\n")













def print_g(str): #g: green color
    print("\033[1;32m{}\033[0;m".format(str))

def print_r(str): #g: red color
    print("\033[1;31m{}\033[0;m".format(str))

def print_y(str): #g: yellow color
    print("\033[1;33m{}\033[0;m".format(str))
