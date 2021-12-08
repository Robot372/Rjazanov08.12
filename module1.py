from module2 import*

riigid={"Eesti": "Tallinn", "Austria": "Veen", "Belgia": "Brüssel", "Saksamaa": "Berlin", "Liechtenstein": "Vaduz", "Holland": "Amsterdam",  
           "Prantsusmaa": "Pariis", "Bulgaaria": "Sofija", "Poola": "Varssavi", "tsehhi": "Praha", "Albaania": "Tirana", "Bosnia ja Hertsegoviina": "Sarajevo",
           "Põhja-Makedoonia": "Skopje", "Serbia": "Belgrad"}
print(riigid)
while True:
    print("Tutvuda pealinnaga - Узнать столицу,\nadd - lisage riiki nimekirja,\nchange - muuta riiki või pealinna,\ntest - Test")
    v=str(input())
    if v=="uznatstolicy":
        v=input("Страна по стoлице(1) или стoлицу по стране(2)?")
        goroda(v)
    elif v=="add":
        addstrana(v) 
    elif v=="change":
        changestrana(v)