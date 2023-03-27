import requests
import unittest


class MyTestCase(unittest.TestCase):
    def test1_get_all_books(self):
        response = requests.get('http://localhost:5000/api/books')
        self.assertEqual(response.status_code, 200)

        books = response.json()
        self.assertTrue(len(books) > 0)
        expected_books = {"books": [{"author": "Роберт Мартин", "id": 1, "isElectronicBook": False, "name": "Чистый код", "year": 1998},
                                    {"author": "Томас Кормен, Чарльз Лейзерсон", "id": 2, "isElectronicBook": True, "name": "Алгоритмы: построение и анализ", "year": 1989}]}
        self.assertEqual(books, expected_books)

    def test2_add_book(self):
        new_book = {"name": "Test Book"}
        response = requests.post('http://localhost:5000/api/books', json=new_book)
        self.assertEqual(response.status_code, 201)

    def test3_get_book_by_id_after_add(self):
        response = requests.get('http://localhost:5000/api/books/3')
        self.assertEqual(response.status_code, 200)

        book = response.json()
        expected_book = {"book": {"author": "", "id": 3, "isElectronicBook": False, "name": "Test Book", "year": 0}}
        self.assertEqual(book, expected_book)

    def test4_update_book(self):
        updated_book = {"name": "Updated Book", "author": "Test Author", "year": 2022, "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 200)

    def test5_get_book_by_id_after_update(self):
        response = requests.get('http://localhost:5000/api/books/1')
        self.assertEqual(response.status_code, 200)

        book = response.json()
        expected_book = {"book": {"author": "Test Author", "id": 1, "isElectronicBook": True, "name": "Updated Book", "year": 2022}}
        self.assertEqual(book, expected_book)

    def test6_delete_books(self):
        response = requests.delete('http://localhost:5000/api/books/1')
        response = requests.delete('http://localhost:5000/api/books/2')
        response = requests.delete('http://localhost:5000/api/books/3')
        self.assertEqual(response.status_code, 200)

    def test7_get_empty_list(self):
        response = requests.get('http://localhost:5000/api/books')
        self.assertEqual(response.status_code, 200)

        expected_books = {"books": []}
        self.assertEqual(response.json(), expected_books)

if __name__ == '__main__':
    unittest.main()



