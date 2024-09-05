from datetime import date

from django.core.exceptions import ValidationError


def real_age_validator(value: date):
    age = (date.today() - value).days // 365
    if age < 1 or age > 120:
        raise ValidationError(
            'Возраст должен быть в пределах от 1 до 120 лет.'
        )