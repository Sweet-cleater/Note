from lxml import html

html_file = r'itiran.html'

with open(html_file, mode='rb') as f:
    t = html.fromstring(f.read())

remove_tags = ('.//style', './/script', './/noscript')
for remove_tag in remove_tags:
    for tag in t.findall(remove_tag):
        tag.drop_tree()

text1 = t.text_content().strip()
#text1 = text1.replace('\n', '')
text1 = text1.replace(' ', '')

text1 = text1.replace('編集', '')

path_w = 'out.txt'

with open(path_w, mode='w') as f:
    f.write(text1)

print("It was executed.")