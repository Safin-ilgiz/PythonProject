def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей и возвращает новый с указанным значением 'state'"""
    # Создаем новый пустой список
    filter_list = []
    # Запускаем цикл for и создаем условие
    for item in list_dict:
        if item.get("state") == state:
            filter_list.append(item)
    return filter_list


def sort_by_date(list_dict: list[dict], reverse_order: bool = True) -> list:
    """Функция, которая принимает список словарей и возвращает новый отсортированый по дате список"""
    return sorted(list_dict, key=lambda x: x.get("data", ""), reverse=reverse_order)
