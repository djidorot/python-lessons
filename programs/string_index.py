"""
Instructions:
Multiline Paragraph:
Create a variable named multi_line_paragraph and assign it a multiline string containing information about Python. Include at least three lines of text.

Indexing Lines:
Use indexing to extract specific lines from the multi_line_paragraph.
Create three variables: first_line, second_line, and third_line.
Assign each variable the corresponding line from the multi_line_paragraph using slicing.

Display Results:
Print each of the extracted lines individually.

Example Output:
Python is a versatile programming language.


It is widely used for web development, data science, and artificial intelligence.


The syntax is clear and concise, making it easy to learn and use.
"""

# Creating a multi-line paragraph
multi_line_paragraph = """Python is a versatile programming language.
It is widely used for web development, data science, and artificial intelligence.
The syntax is clear and concise, making it easy to learn and use."""

# Using index to access specific lines
first_line = multi_line_paragraph[0:44]
second_line = multi_line_paragraph[44:126]
third_line = multi_line_paragraph[126:]

# Displaying the results
print()
print(first_line)
print()
print(second_line)
print()
print(third_line)
