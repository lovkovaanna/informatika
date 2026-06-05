# TODO Напишите функцию для поиска индекса товара
def find_item_index (items, target): #функция для поиска первого вхождения товара в список
    for n, item in enumerate(items): #перебираем список с индексами
        if item==target: #если выполняется условие
            return n #возвращаем индекс первого вхождения
    return  None #если товар не найден, возвращаем None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item) #вызываем функцию, чтобы получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.") #выводим
    else:
        print(f"Товар '{find_item}' не найден в списке.") #выводим если не найден
