import requests
import unittest

class MyTestCase (unittest.TestCase):
    def test1_get_book_by_incorrect_id(self):
        response = requests.get('http://localhost:5000/api/books/15')
        self.assertEqual(response.status_code, 404)

    def test2_add_book_with_id(self):
        new_book = {"name": "Пятница 13-е"}
        response = requests.post('http://localhost:5000/api/books/10', json=new_book)
        self.assertEqual(response.status_code, 405)

    def test3_update_book_with_incorrect_id(self):
        updated_book = {"name": "Updated Book", "author": "Test Author", "year": 2022, "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books/135', json=updated_book)
        self.assertEqual(response.status_code, 404)

    def test4_update_book_without_id(self):
        updated_book = {"name": "Updated Book", "author": "Test Author", "year": 2022, "isElectronicBook": True}
        response = requests.put('http://localhost:5000/api/books', json=updated_book)
        self.assertEqual(response.status_code, 405)

    def test5_delete_book_with_incorrect_id(self):
        response = requests.delete('http://localhost:5000/api/books/140')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()