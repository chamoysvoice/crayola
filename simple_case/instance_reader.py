import sys

f = open(sys.argv[1], 'r')
line = f.readline()



while(line):
    words = line.split()
    if(line[0] == 'p'):
        size = int(words[2])
        matrix = [[0 for x in range(size)] for y in range(size)] 
    if(line[0] == 'e'):
        vertice_a = int(words[1]) - 1
        vertice_b = int(words[2]) - 1
        matrix[vertice_a][vertice_b] = 1
    
    line = f.readline()


for row in matrix:
    print ",".join(str(x) for  x in row)
