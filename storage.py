import json
import os
from datetime import datetime


def save_password(service_name: str, password: str, filepath: str = "passwords.json") -> None:
    """
    Сохраняет сгенерированный пароль в локальный JSON-файл.
    
    :param service_name: Название сервиса или сайта.
    :param password: Сгенерированный пароль.
    :param filepath: Путь к файлу хранилища (по умолчанию passwords.json).
    """
    data = {}
    
    # Проверка, существует ли уже файл хранилища
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # Если файл поврежден или пуст, начать с чистого словаря
                pass

    # Добавить или обновить запись
    data[service_name] = {
        "password": password,
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Перепакетирование данных обратно в файл
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        
    print(f"\n[+] Пароль для '{service_name}' надежно сохранен в {filepath}")