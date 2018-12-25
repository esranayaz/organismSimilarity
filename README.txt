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

$similarity.py


1ST MAPREDUCE
input: ["insulin","insan","ABC.."]
output: ["insulin",(("insan","ABC.."),("kedi","XYZ.."),...)]

EDIT DISTANCE
input: ["insulin",(("insan","ABC.."),("kedi","XYZ.."),...)]
output: ["insulin",(("kedi, 95%"),("fare","87%"),...)]

2ND OUTPUT
input: ["insulin",(("kedi, 95%"),("fare","87%"),...)]
output: ["insan",("kedi, 95%"),("fare","87%"),...)]