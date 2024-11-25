import json
from library import Book, Library
from save_data import delete_from_file, edit_status_in_file, parse_books_from_file, post_book_to_lib

def add_book(lib):
    """
    Добавление новой книги 
    """
    title = input('Введите название книги: ')
    author = input('Введите автора: ')
    year = input('Введите год издания: ')
    try:
        new_book = Book(title=title, author=author, year=year)
        lib.add_book(new_book)
        post_book_to_lib(new_book)
        return new_book
    except Exception as e:
        print(e)
       
def delete_book(lib):
    """
    Удаление книги по id
    """
    id = input('Введите id: ')
    try:
        id=int(id)
        lib.del_book(id)
        delete_from_file(id)
        print('Книга успешно удалена')
    except Exception as e:
        print(e)
       
def search_book(lib):
    """
    Поиск книг
    """
    print('Выберете параметр поиска:')
    print('1. Название')
    print('2. Автор')
    print('3. Год')
    num = int(input())
    search_value = input(f'Поиск книги по параметру {num}: ')
    match num:
        case 1:
            query = 'title'
        case 2:
            query = 'author'
        case 3:
            query = 'year'
    
    books = lib.books
    filtered_books = list(filter(lambda book: search_value.lower() in getattr(book, query).lower(), books.values()))
    return ',\n'.join(str(book) for book in filtered_books)
    
def change_status(lib):
    """
    Изменение статуса книги
    """
    id = int(input('Введите айди книги: '))
    try:
        book = lib.books[id]
    except:
        print('Книги с таким id не существует')
    try:
        print('Возможные статусы: Выдана, В наличии')
        new_status = input('Введите новый статус: ') 
        book.status = new_status
        edit_status_in_file(id, new_status)
        return book
    except Exception as e:
        print(e)
            
if __name__ == '__main__':
    library = Library()
    parse_books_from_file(library)
    while True:
        print('Библиотека')
        print('----------------------------------')
        print('1. Добавить книгу')
        print('2. Удалить книгу')
        print('3. Поиск книги')
        print('4. Посмотреть все книги')
        print('5. Изменить статус книги')
        print('6. Выйти')
        num = input()
        match num:
            case '1':
                print(add_book(library))
            case '2':
                delete_book(library)
            case '3':
                print(search_book(library))
            case '4':
                print(library)
            case '5':
                print(change_status(library))
            case '6':
                exit()
            case _:
                print('Некорректный ввод')
    
    