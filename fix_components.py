with open('src/components/Footer.tsx', 'r') as f:
    content = f.read()
content = content.replace('      {/* Footer */}\n', '')
with open('src/components/Footer.tsx', 'w') as f:
    f.write(content)

with open('src/components/Header.tsx', 'r') as f:
    content = f.read()
content = content.replace('      {/* Navigation */}\n', '')
with open('src/components/Header.tsx', 'w') as f:
    f.write(content)

