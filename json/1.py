import json
import os

# Шаблон для данных
template = {
    "name": "HODL GIRL #[NUMBER]",
    "description": "Это обычная девушка, которая получила перевод в кошельке @wallet в телеграм.",
    "external_url": "https://getgems.io/collection/EQCi5q8Zos-zXTiUo0ghves2v_WWA6Upo9vRR3CtROjahQP8",
    "image": "https://hodlgirlsnft.pages.dev/images/[NUMBER].png",
    "attributes": [
        {
            "trait_type": "Девушка",
            "value": "Обычная"
        }
    ]
}

# Создание файлов
for i in range(1001):
    data = {
        "name": template["name"].replace("[NUMBER]", str(i)),
        "description": template["description"],
        "external_url": template["external_url"],
        "image": template["image"].replace("[NUMBER]", str(i)),
        "attributes": template["attributes"]
    }

    # Определяем имя файла
    filename = f'{i}.json'

    # Запись данных в файл
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
