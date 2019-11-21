from fuzzytable import FieldPattern


def cellpattern_id(self):
    """Validate this field"""
    work_items = context.work_items.get()
    self._val_results = self.val_results_header_and_field_exists()
    if self.found:
        self._val_results += [
            # No need for explicit "not empty" check b/c this is caught by pxxx
            #   format and val_match_parent_prefix.
            val.unique(self.values),
            val.alphabetical_sort(self.values),
            val.procedure_step_format(self.values, work_items),
            val.start_w_root_id(),
        ]


fieldpattern_id = FieldPattern(
    name='id',
    approximate_match=True,
    cellpattern=cellpattern_id,
)


# TODO how to do left/right order checking?
#   This check requires broader context


