def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    return f"**{account_number[-4:]}"


def get_mask_card_number(number_card: str) -> str:
    """Функция, которая маскирует номер карты"""
    if  not number_card:
        return 'Номер карты отсутствует'
    elif not number_card.isdigit():
        return 'Номер карты должен состоять только из цифр'
    elif len(number_card) != 16:
        return 'Номер карты должен состоять из 16 цифр'
    else:
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"