# TODO решите задачу
import json
def task() -> float:
    filename = "input.json" #пусть файл называется input.json
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f) #загружаем список словарей
    total = 0.0
    for item in data:
        score = item.get("score", 0.0) # Каждый item — словарь с ключами "score" и "weight"
        weight = item.get("weight", 0)
        total += score * weight
    return round(total, 3) # Округляем до 3 знаков
if __name__ == "__main__":
    result = task()
    print(result) #выводим ответ

