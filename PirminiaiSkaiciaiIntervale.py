import math

min = int(input("Min reiksme: "))  
max = int(input("Max reiksme: "))
n = int(input("Skaitmenu suma: "))

skaiciai = []
ats = []
def pirminiaiSkaiciai(min, max):  
    for num in range(min, max + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:
                skaiciai.append(num) 
    #print(skaiciai)

def skaitmenuSuma(skaiciai):
    for i in range(len(skaiciai)):
        skaicius = skaiciai[i]
        s = 0
        while skaiciai[i]:
            s += skaiciai[i] % 10
            skaiciai[i] //= 10
        if s == n:
            ats.append(skaicius)
        #print(s)    

pirminiaiSkaiciai(min, max)
skaitmenuSuma(skaiciai)      
print(ats)