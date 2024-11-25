import json
from library import Book, Library
import json
import os

def post_book_to_lib(book: Book):
    """
    Записывает новую книгу в библиотеку (файл library.json).
    """
    file_path = 'library.json'

    # with open(file_path, 'rb+') as library:
    #     library.seek(-2, 2)
    #     second_last_char = library.read(1).decode()
    #     library.seek(-1, os.SEEK_END)
    #     library.truncate()
    #     if second_last_char != "[":
    #         library.write(b",\n")
    
    with open('curr_id.json', 'r') as new_id:
        curr_id = json.load(new_id)
    

    # with open(file_path, 'a') as library:
        # json.dump({
        #     "id": curr_id["curr_id"],
        #     "title": book.title,
        #     "author": book.author,
        #     "year": book.year,
        #     "status": book.status
        # }, library, indent=4)
        # library.write("]")

    with open(file_path, 'r', encoding='utf-8') as library:
        books = json.load(library)
        
    books.append({
            "id": curr_id["curr_id"],
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "status": book.status
        })
    with open(file_path, 'w', encoding='utf-8') as library:
        json.dump(books, library, ensure_ascii=False, indent=4)
    with open('curr_id.json', 'w') as new_id:   
        curr_id["curr_id"] += 1
        json.dump(curr_id, new_id, indent=4)
            
def parse_books_from_file(lib:Library):
    """
    Чтение файла перед началом работы, добавление книг типа Book в библиотеку типа Library
    """
    with open('library.json', 'r', encoding='utf-8') as file:
        books = json.load(file)
        

    for book in books:
        new_book = Book(*book.values())
        lib.add_book(new_book)
    
    with open('curr_id.json', 'r') as new_id:
        curr_id = json.load(new_id)
    Book.id = curr_id["curr_id"]
    return books

def delete_from_file(id):
    """
    Удаляет книгу из библиотеки(файл library.json).
    """
    with open('library.json', 'r', encoding='utf-8') as library:
        books = json.load(library)
    
    last_book = books[-1]
    books.pop()
    if last_book['id'] != id:
        target_index = next(index for index, record in enumerate(books) if record['id'] == id)
        books[target_index] = last_book
    
    with open('library.json', 'w', encoding='utf-8') as library:
        json.dump(books, library, ensure_ascii=False, indent=4)
    with open('curr_id.json', 'r') as new_id:
        curr_id = json.load(new_id)
    with open('curr_id.json', 'w') as new_id:   
        curr_id["curr_id"] -= 1
        json.dump(curr_id, new_id, indent=4)
           
def edit_status_in_file(id:int, new_status:str) -> None:
    """
    Меняет статус книги по айди (файл library.json).
    """
    with open('library.json', 'r', encoding='utf-8') as library:
        books = json.load(library)
    
    target_index = next(index for index, record in enumerate(books) if record['id'] == id)
    books[target_index]["status"] = new_status
    
    with open('library.json', 'w', encoding='utf-8') as library:
        json.dump(books, library, indent=4)

lib = Library()
parse_books_from_file(lib)
print(lib.books)