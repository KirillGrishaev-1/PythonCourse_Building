def index_item(items, item):
    i = 0
    while i <= len(items)-1 and items[i] != item:
        i += 1
    if i>=len(items)-1:
        return None
    return i



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item_ = index_item(items_list, find_item)
    if index_item_ is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item_}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
