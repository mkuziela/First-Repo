class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Library: {self.city}, {self.street}, {self.zip_code},"
                f" Open: {self.open_hours}, Phone: {self.phone}")


class Employee:
    def __init__(self, first_name, last_name, hire_date,
                 birth_date, city, street):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street

    def __str__(self):
        return (f"Employee: {self.first_name} {self.last_name}, "
                f"Hired: {self.hire_date}"f", Birth: {self.birth_date}"
                f", Address: {self.street}, {self.city}")


class Student:
    def __init__(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def __str__(self):
        return (f"Student: {self.first_name} {self.last_name},"
                f" Birth: {self.birth_date}")


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Book by {self.author_name} {self.author_surname},"
                f" Published: {self.publication_date},"
                f" Pages: {self.number_of_pages}, Library: [{self.library}]")


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n  ".join(str(book) for book in self.books)
        return (f"Order Date: {self.order_date}\nEmployee: {self.employee}\n"
                f"Student: {self.student}\nBooks:\n  {books_str}\n")


library1 = Library("Warsaw", "Main St 1", "00-001",
                   "8:00-18:00", "123-456-789")
library2 = Library("Krakow", "Second St 2", "30-002",
                   "9:00-17:00", "987-654-321")

employees = [
    Employee("Jan", "Kowalski", "2020-01-01",
             "1990-05-10", "Warsaw", "Main St 1"),
    Employee("Anna", "Nowak", "2019-03-15",
             "1988-07-20", "Krakow", "Second St 2"),
    Employee("Alicja", "", "2021-06-10",
             "1992-12-05", "Warsaw", "Main St 1")
]

students = [
    Student("Marek", "Zieliński", "2000-02-02"),
    Student("Kasia", "Lewandowska", "1999-11-11"),
    Student("Tomek", "Kowalczyk", "2001-07-15")
]

books = [
    Book(library1, "2015", "Author1",
         "Surname1", 200),
    Book(library1, "2018", "Author2",
         "Surname2", 300),
    Book(library2, "2020", "Author3",
         "Surname3", 250),
    Book(library2, "2017", "Author4",
         "Surname4", 150),
    Book(library1, "2019", "Author5",
         "Surname5", 400)
]

order1 = Order(employees[0], students[0], [books[0], books[2]],
               "2025-11-30")
order2 = Order(employees[1], students[1], [books[1], books[3],
                                           books[4]], "2025-11-30")

print(order1)
print(order2)
