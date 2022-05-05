from bisect import bisect_left
from sys import stdin, stdout
from time import perf_counter


def readInput():
    values = stdin.readline().split()
    return values

def binarySearch(arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
        # Element is not present in the array
        return -1


def percentil(matrix, value):
    n = 0

    lenMat = len(matrix)
    
    val = binarySearch(matrix, 0, len(matrix)-1, value)
    #val = int(bisect_left(matrix, value) / lenMat * 100)
    if val == -1:
        if val > matrix[lenMat-1]:
            return str(100) + " "
        else:
            return str(0) + " "
    else:
        return str(val/lenMat * 100)
    



def main():
    for h in range(3):
        stdin = open("testes.txt", "r")
        inp = stdin.readline().rstrip().split()

        while inp[0] != "TCHAU":
            if inp[0] == "RASTER":
                if (len(inp) != 3):
                    #stdout.write("WRONG FORMAT <RASTER> <N> <M>\n")
                    pass
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

                #insertion sort
                    start = perf_counter()
                    for i in range(1, len(rasterUni)):
                        tmp = rasterUni[i]
                        j = i
                        while j > 0 and tmp < rasterUni[j-1]:
                            rasterUni[j] = rasterUni[j-1]
                            j -= 1
                        rasterUni[j] = tmp



                    #stdout.write("RASTER GUARDADO\n")

            if inp[0] == "PERCENTIL":
                if len(inp) != 2:
                    #stdout.write("WRONG FORMAT\n")
                    pass
                else:
                    #payload = ""
                    n = int(inp[1])
                    inp2 = stdin.readline().rstrip().split()
                    if n != len(inp2):
                        #stdout.write("WRONG NUMBER OF NUMBERS\n")
                        pass
                    else:
                        
                        for i in range(len(inp2)):
                            percentil(rasterUni, int(inp2[i]))
                        finish = perf_counter()

                        #stdout.write(payload.rstrip())
                        #stdout.write("\n")
            inp = stdin.readline().rstrip().split()
        with open("resultados2.txt", "a") as f:
            f.write(str(finish-start)+ "\n")


if __name__ == '__main__':
    main()
