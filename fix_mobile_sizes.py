with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Hero
c = c.replace('text-4xl md:text-6xl', 'text-3xl md:text-6xl')
c = c.replace('pt-40 pb-32', 'pt-32 pb-24 md:pt-40 md:pb-32')

# Niyə Bizi Seçməlisiniz etc. - change py-24 to py-16 md:py-24
c = c.replace('py-24 px-6', 'py-16 md:py-24 px-6')
c = c.replace('text-5xl font-bold', 'text-3xl md:text-5xl font-bold')
c = c.replace('mb-16', 'mb-10 md:mb-16')
c = c.replace('mb-8', 'mb-6 md:mb-8')
c = c.replace('mb-6', 'mb-4 md:mb-6')

# TƏCİLİ button and text
c = c.replace('text-4xl md:text-5xl font-bold', 'text-3xl md:text-5xl font-bold')
c = c.replace('py-16 px-6', 'py-12 md:py-16 px-6')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

