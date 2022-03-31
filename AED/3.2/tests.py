from string import ascii_letters
from sys import stdin
from collections import deque
import sys
sys.setrecursionlimit(1000000)


import string
import numpy as np


def rndmHash():

    
    hexStr = ""
    for i in range(3):
        hexStr += np.random.choice( (string.ascii_lowercase + string.digits).split() )
    
    return hexStr


def rndmName():

    rndmStr = ""

    for i in range(np.random.randint(6,9)):
        rndmStr += np.random.choice( string.ascii_lowercase.split() )
    
    return rndmStr

def rndmArt(f,nrArtigos,mode):

    artigos = []

    #Gerar artigos
    for elemIndex in range(nrArtigos):
        random_name = rndmName()
        f.write("ARTIGO "+random_name+" " + str(rndmHash()) + " " + str(np.random.randint(1, 750)) + "\n")
        artigos.append(random_name)

    #Se for o modo assimétrico
    if mode == 1:
        artigos50 = []

        for i in range(nrArtigos):
            rndmNumber = np.random.randint(0,1000)
            if rndmNumber <= 50:
                artigos50.append(artigos[i])

        return artigos, artigos50

    return artigos


def genAccess(f,nrAcessos,artigos,mode,*args):

    opsList = ["OFERTA","CONSULTA"]
    
    if mode == 1:
        artigos50 = args[0]

    #Gerar Acessos
    if mode == 2:
        for i in range(nrAcessos):
            opAtual = np.random.choice(opsList)

            if opAtual == "CONSULTA":
                f.write("CONSULTA "+ str(np.random.choice(artigos)) + "\n")

            else:
                f.write("OFERTA " + str(np.random.choice(artigos))+ " " + str(np.random.randint(751,1500)))

    else:
        
        for i in range(nrAcessos):
            opAtual = np.random.choice(opsList)
            rndmNumber = np.random.randint(0,1000)

            if opAtual == "CONSULTA":

                if(rndmNumber <= 50):
                    f.write("CONSULTA " + str(np.random.choice(artigos)) + "\n")

                else:
                    f.write("CONSULTA " + str(np.random.choice(artigos50)) + "\n")


            else:


                if(rndmNumber <= 50):
                    f.write("OFERTA " + str(np.random.choice(artigos)) + " " + str(np.random.randint(751, 1500)))

                else:
                    f.write("OFERTA " + str(np.random.choice(artigos50)) + " " + str(np.random.randint(751, 1500)))

def main():

    


    """
    TESTS
    """

    #valores = [100,1000,5000,10000,15000,20000,30000,40000,50000]
    valores = [50000]
    numero_nos = 100000

    print("\nMODO1\n")
    f1 = open("Modo1.txt","w")
    #Modo 1
    for val in valores:



        rt,rt50 = rndmArt(f1,numero_nos,1)


        genAccess(f1,val,rt,1,rt50)
    f1.write("FIM\n")

    f1.close()


    f2 = open("Modo2.txt","w")
    print("\nMODO2\n")
    #Modo 2
    for val in valores:

        rt = rndmArt(f2, numero_nos, 2)


        genAccess(f2,val,rt,2)

    f2.write("FIM\n")
    f2.close()

if __name__ == '__main__':
    main()