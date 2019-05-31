"""Тестирование модуля server.py"""
import time
import json
import unittest
from server import make_response


class TestMakeResponse(unittest.TestCase):
    """Тестирование функции make_response()"""
    def test_equal_response(self):
        """Проверяет корректность создания json сообщения из python словаря"""
        MSG = {
            "response": 200,
            "alert": "OK"
        }
        res = json.dumps(MSG)
        self.assertEqual(make_response(), res)


if __name__ == '__main__':
    unittest.main()
