from general.packets.price import get_prices_for_list_of_items

a = [('300430002', 7),('200350018', 6),('100950001', 9),('200540006', 0),('200340009', 8)]

get_prices_for_list_of_items('8001', a, False)