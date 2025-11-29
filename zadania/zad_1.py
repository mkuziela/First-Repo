names = ['Pierre', 'Esteban', 'Max', 'Charles', 'Oscar']

def funkcja_listy(lista):
    for name in lista:
        print(name)

funkcja_listy(names)

def multiply_func(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik

print(multiply_func([1, 2, 3, 4, 5]))

def multiply_lc(lista):
    return [liczba * 2 for liczba in lista]

print(multiply_lc([1, 2, 3, 4, 5]))

def pokaz_parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

pokaz_parzyste(list(range(10)))

def co_drugi_element(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

co_drugi_element(list(range(10)))