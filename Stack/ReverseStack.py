def reverse_string(my_string):
    stack = []
    for letter in my_string:
        stack.append(letter)

    reversed_string = ""

    while len(stack) > 0:
        reversed_string = reversed_string + stack.pop()
    
    return reversed_string

naam = "ARYAN"
print("Original:", naam)
print("Reversed:", reverse_string(naam))