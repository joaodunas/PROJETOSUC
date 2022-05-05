from bisect import bisect_left
from sys import stdin, stdout

from time import perf_counter


 


def readInput():
    values = stdin.readline().split()
    return values


def percentil(matrix, value):
    lenMat = len(matrix)
    val = int(bisect_left(matrix, value) / lenMat * 100)
    return str(val) + " "


'''
def quicksort(raster, low=0, high=None):
    if high is None:
        high = len(raster)
    while(len(raster) > 30):
        if low < high:
            p = partition(raster, low, high)
            quicksort(raster, low, p)
            quicksort(raster, p + 1, high)


    for i in range(1, len(raster)):
        tmp = raster[i]
        j = i
        while j > 0 and tmp < raster[j-1]:
            raster[j] = raster[j-1]
            j -= 1
        raster[j] = tmp
    return raster

def partition(raster, low, high):
    #median of three
    pivotArray = []
    pivotArray.append(raster[low])
    pivotArray.append(raster[high-1])
    pivotArray.append(raster[(low+high)//2])
    sorted(pivotArray)
    pivot = pivotArray[1]

    for i in range(low, high):
        if raster[i] > pivot:
            high += 1
        else:
            high += 1
            low += 1
            buff = raster[i]
            raster[i] = raster[low-1]
            raster[low-1] = buff
    return low - 1
'''

def quicksort(raster, low=0, high=None):
    if high is None:
        high = len(raster)
    if (low+1>high):
        for i in range(1, len(raster)):
            tmp = raster[i]
            j = i
            while j > 0 and tmp < raster[j-1]:
                raster[j] = raster[j-1]
                j -= 1
            raster[j] = tmp
    else:
        pivotArray = []
        pivotArray.append(raster[low])
        pivotArray.append(raster[high-1])
        pivotArray.append(raster[(low+high)//2])
        pivotArray.sort()
        pivot = pivotArray[1]

        posPivot= raster.index(pivot)
        tmp = raster[posPivot]
        raster[posPivot] = raster[high-1]
        raster[high-1] = tmp

        i = low
        j = high-1
        while(1):
            while(1):
                i+=1
                if (raster[i] >= pivot):
                    break
            
            while(1):
                j-= 1
                if (pivot >= raster[j]):
                    break
            if (i<j):
                tmp = raster[i]
                raster[i] = raster[j]
                raster[j] = tmp
            else:
                break

        tmp = raster[i]
        raster[i] = raster[high-1]
        raster[high-1] = tmp

        quicksort(raster, low, i-1)
        
        quicksort(raster, i+1, high)






    

    

def main():
    for h in range(1):
        stdin = open("testes.txt", "r")
        inp = stdin.readline().rstrip().split()
        while inp[0] != "TCHAU":
            
            if inp[0] == "RASTER":
                if (len(inp) != 3):
                    stdout.write("WRONG FORMAT <RASTER> <N> <M>\n")
                else:
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

            

                    #quick sort
                    start = perf_counter()
                    quicksort(rasterUni)
                    #stdout.write("RASTER GUARDADO\n")


            if inp[0] == "AMPLITUDE":
                stdout.write(str(rasterUni[-1] - rasterUni[0]) + "\n")

            if inp[0] == "MEDIANA":
                if len(rasterUni) % 2 == 0:
                    res = (rasterUni[int(len(rasterUni) / 2) - 1] + rasterUni[
                        int(len(rasterUni) / 2)]) / 2
                    stdout.write(str(int(res)) + "\n")
                else:
                    stdout.write(str(rasterUni[int(len(rasterUni) / 2)]) + "\n")

            if inp[0] == "PERCENTIL":
                if len(inp) != 2:
                    stdout.write("WRONG FORMAT\n")
                else:
                    payload = ""
                    n = int(inp[1])
                    inp2 = stdin.readline().rstrip().split()
                    if n != len(inp2):
                        stdout.write("WRONG NUMBER OF NUMBERS\n")
                    else:
                        for i in range(len(inp2)):
                            payload += percentil(rasterUni, int(inp2[i]))
                        finish = perf_counter()
                        #stdout.write(payload.rstrip())
                        #stdout.write("\n")
            inp = stdin.readline().rstrip().split()
        with open("resultados3.txt", "a") as f:
            f.write(str(finish-start)+ "\n")


if __name__ == '__main__':
    main()
