# unit-tests-lab-4

ПІБ: Калініченко Артем

Група: 3-41

Номер у журналі: 17

Варіант: 7

Мова програмування: Python

Опис завдання

Реалізовано функцію normalize_ua_phone(raw), яка перевіряє український номер телефону та приводить його до формату +380XXXXXXXXX. Функція приймає номери у форматах 0XXXXXXXXX, 380XXXXXXXXX і +380XXXXXXXXX. Пробіли та дефіси прибираються. Некоректний формат або значення, яке не є рядком, спричиняє ValueError.

Установлення:

python -m venv .venv

Установлення залежностей:

python -m pip install -r requirements.txt

Запуск тестів:

python -m pytest -v

Перевірка покриття:

python -m pytest --cov=phone --cov-report=term-missing --cov-report=html:coverage

Фактичне покриття: 100%
