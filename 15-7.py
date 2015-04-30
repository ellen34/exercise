#reverse
def reverse(text):
    new_word = ""
    for item in range(len(text)-1, -1, -1):
        new_word += text[item]
    return new_word
    
print reverse("This is a book.")

text = "this is a book"
new_list = text.split()
new_list = " ".join(new_list[::-1])
print new_list
#for item in text:
#    if item != '':
#        new_list.append(item)
#print new_list
