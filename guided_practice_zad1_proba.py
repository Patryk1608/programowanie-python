import csv
import os
import glob

# Konfiguracja - ścieżka do folderu z plikami CSV
sciezka_do_folderu = 'guided_practice'  # Upewnij się, że ta nazwa folderu jest poprawna
wzorzec_plikow = os.path.join("C:/Users/339858/Documents/Programowanie_Koniecka/guided_practice/", '*.csv')

# Zmienne do przechowywania wyników
min_temp = float('inf')
min_temp_info = {} # Przechowa stację i godzinę dla min
max_temp = float('-inf')
max_temp_info = {} # Przechowa stację i godzinę dla max

opady_lista = [] # Lista krotek: (stacja, godzina, wielkość opadu)

print(f"Szukam plików w: {wzorzec_plikow}...")

lista_plikow = glob.glob(wzorzec_plikow)

if not lista_plikow: 
    print("Nie znaleziono plików CSV! Sprawdź ścieżkę.")
else:
    # Pętla po wszystkich znalezionych plikach (otwieranie w pętli)
    for nazwa_pliku in lista_plikow:
        print(f"Przetwarzam plik: {nazwa_pliku}")
        
        try:
            with open(nazwa_pliku, mode='r', encoding='utf8') as plik:
                # Używamy DictReader, zakładając że pliki mają nagłówki (zgodnie z treścią zadania)
                # Jeśli pliki NIE mają nagłówków, trzeba użyć csv.reader i indeksów (np. row[0])
                reader = csv.DictReader(plik, delimiter=',') # Czasem separatorem jest średnik ';', warto sprawdzić plik
                
                # Normalizacja nazw kolumn (usuwamy ewentualne spacje)
                reader.fieldnames = [name.strip() for name in reader.fieldnames]

                for wiersz in reader:
                    try:
                        # Pobieranie danych z wiersza (dostosuj klucze jeśli nagłówki są inne)
                        stacja = wiersz.get('nazwa_stacji', wiersz.get('stacja', 'Nieznana'))
                        godzina = wiersz.get('godzina_pomiaru', wiersz.get('godzina', '00'))
                        
                        # Obsługa temperatury
                        temp_str = wiersz.get('temperatura_powietrza', wiersz.get('temperatura'))
                        if temp_str:
                            temp = float(temp_str)
                            
                            # Sprawdzanie minimum
                            if temp < min_temp:
                                min_temp = temp
                                min_temp_info = {'stacja': stacja, 'godzina': godzina}
                            
                            # Sprawdzanie maksimum
                            if temp > max_temp:
                                max_temp = temp
                                max_temp_info = {'stacja': stacja, 'godzina': godzina}

                        # Obsługa opadów
                        opad_str = wiersz.get('suma_opadu', wiersz.get('opad'))
                        if opad_str:
                            opad = float(opad_str)
                            # Jeśli wystąpił jakikolwiek opad (> 0)
                            if opad > 0:
                                opady_lista.append({
                                    'stacja': stacja,
                                    'godzina': godzina,
                                    'ilosc': opad
                                })

                    except ValueError:
                        # Pomijamy wiersze z błędnymi danymi liczbowymi (brak danych)
                        continue
                        
        except Exception as e:
            print(f"Błąd podczas otwierania pliku {nazwa_pliku}: {e}")

    # --- WYPISYWANIE WYNIKÓW ---
    print("-" * 40)
    print("WYNIKI ANALIZY:")
    print("-" * 40)

    if min_temp_info:
        print(f"1. Minimalna temperatura: {min_temp}°C")
        print(f"   Stacja: {min_temp_info['stacja']}, Godzina: {min_temp_info['godzina']}")
    else:
        print("Nie znaleziono danych o temperaturze.")

    print("-" * 20)

    if max_temp_info:
        print(f"2. Maksymalna temperatura: {max_temp}°C")
        print(f"   Stacja: {max_temp_info['stacja']}, Godzina: {max_temp_info['godzina']}")
    else:
        print("Nie znaleziono danych o temperaturze.")

    print("-" * 20)

    print("3. Stacje z odnotowanym opadem:")
    if opady_lista:
        for wpis in opady_lista:
            print(f"   - Stacja: {wpis['stacja']}, Godzina: {wpis['godzina']} (Opad: {wpis['ilosc']} mm)")
    else:
        print("   Brak opadów we wszystkich stacjach.")