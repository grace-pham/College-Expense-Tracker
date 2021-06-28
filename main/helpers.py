import datetime

from openpyxl import load_workbook

from main.enums import ExpenseCategory, RecordType, RecordOption


class WorkbookHelpers:
    def __init__(self, source):
        self.wb = load_workbook(source)
        self.ws = self.wb.get_sheet_by_name("Sheet")
        self.dest = source

    def _get_worksheet(self):
        return self.ws

    def _get_occupied_row(self):
        occupied_cells = [s for s in self.get_occupied_dimension().split(":")]
        cell = occupied_cells[1]
        occupied_row = int(''.join([d for d in cell if d.isdigit()]))
        return occupied_row

    def _get_input_row(self):
        return self._get_occupied_row() + 1

    def _input_amount(self, input_row, amount):
        input_cell = f'D{input_row}'
        self._get_worksheet()[input_cell] = int(amount)

    def _input_type(self, input_row, type):
        assert type in RecordType.get_list()

        input_cell = f'B{input_row}'
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

    def check_record_type(self, record_type, cell_content):
        assert record_type in RecordType.get_list()
        if cell_content == record_type:
            return True
        else:
            return False

    def check_option(self, option, cell_content):
        assert option in RecordOption.get_list()
        if cell_content == option:
            return True
        else:
            return False

    def get_amount_by_row(self, row):
        cell = f'D{row}'
        return self._get_worksheet()[cell].value

    def calculate_amount_by_record_type_and_option(self, record_type, option):
        total = 0
        for i in range(1, self._get_occupied_row()+1):
            cell = f'B{i}'
            cell_content = self._get_worksheet()[cell].value
            if self.check_record_type(record_type, cell_content):
                if option == "Total":
                    total += self.get_amount_by_row(i)
                else:
                    option_cell = f'C{i}'
                    cell_option_content = self._get_worksheet()[option_cell]
                    if self.check_option(option, cell_option_content):
                        total += self.get_amount_by_row(i)
        return total

    def get_amount_by_record_type_and_option(self, record_type, option=RecordOption.TOTAL):
        if record_type == "Deposit":
            return self.calculate_amount_by_record_type_and_option(record_type, option)
        elif record_type == "Expense":
            return self.calculate_amount_by_record_type_and_option(record_type, option)
        else:
            raise Exception("Record Type Invalid")

    def get_expense_by_option(self, option="Total"):
        if option == RecordOption.TOTAL:
            return self.get_amount_by_record_type_and_option(RecordType.EXPENSE)
        else:
            raise Exception("Option Invalid")

    def get_total_deposit(self):
        return self.get_amount_by_record_type_and_option(RecordType.DEPOSIT)

    def get_balance(self):
        return self.get_total_deposit() - self.get_expense_by_option()

    def input_expense(
            self,
            amount,
            expense_category,
    ):
        input_row = self._get_input_row()
        self._input_date(input_row)
        self._input_type(input_row, RecordType.EXPENSE)
        self._input_amount(input_row, amount)
        self._input_category(input_row, expense_category)

    def input_deposit(
            self,
            amount,
    ):
        input_row = self._get_input_row()
        self._input_type(input_row, RecordType.DEPOSIT)
        self._input_date(input_row)
        self._input_amount(input_row, amount)

    def save_workbook(self):
        self.wb.save(self.dest)