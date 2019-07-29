from typing import List
from rtm.fields import Field
from rtm.fields.validation import cells_must_not_be_empty, example_results


class ID(Field):
    field_name = "ID"
    def _validate_this_field(self) -> List[dict]:
        return example_results()


class CascadeLevel(Field):
    field_name = "Cascade Level"
    def _validate_this_field(self) -> List[dict]:
        return example_results()


class ReqStatement(Field):
    field_name = "Requirement Statement"
    def _validate_this_field(self) -> List[dict]:
        return example_results()


class ReqRationale(Field):

    field_name = "Requirement Rationale"
    def _validate_this_field(self):
        return [cells_must_not_be_empty(self._body)]


class VVStrategy(Field):
    field_name = "Verification or Validation Strategy"
    def _validate_this_field(self) -> List[dict]:
        return example_results()

class VVResults(Field):
    field_name = "Verification or Validation Results"


class DOFeatures(Field):
    field_name = "Design Output Feature (with CTQ ID #)"


class CTQ(Field):
    field_name = "CTQ? Yes, No, N/A"


class Devices(Field):

    field_name = "Devices"

    def _validate_this_field(self):
        return [cells_must_not_be_empty(self._body)]


if __name__ == "__main__":
    pass
