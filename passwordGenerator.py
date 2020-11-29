import random


def generate_password():
    try:
        special = "!$%*?"
        decimal = "0123456789"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        characters = special + decimal + upper + lower
        while input() == "":
            password = random.choice(special) + random.choice(decimal) + random.choice(upper) + random.choice(lower)
            for i in range(8):
                password += random.choice(characters)
            password = list(password)
            random.shuffle(password)
            print(password)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    generate_password()
