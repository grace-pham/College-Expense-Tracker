import datetime

from main.enums import ExpenseCategory, RecordType


class WorkbookHelpers:
    def __init__(self, wb):
        self.wb = wb

    def _get_worksheet(self):
        ws = self.wb.active
        return ws

    def _input_amount(self, input_row, amount):
        input_cell = f'D{input_row}'
        self._get_worksheet()[input_cell] = int(amount)

    def _input_type(self, input_row, type):
        assert type in RecordType.get_list()

        input_cell = f'A{input_row}'
        self._get_worksheet()[input_cell] = type

    def _input_date(self, input_row):
        input_cell = f'A{input_row}'
        self._get_worksheet()[input_cell] = datetime.datetime.now()

    def _input_category(self, input_row, category):
        assert category in ExpenseCategory.get_list()

        input_cell = f'C{input_row}'
        self._get_worksheet()[input_cell] = category

    def get_occupied_dimension(self):
        dimension = self._get_worksheet().calculate_dimension()
        return dimension

    def get_balance(self):
        pass

    def get_expense(self, option="Total"):
        if option == "Month":
            pass
        elif option == "Category":
            pass
        elif option == "Total":
            pass
        else:
            raise Exception("Option Invalid")

    def input_expense(
            self,
            amount,
            expense_category,
    ):
        input_row = int(self.get_occupied_dimension()[-2:]) + 1
        self._input_date(input_row)
        self._input_type(input_row, "Expense")
        self._input_amount(input_row, amount)
        self._input_category(input_row, expense_category)

    def input_deposit(
            self,
            amount,
    ):
        input_row = int(self.get_occupied_dimension()[-2:]) + 1
        self._input_type(input_row, "Deposit")
        self._input_date(input_row)
        self._input_amount(input_row, amount)

