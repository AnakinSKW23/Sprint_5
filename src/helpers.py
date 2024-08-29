import random

def generate_user_data():
    name = 'NikolayKluchnikov10'
    domen = '@mail.ru'

    new_num = ''
    for i in range(3):
        num = random.randint(0, 9)
        new_num += str(num)
    user_email = name + new_num + domen

    symbols_for_password = '0123456789abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    password = ''
    for i in range(6):
        symbol = random.choice(symbols_for_password)
        password += symbol

    return user_email, password