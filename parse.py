import sys
import re

fasta = []
test = []
infile=sys.argv[1]
outfile="processed_" + infile.split(".")[0] + ".json"
of = open(outfile, "a")
count = 0

with open(infile) as file_one:
    for line in file_one:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith(">"):
            if count == 0:
                count = 1
            else:
                fasta.append('"]\n')
            fasta.append('["')
            
            start='OS='
            stop='OX='
            organismname=((line.split(start))[1].split(stop)[0])
            organismname=organismname[0:len(organismname)-1]
            fasta.append(organismname)
            fasta.append('", "')
            
            start='|'
            stop='OS='
            proteinname = (line.split(start))[2].split(stop)[0]
            proteinname = proteinname.split(' ', 1)[1]
            proteinname=proteinname[0:len(proteinname)-1]
            fasta.append(proteinname)
            fasta.append('", "')
            
            active_sequence_name = line[2:]
            if active_sequence_name not in fasta:
                test.append(''.join(fasta))
                fasta = []
            continue
        sequence = line
        fasta.append(sequence)
fasta.append('"]')

# Flush the last fasta block to the test list
if fasta:
    test.append(''.join(fasta))

# Print the test list
for i, row in enumerate(test):
    of.write(row)
    #print(row)

