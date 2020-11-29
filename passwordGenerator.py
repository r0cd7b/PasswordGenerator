import random


def generate_password():
    try:
        while input() == "":
            password = ""
            for i in range(12):
                password += random.choice("!$%*0123456789?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            print(password)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    generate_password()
