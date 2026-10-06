with open('src/components/Header.tsx', 'r') as f:
    c = f.read()

# max-w-5xl -> max-w-4xl (to tighten it more)
c = c.replace('w-full max-w-5xl shadow-sm', 'w-full max-w-4xl shadow-sm')
# text-[15px] -> text-[16px]
c = c.replace('text-[15px]', 'text-[16px]')

with open('src/components/Header.tsx', 'w') as f:
    f.write(c)

