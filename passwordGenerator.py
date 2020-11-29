import random


def generate_password():
    try:
        text = ["!$%*?", "0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"]
        while input() == "":
            password = ""
            for characters in text:
                password += random.choice(characters)
            for i in range(8):
                password += random.choice(text)
            print(password)
            password = list(password)
            random.shuffle(password)
            print(password)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    generate_password()
