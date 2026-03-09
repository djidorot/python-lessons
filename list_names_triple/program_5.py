# Program 5: copy(), append(), reverse()

colors = input("Enter colors separated by space: ").split()

new_colors = colors.copy()
print("Copied list:", new_colors)

new_color = input("Enter a color to append: ")
new_colors.append(new_color)
print("After append:", new_colors)

new_colors.reverse()
print("After reverse:", new_colors)
