from helpers import WorkbookHelpers
import matplotlib as plt

class PlottingHelpers(WorkbookHelpers):
    def get_existing_expense_category(self):
        categories = {}
        for i in range(1, self._get_occupied_row() + 1):
            cell = f'C{i}'
            cell_content = self._get_worksheet()[cell].value
            categories.add(cell_content)
        return list(categories)

    def get_expense_category_data(self, category_list):
        pass

    def graph_expense_by_category(self):
        labels = self.get_existing_expense_category()
        data = []
        for label in labels:
            category_data = self.get_expense_category_data(label)
            data.append(category_data)

        plt.pyplot.pie(data=data, labels=labels)
