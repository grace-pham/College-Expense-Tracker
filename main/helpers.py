import datetime

from main.enums import ExpenseCategory


class WorkbookHelpers:
    def __init__(self, wb):
        self.wb = wb

    def _get_worksheet(self):
        ws = self.wb.active
        return ws

    def _input_amount(self, amount):
        return int(amount)

    def _input_date(self):
        return datetime.datetime.now()

    def _input_category(self, category):
        assert category in ExpenseCategory.get_list()

        return category

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
            worksheet,
            amount,
            expense_category,
    ):
        pass
    def input_deposit(
            self,
            worksheet,
            amount,
    ):
        pass

