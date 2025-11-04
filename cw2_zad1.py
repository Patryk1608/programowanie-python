wiek_studenta1 = int(input("Podaj wiek pierwszego studenta: "))
wiek_studenta2 = int(input("Podaj wiek drugiego studenta: "))

tekst = ("Pierwszy student jest starszy i ma " + str(wiek_studenta1) + " lat(a).")

if wiek_studenta1 > wiek_studenta2:
    print (tekst)
    
with open("wiek1.txt", "a") as plik:
    plik.write(tekst)