from bisect import bisect_left
from sys import stdin, stdout

 


def readInput():
    values = stdin.readline().split()
    return values


def percentil(matrix, value):
    n = 0
    lenMat = len(matrix)
    val = int(bisect_left(matrix, value) / lenMat * 100)
    return str(val) + " "

def quicksort(raster, low=0, high=None):
    if high is None:
        high = len(raster)-1
    if (low+1>high):
        for i in range(low, high+1):
            tmp = raster[i]
            j = i
            while j > 0 and tmp < raster[j-1]:
                raster[j] = raster[j-1]
                j -= 1
            raster[j] = tmp
    else:
    
        mid = (high + low) // 2

        if raster[mid] < raster[low]:
            tmp = raster[low]
            raster[low] = raster[mid]
            raster[mid] = tmp

        if raster[high] < raster[low]:
            tmp = raster[low]
            raster[low] = raster[high]
            raster[high] = tmp

        if raster[high] < raster[mid]:
            tmp = raster[mid]
            raster[mid] = raster[high]
            raster[high] = tmp

       
        tmp = raster[mid]
        raster[mid] = raster[high - 1]
        raster[high - 1] = tmp

    
        pivot = raster[high - 1]

        

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
    inp = readInput()

    while inp[0] != "TCHAU":
        if inp[0] == "RASTER":
            if (len(inp) != 3):
                stdout.write("WRONG FORMAT <RASTER> <N> <M>\n")
            else:
                N = int(inp[1])
                M = int(inp[2])
                rasterUni = []
                for i in range(N):
                    inp2 = readInput()
                    if len(inp2) != M:
                        stdout.write("WRONG FORMAT\n")
                        return 1
                    else:
                        for l in range(M):
                            rasterUni.append(int(inp2[l]))

        

                #quick sort
                quicksort(rasterUni)
                print(rasterUni)
                stdout.write("RASTER GUARDADO\n")


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
                inp2 = readInput()
                if n != len(inp2):
                    stdout.write("WRONG NUMBER OF NUMBERS\n")
                else:
                    for i in range(len(inp2)):
                        payload += percentil(rasterUni, int(inp2[i]))

                    stdout.write(payload.rstrip())
                    stdout.write("\n")
        inp = readInput()


if __name__ == '__main__':
    main()