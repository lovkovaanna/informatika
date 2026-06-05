# TODO Напишите функцию find_common_participants

def find_common_participants(gr1, gr2, separator=','): #Находит общих участников в двух группах
 participants1 = [name.strip() for name in gr1.split(separator)]
 participants2 = [name.strip() for name in gr2.split(separator)]
 common_set = set(participants1) & set(participants2)#Находим общих участников
 common_list = sorted(list(common_set))#Преобразуем множество обратно в список и сортируем
 return common_list #Возвращаем результат

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')#Проверяем работу функции с разделителем "|"
print("Общие участники:") #Выводим результат
print(common_participants)
print("\nСписок общих участников:") #Дополнительная проверка: выводим каждого участника на отдельной строке
for participant in common_participants:
    print(f"  • {participant}")








