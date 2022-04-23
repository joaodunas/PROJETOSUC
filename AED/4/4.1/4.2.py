from sys import stdin, stdout


def readInput():
    values = stdin.readline().split()
    return values


def percentil(matrix, value):
    n = 0

    lenMat = len(matrix)
    i = 0
    while i < lenMat and matrix[i] < value:
        n += 1
        i += 1
    val = int(n / lenMat * 100)
    return str(val) + " "



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

                #bubble sort

                for i in range(len(rasterUni)):
                    h = len(rasterUni)-1-i
                    c = 1

                    while c <= h:
                        if rasterUni[c] < rasterUni[c-1]:
                            buffer = rasterUni[c]
                            rasterUni[c] = rasterUni[c-1]
                            rasterUni[c-1] = buffer
                        c += 1

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
