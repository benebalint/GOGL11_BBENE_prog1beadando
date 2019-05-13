def converter(n):
    """A bemeneti szamot binaris alakba irja , es egy listat ad vissza
     melynek elemeit kettes alapra hatvanyozva es azokat osszegezve megkapjuk a bemeneti szamot
     """
    binaris_alak = []
    while(n > 0):
        binaris_alak.append(int(n % 2))
        n = int(n / 2)
    for i in range(0, len(binaris_alak)):
        if (binaris_alak[i] == 1):
            print(i, end="")
            if (i != len(binaris_alak) - 1):
                print(", ", end="")
    print("\n")

try:
    bemenet = int(input("Add meg a bemenetet: "))
    converter(bemenet)
except ValueError:
    print("A bemenet nem egesz szam.")