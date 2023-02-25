import re
def validate_phone(phone):
    return bool(re.match("[0-9]+",phone))
