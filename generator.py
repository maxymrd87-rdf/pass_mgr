"""
Модуль для криптографически стойкой генерации паролей.
Использует системный источник энтропии (модуль secrets).
"""

import secrets
import string


def generate_password(
    length: int,
    use_upper: bool = True,
    use_digits: bool = True,
    use_special: bool = True
) -> str:
    """
    Генерирует криптографически стойкий случайный пароль.

    :param length: Длина пароля.
    :param use_upper: Использовать ли заглавные буквы.
    :param use_digits: Использовать ли цифры.
    :param use_special: Использовать ли специальные символы.
    :return: Сгенерированная строка пароля.
    """
    if length < 4:
        raise ValueError("Длина пароля должна быть не менее 4 символов.")

    # Сборка разрешенного алфавит
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_special:
        # Добавлен ограниченный набор спецсимволов для надежности и исключения конфликтов
        alphabet += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Указание, что пароль содержит хотя бы один символ из каждой выбранной категории
    password_chars = [secrets.choice(string.ascii_lowercase)]
    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(secrets.choice(string.digits))
    if use_special:
        password_chars.append(secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))

    # Комплит оставшейся длины случайными символами из общего пула
    remaining_length = length - len(password_chars)
    password_chars.extend(secrets.choice(alphabet) for _ in range(remaining_length))

    # Тщательно перемешиваем, чтобы обязательные символы не всегда шли в начале
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def generate_multiple_passwords(
    count: int,
    length: int,
    use_upper: bool = True,
    use_digits: bool = True,
    use_special: bool = True
) -> list[str]:
    """
    Генерирует список из нескольких вариантов паролей.
    
    :param count: Количество паролей для генерации.
    :param length: Длина каждого пароля.
    :return: Список строк сгенерированных паролей.
    """
    return [
        generate_password(length, use_upper, use_digits, use_special)
        for _ in range(count)
    ]