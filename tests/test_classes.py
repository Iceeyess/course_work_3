import json
import unittest
from classes.classes import Check
from _datetime import datetime

json_sample = '''[{
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
  }]'''

dict_json = json.loads(json_sample)


class TestCalc(unittest.TestCase):

    def setUp(self):
        """Определяем инициализацию класса стандартным методом unittest setUp
        через присвоение случайновыбранного словаря."""
        checks_list = [Check(check_file.get('id'), check_file.get('state'), check_file.get('date'),
                             check_file.get('operationAmount'), check_file.get('description'), check_file.get('from'),
                             check_file.get('to')) for check_file in dict_json if check_file]
        self.verification = checks_list[0]

    def test_format_date_string(self):
        self.assertEqual(self.verification.format_date_string('2019-12-08T22:46:21.935582'),
                         datetime(2019, 12, 8, 22, 46, 21, 935582))

    def test_str_date_format(self):
        self.assertEqual(self.verification.str_date_format(datetime(2019, 12, 8, 22, 46, 21, 935582)), '08.12.2019')

    def test_get_card_number_account_number(self):
        self.assertEqual(self.verification.get_card_number_account_number('Счет 90424923579946435907'), 'Счет **5907')
        self.assertEqual(self.verification.get_card_number_account_number(None), 'Нет данных. Открытие вклада')
        self.assertEqual(self.verification.get_card_number_account_number('Visa Platinum 1246377376343588'), 'Visa Platinum 1246 37XX XXXX 3588')

if __name__ == '__main__':
    unittest.main()
