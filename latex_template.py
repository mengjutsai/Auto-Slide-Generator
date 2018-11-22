#!/usr/bin/env python2
import os
import sys
import time
import datetime

from os import listdir
from os.path import isfile, join, getsize
from os import walk

############ Run with ###############

#  python latex_template.py file_path texFile_path

#####################################
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
if (len(sys.argv)!=3 and len(sys.argv)!=2):
    exit("Please insert option")

here = os.getcwd() #where are you now

# sys.argv[0] -> latex_template.py
# sys.argv[1] -> file_path (ex. histograms)
# sys.argv[2] -> texFile_path

PythonFile = sys.argv[0]
file_path = sys.argv[1]

if len(sys.argv)==2:
    print("PythonFile = ", PythonFile, ", file_path = ", file_path, ", texfile_path = ", here)
    if os.path.isfile(here+"/slides/Validation.tex"):
        os.remove(here+"/slides/Validation.tex")
    outF = open(here+"/slides/Validation.tex","w+")
    print(here+"/slides/Validation.tex")
if len(sys.argv)==3:
    texfile_path = sys.argv[2]
    print("PythonFile = ", PythonFile, ", file_path = ", file_path, ", texfile_path = ", texfile_path)
    if os.path.isfile(texfile_path+"/slides/Validation.tex"):
        os.remove(texfile_path+"/slides/Validation.tex")

    outF = open(texfile_path+"/slides/Validation.tex","w+")
    print(texfile_path+"/slides/Validation.tex")
abs_file_path = os.path.abspath(file_path) # get abs path for file path go for latex compile

files_list = []
hist_list = []

# for path, dirs, files in os.walk(file_path): #find the files in the histograms folder
#     # files_list.extend([(os.path.join(path, file), getsize(os.path.join(path, file))) for file in files])
#     files_list.extend([os.path.join(abs_file_path, file) for file in files]) #get files abs path
#     hist_list.extend([os.path.join(path, file)[10:] for file in files]) #get files names
#     channels = [os.path.join(path, file)[10:].split("-")[0] for file in files] #Take only variables
#     cuts = [os.path.join(path, file)[10:].split("-")[1] for file in files] #Take only variables
#     variables = [os.path.join(path, file)[10:].split("-")[2] for file in files] #Take only variables
#     channels_only = list(set(channels))
#     cuts_only = list(set(cuts))
#     variables_ony = list(set(variables))
#     # print(channels, cuts, variables)
#     # print(files_list)

# print(files_list)
# print(hist_list)

def make_general_structure(File_title = "Recent Work"):
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
    outF.write("    \\includegraphics[width=3cm]{/Users/ploww/ploww/Slides/HWW-VBF-WORK/template/nthu_logo.jpg}\n")
    outF.write("    \\hspace{1cm}\n")
    outF.write("    \\includegraphics[width=2cm]{/Users/ploww/ploww/Slides/HWW-VBF-WORK/template/ATLAS-Logo1}\n")
    outF.write("}\n")
    outF.write("\\begin{document}\n")
    outF.write("\\setbeamertemplate{caption}{\\raggedright\\insertcaption\\par}\n")
    outF.write("\\begin{frame}\n")
    outF.write("\\titlepage\n")
    outF.write("\\end{frame}\n")
    outF.write("\\begin{frame}{Introduction}\n")
    outF.write("\\tableofcontents\n")
    outF.write("\\end{frame}\n")

make_general_structure("Recent Work")

def _make_plots_6_1_(title, channel, CutStage, CutStage_name ,variable):
                outF.write("\\begin{frame}{"+title+"}\n")
                outF.write("\\vspace{-0.5cm}\n")
                outF.write("\\begin{figure}\n\\centering\n")
                variable_name = []
                for i in range(0,3):
                    variable_name.append(variable[i])
                    if variable[i] == "leadJetPt_Central":
                        variable_name[i] = "leadJetPt-Central"
                    if variable[i] == "leadJetPt_Forward":
                        variable_name[i] = "leadJetPt-Forward"
                    if variable[i] == "subleadJetPt_Central":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "subleadJetPt_Forward":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "Jet3_Pt":
                        variable_name[i] = "Jet3-Pt"
                    if variable[i] == "Jet3_Eta":
                        variable_name[i] = "Jet3-Eta"
                    if variable[i] == "Jet3_Phi":
                        variable_name[i] = "Jet3-Phi"
                    if variable[i] == "Jet4_Pt":
                        variable_name[i] = "Jet4-Pt"
                    if variable[i] == "Jet4_Eta":
                        variable_name[i] = "Jet4-Eta"
                    if variable[i] == "Jet4_Phi":
                        variable_name[i] = "Jet4-Phi"
                    if variable[i] == "Jet1_Pt":
                        variable_name[i] = "Jet1-Pt"
                    if variable[i] == "Jet1_Eta":
                        variable_name[i] = "Jet1-Eta"
                    if variable[i] == "Jet1_Phi":
                        variable_name[i] = "Jet1-Phi"
                    if variable[i] == "Jet2_Pt":
                        variable_name[i] = "Jet2-Pt"
                    if variable[i] == "Jet2_Eta":
                        variable_name[i] = "Jet2-Eta"
                    if variable[i] == "Jet2_Phi":
                        variable_name[i] = "Jet2-Phi"
                    outF.write("    \subfloat["+channel[i]+"-"+variable_name[i]+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+channel[i]+"-"+CutStage[i]+"-"+variable[i]+".pdf"+"}}\n")
                outF.write("\\end{figure}\n\\vspace{-0.8cm}\n")
                outF.write("\\begin{figure}\n\\centering\n")
                for i in range(3,6):
                    variable_name.append(variable[i])
                    if variable[i] == "leadJetPt_Central":
                        variable_name[i] = "leadJetPt-Central"
                    if variable[i] == "leadJetPt_Forward":
                        variable_name[i] = "leadJetPt-Forward"
                    if variable[i] == "subleadJetPt_Central":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "subleadJetPt_Forward":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "Jet3_Pt":
                        variable_name[i] = "Jet3-Pt"
                    if variable[i] == "Jet3_Eta":
                        variable_name[i] = "Jet3-Eta"
                    if variable[i] == "Jet3_Phi":
                        variable_name[i] = "Jet3-Phi"
                    if variable[i] == "Jet4_Pt":
                        variable_name[i] = "Jet4-Pt"
                    if variable[i] == "Jet4_Eta":
                        variable_name[i] = "Jet4-Eta"
                    if variable[i] == "Jet4_Phi":
                        variable_name[i] = "Jet4-Phi"
                    if variable[i] == "Jet1_Pt":
                        variable_name[i] = "Jet1-Pt"
                    if variable[i] == "Jet1_Eta":
                        variable_name[i] = "Jet1-Eta"
                    if variable[i] == "Jet1_Phi":
                        variable_name[i] = "Jet1-Phi"
                    if variable[i] == "Jet2_Pt":
                        variable_name[i] = "Jet2-Pt"
                    if variable[i] == "Jet2_Eta":
                        variable_name[i] = "Jet2-Eta"
                    if variable[i] == "Jet2_Phi":
                        variable_name[i] = "Jet2-Phi"
                    outF.write("    \subfloat["+channel[i]+"-"+variable_name[i]+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+channel[i]+"-"+CutStage[i]+"-"+variable[i]+".pdf"+"}}\n")
                outF.write("\\end{figure}\n")
                outF.write("\\end{frame}\n")

def _make_plots_4_1_(title, channel, CutStage ,variable):
                outF.write("\\begin{frame}{"+title+"}\n")
                outF.write("\\vspace{-0.5cm}\n")
                outF.write("\\begin{figure}\n\\centering\n")
                variable_name = []
                for i in range(0,2):
                    variable_name.append(variable[i])
                    if variable[i] == "leadJetPt_Central":
                        variable_name[i] = "leadJetPt-Central"
                    if variable[i] == "leadJetPt_Forward":
                        variable_name[i] = "leadJetPt-Forward"
                    if variable[i] == "subleadJetPt_Central":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "subleadJetPt_Forward":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "Jet3_Pt":
                        variable_name[i] = "Jet3-Pt"
                    if variable[i] == "Jet3_Eta":
                        variable_name[i] = "Jet3-Eta"
                    if variable[i] == "Jet3_Phi":
                        variable_name[i] = "Jet3-Phi"
                    if variable[i] == "Jet4_Pt":
                        variable_name[i] = "Jet4-Pt"
                    if variable[i] == "Jet4_Eta":
                        variable_name[i] = "Jet4-Eta"
                    if variable[i] == "Jet4_Phi":
                        variable_name[i] = "Jet4-Phi"
                    if variable[i] == "Jet1_Pt":
                        variable_name[i] = "Jet1-Pt"
                    if variable[i] == "Jet1_Eta":
                        variable_name[i] = "Jet1-Eta"
                    if variable[i] == "Jet1_Phi":
                        variable_name[i] = "Jet1-Phi"
                    if variable[i] == "Jet2_Pt":
                        variable_name[i] = "Jet2-Pt"
                    if variable[i] == "Jet2_Eta":
                        variable_name[i] = "Jet2-Eta"
                    if variable[i] == "Jet2_Phi":
                        variable_name[i] = "Jet2-Phi"
                    if variable[i] == "nInteraction_old_1_09":
                        variable_name[i] = "AverageMu(1.09)"
                    if variable[i] == "nInteraction_new_1_03":
                        variable_name[i] = "AverageMu(1.03)"
                    if variable[i] == "skl1_5bins":
                        variable_name[i] = "skl1-5bins"
                    if variable[i] == "MT2_1jet":
                        variable_name[i] = "MT2-1jet"
                    outF.write("    \subfloat[R20.7-"+channel[i]+"-"+variable_name[i]+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight, angle = 0]{"+abs_file_path+"/R20.7/"+channel[i]+"-"+CutStage[i]+"-"+variable[i]+"-lin.pdf"+"}}\n")
                outF.write("\\end{figure}\n\\vspace{-0.8cm}\n")
                outF.write("\\begin{figure}\n\\centering\n")
                for i in range(2,4):
                    variable_name.append(variable[i])
                    if variable[i] == "leadJetPt_Central":
                        variable_name[i] = "leadJetPt-Central"
                    if variable[i] == "leadJetPt_Forward":
                        variable_name[i] = "leadJetPt-Forward"
                    if variable[i] == "subleadJetPt_Central":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "subleadJetPt_Forward":
                        variable_name[i] = "subleadJetPt-Central"
                    if variable[i] == "Jet3_Pt":
                        variable_name[i] = "Jet3-Pt"
                    if variable[i] == "Jet3_Eta":
                        variable_name[i] = "Jet3-Eta"
                    if variable[i] == "Jet3_Phi":
                        variable_name[i] = "Jet3-Phi"
                    if variable[i] == "Jet4_Pt":
                        variable_name[i] = "Jet4-Pt"
                    if variable[i] == "Jet4_Eta":
                        variable_name[i] = "Jet4-Eta"
                    if variable[i] == "Jet4_Phi":
                        variable_name[i] = "Jet4-Phi"
                    if variable[i] == "Jet1_Pt":
                        variable_name[i] = "Jet1-Pt"
                    if variable[i] == "Jet1_Eta":
                        variable_name[i] = "Jet1-Eta"
                    if variable[i] == "Jet1_Phi":
                        variable_name[i] = "Jet1-Phi"
                    if variable[i] == "Jet2_Pt":
                        variable_name[i] = "Jet2-Pt"
                    if variable[i] == "Jet2_Eta":
                        variable_name[i] = "Jet2-Eta"
                    if variable[i] == "Jet2_Phi":
                        variable_name[i] = "Jet2-Phi"
                    if variable[i] == "nInteraction_old_1_09":
                        variable_name[i] = "AverageMu(1.09)"
                    if variable[i] == "nInteraction_new_1_03":
                        variable_name[i] = "AverageMu(1.03)"
                    if variable[i] == "skl1_5bins":
                        variable_name[i] = "skl1-5bins"
                    if variable[i] == "MT2_1jet":
                        variable_name[i] = "MT2-1jet"
                    outF.write("    \subfloat[R21-"+channel[i]+"-"+variable_name[i]+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight, angle = 0]{"+abs_file_path+"/R21/"+channel[i]+"-"+CutStage[i]+"-"+variable[i]+"-lin.pdf"+"}}\n")
                outF.write("\\end{figure}\n")
                outF.write("\\end{frame}\n")

def _make_plots_5_1_(title, channel, CutStage, CutStage_name ,variable):
                outF.write("\\begin{frame}{"+title+"}\n")
                outF.write("\\vspace{-0.5cm}\n")
                outF.write("\\begin{figure}\n\\centering\n")
                for i in range(0,3):
                    outF.write("    \subfloat["+channel[i]+"-"+CutStage_name[i]+"-"+variable[i]+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+channel[i]+"-"+CutStage[i]+"-"+variable[i]+".pdf"+"}}\n")
                outF.write("\\end{figure}\n\\vspace{-0.8cm}\n")
                outF.write("\\begin{figure}\n\\centering\n")
                for i in range(3,5):
                    outF.write("    \subfloat["+channel[i]+"-"+CutStage_name[i]+"-"+variable[i]+"]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+channel[i]+"-"+CutStage[i]+"-"+variable[i]+".pdf"+"}}\n")
                outF.write("\\end{figure}\n")
                outF.write("\\end{frame}\n")

def make_frame(inputText="Backup"):
    outF.write("\\begin{frame}{}\n")
    outF.write("\\centering\n")
    outF.write("\\textbf{"+inputText+"}\n")
    outF.write("\\end{frame}\n")

#
# def _make_cutflow_(File_cutflow,_subfolder_=""):
#     # cutflow = open(path+"cutflows/"+File_cutflow,"r")
#     outF.write("\\begin{frame}{Cutflow}\n")
#     outF.write("\\begin{table}[h!]\n")
#     outF.write("\\begin{adjustbox}{width=1.18\\textwidth,center=\\textwidth}\n")
#     # with open(path+"plots/"+_subfolder_+"cutflows/"+File_cutflow,"r") as cutflow:
#     with open(path+_subfolder_+"cutflows/"+File_cutflow,"r") as cutflow:
#         next(cutflow)
#         next(cutflow)
#         next(cutflow)
#         for line in cutflow:
#             print line
#             outF.write("       "+line)
#     outF.write("\\end{adjustbox}\n")
#     outF.write("\\end{table}\n")
#     outF.write("\\end{frame}\n")

# list_ = ['MT2_origin', 'MT2_origin-WW-totalbkg']
# list__name = ['WW / ttbar', 'WW / total bkg']
# _make_plots_2_1_(list_,list__name,"CutGGF_WWControl_1jet", "Check cut values","MT2 Distribution ggF 1-jet WWCR")
#
# list1_ = ['MT_wide_30bins-WW-ttbar', 'MT_wide_30bins-WW-totalbkg', 'MT2_origin-WW-ttbar', 'MT2_origin-WW-totalbkg']
# list1__name = ['MT - WW / ttbar', 'MT - WW / total bkg', 'MT2 - WW / ttbar', 'MT2 - WW / total bkg']
# Region_=['CutVBFbVeto_2jet','CutVBFbVeto_2jet','CutVBFWWControl_2jetinclMT','CutVBFWWControl_2jetinclMT']
# _make_plots_4_1_(list1_, list1__name,Region_,"Check cut values", "MT \& MT2 distribution VBF 2-jet WWVR")

# VBFlist_ = ['MT2_VR', 'skl1_5Bins']
# VBFlist__name = ['MT2', 'skl1\\_5Bins']
# _make_plots_2_1_(VBFlist_,VBFlist__name,"CutVBFWWControl_CJV20", "VBF_v17b_WWSherpa222_v4_1/plots/","VBF")
#
# VBFlist_2 = ['MT2_VR', 'skl1_5Bins','MT2_VR', 'skl1_5Bins']
# VBFlist__name2 = ['MT2', 'skl1\\_5Bins','MT2', 'skl1\\_5Bins']
# _make_plots_4_1_(VBFlist_2,VBFlist__name2,"CutVBFWWControl_CJV20", "VBF_v17b_WWSherpa222_v4_1/plots/","VBF")
#
#
# ggFlist_ = ['MT2_origin', 'MT_VR2','MT_VR2']
# ggFlist__name = ['MT2', 'MT','MT']
# ggFlist__Region = ['CutGGF_WWControl_1jet','CutGGF_WWControl_1jet','CutGGF_WWControl_1jet_inclMT2']
# _make_plots_3_1_Iterator(ggFlist_,ggFlist__name,ggFlist__Region, "ggF_v17b_WWSherpa222_v3_noNF/plots/","ggF")
# _make_cutflow_("emme-ggf_cuts-ggf.tex","ggF_v17b_WWSherpa222_v3_noNF/")
# _make_cutflow_("emme-vbf-vbf-bdt.tex","VBF_v17b_WWSherpa222_v5/")

# _make_cutflow_("emme-vbf-vbf-bdt.tex","VBF_v17b_WWSherpa222_v6_1/")
# _make_cutflow_("emme-vbf-vbf-bdt-1.tex","VBF_v17b_WWSherpa222_v6_1/")
#
# _make_cutflow_("emme-ggf_cuts-ggf.tex","ggF_v17b_WWSherpa222_v8_noNF/")
# _make_cutflow_("emme-ggf_cuts-ggf-1.tex","ggF_v17b_WWSherpa222_v8_noNF/")

#Variable


# Lep_Kinematics = ["leadLepPt", "leadLepEta", "leadLepPhi", "subleadLepPt", "subleadLepEta", "subleadLepPhi"]
#
# VBFJet_Kinematics = ["leadJetPt", "leadJetEta", "leadJetPhi", "subleadJetPt", "subleadJetEta", "subleadJetPhi"]
# VBFJet_Kinematics_region = ["leadJetPt_Central", "leadJetPt_Forward", "SubleadJetPt_Central", "subleadJetPt_Forward"]
#
# GGF1jet_Jet_Kinematics = ["leadJetPt", "leadJetEta", "leadJetPhi", "leadJetPt_Central", "leadJetPt_Forward"]
#
# Kinematics_1 = ["nPV", "nInteraction", "nJet", "nJetsTight", "leadJetPt_Forward"]
#
# BDT_Input1 = ["Mjj", "Mll", "DYjj", "DPhill"]
# BDT_Input2 = ["MT", "PtTot", "SumOFMLepxJety", "contOLV"]


# 6 var
nPV_Kinematics = ["nPV", "nInteraction", "mtt", "nPV", "nInteraction", "mtt"] #

Lep_Kinematics = ["leadLepPt", "leadLepEta", "leadLepPhi", "leadLepPt", "leadLepEta", "leadLepPhi"] #
SubLep_Kinematics = ["subleadLepPt", "subleadLepEta", "subleadLepPhi", "subleadLepPt", "subleadLepEta", "subleadLepPhi"] #

Jet1_Kinematics = ["Jet1_Pt", "Jet1_Eta", "Jet1_Phi", "Jet1_Pt", "Jet1_Eta", "Jet1_Phi"]
Jet2_Kinematics = ["Jet2_Pt", "Jet2_Eta", "Jet2_Phi", "Jet2_Pt", "Jet2_Eta", "Jet2_Phi"]

VBFJet1_Kinematics = ["leadJetPt", "leadJetEta", "leadJetPhi", "leadJetPt", "leadJetEta", "leadJetPhi"]
VBFJet2_Kinematics = ["subleadJetPt", "subleadJetEta", "subleadJetPhi", "subleadJetPt", "subleadJetEta", "subleadJetPhi"]
VBFJet3_Kinematics = ["Jet3_Pt", "Jet3_Eta", "Jet3_Phi", "Jet3_Pt", "Jet3_Eta", "Jet3_Phi"]
VBFJet4_Kinematics = ["Jet4_Pt", "Jet4_Eta", "Jet4_Phi", "Jet4_Pt", "Jet4_Eta", "Jet4_Phi"]

nJet_1_Kinematics = ["nJetsTight", "DPhillMET","nJetsTight", "DPhillMET"] #

nJet_Kinematics = ["nJet", "nJetsTight", "DPhillMET", "nJet", "nJetsTight", "DPhillMET"] #
MT_mll_dphill_Kinematics = ["MT", "Mll", "DPhill", "MT", "Mll", "DPhill"] #
Ptll_MTlep0_MTlep1_Kinematics = ["Ptll", "MTlep0", "MTlep1", "Ptll", "MTlep0", "MTlep1"] #
MET_Kinematics = ["MET", "METPhi", "MaxMTlep", "MET", "METPhi", "MaxMTlep"] #

# 4 var
VBFJet1_Region_Kinematics = ["leadJetPt_Central", "leadJetPt_Forward", "leadJetPt_Central", "leadJetPt_Forward"]
VBFJet2_Region_Kinematics = ["subleadJetPt_Central", "subleadJetPt_Forward", "subleadJetPt_Central", "subleadJetPt_Forward"]

#Region
CutFF       = ["CutFF","CutFF", "CutFF", "CutFF", "CutFF", "CutFF"]
CutMET      = ["CutMET","CutMET", "CutMET", "CutMET", "CutMET", "CutMET"]
CutGGF_1jet = ["CutGGF_1jet","CutGGF_1jet", "CutGGF_1jet", "CutGGF_1jet", "CutGGF_1jet", "CutGGF_1jet"]
CutVBF_2jet = ["CutVBF_2jet","CutVBF_2jet", "CutVBF_2jet", "CutVBF_2jet", "CutVBF_2jet", "CutVBF_2jet"]


#name
CutGGF_1jet_name = ["CutGGF-1jet","CutGGF-1jet", "CutGGF-1jet", "CutGGF-1jet", "CutGGF-1jet", "CutGGF-1jet"]
CutVBF_2jet_name = ["CutVBF-2jet","CutVBF-2jet", "CutVBF-2jet", "CutVBF-2jet", "CutVBF-2jet", "CutVBF-2jet"]



em_channel = ["em","em","em","em","em","em"]
me_channel = ["me","me","me","me","me","me"]
emme_channel = ["emme","emme","emme","emme","emme","emme"]

em_me_comparison_channel = ["em","em","em","me","me","me"]

em_me_comparison_channel_4plot = ["em","me","em","me"]


MT = ["MT", "MT", "MT", "MT"]
nJetsTight = ["nJetsTight", "nJetsTight", "nJetsTight", "nJetsTight"]
nInteraction = ["nInteraction_old_1_09", "nInteraction_old_1_09", "nInteraction_new_1_03", "nInteraction_new_1_03"]
DPhill = ["DPhill", "DPhill", "DPhill", "DPhill"]
Mll = ["Mll", "Mll", "Mll", "Mll"]
contOLV = ["contOLV", "contOLV", "contOLV", "contOLV"]
skl1 = ["skl1", "skl1", "skl1", "skl1"]
skl1_5bins = ["skl1_5bins", "skl1_5bins", "skl1_5bins", "skl1_5bins"]
DYjj = ["DYjj", "DYjj", "DYjj", "DYjj"]
Mjj = ["Mjj", "Mjj", "Mjj", "Mjj"]
SumOFMLepxJety = ["SumOFMLepxJety", "SumOFMLepxJety", "SumOFMLepxJety", "SumOFMLepxJety"]
PtTot = ["PtTot", "PtTot", "PtTot", "PtTot"]
leadJetPt = ["leadJetPt", "leadJetPt", "leadJetPt", "leadJetPt"]
leadJetEta = ["leadJetEta", "leadJetEta", "leadJetEta", "leadJetEta"]
leadJetPhi = ["leadJetPhi", "leadJetPhi", "leadJetPhi", "leadJetPhi"]
subleadJetPt = ["subleadJetPt", "subleadJetPt", "subleadJetPt", "subleadJetPt"]
subleadJetEta = ["subleadJetEta", "subleadJetEta", "subleadJetEta", "subleadJetEta"]
subleadJetPhi = ["subleadJetPhi", "subleadJetPhi", "subleadJetPhi", "subleadJetPhi"]
leadLepPt = ["leadLepPt", "leadLepPt", "leadLepPt", "leadLepPt"]
leadLepEta = ["leadLepEta", "leadLepEta", "leadLepEta", "leadLepEta"]
leadLepPhi = ["leadLepPhi", "leadLepPhi", "leadLepPhi", "leadLepPhi"]
subleadLepPt = ["subleadLepPt", "subleadLepPt", "subleadLepPt", "subleadLepPt"]
subleadLepEta = ["subleadLepEta", "subleadLepEta", "subleadLepEta", "subleadLepEta"]
subleadLepPhi = ["subleadLepPhi", "subleadLepPhi", "subleadLepPhi", "subleadLepPhi"]
MT2_1jet = ["MT2_1jet", "MT2_1jet", "MT2_1jet", "MT2_1jet"]

CutFF_4plots       = ["CutFF","CutFF", "CutFF", "CutFF"]
CutTopContrl_4plots       = ["CutVBFTopControl_2jetinclZttVeto","CutVBFTopControl_2jetinclZttVeto", "CutVBFTopControl_2jetinclZttVeto", "CutVBFTopControl_2jetinclZttVeto"]
CutZttContrl_4plots       = ["CutVBFZtautauControl_2jetinclOLV","CutVBFZtautauControl_2jetinclOLV", "CutVBFZtautauControl_2jetinclOLV", "CutVBFZtautauControl_2jetinclOLV"]
CutWWContrl_4plots       = ["CutVBFWWControl_CJV20","CutVBFWWControl_CJV20", "CutVBFWWControl_CJV20", "CutVBFWWControl_CJV20"]


CutFF_4plots       = ["CutFF","CutFF", "CutFF", "CutFF"]
CutFF_4plots       = ["CutFF","CutFF", "CutFF", "CutFF"]


make_frame("CutFF")
# _make_plots_4_1_("CutFF - ", em_me_comparison_channel_4plot, CutFF_4plots, CutFF_4plots , )

_make_plots_4_1_("CutFF - MT", em_me_comparison_channel_4plot, CutFF_4plots , MT)
_make_plots_4_1_("CutFF - nJetsTight", em_me_comparison_channel_4plot, CutFF_4plots , nJetsTight)
_make_plots_4_1_("CutFF - AverageMu(scaled)", em_me_comparison_channel_4plot, CutFF_4plots , nInteraction)
_make_plots_4_1_("CutFF - DPhill", em_me_comparison_channel_4plot, CutFF_4plots , DPhill)
_make_plots_4_1_("CutFF - Mll", em_me_comparison_channel_4plot, CutFF_4plots , Mll)
_make_plots_4_1_("CutFF - contOLV", em_me_comparison_channel_4plot, CutFF_4plots , contOLV)

_make_plots_4_1_("CutFF - leadLepPt", em_me_comparison_channel_4plot, CutFF_4plots , leadLepPt)
_make_plots_4_1_("CutFF - leadLepEta", em_me_comparison_channel_4plot, CutFF_4plots , leadLepEta)
_make_plots_4_1_("CutFF - leadLepPhi", em_me_comparison_channel_4plot, CutFF_4plots , leadLepPhi)
_make_plots_4_1_("CutFF - subleadLepPt", em_me_comparison_channel_4plot, CutFF_4plots , subleadLepPt)
_make_plots_4_1_("CutFF - subleadLepEta", em_me_comparison_channel_4plot, CutFF_4plots , subleadLepEta)
_make_plots_4_1_("CutFF - subleadLepPhi", em_me_comparison_channel_4plot, CutFF_4plots , subleadLepPhi)


make_frame("Top CR")
_make_plots_4_1_("Top CR - skl1", em_me_comparison_channel_4plot, CutTopContrl_4plots , skl1)
_make_plots_4_1_("Top CR - skl1 5bins", em_me_comparison_channel_4plot, CutTopContrl_4plots , skl1_5bins)
_make_plots_4_1_("Top CR - nJetsTight", em_me_comparison_channel_4plot, CutTopContrl_4plots , nJetsTight)
_make_plots_4_1_("Top CR - DYjj", em_me_comparison_channel_4plot, CutTopContrl_4plots , DYjj)
_make_plots_4_1_("Top CR - Mjj", em_me_comparison_channel_4plot, CutTopContrl_4plots , Mjj)
_make_plots_4_1_("Top CR - contOLV", em_me_comparison_channel_4plot, CutTopContrl_4plots , contOLV)
_make_plots_4_1_("Top CR - DPhill", em_me_comparison_channel_4plot, CutTopContrl_4plots , DPhill)
_make_plots_4_1_("Top CR - Mll", em_me_comparison_channel_4plot, CutTopContrl_4plots , Mll)
_make_plots_4_1_("Top CR - MT", em_me_comparison_channel_4plot, CutTopContrl_4plots , MT)
_make_plots_4_1_("Top CR - SumOFMLepxJety", em_me_comparison_channel_4plot, CutTopContrl_4plots , SumOFMLepxJety)
_make_plots_4_1_("Top CR - PtTot", em_me_comparison_channel_4plot, CutTopContrl_4plots , PtTot)
_make_plots_4_1_("Top CR - leadJetPt", em_me_comparison_channel_4plot, CutTopContrl_4plots , leadJetPt)
_make_plots_4_1_("Top CR - leadJetEta", em_me_comparison_channel_4plot, CutTopContrl_4plots , leadJetEta)
_make_plots_4_1_("Top CR - leadJetPhi", em_me_comparison_channel_4plot, CutTopContrl_4plots , leadJetPhi)
_make_plots_4_1_("Top CR - subleadJetPt", em_me_comparison_channel_4plot, CutTopContrl_4plots , subleadJetPt)
_make_plots_4_1_("Top CR - subleadJetEta", em_me_comparison_channel_4plot, CutTopContrl_4plots , subleadJetEta)
_make_plots_4_1_("Top CR - subleadJetPhi", em_me_comparison_channel_4plot, CutTopContrl_4plots , subleadJetPhi)
_make_plots_4_1_("Top CR - leadLepPt", em_me_comparison_channel_4plot, CutTopContrl_4plots , leadLepPt)
_make_plots_4_1_("Top CR - leadLepEta", em_me_comparison_channel_4plot, CutTopContrl_4plots , leadLepEta)
_make_plots_4_1_("Top CR - leadLepPhi", em_me_comparison_channel_4plot, CutTopContrl_4plots , leadLepPhi)
_make_plots_4_1_("Top CR - subleadLepPt", em_me_comparison_channel_4plot, CutTopContrl_4plots , subleadLepPt)
_make_plots_4_1_("Top CR - subleadLepEta", em_me_comparison_channel_4plot, CutTopContrl_4plots , subleadLepEta)
_make_plots_4_1_("Top CR - subleadLepPhi", em_me_comparison_channel_4plot, CutTopContrl_4plots , subleadLepPhi)

make_frame("Z$\\tau\\tau$ CR")

_make_plots_4_1_("Z$\\tau\\tau$ CR - skl1", em_me_comparison_channel_4plot, CutZttContrl_4plots , skl1)
_make_plots_4_1_("Z$\\tau\\tau$ CR - skl1 5bins", em_me_comparison_channel_4plot, CutZttContrl_4plots , skl1_5bins)
_make_plots_4_1_("Z$\\tau\\tau$ CR - nJetsTight", em_me_comparison_channel_4plot, CutZttContrl_4plots , nJetsTight)
_make_plots_4_1_("Z$\\tau\\tau$ CR - DYjj", em_me_comparison_channel_4plot, CutZttContrl_4plots , DYjj)
_make_plots_4_1_("Z$\\tau\\tau$ CR - Mjj", em_me_comparison_channel_4plot, CutZttContrl_4plots , Mjj)
_make_plots_4_1_("Z$\\tau\\tau$ CR - contOLV", em_me_comparison_channel_4plot, CutZttContrl_4plots , contOLV)
_make_plots_4_1_("Z$\\tau\\tau$ CR - DPhill", em_me_comparison_channel_4plot, CutZttContrl_4plots , DPhill)
_make_plots_4_1_("Z$\\tau\\tau$ CR - Mll", em_me_comparison_channel_4plot, CutZttContrl_4plots , Mll)
_make_plots_4_1_("Z$\\tau\\tau$ CR - MT", em_me_comparison_channel_4plot, CutZttContrl_4plots , MT)
_make_plots_4_1_("Z$\\tau\\tau$ CR - SumOFMLepxJety", em_me_comparison_channel_4plot, CutZttContrl_4plots , SumOFMLepxJety)
_make_plots_4_1_("Z$\\tau\\tau$ CR - PtTot", em_me_comparison_channel_4plot, CutZttContrl_4plots , PtTot)
_make_plots_4_1_("Z$\\tau\\tau$ CR - leadJetPt", em_me_comparison_channel_4plot, CutZttContrl_4plots , leadJetPt)
_make_plots_4_1_("Z$\\tau\\tau$ CR - leadJetEta", em_me_comparison_channel_4plot, CutZttContrl_4plots , leadJetEta)
_make_plots_4_1_("Z$\\tau\\tau$ CR - leadJetPhi", em_me_comparison_channel_4plot, CutZttContrl_4plots , leadJetPhi)
_make_plots_4_1_("Z$\\tau\\tau$ CR - subleadJetPt", em_me_comparison_channel_4plot, CutZttContrl_4plots , subleadJetPt)
_make_plots_4_1_("Z$\\tau\\tau$ CR - subleadJetEta", em_me_comparison_channel_4plot, CutZttContrl_4plots , subleadJetEta)
_make_plots_4_1_("Z$\\tau\\tau$ CR - subleadJetPhi", em_me_comparison_channel_4plot, CutZttContrl_4plots , subleadJetPhi)
_make_plots_4_1_("Z$\\tau\\tau$ CR - leadLepPt", em_me_comparison_channel_4plot, CutZttContrl_4plots , leadLepPt)
_make_plots_4_1_("Z$\\tau\\tau$ CR - leadLepEta", em_me_comparison_channel_4plot, CutZttContrl_4plots , leadLepEta)
_make_plots_4_1_("Z$\\tau\\tau$ CR - leadLepPhi", em_me_comparison_channel_4plot, CutZttContrl_4plots , leadLepPhi)
_make_plots_4_1_("Z$\\tau\\tau$ CR - subleadLepPt", em_me_comparison_channel_4plot, CutZttContrl_4plots , subleadLepPt)
_make_plots_4_1_("Z$\\tau\\tau$ CR - subleadLepEta", em_me_comparison_channel_4plot, CutZttContrl_4plots , subleadLepEta)
_make_plots_4_1_("Z$\\tau\\tau$ CR - subleadLepPhi", em_me_comparison_channel_4plot, CutZttContrl_4plots , subleadLepPhi)

make_frame("WW VR")
_make_plots_4_1_("WW VR - MT2-1jet", em_me_comparison_channel_4plot, CutWWContrl_4plots , MT2_1jet)
_make_plots_4_1_("WW VR - nJetsTight", em_me_comparison_channel_4plot, CutWWContrl_4plots , nJetsTight)
_make_plots_4_1_("WW VR - DYjj", em_me_comparison_channel_4plot, CutWWContrl_4plots , DYjj)
_make_plots_4_1_("WW VR - Mjj", em_me_comparison_channel_4plot, CutWWContrl_4plots , Mjj)
_make_plots_4_1_("WW VR - contOLV", em_me_comparison_channel_4plot, CutWWContrl_4plots , contOLV)
_make_plots_4_1_("WW VR - DPhill", em_me_comparison_channel_4plot, CutWWContrl_4plots , DPhill)
_make_plots_4_1_("WW VR - Mll", em_me_comparison_channel_4plot, CutWWContrl_4plots , Mll)
_make_plots_4_1_("WW VR - MT", em_me_comparison_channel_4plot, CutWWContrl_4plots , MT)
_make_plots_4_1_("WW VR - SumOFMLepxJety", em_me_comparison_channel_4plot, CutWWContrl_4plots , SumOFMLepxJety)
_make_plots_4_1_("WW VR - PtTot", em_me_comparison_channel_4plot, CutWWContrl_4plots , PtTot)
_make_plots_4_1_("WW VR - leadJetPt", em_me_comparison_channel_4plot, CutWWContrl_4plots , leadJetPt)
_make_plots_4_1_("WW VR - leadJetEta", em_me_comparison_channel_4plot, CutWWContrl_4plots , leadJetEta)
_make_plots_4_1_("WW VR - leadJetPhi", em_me_comparison_channel_4plot, CutWWContrl_4plots , leadJetPhi)
_make_plots_4_1_("WW VR - subleadJetPt", em_me_comparison_channel_4plot, CutWWContrl_4plots , subleadJetPt)
_make_plots_4_1_("WW VR - subleadJetEta", em_me_comparison_channel_4plot, CutWWContrl_4plots , subleadJetEta)
_make_plots_4_1_("WW VR - subleadJetPhi", em_me_comparison_channel_4plot, CutWWContrl_4plots , subleadJetPhi)
_make_plots_4_1_("WW VR - leadLepPt", em_me_comparison_channel_4plot, CutWWContrl_4plots , leadLepPt)
_make_plots_4_1_("WW VR - leadLepEta", em_me_comparison_channel_4plot, CutWWContrl_4plots , leadLepEta)
_make_plots_4_1_("WW VR - leadLepPhi", em_me_comparison_channel_4plot, CutWWContrl_4plots , leadLepPhi)
_make_plots_4_1_("WW VR - subleadLepPt", em_me_comparison_channel_4plot, CutWWContrl_4plots , subleadLepPt)
_make_plots_4_1_("WW VR - subleadLepEta", em_me_comparison_channel_4plot, CutWWContrl_4plots , subleadLepEta)
_make_plots_4_1_("WW VR - subleadLepPhi", em_me_comparison_channel_4plot, CutWWContrl_4plots , subleadLepPhi)



# _make_plots_6_1_("CutFF - nPV, nInteraction, mtt", em_me_comparison_channel, CutFF, CutFF ,nPV_Kinematics)
# _make_plots_6_1_("CutFF - Leading Leptons kinematics", em_me_comparison_channel, CutFF, CutFF ,Lep_Kinematics)
# _make_plots_6_1_("CutFF - Sub-leading Leptons kinematics", em_me_comparison_channel, CutFF, CutFF ,SubLep_Kinematics)
# _make_plots_6_1_("CutFF - Leading Jets kinematics", em_me_comparison_channel, CutFF, CutFF ,Jet1_Kinematics)
# _make_plots_6_1_("CutFF - Sub-leading Jets kinematics", em_me_comparison_channel, CutFF, CutFF ,Jet2_Kinematics)
# _make_plots_6_1_("CutFF - Jet 3 kinematics", em_me_comparison_channel, CutFF, CutFF ,VBFJet3_Kinematics)
# _make_plots_6_1_("CutFF - Jet 4 kinematics", em_me_comparison_channel, CutFF, CutFF ,VBFJet4_Kinematics)
# _make_plots_6_1_("CutFF - nJet, nJetsTight, DPhillMET", em_me_comparison_channel, CutFF, CutFF , nJet_Kinematics)
# _make_plots_6_1_("CutFF - MT, Mll, DPhill", em_me_comparison_channel, CutFF, CutFF , MT_mll_dphill_Kinematics)
# _make_plots_6_1_("CutFF - Ptll, MTlep0, MTlep1", em_me_comparison_channel, CutFF , CutFF, Ptll_MTlep0_MTlep1_Kinematics)
# _make_plots_6_1_("CutFF - MET, METPhi, MaxMTlep", em_me_comparison_channel, CutFF , CutFF, MET_Kinematics)

# make_frame("CutMET")
# _make_plots_6_1_("CutMET - nPV, nInteraction, mtt", em_me_comparison_channel, CutMET , CutMET,nPV_Kinematics)
# _make_plots_6_1_("CutMET - Leading Leptons kinematics", em_me_comparison_channel, CutMET, CutMET ,Lep_Kinematics)
# _make_plots_6_1_("CutMET - Sub-leading Leptons kinematics", em_me_comparison_channel, CutMET, CutMET ,SubLep_Kinematics)
# _make_plots_6_1_("CutMET - Leading Jets kinematics", em_me_comparison_channel, CutMET, CutMET ,Jet1_Kinematics)
# _make_plots_6_1_("CutMET - Sub-leading Jets kinematics", em_me_comparison_channel, CutMET, CutMET ,Jet2_Kinematics)
# _make_plots_6_1_("CutMET - Jet 3 kinematics", em_me_comparison_channel, CutMET, CutMET ,VBFJet3_Kinematics)
# _make_plots_6_1_("CutMET - Jet 4 kinematics", em_me_comparison_channel, CutMET, CutMET ,VBFJet4_Kinematics)
# _make_plots_6_1_("CutMET - nJet, nJetsTight, DPhillMET", em_me_comparison_channel, CutMET , CutMET, nJet_Kinematics)
# _make_plots_6_1_("CutMET - MT, Mll, DPhill", em_me_comparison_channel, CutMET, CutMET , MT_mll_dphill_Kinematics)
# _make_plots_6_1_("CutMET - Ptll, MTlep0, MTlep1", em_me_comparison_channel, CutMET, CutMET , Ptll_MTlep0_MTlep1_Kinematics)
# _make_plots_6_1_("CutMET - MET, METPhi, MaxMTlep", em_me_comparison_channel, CutMET, CutMET , MET_Kinematics)

# make_frame("CutGGF-1jet")
# _make_plots_6_1_("CutGGF-1jet - nPV, nInteraction, mtt", em_me_comparison_channel, CutGGF_1jet, CutGGF_1jet_name ,nPV_Kinematics)
# _make_plots_6_1_("CutGGF-1jet - Leading Leptons kinematics", em_me_comparison_channel, CutGGF_1jet, CutGGF_1jet_name ,Lep_Kinematics)
# _make_plots_6_1_("CutGGF-1jet - Sub leading Leptons kinematics", em_me_comparison_channel, CutGGF_1jet, CutGGF_1jet_name ,SubLep_Kinematics)
#
# _make_plots_6_1_("CutGGF-1jet - Leading jets kinematics", em_me_comparison_channel, CutGGF_1jet, CutGGF_1jet_name ,VBFJet1_Kinematics)
# _make_plots_4_1_("CutGGF-1jet - Leading jets central and forward kinematics", em_me_comparison_channel, CutGGF_1jet , CutGGF_1jet_name,VBFJet1_Region_Kinematics)
#
# _make_plots_4_1_("CutGGF-1jet - nJetsTight, DPhillMET", em_me_comparison_channel, CutGGF_1jet , CutGGF_1jet_name, nJet_1_Kinematics)
# _make_plots_6_1_("CutGGF-1jet - MT, Mll, DPhill", em_me_comparison_channel, CutGGF_1jet, CutGGF_1jet_name , MT_mll_dphill_Kinematics)
# _make_plots_6_1_("CutGGF-1jet - Ptll, MTlep0, MTlep1", em_me_comparison_channel, CutGGF_1jet, CutGGF_1jet_name , Ptll_MTlep0_MTlep1_Kinematics)
# _make_plots_6_1_("CutGGF-1jet - MET, METPhi, MaxMTlep", em_me_comparison_channel, CutGGF_1jet , CutGGF_1jet_name, MET_Kinematics)
#
# make_frame("CutVBF-2jet")
# _make_plots_6_1_("CutVBF-2jet - nPV, nInteraction, mtt", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,nPV_Kinematics)
# _make_plots_6_1_("CutVBF-2jet - Leading Leptons kinematics", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,Lep_Kinematics)
# _make_plots_6_1_("CutVBF-2jet - Sub leading Leptons kinematics", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,SubLep_Kinematics)
#
# _make_plots_6_1_("CutVBF-2jet - Leading jets kinematics", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,VBFJet1_Kinematics)
# _make_plots_4_1_("CutVBF-2jet - Leading jets central and forward kinematics", em_me_comparison_channel, CutVBF_2jet , CutVBF_2jet_name,VBFJet1_Region_Kinematics)
#
# _make_plots_6_1_("CutVBF-2jet - Sub-leading jets kinematics", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,VBFJet2_Kinematics)
# _make_plots_4_1_("CutVBF-2jet - Sub-leading jets central and forward kinematics", em_me_comparison_channel, CutVBF_2jet , CutVBF_2jet_name,VBFJet2_Region_Kinematics)
#
# _make_plots_6_1_("CutVBF-2jet - jet3 kinematics", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,VBFJet3_Kinematics)
# _make_plots_6_1_("CutVBF-2jet - jet4 kinematics", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name ,VBFJet4_Kinematics)
#
# _make_plots_4_1_("CutVBF-2jet - nJetsTight, DPhillMET", em_me_comparison_channel, CutVBF_2jet , CutVBF_2jet_name, nJet_1_Kinematics)
# _make_plots_6_1_("CutVBF-2jet - MT, Mll, DPhill", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name , MT_mll_dphill_Kinematics)
# _make_plots_6_1_("CutVBF-2jet - Ptll, MTlep0, MTlep1", em_me_comparison_channel, CutVBF_2jet, CutVBF_2jet_name , Ptll_MTlep0_MTlep1_Kinematics)
# _make_plots_6_1_("CutVBF-2jet - MET, METPhi, MaxMTlep", em_me_comparison_channel, CutVBF_2jet , CutVBF_2jet_name, MET_Kinematics)





outF.write("\\begin{frame}\n")
outF.write("\\centering\n")
outF.write("\\textbf{Backup}\n")
outF.write("\\end{frame}\n")
outF.write("\n\end{document}\n")
outF.close()

# os.chdir(path)
# os.system("pdflatex "+path+"Validation.tex")
# os.system("pdflatex "+path+"Validation.tex")

# print(here, texfile_path)

# os.system("pdflatex "+here+"/slides/Validation.tex")
# os.system("pdflatex "+here+"/slides/Validation.tex")

if len(sys.argv)==2:
    print(here)
    os.system("pdflatex "+here+"/slides/Validation.tex")
    os.system("pdflatex "+here+"/slides/Validation.tex")
if len(sys.argv)==3:
    print(texfile_path)
    # os.system("pdflatex "+texfile_path+"Validation.tex")
    # os.system("pdflatex "+texfile_path+"Validation.tex")
