"""
Модуль графического интерфейса (GUI).
Обеспечивает визуальное взаимодействие с генератором и хранилищем.
"""
import tkinter as tk
from tkinter import messagebox
import generator
import checker
import storage

# Глобальные переменные для временного хранения текущего результата
current_password = ""
current_service = ""


def on_generate() -> None:
    """Обработчик нажатия на кнопку генерации."""
    global current_password, current_service
    
    # Открытие данных из полей ввода
    service = entry_service.get().strip() or "unknown_service"
    try:
        length = int(entry_length.get())
        if length < 4:
            length = 4
    except ValueError:
        length = 16  # Значение по умолчанию при ошибке ввода

    current_service = service
    current_password = generator.generate_password(length)
    stats = checker.evaluate_strength(current_password)

    # Обновляем текст на экране
    lbl_password_result.config(text=current_password)
    lbl_stats.config(
        text=f"Энтропия: {stats['entropy_bits']} бит | Уровень: {stats['strength']}"
    )


def on_save() -> None:
    """Обработчик нажатия на кнопку сохранения."""
    if not current_password:
        messagebox.showwarning("Внимание", "Сначала сгенерируйте пароль!")
        return
        
    storage.save_password(current_service, current_password)
    messagebox.showinfo(
        "Успех", 
        f"Пароль для '{current_service}' успешно сохранен в базу!"
    )


# --- Настройка визуального окна (Pipeline интерфейса) ---
root = tk.Tk()
root.title("Crypto Password Manager")
root.geometry("450x350")
root.resizable(False, False)

# Рамка для отступов
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

# Поле: Название сервиса
tk.Label(frame, text="Название сервиса (например, vk):", font=("Arial", 10)).pack(anchor="w")
entry_service = tk.Entry(frame, width=40, font=("Arial", 12))
entry_service.pack(pady=5)

# Поле: Длина пароля
tk.Label(frame, text="Длина пароля (число):", font=("Arial", 10)).pack(anchor="w", pady=(10, 0))
entry_length = tk.Entry(frame, width=40, font=("Arial", 12))
entry_length.insert(0, "16")  # Значение по умолчанию вписано сразу
entry_length.pack(pady=5)

# Кнопка генерации
btn_generate = tk.Button(
    frame, text="Сгенерировать", font=("Arial", 12, "bold"), 
    bg="#4CAF50", fg="white", command=on_generate
)
btn_generate.pack(pady=15, fill=tk.X)

# Вывод результата
lbl_password_result = tk.Label(frame, text="...", font=("Courier", 16, "bold"), fg="#D32F2F")
lbl_password_result.pack(pady=5)

# Вывод статистики
lbl_stats = tk.Label(frame, text="Энтропия: 0 бит", font=("Arial", 10), fg="#555555")
lbl_stats.pack(pady=5)

# Кнопка сохранения
btn_save = tk.Button(frame, text="Сохранить в базу", font=("Arial", 10), command=on_save)
btn_save.pack(pady=10, fill=tk.X)

# Запуск основного цикла окна
if __name__ == "__main__":
    root.mainloop()