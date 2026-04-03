# TODO импортировать необходимые молули
import csv# для работы с CSV файлами
import json# для работы с JSON форматом

INPUT_FILENAME = "input.csv" # файл с исходными данными
OUTPUT_FILENAME = "output.json" # файл для результата

def task() -> None: # Открываем CSV файл для чтения
    with open(INPUT_FILENAME, mode='r', newline='', encoding='utf-8') as csvfile: # DictReader сам определяет заголовки из первой строки
        csv_reader = csv.DictReader(csvfile)
        data = list(csv_reader)  # Преобразуем reader в список словарей

    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as jsonfile: # Открываем JSON файл для записи
            json.dump(data, jsonfile, indent=4) # Записываем данные в JSON с отступами 4

if __name__ == '__main__':# Нужно для проверки
    task() # Выполняем основную функцию

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="") # Выводим содержимое созданного файла на экран





