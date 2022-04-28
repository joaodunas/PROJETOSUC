from sys import stdin, stdout


def readInput():
    values = stdin.readline().split()
    return values


def percentil(matrix, value):
    n = 0
    
    
    lenMat = len(matrix)
    for i in matrix:
        if i < value:
            n += 1
    val = int(n / lenMat * 100)
    return str(val) + " "


def mediana(matrix):
    buff = matrix.copy()
    buff2 = []
    half = len(matrix) // 2
    i = 0
    minimum = min(buff)

    while i != half:
        buff.remove(minimum)
        buff2.append(minimum)
        minimum = min(buff)
        i += 1

    if (len(matrix) % 2) == 0:
        return (minimum + buff2[-1]) // 2
    else:
        return minimum


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
                                
                               
                        

                stdout.write("RASTER GUARDADO\n")
        if inp[0] == "AMPLITUDE":
            maximum = rasterUni[0]
            minimum = rasterUni[0]
            for i in rasterUni:
                if maximum < i:
                    maximum = i
                if minimum > i:
                    minimum = i
            stdout.write(str(maximum - minimum) + "\n")

        if inp[0] == "MEDIANA":
            stdout.write(str(mediana(rasterUni)) + "\n")

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