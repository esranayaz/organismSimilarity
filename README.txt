$parse.py <input file>
parses a .fatsa file and converts it to a file in form [ "organism", "protein", "fasta"]
output file name --> processed_<infile>.json

$parseOrganism.py <input file> <organism name in quotes>
parses a .fasta file and passes organism's proteins to output file line by line
output file name --> <organism>_proteins_<infile>.txt

$protein.py <processed input file> <file containing proteins line by line>
mapreduce
	input: ["insulin","insan","ABC.."]
	output: ["insulin",(("insan","ABC.."),("kedi","XYZ.."),...)]
output file name --> out_<processed input file>.json

*warning: there were protein names like insulin-1, insulin-2, ..., etc. indicating the
	  same protein. protein.py merges them together as well as grouping them using
	  mapreduce.

$EditDistance.py <output of protein.py>
output file name -> editdistance_<infile>.json

$protein2.py <output of EditDistance.py>


***

Original MapReduce.py: https://github.com/mon95/Implementation-of-MapReduce-algorithms-using-a-simple-Python-MapReduce-framework 
Note: MapReduce is used to group data together, not for speed up.

***

1ST MAPREDUCE
input: ["insulin","insan","ABC.."]
output: ["insulin",(("insan","ABC.."),("kedi","XYZ.."),...)]

EDIT DISTANCE
input: ["insulin",(("insan","ABC.."),("kedi","XYZ.."),...)]
output: ["insulin",(("kedi, 95%"),("fare","87%"),...)]

2ND MAPREDUCE
input: ["insulin",(("kedi, 95%"),("fare","87%"),...)]
output: ["insan",("kedi, 95%"),("fare","87%"),...)]

*** 

sample output:

[["Homo sapiens", "Mus musculus"], 0.6940215456658885]
[["Homo sapiens", "Sus scrofa"], 0.7027358307680194]
[["Homo sapiens", "Xenopus laevis"], 0.5941235463296289]
