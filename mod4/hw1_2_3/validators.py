from typing import Optional

from flask_wtf import FlaskForm
from wtforms import Field
from wtforms.validators import ValidationError


def number_length(min: int, max: int):
    def _number_length(form: FlaskForm, field: Field):
        number: int = field.data()
        if number < min or number > max:
            message = f'Номер должен находиться в интервале {min}-{max}.'
            raise ValidationError(message)
    return _number_length


class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        if not message:
            message = f'Номер должен находиться в интервале {min}-{max}.'
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        number: int = field.data
        if number < self.min or number > self.max:
            raise ValidationError(self.message)