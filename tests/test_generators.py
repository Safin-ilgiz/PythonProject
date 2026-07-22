import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 2),
    ("EUR", 0),
])
def test_filter_by_currency(sample_transactions, currency, expected_count):
    result = list(filter_by_currency(sample_transactions, currency))
    assert len(result) == expected_count
    if expected_count > 0:
        assert result[0]["operationAmount"]["currency"]["code"] == currency

def test_filter_by_currency_empty():
    assert list(filter_by_currency([], "USD")) == []


@pytest.mark.parametrize("transactions, expected", [
    # Тест с нормальными данными
    ([{"description": "Перевод"}, {"description": "Оплата"}], ["Перевод", "Оплата"]),
    # Тест на пустой список
    ([], []),
])
def test_transaction_descriptions(transactions, expected):
    assert list(transaction_descriptions(transactions)) == expected



@pytest.mark.parametrize("start, end, expected", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (999, 999, ["0000 0000 0000 0999"]),  # Крайние значения
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод организации"},
        {"id": 2, "operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод со счета"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод с карты"},
    ]
