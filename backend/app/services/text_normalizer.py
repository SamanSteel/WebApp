# Standard Library
import re

PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
EN_DIGITS = "0123456789"


def normalize_text(text: str) -> str:
    if not text:
        return ""

    for persian_digits, en_digits in zip(PERSIAN_DIGITS, EN_DIGITS):
        text = text.replace(persian_digits, en_digits)

    text = text.replace("‌", " ")

    text = re.sub(r"([آ-یA-Za-z])(\d)", r"\1 \2", text)
    text = re.sub(r"(\d)([آ-یA-Za-z])", r"\1 \2", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text
