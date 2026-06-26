from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(string_info: str) -> str:
    """Функция, которая маскирует номера карт и счетов"""
    if not string_info:
        return 'Данные не переданы'
    # Разбиваем строку на элементы списка
    string_info_list = string_info.split()
    if not string_info_list:
        return 'Некорректные данные'
    # Получаем номер карты или счета с помощью отрицательного индекса
    number = string_info_list[-1]
    if not number.isdigit():
        return 'Номер должен сосотоять только из цифр'
    # Собираем название карты или счета без номера
    name = " ".join(string_info_list[:-1])
    # Дальше ставим условие через if и применяем нужную функцию
    if "Счет" in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{name} {masked_number}"


def get_date(date: str) -> str:
    """Функция, которая принимает строку с датой и возвращает в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
