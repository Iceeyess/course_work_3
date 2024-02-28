from ..classes.classes import Check
import json
import unittest
from classes.classes import Check
from datetime import datetime

json_sample = '''{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }'''

dict_json = json.loads(json_sample)

class TestCalc(unittest.TestCase):

    test_check = Check(id: '863064926', state:'EXECUTED', 'date'='2019-12-08T22:46:21.935582',
                     'operationAmount'={"amount": "41096.24","currency": {"name": "USD","code": "USD"}},
                    'description'='Открытие вклада', 'from'='',
                     'to'='Счет 90424923579946435907')
    def test_format_date_string(self):
        self.assertEqual(Check.format_date_string('2019-12-08T22:46:21.935582'), datetime.datetime(2019, 12, 8, 22, 46, 21, 935582))


if __name__ == '__main__':
    unittest.main()