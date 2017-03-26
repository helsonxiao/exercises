dictionary = {}
while True:
    user_action = input("Add or look up a word (a/l)?")
    if user_action == "a":
        type_word = input("Type the word:")
        type_definition = input("Type the definition:")
        dictionary[type_word] = type_definition
    elif user_action == "l":
        type_word = input("Type the word:")
        print(dictionary[type_word])
    else:
        print("Please enter a/l.")