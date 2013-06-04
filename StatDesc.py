#
#   Module: 
#   Author: JShen
#   Date: 2/7/13
#   Time: 10:00 AM
#   Version: 
#
#
#	Description:
#       This program is used to analysis the CV results outputted from DF. Calculate the descriptor frequency
#
#
#	Dependence:
#	
#	Usage: 
#
#!/bin/python
import sys
import re

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
    content=inp.readlines()
    desclist=[]
    for line in content:
        descs=re.findall("D\d\d\d",line)
        if len(descs)>0:
            desclist.append(descs[0])
    inp.close()
    return desclist

if __name__ == '__main__':


    if len(sys.argv) < 0:
        print(usage)
        sys.exit(1)

    pass_through_options=[]

    i = 1
    infilelist=[]

    while i < len(sys.argv) - 1:
        if i < len(sys.argv) and sys.argv[i] == "-i":
            i += 1
            while i < len(sys.argv) and sys.argv[i] != "-o":
                infilelist.append(sys.argv[i])
                i += 1
        if i < len(sys.argv) and sys.argv[i] == "-o":
            i += 1
            outfile = sys.argv[i]
        i += 1

    alldesc=[]
    for infile in infilelist:
        desclist=readfile(infile)
        alldesc=alldesc+desclist

    uniqdesc=set(alldesc)

    outp=open(outfile,"w")
    for desc in sorted(uniqdesc):
        outp.write("%s\t%d\n" % (desc,alldesc.count(desc)))

    outp.close()




