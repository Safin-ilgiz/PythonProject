import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11"},
        {"id": 2, "state": "CANCELED", "date": "2019-08-26"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-11"},
    ]


@pytest.mark.parametrize(
    "state, expected_len",
    [
        ("EXECUTED", 2),
        ("CANCELED", 1),
        ("NON_EXISTENT", 0),
    ],
)
def test_filter_by_state(sample_operations, state, expected_len):
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_len


def test_sort_by_date_desc(sample_operations):
    result = sort_by_date(sample_operations, reverse_order=True)
    assert result[0]["date"] == "2024-03-11"


def test_sort_by_date_asc(sample_operations):
    result = sort_by_date(sample_operations, reverse_order=False)
    assert result[0]["date"] == "2019-08-26"

