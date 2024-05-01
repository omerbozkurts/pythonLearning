from bs4 import BeautifulSoup

html_doc='''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Page</title>
</head>
<body>
    <h1>Test</h1>
    <div><ul>
<li>list element 1</li>
    <li>list element 2</li>
                        <li>list element 3</li>
    </ul></div>
</body>
</html>

'''

soup = BeautifulSoup(html_doc,'html.parser')

print(soup.prettify())
print(soup.title)
print(soup.h1)
print(soup.h1.name)
print(soup.h1.string)


print(soup.find_all('h1'))

print(soup.div)


print(soup.div.findChild())