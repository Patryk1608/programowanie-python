zmienna = 3.1

if isinstance(zmienna, float) or isinstance(zmienna, int) :
    print ("Jest to liczba")

    if isinstance(zmienna, float):
        if zmienna.is_integer():
            print("Zmienna jest typu float, ale ma wartosc calkowita")
        else:
            print("Zmienna jest liczbą niecałkowita")

    else:
        print("Zmienna jest liczbą calkowita")

else:
    print ("Nie jest to liczba")
