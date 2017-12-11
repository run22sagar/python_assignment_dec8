password = "I_Love_Nepal"


def pas(word):
    global password
    if word == password:
        print("Password match")
    else:
        print("Wrong Password")


p_word = input("Please enter password: ")
pas(p_word)