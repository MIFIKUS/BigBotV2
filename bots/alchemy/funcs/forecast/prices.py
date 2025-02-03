from general.packets.price import get_prices_for_list_of_items


def get_prices_for_each_slot(server_id: str, items_info: dict) -> dict:
    """Получает цену для каждого слота"""
    request = []
    for slot, item_info in items_info.items():
        request.append(item_info)

    return get_prices_for_list_of_items(server_id, request, True)



