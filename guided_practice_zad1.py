import csv
import os
import numpy as np

moj_folder = "C:/Users/339858/Documents/Programowanie_Koniecka/guided_practice/"

lista_plikow = os.listdir(moj_folder)
print(lista_plikow)

lista = []

for plik in lista_plikow:
    nazwa = moj_folder + plik
    print(nazwa)

    with open(nazwa, 'r',encoding="utf8") as plikcsv:
        csvreader = csv.reader(plikcsv)
        next(csvreader)

        for wiersz in csvreader:
            lista.append(wiersz)

    tablica = np.array(lista)

print(tablica[:,4])

temperatura = []
opad = []


for i in range(0,len(tablica[:,4])):
    temperatura.append(float(tablica[i,4]))
    opad.append(float(tablica[i,8]))

temperatura = np.array(temperatura)
opad - np.array(opad)

minimalna_temperatura = min(temperatura)
maksymalna_temperatura = max(temperatura)

print(minimalna_temperatura)
print(maksymalna_temperatura)
    
indeks_min_temp = np.where(temperatura == minimalna_temperatura)
indeks_max_temp = np.where(temperatura == maksymalna_temperatura)

godzina_min_temp = tablica[indeks_min_temp,3]
data_min_temp = tablica[indeks_min_temp,2]
lokalizacja_min_temp = tablica[indeks_min_temp,1]

godzina_max_temp = tablica[indeks_max_temp,3]
data_max_temp = tablica[indeks_max_temp,2]
lokalizacja_max_temp = tablica[indeks_max_temp,1]

napis_min = "Temperatura minimalna zostala odnotowana na stacji " + str(lokalizacja_min_temp[0][0]) + " dnia " + str(data_min_temp[0][0]) + " o godzinie " + str(godzina_min_temp[0][0]) + " i wynosila " + str(minimalna_temperatura) + " stopni celsjusza."
napis_max = "Temperatura maksymalna zostala odnotowana na stacji " + str(lokalizacja_max_temp[0][0]) + " dnia " + str(data_max_temp[0][0]) + " o godzinie " + str(godzina_max_temp[0][0]) + " i wynosila " + str(maksymalna_temperatura) + " stopni celsjusza."

niezerowy_opad_index = np.where(opad > 0)

niezerowy_opad_lokalizacja = tablica[niezerowy_opad_index,1]
niezerowy_opad_data = tablica[niezerowy_opad_index,2]
niezerowy_opad_godzina = [niezerowy_opad_index,3]

print(niezerowy_opad_lokalizacja[0])
for j in range(0,len(niezerowy_opad_lokalizacja[0])):
    print("Opad wystapil na stacji " + str(niezerowy_opad_lokalizacja[0][j]) + " dnia " + str(niezerowy_opad_data[0][j]) + "o godzinie" + str(niezerowy_opad_godzina[0][j]) + ".")
