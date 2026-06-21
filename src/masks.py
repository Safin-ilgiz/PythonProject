def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""
    return f"**{account_number[-4:]}"


def get_mask_card_number(number_card: str) -> str:
    """Функция, которая маскирует номер карты"""
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
