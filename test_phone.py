
import pytest

from phone import normalize_ua_phone


def test_phone_with_spaces_is_normalized():
    raw = "0 67 123 45 67"

    result = normalize_ua_phone(raw)

    assert result == "+380671234567"


def test_phone_with_plus380_is_preserved():
    result = normalize_ua_phone("+380671234567")

    assert result == "+380671234567"


def test_phone_with_380_is_normalized():
    result = normalize_ua_phone("380671234567")

    assert result == "+380671234567"


def test_phone_with_hyphens_is_normalized():
    result = normalize_ua_phone("067-123-45-67")

    assert result == "+380671234567"


def test_short_phone_is_rejected():
    with pytest.raises(ValueError, match="Некоректний"):
        normalize_ua_phone("067123456")


def test_phone_with_letters_is_rejected():
    with pytest.raises(ValueError, match="Некоректний"):
        normalize_ua_phone("+38067ABC4567")


def test_phone_with_wrong_prefix_is_rejected():
    with pytest.raises(ValueError, match="Некоректний"):
        normalize_ua_phone("+12345678901")


def test_non_string_input_is_rejected():
    with pytest.raises(ValueError, match="рядком"):
        normalize_ua_phone(671234567) 
