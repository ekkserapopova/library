import unittest
from library import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book(title='book 1', author='author 1', year=2000)
        self.book2 = Book(title='book 2', author='author 2', year=1900)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        new_book = Book(title='book 3', author='author 3', year=2001)
        self.library.add_book(new_book)
        self.assertIn(new_book.id, self.library.books)
        self.assertEqual(self.library.books[new_book.id].title, 'book 3')

    def test_delete_book(self):
        self.library.del_book(0)
        self.assertNotIn(0, self.library.books)
        
        with self.assertRaises(ValueError):
            self.library.del_book(0)

    def test_change_status_valid(self):
        self.library.books[1].status = 'Выдана'
        self.assertEqual(self.library.books[1].status, 'Выдана')
        
        self.library.books[1].status = 'В наличии'
        self.assertEqual(self.library.books[1].status, 'В наличии')

    def test_change_status_invalid(self):
        with self.assertRaises(ValueError):
            self.library.books[1].status = 'что-то другое'

    def test_missing_fields(self):
        with self.assertRaises(ValueError):
            Book(title='', author='author', year=2021)
        with self.assertRaises(ValueError):
            Book(title='title', author='', year=2021)
        with self.assertRaises(ValueError):
            Book(title='title', author='author', year='')
        with self.assertRaises(ValueError):
            Book(title='title', author='author', year='qwerty')

if __name__ == '__main__':
    unittest.main()
