import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Hector Hector Uriel Fernandez Taño Fernandez Taño', 'Hector Uriel Fernandez Taño')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
