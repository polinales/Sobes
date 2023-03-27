import requests
import unittest

class MyTestCase (unittest.TestCase):
    def test1_update_book_without_name(self):
        updated_book = {"call": 1}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test2_update_book_without_author(self):
        updated_book = {"name": "Updated Book"}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test3_update_book_without_year(self):
        updated_book = {"name": "Updated Book", "author": "Test Author"}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test4_update_book_without_isElectronicbook(self):
        updated_book = {"name": "Updated Book", "author": "Test Author", "year": 2022}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test5_update_book_with_incorrect_name(self):
        updated_book = {"name": 11, "author": "Test Author", "year": 2022, "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test6_update_book_with_incorrect_author(self):
        updated_book = {"name": "Книга", "author": 12, "year": 2022, "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test7_update_book_with_incorrect_isElectronicbook(self):
        updated_book = {"name": "Книга", "author": "Test Author", "year": 2022, "isElectronicBook": "бебебе"}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test8_update_book_with_incorrect_year_string(self):
        updated_book = {"name": "Книга", "author": "Test Author", "year": "бубубу", "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

    def test9_update_book_with_negative_year(self):
        updated_book = {"name": "Книга", "author": "Test Author", "year": -5000, "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books/1', json=updated_book)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()