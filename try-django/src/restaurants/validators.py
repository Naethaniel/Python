from django.core.exceptions import ValidationError


def clean_email(value):
    email = value
    if '.edu' in email:
        raise ValidationError('WE do not accept edu emails')


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']


def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError('This is not valid category')
