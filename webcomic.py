

//comment = 
What‽ Oh no · GitHub desi uxxo interroband ij 
//

import markdown
import os

# Read the Markdown file
with open('comic.md', 'r') as f:
    content = f.read()

# Convert the Markdown to HTML
html = markdown.markdown(content)

# Generate the HTML for the webcomic
webcomic = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Webcomic</title>
</head>
<body>
    {html}
</body>
</html>
'''

# Write the HTML to a file
with open('webcomic.html', 'w') as f:
    f.write(webcomic)

# Open the webcomic in a web browser
os.system('open webcomic.html')
