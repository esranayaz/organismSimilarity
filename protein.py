import MapReduce
import sys

infile = sys.argv[1]
protfile = sys.argv[2]
outfile = "out_" + protfile.split(".")[0] + ".json"
of = open( outfile, "w")

print(infile)
print(protfile)
print(outfile)

proteins = set()
#lineno = 1
with open(protfile) as f:
    for line in f:
        proteins.add(line.split('|')[1])
#print(proteins)

"""
INPUT
    organism, protein, fasta
OUTPUT
    protein, (organism, fasta)
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: protein
    # value: (organism, fasta)
    #print(record[0]) #organism
    #print(record[1]) #protein
    #print(record[2]) #fasta
    for protein in proteins:
        #print(protein)
        if record[1] == protein:
        #print("protein: " + protein + "\trecord[1]: " + record[1])
            key = protein
            value = (record[0], record[2])
            mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    # key: protein
    # value: ((organism, fasta), (organism, fasta), ...)
    #print(key)
    mr.emit((key, list(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(infile)
    mr.execute(inputdata, mapper, reducer, of)
