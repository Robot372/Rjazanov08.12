def linnad(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="Tutvuma pealinnaga":
        mas=[]
        capital=(input("Sisestage pealinn: "))
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("Riik -", keys_list[i],"<-->", "Pealinn -", values_list[i])
    else:
        country==(input("Sisestage riik: ")).capitalize()
        a=d.get(country)
        print("Riik -", country ,"<-->", "Pealinn -", a)
    return

def addriik(d:dict, v:int):
    if v=="add":
        new={}
        country=(input("Sisestage riik: ")).capitalize()
        capital=(input("Sisestage riik: ")).capitalize()
        new={country:capital}

    return d,new

def changeriik(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="changeriik":
        a=str(input("Sisestage selle riigi nimetus,mida soovite muuta"))
        del dictionary[a]
        b=str(input(a))
        c=str(input("Muuta ka pealinn"))
        riigid={a: c}
    return a,c,b
