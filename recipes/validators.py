from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

valid_unit_of_measurement = ['pounds','lbs','oz','gram']


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"'{value}' is not a valid unit of measurement")
    except:
        raise ValidationError(f"'{value}' is invalid. Unknown error.")
    # if value not in valid_unit_of_measurement:
    #     raise ValidationError(f"{value} is not a valid unit of measurement")