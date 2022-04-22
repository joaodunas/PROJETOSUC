from sys import stdin, stdout




def readInput():
    values = stdin.readline().split()
    return values

def percentil(matrix, value):
    n= 0
    lenMat = 0
    if isinstance(matrix[0], list):
        lenMat = len(matrix) * len(matrix[0])
        for i in matrix:
            for l in i:
                if l < value:
                    n += 1
    else:
        lenMat = len(matrix)
        for i in matrix:
            if i < value:
                n += 1
    val = int(n/lenMat * 100)
    return str(val) + " "

'''
def ordenar(matrix):
    matrix1d =[]
    if isinstance(matrix[0], list):
        for i in matrix:
            for l in i:
                matrix1d.append(l)
    else:
        matrix1d = matrix

    result = []
    
    while len(matrix1d) >0:
        minVal = matrix1d[0]
        for i in matrix1d:
            if minVal >= i:
                minVal = i

        matrix1d.remove(minVal)
        result.append(minVal)
    return result
'''

def mediana(matrix):
    
    


def main():
    inp = readInput()
    
    while(inp[0] != "TCHAU"):
        if (inp[0] == "RASTER"):
            if (len(inp) != 3):
                stdout.write("WRONG FORMAT <RASTER> <N> <M>\n")
            else:
                N = int(inp[1])
                M = int(inp[2])
                raster = [[0 for x in range(M)] for x in range(N)] 
                for i in range(N):
                    inp2 = readInput()
                    if (len(inp2) != M):
                        stdout.write("WRONG FORMAT\n")
                        return 1
                    else:
                        if M >1:
                            for l in range(M):
                                raster[i][l] = int(inp2[l])
                        else:
                            raster[i] = int(inp2[0])
                            '''
                            if max < inp[l]:
                                max = inp[l]
                            if min > inp[l]:
                                min = inp[l]
                            '''
                stdout.write("RASTER GRADUADO\n")
        if (inp[0] == "AMPLITUDE"):
            if M > 1:
                max = raster[0][0]
                min = raster[0][0]
                for i in range (N):
                    for l in range (M):
                        if max < raster[i][l]:
                            max = raster[i][l]
                        if min > raster[i][l]:
                            min = raster[i][l]
            else:
                max = raster[0]
                min = raster[0]
                for i in range(N):
                    if max < raster[i]:
                        max = raster[i]
                    if min > raster[i]:
                        min = raster[i]
            stdout.write(str(max-min)+ "\n")

        if (inp[0] == "MEDIANA"):
            '''
            rasterOrdenado = ordenar(raster)
            if len(rasterOrdenado) % 2 == 0:
                res = (rasterOrdenado[int(len(rasterOrdenado)/2)-1]+ rasterOrdenado[int(len(rasterOrdenado)/2)]) / 2
                stdout.write(str(int(res))+"\n")
            else:
                stdout.write(str(rasterOrdenado[int(len(rasterOrdenado)/2)])+ "\n")
            '''
            mediana(raster)

        if (inp[0] == "PERCENTIL"):
            if (len(inp) != 2):
                stdout.write("WRONG FORMAT\n")
            else:
                payload = ""
                n = int(inp[1])
                inp2 = readInput()
                if n != len(inp2):
                    stdout.write("WRONG NUMBER OF NUMBERS\n")
                else:
                    for i in range(len(inp2)):
                        payload += percentil(raster, int(inp2[i]))
                    

                    stdout.write(payload.rstrip())
                    stdout.write("\n")
        inp = readInput()
                    




                    
            


        
        


if __name__ == '__main__':
    main()