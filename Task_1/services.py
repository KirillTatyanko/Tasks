from string import ascii_letters, digits, punctuation
import random


def password_generator(
        total_count: int,
        length: int,
        use_numbers: bool,
        use_special_chars: bool
) -> list:
    chars = ascii_letters

    if use_numbers and use_special_chars:
        chars += digits + punctuation
    elif use_numbers and not use_special_chars:
        chars += digits
    elif not use_numbers and use_special_chars:
        chars += punctuation

    return generate_passwords(total_count, length, chars)


def generate_passwords(total_count: int, length: int, chars: str) -> list:
    passwords_list = []
    password = ""
    start = 1
    while start <= total_count:
        for i in range(length):
            password += random.choice(chars)
        passwords_list.append(password)
        password = ""
        start += 1
    return passwords_list
