with open('src/app/layout.tsx', 'r') as f:
    c = f.read()

if 'overflow-x-hidden' not in c:
    c = c.replace('<body className={inter.className}>', '<body className={`${inter.className} overflow-x-hidden w-full max-w-[100vw]`}>')

with open('src/app/layout.tsx', 'w') as f:
    f.write(c)
