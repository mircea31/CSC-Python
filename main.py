class Calendar:
    def __init__(fanTOMA, zi, luna, an):
        fanTOMA.zi = zi
        fanTOMA.luna = luna
        fanTOMA.an = an

    def Next_day(fanTOMA):
        fanTOMA.zi+=1
        print(f"{fanTOMA.zi}  {fanTOMA.luna} {fanTOMA.an}")

zi = int(input("Alege o zi: "))
luna = int(input("Alege o luna: "))
an = int (input("Alege un an: "))

zi_Craciun = Calendar(zi, luna, an)

zi_Craciun.Next_day()

# zi_Craciun.next_day(zi_Craciun)

