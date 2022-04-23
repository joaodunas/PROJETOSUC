from random import randint


def generate_tests(num, show=False, lvl=0):
    def generate_tests_util(num, show=False, lvl=0):
        temp = []
        while num != 1:
            a = randint(1, num - 1)
            num -= a
            temp.append(a)
            print(f"Utilizador{randint(0, 10000)} {randint(0, 1000)} {randint(1000, 9999)}")
        for i in temp:
            generate_tests_util(i, show, lvl + 1)

    generate_tests_util(num, show, lvl)


if __name__ == '__main__':

    n = 2000000
    numeroInsercoes = 100000
    numeroConsulta = int(n)

    ficheiro = open("input - Splay.txt", "w")

    listaInsercoes = []
    listaAlpha = []
    for i in range(numeroInsercoes):
        numeroRandom = randint(0, n)
        listaAlpha.append(randint(100000, 999999))
        ficheiro.write(f"ARTIGO Pintura{numeroRandom} {listaAlpha[i]} {randint(1000, 9999)}\n")
        listaInsercoes.append(f"Pintura{numeroRandom}")



    for i in range(numeroConsulta):
        ficheiro.write(f"CONSULTA {listaInsercoes[randint(1,len(listaInsercoes)-1)]}\n")
        numeroConsulta -= 1

    
    ficheiro.write("FIM\n")
