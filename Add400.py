import requests
import unittest

class MyTestCase (unittest.TestCase):

    def test1_add_book_without_name(self):
        new_book = {"author": "Какой-то автор", "year": 2023, "isElectronicBook": True}
        response = requests.post('http://localhost:5000/api/books', json=new_book)
        self.assertEqual(response.status_code, 400)

    def test2_add_book_with_incorrect_name(self):
        new_book = {"name": 13}
        response = requests.post('http://localhost:5000/api/books', json=new_book)
        self.assertEqual(response.status_code, 400)

    def test3_add_book_with_incorrect_other_fields(self):
        new_book = {"author": 13, "name": "New Book", "year": "бубубу", "isElectronicBook": "бебебе"}
        response = requests.post('http://localhost:5000/api/books', json=new_book)
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()






















