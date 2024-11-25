import json

class Library:
    def __init__(self, books={}):
        self.books = books
    
    def add_book(self, book):
        self.books[book.id] = book
        
    def del_book(self, id):
        if id in self.books:
            del self.books[id]
        else:
            raise ValueError('Книги с таким id не существует')
    def __str__(self):
        return ',\n'.join(str(book) for book in self.books.values())
        
class Book:
    id=0
    def __init__(self, id=-1, title='', author='', year=0, status='В наличии'):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        if id == -1:
            self.id = Book.id
            Book.id += 1
        else:
            self.id = id
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, new_status):
        if new_status not in ['Выдана', 'В наличии']:
            raise ValueError("Статус должен быть 'Выдана' или 'В наличии'")
        self.__status = new_status
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title):
        if not new_title:
            raise ValueError("{\n    'title': Обязательное поле\n}")
        self.__title = new_title
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, new_author):
        if not new_author:
            raise ValueError("{\n    'author': Обязательное поле\n}")
        self.__author = new_author
    
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, new_year):
        if not new_year:
            raise ValueError("{\n    'yaer': Обязательное поле\n}")
        try:
            self.__year = int(new_year)
        except ValueError:
            raise ValueError("{\n    'year': Должен быть типа integer\n}")
           
    def __serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.__status,
        }
        
    def __str__(self):
        iter_names = iter(['id', 'Название', 'Автор', 'Год издания', 'Статус'])
        res = ',\n    '.join([f'{next(iter_names)}: {value}' for value in self.__serialize().values()])
        return f'{{\n    {res}\n}}'

    