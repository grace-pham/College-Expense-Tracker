from enum import Enum


class EnumBase(Enum):
    @classmethod
    def get_list(cls):
        attributes = [member.value for role, member in cls.__members__.items()]
        return attributes


class ExpenseCategory(EnumBase):
    UTILITIES = "Utilities"
    RENT = "Rent"
    TRAVEL = "Travel"
    ENTERTAINING = "Entertaining"
