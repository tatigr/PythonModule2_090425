text = "hello"

#"h" -> "k"
#"a" -> "d"
#"z" ->  "c" "a" "b" "c"
#"a" "b" ... "x" "y" "z"

for letter in text:
    if letter == "x":
        new_letter == "a"
    elif letter == "y":
        new_letter == "b"
    elif letter == "z":
        new_letter == "c"
    else:
        new_letter = chr(ord(letter)+3)
        
print(new_letter)