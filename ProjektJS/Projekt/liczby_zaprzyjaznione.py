import sys,os

def sumDivisors(number):
    newSum = 0
    for x in range(1, number):
        if number%x == 0:
            newSum+=x
        else:
            continue
    return newSum

def areFriends(num1,num2):
    k=""
    if num1!=num2:
        a=sumDivisors(num1)
        b=sumDivisors(num2)
        if num1==b and num2==a:
            k="Liczby "+str(num1)+" oraz "+ str(num2)+" są razem zaprzyjaźnione! :)"
        else:
            k="Liczby "+str(num1)+" oraz "+str(num2)+" nie są zaprzyjaźnione! :("
    else:
       k = "TO TA SAMA LICZBA! Oszustwo!"
    
    return k

def LoadFile(fol):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, fol)
    text=""
    try:
        folder=open(filename,"r")
        text = folder.readlines()    
    except IOError:
        print("Błąd przy próbie otworzenia pliku!")
        print(filename)
        exit() 
    return text

def SaveFile(czyzap, fileName):
    fil = open(fileName+"_wyniki.txt", "a")
    fil.write(str(czyzap))
    fil.write("\nPochodzą z pliku: "+fileName+"\n")
    fil.close()

def statistics(fileName):
    yes = 0
    no = 0
    lie = 0
    newName=fileName+"_wyniki.txt"
    fol = LoadFile(newName)
    fol1=[]
    for n in range(0,len(fol)):
        fol1+=fol[n].split(" ")

    #fol1=fol.split("\w ")
    for x in range(0, len(fol1)):
        if fol1[x]=="nie":
            no+=1
        if fol1[x]=="razem":
            yes+=1
        if fol1[x]=="SAMA":
            lie+=1
        else:
            continue
    
    naTak = "Ilość par zaprzyjaźnionych: "+str(yes)
    naNie = "Ilość par niezaprzyjaźnionych: "+str(no)
    together = "Ilość par przeszukanych: "+str((yes+no))
    oszustwa = "Ilość par, które były tymi samymi liczbami: "+str(lie)
    saveName = fileName+"_statystyka.txt"
    k = open(saveName, "w")
    k.write(naTak+"\n"+naNie+"\n"+together+"\n"+oszustwa)


l = input("Podaj nazwę pliku bez jego rozszerzenia: ")
test = LoadFile(l+".txt")
for x in range(0,len(test)):
    luv = test[x].split(" ")
    c = int(luv[0])
    d = int(luv[1])
    kap=areFriends(c,d)
    SaveFile(kap, l)
statistics(l)





