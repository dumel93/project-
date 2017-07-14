from prompt_toolkit.validation import ValidationError


def validate_course(value):
    if value < 1.0:
        raise ValidationError("%s Course should be more than 1.0!" % value)


def validate_bet(value):
    if value < 0.0:
        raise ValidationError("%s Bet should be positive number!" % value)