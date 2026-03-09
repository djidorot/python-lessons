# Program 8: append(), extend(), reverse()

animals = input("Enter animals separated by space: ").split()

new_animal = input("Enter one animal to append: ")
animals.append(new_animal)
print("After append:", animals)

more_animals = input("Enter more animals to extend: ").split()
animals.extend(more_animals)
print("After extend:", animals)

animals.reverse()
print("After reverse:", animals)
