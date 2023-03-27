import requests
import unittest


class MyTestCase(unittest.TestCase):

    def test1_delete_book1(self):
        response = requests.delete('http://localhost:5000/api/books/1')
        self.assertEqual(response.status_code, 200)

    def test2_delete_book2(self):
        response = requests.delete('http://localhost:5000/api/books/2')
        self.assertEqual(response.status_code, 200)

    def test3_add_book(self):
        new_book = {"name": "Test Book"}
        response = requests.post('http://localhost:5000/api/books', json=new_book)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()