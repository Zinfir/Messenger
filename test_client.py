"""Тестирование модуля client.py"""
import time
import json
import unittest
from client import make_presence_msg


class TestMakePresenceMsg(unittest.TestCase):
    """Тестирование функции make_presence_msg()"""
    def test_equal_response_msg(self):
        """Проверяет корректность создания json сообщения из python словаря"""
        timestamp = time.ctime(time.time())
        presence_msg = {
            "action": "presence",
            "time": timestamp,
            "type": "status",
            "user": {
                "account_name": "Zinfir",
                "status": "Yep, I am here!"
            }
        }
        res = json.dumps(presence_msg)
        self.assertEqual(make_presence_msg(), res)


if __name__ == '__main__':
    unittest.main()
