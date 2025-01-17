import requests

# Tips: använd sidan nedan för att se vilken data vi får tillbaks och hur apiet fungerar
# vi använder oss enbart av /nobelPrizes
# Dokumentation, hjälp samt verktyg för att testa apiet fins här: https://app.swaggerhub.com/apis/NobelMedia/NobelMasterData/2.1

HELP_STRING = """
Ange ett år och fält
Exempelvis 1965 fysik/kemi/litteratur/ekonomi/fred/medicin
För att avsluta enter Q
"""

cat = {"fysik": "phy",
       "kemi": "che",
       "litteratur": "lit",
       "ekonomi": "eco",
       "fred": "pea",
       "medicin": "med"}



# 10p programmet skall ge en hjälpsam utskrift istället för en krasch om användaren skriver in fel input
# 15p om användaren inte anger ett område som exempelvis fysik eller kemi så skall den parametern inte skickas med till apiet och vi får då alla priser det året





def main():
    print(HELP_STRING)

    while True:

        #  5p Skriv bara ut hjälptexten en gång när programmet startar inte efter varje gång användaren matat in en fråga
        #      Förbättra hjälputskriften så att användaren vet vilka fält, exempelvis kemi som finns att välja på

        #  5p Gör så att det finns ett sätt att avsluta programmet, om användaren skriver Q så skall programmet stängas av
        #      Beskriv i hjälptexten hur man avslutar programmet
        #  5p Gör så att hjälptexten skrivs ut om användaren skriver h eller H
        aaa = input(">")
        if aaa == "Q":
            exit(0)

        if aaa == "h" or aaa == "H":
            print(HELP_STRING)
            continue

        ln = len(aaa.split())

        if ln == 2:
            a, b = aaa.split()
            if b in cat:
                c = cat[b]
                c = {"nobelPrizeYear": int(a), "nobelPrizeCategory": c}
            else:
                print("Fel input")
                continue


        if ln == 1:
            c = {"nobelPrizeYear": int(aaa)}

        res = requests.get("http://api.nobelprize.org/2.1/nobelPrizes", params=c).json()
        # 5p Lägg till någon typ av avskiljare mellan pristagare, exempelvis --------------------------

        # TODO 20p Skriv ut hur mycket pengar varje pristagare fick, tänk på att en del priser delas mellan flera mottagare, skriv ut både i dåtidens pengar och dagens värde
        #   Skriv ut med tre decimalers precision. exempel 534515.123
        #   Skapa en funktion som hanterar uträkningen av prispengar och skapa minst ett enhetestest för den funktionen
        #   Tips, titta på variabeln andel
        # Feynman fick exempelvis 1/3 av priset i fysik 1965, vilket borde gett ungefär 282000/3 kronor i dåtidens penningvärde

        for p in res["nobelPrizes"]:
            peng = p["prizeAmount"]
            idagpeng = p["prizeAmountAdjusted"]
            print(f"{p['categoryFullName']['se']} \n -------------------------- \n prissumma {peng} SEK")

            x = p["laureates"]
            for m in p["laureates"]:
                print(m['knownName']['en'])
                print(m['motivation']['en'])
                andel = m['portion']


if __name__ == '__main__':
    main()