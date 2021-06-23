from enum import Enum


class EnumBase(Enum):
    @classmethod
    def get_list(cls):
        attributes = [att_value.value for att, att_value in cls.__members__.items()]
        return attributes


class ExpenseCategory(EnumBase):
    HEALTHCARE = "Healthcare"
    UTILITIES = "Utilities"
    RENT = "Rent"
    FOOD_AND_BEVERAGE = "Food & Beverage"
    NECESSITIES = "Necessities"
    TRAVEL = "Travel"
    ENTERTAINING = "Entertaining"
