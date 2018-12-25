import sys

protfile = sys.argv[1]
infile = sys.argv[2]
outfile = "editdistance_" + infile.split(".")[0] + ".json"
of = open( outfile, "w")

#human proteins
proteins = {}
protcount = 0
with open(protfile) as f:
    for line in f:
        key = line.split('| ')[0]
        key = key[1:len(key)]
        value = line.split('| ')[1]
        value = value[0:len(value)-1]
        proteins[key] = value
        protcount = protcount + 1

db = {}
with open(infile) as f:
    for line in f:
        proteinname = (line.split(']]]')[0]).split('[[')[0]
        proteinname = proteinname[2:len(proteinname)-3]
        orgfasta = (line.split(']]]')[0]).split('[[')[1]
        orgfasta = "[" + orgfasta + "]"
        orgfastasplit = orgfasta.split("],")
        length = len(orgfastasplit)
        key = proteinname
        db.setdefault(key, [])
        for i in range(length):
            organism = (orgfastasplit[i].split('["')[1]).split('"')[0]
            fasta = (orgfastasplit[i].split(' "')[1]).split('"]')[0]
            #if organism != "Homo sapiens":
            db[key].append([organism, fasta])

#######
def ed(word1, word2):
    len_1=len(word1)
    len_2=len(word2)
    
    x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance
    
    for i in range(0,len_1+1): #initialization of base case values
        x[i][0]=i
    for j in range(0,len_2+1):
        x[0][j]=j
    for i in range (1,len_1+1):
        
        for j in range(1,len_2+1):
            
            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1]
            
            else :
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1

    if len_1 < len_2:
        return (1-(x[i][j])/len_2)
    else:
        return (1-(x[i][j])/len_1)

##########

for i in proteins:
    word1 = proteins[i]
    of.write('["' + i + '",[')
    print('["' + i + '",]')
    for key in db:
        val = db[key]
        if i == key:
            k = 0 
            for j in val:
                word2 = j[1]
                distance = ed(word1, word2)
                if k < (len(val) - 1):
                    of.write('["' + j[0] + '", "' + str(distance) + '"],')
                    if j[0] != "Homo sapiens":
                        print( ('[' + j[0] + '", "' + str(distance) + '"],'))
                else:
                    of.write('["' + j[0] + '", "' + str(distance) + '"]')
                    if j[0] != "Homo sapiens":
                        print( ('[' + j[0] + '", "' + str(distance) + '"]'))
                k += 1
    print(']]\n')
    of.write(']]\n')

# output: ["insulin",(("kedi, 95%"),("fare","87%"),...)]
