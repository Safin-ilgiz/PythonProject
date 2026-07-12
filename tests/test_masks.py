from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_account():
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('7365410843013587430528') == '**0528'
    assert get_mask_account('Счет 73654108430135874305') == '**4305'

def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('') == 'Номер карты отсутствует'
    assert get_mask_card_number('700079228960636159') == 'Номер карты должен состоять из 16 цифр'
    assert get_mask_card_number('Карта №7000792289606361') == 'Номер карты должен состоять только из цифр'