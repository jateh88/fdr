"""This module defines both the work item class (equivalent to a worksheet row)
and the work items class, a custom sequence contains all work items."""

# --- Standard Library Imports ------------------------------------------------
import collections
from typing import List

# --- Third Party Imports -----------------------------------------------------
# None

# --- Intra-Package Imports ---------------------------------------------------
from rtm.containers.fields import CascadeBlock
import rtm.main.context_managers as context
from rtm.main.exceptions import UninitializedError
from rtm.validate.checks import cell_empty


CascadeBlockCell = collections.namedtuple("CascadeBlockCell", "depth value")


class WorkItem:

    def __init__(self, index):
        """A work item is basically a row in the RTM worksheet. It's an item
        that likely a parent and at least one child."""
        self.index = index  # work item's vertical position relative to other work items
        self.cascade_block = []
        self.parent = UninitializedError()  # The index (integer) of the parent. Or None if no parent.

    @property
    def has_parent(self):
        """If false, is either because or error or it is a root item"""
        if self.parent is None:
            return False
        elif self.parent >= 0:
            return True
        else:
            return False

    @property
    def depth(self):
        """Depth is equivalent to the number of edges from this work item to a root work item."""
        try:
            return self.cascade_block[0].depth
        except IndexError:
            return None

    def set_cascade_block_row(self, cascade_block_row: list):
        """Save non-empty cascade block cell values"""
        for depth, value in enumerate(cascade_block_row):
            if not cell_empty(value):
                self.cascade_block.append(CascadeBlockCell(depth, value))

    def find_parent(self, work_items):
        """Find parent. """

        # set default
        self.parent = None

        if self.depth is None:
            # If no position (row was blank), then no parent
            return
        elif self.depth == 0:
            # If in first position, then it's the trunk of a tree!
            self.parent = -1
            return

        # Search back through previous work items
        for index in reversed(range(self.index)):

            other = work_items[index]

            if other.depth is None:
                # Skip work items that have a blank cascade. Keep looking.
                continue
            elif other.depth == self.depth:
                # same position, same parent
                self.parent = other.parent
                return
            elif other.depth == self.depth - 1:
                # one column to the left; that work item IS the parent
                self.parent = other.index
                return
            elif other.depth < self.depth - 1:
                # cur_work_item is too far to the left. There's a gap in the chain. No parent
                return
            else:
                # self.position < other.position
                # Skip work items that come later in the cascade. Keep looking.
                continue


class WorkItems(collections.abc.Sequence):

    def __init__(self):
        """Sequence of work items"""

        # --- Get Cascade Block -----------------------------------------------
        fields = context.fields.get()
        cascade_block = fields.get_field_object(CascadeBlock)

        # --- Initialize Work Items -------------------------------------------
        self._work_items = [WorkItem(index) for index in range(fields.height)]
        for work_item in self:
            row_data = self.get_row(cascade_block.values, work_item.index)
            work_item.set_cascade_block_row(row_data)
            work_item.find_parent(self._work_items)

    @staticmethod
    def get_row(columns: List[list], index: int) -> list:
        return [col[index] for col in columns]

    # --- Sequence ------------------------------------------------------------
    def __getitem__(self, item) -> WorkItem:
        return self._work_items[item]

    def __len__(self) -> int:
        return len(self._work_items)


if __name__ == "__main__":
    pass
