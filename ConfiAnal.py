#
#   Module: 
#   Author: JShen
#   Date: 2/7/13
#   Time: 10:00 AM
#   Version: 
#
#
#	Description:
#       This program is used to analysis the CV results outputted from DF. Analysis the confidence
#       It counts the correct and total numbers with the confidence of 0, 0~0.1,0.1~0.2,0.2~0.3,...,0.8~0.9,0.9~1,1
#
#
#	Dependence:
#	
#	Usage: 
#
#!/bin/python
import sys
import re
import string

def usage(name):
    print "\n"
    print "\tUSAGE\n"
    print "\t\t", name, "-i INPUTFILES -o OUTFILES"
    print """
        PARAMETERS

            -h, --help  : Help
            -i,         : input files, delimited by " "
            -o,         : output file

        """
    sys.exit()

def readfile(inputfile):
    # read the input file and generate a matrix
    inp=open(inputfile,"r")
    inpmatrix=inp.readlines()
    Ylist=[]
    matrix=[inpmatrix[0].strip("\n").strip("\r").split("\t")]
    for line in inpmatrix[1:]:
        items=line.strip("\n").strip("\r").split("\t")
        Ylist.append(int(items[2]))
        dataline=[]
        for item in items:
            dataline.append(item)
        matrix.append(dataline)
    inp.close()
    return Ylist, matrix

def getprediction(infile):
    # read the output file and generate a matrix of predictions(Lines between "ID\tchemid...." and "TOTAL\ data\ set")
    """

    """
    inp=open(infile,"r")
    boolstart=False;
    prematrix=[]
    while True:
        line=inp.readline()

        if "Total data set" in line :
            break
        if "ID\tchemid" not in line:
            if not boolstart:
                continue
        else:
            boolstart=True
            continue
        if boolstart:
            item=line.strip("\n").strip("\r").split("\t")
            prematrix.append([int(item[2]),int(round(float(item[4]))),float(item[-1])])
            continue
    return prematrix;


if __name__ == '__main__':


    if len(sys.argv) <= 1:
        print(usage)
        sys.exit(1)

    pass_through_options=[]

    i = 1
    infilelist=[]

    while i < len(sys.argv) - 1:
        if i < len(sys.argv):
            print(usage)
            sys.exit(1)
        if i < len(sys.argv) and sys.argv[i] == "-i":
            i += 1
            while i < len(sys.argv) and sys.argv[i] != "-o":
                infilelist.append(sys.argv[i])
                i += 1
        if i < len(sys.argv) and sys.argv[i] == "-o":
            i += 1
            outfile = sys.argv[i]
        i += 1



    totaln=[0,0,0,0,0,0,0,0,0,0,0]
    correctn=[0,0,0,0,0,0,0,0,0,0,0]
    for infile in infilelist:
        prematrix=getprediction(infile)
        l=len(prematrix)
        for i in range(0,l):
            totaln[int(prematrix[i][2]*10)]+=1
            if prematrix[i][0]==prematrix[i][1]:
                correctn[int(prematrix[i][2]*10)]+=1
    for i in range(0,len(totaln)):
        print("%f\t%d\t%d\t%f" % (i/10.0, correctn[i], totaln[i], correctn[i]*1.0/totaln[i]))







"""
        desclist=readfile(infile)
        alldesc=alldesc+desclist

    uniqdesc=set(alldesc)

    outp=open(outfile,"w")
    for desc in sorted(uniqdesc):
        outp.write("%s\t%d\n" % (desc,alldesc.count(desc)))

    outp.close()
"""



