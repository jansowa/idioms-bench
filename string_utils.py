import math

def is_not_blank(text) -> bool:
    if isinstance(text, float) and math.isnan(text):
        return False
    return bool(text and text.strip())
