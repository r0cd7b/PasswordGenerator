import random


def manufacture_password():
    try:
        while True:
            password = ""
            for i in range(int(input("Input figures: "))):
                password += random.choice("!%*0123456789?@ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            print(password)
    except:
        print("Exit.")


if __name__ == '__main__':
    manufacture_password()
