#
#   Module: 
#   Author: JShen
#   Date: 2/5/13
#   Time: 8:55 AM
#   Version: 
#
#
#	Description:
#       This module is used to generate permutation input matrix for DF developed by NCTR.
#       It reads the input file with the same format of DF and generate N random input matrix (permutation)
#
#
#	Dependence:
#	
#	Usage: 
#
#!/bin/python
import getopt
import random
import sys

def usage(name):
    print "\n"
    print "\tUSAGE\n"
    print "\t\t", name, "-i INPUTFILE -n MATRIXNUMBERS"
    print """
        PARAMETERS

            -h, --help    : Help
            -i,        : input sdf file, contain a list of mols
            -n,        : number of permutation matrix generated [1-5000]

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
        Ylist.append(items[2])
        dataline=[]
        for item in items:
            dataline.append(item)
        matrix.append(dataline)
    inp.close()
    return Ylist, matrix

def permutMatrix(matrix, pmYlist):
    # generate a permutation matrix
    i=0
    for dataline in matrix[1:]:
        dataline[2]=pmYlist[i]
        i=i+1
    return matrix

def writeMatrix(matrix,filename):
    outp=open(filename,"w")
    for dataline in matrix:
        for data in dataline[:-1]:
            outp.write("%s\t" % data)
        outp.write("%s\n" % data)
    outp.close()
    return 0

if __name__ == '__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:n:",["help"])
    except getopt.GetoptError:
        usage(sys.argv[0])

    logfile="log.txt"

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage(sys.argv[0])
        elif opt in ("-i"):
            infile=arg
        elif opt in ("-n"):
            n=int(arg)

    source="".join(args)

    Ylist,matrix=readfile(infile)

    for i in range(1,n+1):
        pmYlist=Ylist[:]
        random.shuffle(pmYlist)
        pmMatrix=permutMatrix(matrix,pmYlist)
        writeMatrix(pmMatrix,"pm"+str(i)+".txt")



