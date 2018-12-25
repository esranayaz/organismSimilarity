import sys
import re

infile = sys.argv[1]
on = sys.argv[2]

outfile = on + "_proteins_" + infile.split(".")[0] + ".txt"
of = open( outfile, "w")
count = 0

fasta = ""
test = []

lastorganism = ""
organismname = ""

with open(infile) as file_one:
    for line in file_one:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith(">"):
            if organismname == on:
                print( "fasta: " + fasta)
                of.write(fasta + "\n")
            
            start='OS='
            stop='OX='
            organismname=((line.split(start))[1].split(stop)[0])
            organismname=organismname[0:len(organismname)-1]
            if organismname == on:
                start='|'
                stop='OS='
                proteinname = (line.split(start))[2].split(stop)[0]
                proteinname = proteinname.split(' ', 1)[1]
                proteinname=proteinname[0:len(proteinname)-1]
                print(organismname)
                of.write( "|" + proteinname + "| ")# + '\n')

        elif line.startswith("M"):
            fasta = line
        else:
            lastorganism = organismname
            fasta = fasta + line
