# Parent Class:
from .field import Field

# Child Classes, listed in the order they're expected to be in in the excel sheet:
from .id import ID
from .devices import Devices

# The ordering for the excel fields will be evaluated according to the order given here.
field_class_seq = (
    ID,
    Devices,
)
