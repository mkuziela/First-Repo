def greet(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"

result = greet("Maciej", "Kuziela")
print(result)

def multiply(a: int, b: int) -> int:
    return a * b

wynik_mnozenia = multiply(4, 5)
print(wynik_mnozenia)  # 20

def is_even(number: int) -> bool:
    return number % 2 == 0

liczba = 7
czy_parzysta = is_even(liczba)
if czy_parzysta:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

def sum_check(a: int, b: int, c: int) -> bool:
    return (a + b) >= c

sprawdzenie = sum_check(3, 5, 7)
print(sprawdzenie)  # True

def contains_value(lst: list, value: int) -> bool:
    return value in lst

moja_lista = [1, 3, 5, 7]
szukana = 5
wynik = contains_value(moja_lista, szukana)
print(wynik)  # True