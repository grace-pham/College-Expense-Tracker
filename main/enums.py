import inspect
import re


class EnumBase(object):
    @classmethod
    def get_list(cls):
        attributes = inspect.getmembers(cls, lambda att: not (inspect.ismethod(att)))
        value_list = []
        for key, value in attributes:
            rx = re.compile(r'\b__(?:\w*)__?\b')
            if key not in rx.findall(key):
                value_list.append(value)
        return value_list


class ExpenseCategory(EnumBase):
    HEALTHCARE = "Healthcare"
    UTILITIES = "Utilities"
    RENT = "Rent"
    FOOD_AND_BEVERAGE = "Food & Beverage"
    NECESSITIES = "Necessities"
    TRAVEL = "Travel"
    ENTERTAINING = "Entertaining"


class RecordType(EnumBase):
    EXPENSE = "Expense"
    DEPOSIT = "Deposit"


class RecordOption(EnumBase):
    TOTAL = "Total"
