import random

def pgen():
    print("****Welcome to password generator****")
    Upper_letter = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    Lower_letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    Digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    Sp_symbols = ('~','!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=')

    pass_length = int(input('Enter length of password :'))

    L = []
    L.extend(list(Upper_letter))
    L.extend(list(Lower_letter))
    L.extend(list(Digits))
    L.extend(list(Sp_symbols))

    random.shuffle(L)
    password = (''.join(L[0:pass_length]))
    print(password)

    again = input("DO YOU WANT TO CREATE ANOTHER PASSWORD, TYPE Y for YES and N for NO :")
    if again == "Y" :
        return pgen()
    else:
        print("I hope you like it!")


pgen()
