# HTML and CSS code
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            text-align: center;
        }
        h1 {
            color: #333333;
        }
    </style>
</head>
<body>
    <h1>Hello, Python!</h1>
    <p>This is a simple HTML page with embedded CSS.</p>
</body>
</html>
'''

# Save the HTML code to a file
with open('output.html', 'w') as file:
    file.write(html_code)
