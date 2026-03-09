# Program 6: extend(), index(), pop()

letters = input("Enter letters separated by space: ").split()
more_letters = input("Enter more letters to extend: ").split()

letters.extend(more_letters)
print("After extend:", letters)

search_letter = input("Enter letter to find index: ")
if search_letter in letters:
    pos = letters.index(search_letter)
    print("Index of", search_letter, "is", pos)

    letters.pop(pos)
    print("After pop:", letters)
else:
    print(search_letter, "not found in list.")
