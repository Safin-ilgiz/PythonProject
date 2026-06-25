from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(string_info: str)-> str:
    """Функция, которая маскирует номера карт и счетов"""
    #Разбиваем строку на элементы списка
    string_info_list = string_info.split()
    #Получаем номер карты или счета с помощью отрицательного индекса
    number = string_info_list[-1]
    #Собираем название карты или счета без номера
    name = ' '.join(string_info_list[:-1])
    #Дальше ставим условие через if и применяем нужную функцию
    if 'Счет' in name:
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f'{name} {masked_number}'


def get_date(date: str)-> str:
    """Функция, которая принимает строк с датой и возвращает в формате ДД.ММ.ГГГГ"""
    return f'{date[8:10]}.{5:7}.{:4}'


