# Standard library
# Standard Library
from dataclasses import dataclass


@dataclass
class Chip:
    """
    Chip is compact element, which enable to represent enum values from semantic
    and it is represented as UI chip

    Parameters
    ----------
    label: str
        The label of chip that will be displayed in the UI
    variant: str
        Variant of the chip defined in materialUI, possible values are 'filled' and 'outlined', if variant is not defined, chip will be filled
        See documentation: https://mui.com/material-ui/react-chip/

    variant: str
        Size of the chip defined in materialUI, possible values are 'medium' and 'small', if variant is not defined, chip will be 'medium'
        See documentation: https://mui.com/material-ui/react-chip/

    Raises
    ------
    ValueError
        In case of incorrect label
    """

    label: str
    variant: str
    size: str

    def __init__(self, label: str, variant: str, size: str):
        if len(label) == 0:
            raise ValueError("Incorrect value for label")

        self.label = label
        self.variant = variant if len(variant) != 0 else "filled"
        self.size = size if len(size) != 0 else "medium"
