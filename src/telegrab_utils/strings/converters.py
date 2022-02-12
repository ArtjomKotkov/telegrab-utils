import re


__all__ = [
    'title_case_to_camel_case'
]


def title_case_to_camel_case(string: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()
