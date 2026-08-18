import math
import string


def calculate_entropy(password: str) -> float:
    """
    Вычисляет энтропию пароля по формуле Шеннона.
    
    :param password: Проверяемый пароль.
    :return: Значение энтропии в битах.
    """
    if not password:
        return 0.0

    pool_size = 0
    # Проверяем, какие наборы символов использованы, и увеличиваем мощность алфавита
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
        
    # Учитываем наш расширенный пул спецсимволов из генератора
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special_chars for c in password):
        pool_size += len(special_chars)

    if pool_size == 0:
        return 0.0

    # Формула энтропии: длина * log2(мощность алфавита)
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)


def evaluate_strength(password: str) -> dict:
    """
    Оценивает надежность пароля на основе энтропии и наличия нужных символов.
    
    :param password: Проверяемый пароль.
    :return: Словарь с результатами проверки.
    """
    entropy = calculate_entropy(password)
    
    # Классификация криптостойкости (в битах энтропии)
    # < 40: Очень слабый, 40-60: Слабый, 60-80: Надежный, > 80: Криптостойкий
    if entropy < 40:
        strength_level = "Очень слабый"
    elif entropy < 60:
        strength_level = "Слабый"
    elif entropy < 80:
        strength_level = "Надежный"
    else:
        strength_level = "Криптостойкий"

    return {
        "password": password,
        "length": len(password),
        "entropy_bits": entropy,
        "strength": strength_level,
        "has_upper": any(c.isupper() for c in password),
        "has_lower": any(c.islower() for c in password),
        "has_digits": any(c.isdigit() for c in password),
        "has_special": any(not c.isalnum() for c in password)
    }