wiek_studenta1 = input("Podaj wiek pierwszego studenta: ")
with open("wiek_drugiego_studenta.txt") as plik:
    wiek_studenta2 = plik.read()

wiek_studenta1 = int(wiek_studenta1)
wiek_studenta2 = int(wiek_studenta2)

if (wiek_studenta1 < wiek_studenta2):
    roznica = wiek_studenta2 - wiek_studenta1
    tekst = "Pierwszy student jest mlodszy od studenta drugiego o " + str(roznica) + " lat(a)."
    print (tekst)

with open("wiek2.txt", "a") as plik_wyjsciowy:
    plik_wyjsciowy.write(tekst)