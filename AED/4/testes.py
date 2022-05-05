from sys import stdin,stdout

import random








def main():

    val = 50

    with open("testes.txt","w") as f: 
        f.write("RASTER "+ str(val)+ " "+ str(val)+ "\n")
        for i in range(val):
            payload = ""
            for h in range(val):
                payload += str(random.randint(0,10000))+ " "
            f.write(payload.rstrip()+ "\n")
            
        f.write("PERCENTIL "+ str(val*val)+ "\n")
        payload = ""
        for i in range(val*val):
            payload += str(random.randint(0,10000))+ " "
        f.write(payload.rstrip()+ "\n")
        f.write("TCHAU")
                

        


            

            



if __name__ == "__main__":
    main()