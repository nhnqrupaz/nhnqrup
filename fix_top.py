with open('src/app/page.tsx', 'r') as f:
    content = f.read()

content = content.replace('<div id="top" className="absolute top-0 w-full h-1" />\n', '')

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

