text = "hello everyone how are you?"
new_string = ""
for characters in text:
    if characters == "e":
        new_string += characters.upper()
    else:
        new_string += characters
print(new_string)
