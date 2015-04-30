def censor(text, word):
    new_list = text.split()
    for item in range(len(new_list)):
        if word == new_list[item]:
            new_list[item] = "*" * len(word)
    new_list = " ".join(new_list)
    return new_list
        
print censor("This is a book", "book")
