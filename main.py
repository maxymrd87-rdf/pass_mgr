import generator
import checker
import storage 


def main() -> None:
    print("=== Утилита генерации и анализа паролей ===")
    
    # 1. Запрашивает имя сервиса
    service = input("Введите название сервиса (например, vk, почта, роутер): ").strip()
    if not service:
        service = "unknown_service"
    
    # 2. Запрашивает длину пароля
    try:
        user_input = input("Введите необходимую длину пароля (минимум 4, жми Enter для 16): ")
        length = int(user_input) if user_input.strip() else 16
        if length < 4:
            print("Длина слишком короткая, установлен минимальный порог (4).")
            length = 4
    except ValueError:
        print("Ошибка ввода. Использовать длину по умолчанию (16).")
        length = 16

    print("\n[+] Генерация криптостойкого пароля...")
    password = generator.generate_password(length=length)
    
    print(f"Результат: {password}")
    print("\n[+] Анализ надежности (энтропия по Шеннону)...")
    
    stats = checker.evaluate_strength(password)
    
    print("-" * 40)
    print(f"Длина пароля:            {stats['length']} символов")
    print(f"Вычисленная энтропия:    {stats['entropy_bits']} бит")
    print(f"Общая оценка:            {stats['strength']}")
    print("-" * 40)

    # 3. Сохранение пароля
    storage.save_password(service_name=service, password=password)


if __name__ == "__main__":
    main()