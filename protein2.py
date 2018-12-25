import MapReduce2
import sys

"""
INPUT
    protein (organism, similarity)
OUTPUT
    (human, organism) avg similarity

"""

mr = MapReduce2.MapReduce()

def mapper(record):
    key = record[0]
    value = record[1]
    for w in value:
        if(w[0] != "Homo sapiens"):
            key1 = ("Homo sapiens", w[0])
            val1 = w[1]
            mr.emit_intermediate(key1, val1)

def reducer(key, list_of_values):
    total = 0
    for item in list_of_values:
       i = float(item)
       total = total + i
    avg = total / len(list_of_values)
    mr.emit((key, avg))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
