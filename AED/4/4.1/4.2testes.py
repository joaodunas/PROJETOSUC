from sys import stdin, stdout
from time import perf_counter
from bisect import bisect_left



def percentil(matrix, value):
    lenMat = len(matrix)
    
    
    
    val = int(bisect_left(matrix, value) / lenMat * 100)
    return str(val/lenMat * 100)

def main():
    stdin = open("testes.txt", "r")
    inp = stdin.readline().rstrip().split()
    while inp[0] != "TCHAU":
        if inp[0] == "RASTER":
            
                N = int(inp[1])
                M = int(inp[2])
                rasterUni = []
                for i in range(N):
                    inp2 = stdin.readline().rstrip().split()
                    if len(inp2) != M:
                        #stdout.write("WRONG FORMAT\n")
                        return 1
                    else:
                        for l in range(M):
                            rasterUni.append(int(inp2[l]))
        if inp[0] == "PERCENTIL":
            n = int(inp[1])
            inp2 = stdin.readline().rstrip().split()
            start = perf_counter()
            for i in range(1, len(rasterUni)):
                tmp = rasterUni[i]
                j = i
                while j > 0 and tmp < rasterUni[j-1]:
                    rasterUni[j] = rasterUni[j-1]
                    j -= 1
                    rasterUni[j] = tmp

            for i in range(len(inp2)):
                    percentil(rasterUni, int(inp2[i]))
            finish = perf_counter()
        inp = stdin.readline().rstrip().split()

    with open("resultados2.txt", "a") as f:
            f.write(str(finish-start)+ "\n")

if __name__ == '__main__':
    main()
