from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Generator[dict, Any, None]:
    """Функция,фильтрует транзакции по коду валюты."""
    for transaction in transactions:
        amount = transaction['operationAmount']
        currency = amount['currency']
        code = currency['code']
        if code == currency_code:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[str, None, None]:
    """Генератор, который поочередно выдает описание каждой транзакции."""
    for transaction in transactions:
        yield transaction.get("description", "")

def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор, который выдает номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне."""
    for number in range(start, end + 1):
        number_str = f"{number:016d}"
        formatted_card = f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        yield formatted_card
