f = open('SRQ.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Welcome To GFG</h2>

<p>Default code has been loaded into the Editor.</p>


</body>
</html>
"""

# writing the code into the file
f.write(html_template)
f.write("helloi")
# close the file
f.close()
