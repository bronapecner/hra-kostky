
import random

opak=0
opak2=0
sez=[]
celkskorehrace=0
celkskorepc=0
skorehrace=0
skorepc=0
hod=0
hodpc=0
konec=0
menu=1

#záhlaví, zobrazí se při zpuštění hry
print ("pro zobrazení pravidel stiskni: 1 ")
print ("pro začátek hry stiskni: 2 ")
print ("pro ukončení hry stiskni: 3")
print(".......................................")

while menu!=0:
    a=int(input("Volba: "))
    print (".........................................")


    #pro volbu 1
    if a==1:
        print("Začínajíci hráč hodí kostkou. Padne-li mu jednička, musí předat kostku protihráči. Jestliže mu padlo cokoliv jiného, pokračuje v házení a hodnoty jednotlivých hodů sčítá.  Padne-li mu ovšem ona jednička, musí okamžitě předat kostku a to bez nároku na body. Může ovšem kdykoliv sám rozhodnout, že přeruší úspěšnou sérii hodů a připsat si body na své konto. Hráč, který dosáhne třiceti vyhrál")
        a=int(input("Volba: "))

    #pro volbu 2

    #člověk
    
    import random

    opak=0
    opak2=0
    sez=[]
    celkskorehrace=0
    celkskorepc=0
    skorehrace=0
    skorepc=0
    hod=0
    hodpc=0
    konec=0 

    if a==2:
        while konec!=30:
            opak2=0
            while opak!=1:
                b=int(input("Stiskni 5 pro hod kostkou,0 pro ukončení tahu: "))
                if b>5 or b<5 and b!=0:
                   print("Špatná volba")    
            

                if b==5:
                    hod=random.randint(1,6)   #vygeneruju číslo 1-6 a vložím ho do seznamu
                    sez.append(hod)
                print("Dosud jsi hodil:", sez)
                if hod>1:
                    if hod==1:                    #kombinace a jejich řešení
                        skorehrace=skorehrace+1
                        hod=0
                    if hod==2:
                        skorehrace=skorehrace+2
                        hod=0
                    if hod==3:
                        skorehrace=skorehrace+3
                        hod=0
                    if hod==4:
                        skorehrace=skorehrace+4
                        hod=0
                    if hod==5:
                        skorehrace=skorehrace+5
                        hod=0
                    if hod==6:
                        skorehrace=skorehrace+6
                        hod=0
                    
                    print("Za tenhle hod máš",skorehrace)
                if hod==1:                                                  #smůla s jedničkou
                    skorehrace=0
                    opak=1
                    print("Hodil jsi 1 a tím jsi ukončil tah a tvoje skore v tomto tahu je 0")
                if b==0:
                
                    celkskorehrace=celkskorehrace+skorehrace             #sčítání bodů
                    opak=1
                    print("Tvoje celkový skore je",celkskorehrace)
                    skorehrace=0
            if celkskorehrace>=30:         
                
                    konec=30
            
            
            #pc
            sezpc=[]
            opak=0
            skorepc=0
            
            enter=input("Stiskni enter aby mohl hrát pc")
            while opak2!=2:

                c=random.randint(0,1)          #pc se rozhodne, jestli chce hrát, nebo kostku předá            
                if opak2==0:
                    c=0
                if c==0:
                    hodpc=random.randint(1,6)
                    sezpc.append(hodpc)
                print("Dosud pc hodil:",sezpc)

            
                
                if hodpc>1:
                
                    if hodpc==2:
                        skorepc=skorepc+2
                        hodpc=0
                        opak2=1
                    if hodpc==3:
                        skorepc=skorepc+3
                        hodpc=0
                        opak2=1
                    if hodpc==4:
                        skorepc=skorepc+4
                        hodpc=0
                        opak2=1
                    if hodpc==5:
                        skorepc=skorepc+5
                        hodpc=0
                        opak2=1
                    if hodpc==6:
                        skorepc=skorepc+6
                        hodpc=0
                        opak2=1
                     
                
                if hodpc==1:
                    skorepc=0
                    opak2=2
                if c==1:
                    celkskorepc=celkskorepc+skorepc
                    opak2=2
                    print("Počítač se rozhodl ukončit tah a má zatím",celkskorepc,"bodů")
                if celkskorepc>=30:        
                    konec=30

                skorehrace=0
    
    
    #možnosti výsledku hry
    if celkskorehrace>celkskorepc:                 
        print("Vyhrál jsi")
    elif celkskorehrace<celkskorepc:
        print("Prohrál jsi")
    else:
        print("Je to remíza")
    
    
    #pro volbu 3                
    if a==3:
        menu=0
        print("konec... zmáčkni ctrl+c pro ukončení programu")
    elif a>3:
        print("Neexistující volba")
    elif a<1:
        print("Neexistující volba")
    

