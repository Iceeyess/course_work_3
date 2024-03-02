from _datetime import datetime


class Check:
    def __init__(self, id_number: str, state: str, date: str, operation_amount: str, description: str, from_=None,
                 to_=None) -> None:
        self.id_number = id_number
        self.state = state
        self.date = self.format_date_string(date)  # in order to be datetime format date
        self.str_date = self.str_date_format(self.date)  # in order to be str format date
        self.operation_amount = operation_amount
        self.description = description
        self.__from = from_
        self.__to = to_
        self.amount = float(self.operation_amount['amount'])
        self.currency = self.operation_amount['currency']

    def format_date_string(self, date: str) -> datetime:
        """Function returns reformatted date in following format:
        YYYY-MM-DD HH:MM:SS.f in order to sort a list by date"""
        date = date.replace('T', ' ')
        new_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        return new_date

    def str_date_format(self, date: datetime) -> str:
        """This function formats datetime class to string format: DD.MM.YYYY"""
        year, month, day = str(date).split()[0].split('-')
        return f"{day}.{month}.{year}"

    def __repr__(self) -> str:
        """This func gets str words in the list"""
        return f"Instance for object operation date by {self.str_date}"

    def get_card_number_account_number(self, account) -> str:
        """Returns sequred card number in following format 'card name XXXX XX** **** XXXX'
        or account name ****************XXXX or Нет данных. Открытие вклада if dictionary has None value
        """
        reformatted_card_number, card_number, name_card = '', '', ''
        if account == None:
            return f"Нет данных. Открытие вклада"
        # __from field consist from 2-3 words, we leave only digits.
        for word in account.split():
            if word.isdigit():
                card_number = word
            elif word.isalpha():
                name_card += word + ' '
        # divided on 2 ways: card(16-18 digits) and account(20 digits):
        # returns account name + account number:
        if len(card_number) >= 20:
            return name_card + '*' * 2 + card_number[-4:]
        # returns card name + card_number:
        elif 16 <= len(card_number) <= 18:
            for slice_ in range(0, len(card_number), 2):
                if 0 <= slice_ <= 5 or slice_ > 11:
                    reformatted_card_number += card_number[slice_: slice_ + 2]
                else:
                    reformatted_card_number += "XX"
            return name_card + ''.join(
                [reformatted_card_number[_: _ + 4] + ' ' for _ in range(0, len(reformatted_card_number), 4)]).rstrip()

    def get_account(self, value: str) -> str:
        """Depends which parameter has added inside print_check function
        it will be self.__from or self.__to argument."""
        if value == self.__from:
            return self.get_card_number_account_number(value)
        elif value == self.__to:
            return self.get_card_number_account_number(value)

    def print_check(self) -> None:
        print(self.str_date_format(self.date), "Перевод организации")
        print(self.get_account(self.__from), "->", self.get_account(self.__to))
        print(self.amount, "руб.", '\n')