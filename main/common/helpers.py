class WorkbookHelpers:
    def __init__(self, wb):
        self.wb = wb

    def _get_worksheet(self):
        ws = self.wb.active
        return ws

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

    def _input_amount(self, amount):
        pass

    def _input_date(self, date):
        pass

    def _input_category(self, category):
        pass

    def input_expense(
            self,
            amount,
            date,
            expense_category,
    ):

        self._input_amount(amount)
        self._input_date(date)
        self._input_category(expense_category)

    def input_deposit(
            self,
            amount,
            date,
    ):
        self._input_amount(amount)
        self._input_date(date)
