
import re

def normalize_ua_phone(raw: str) -> str:
    """Перевіряє український номер і повертає його у форматі +380XXXXXXXXX."""
    if not isinstance(raw, str):
        raise ValueError("Номер телефону має бути рядком")

    phone = raw.replace(" ", "").replace("-", "")

    if re.fullmatch(r"0\d{9}", phone):
        normalized = "+38" + phone
    elif re.fullmatch(r"380\d{9}", phone):
        normalized = "+" + phone
    elif re.fullmatch(r"\+380\d{9}", phone):
        normalized = phone
    else:
        raise ValueError("Некоректний український номер телефону")

    return normalized
