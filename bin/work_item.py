

class WorkItem:

    def __init__(self, row_number, work_item_data):
        """Stores a single Work Item (row) of the FDR

        :param row_number: the excel row this Work Item comes from
        :param work_item_data: dictionary. keys = column headers. values = cell values.
        """

        self.__row_number = row_number
        self.__work_item_data

    def id_larger_than(self, other_work_item):
        """Returns True if this work item has an alphabetically larger ID than the other work item."""

        pass

    def __column_exists(self, column_header):

        pass