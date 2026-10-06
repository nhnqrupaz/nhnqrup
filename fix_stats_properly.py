import re

with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Fix the section replacement
c = re.sub(
    r'<section className="bg-\[#ff4f14\] py-[^"]+ px-6 lg:px-20 text-white">',
    '<section className="bg-[#ff4f14] py-6 md:py-16 px-4 md:px-6 lg:px-20 text-white rounded-3xl md:rounded-none mx-4 md:mx-0 mt-[-30px] md:mt-0 relative z-20 shadow-xl">',
    c
)

# Fix the text size in the stats
c = re.sub(
    r'className="text-4xl[^"]*font-bold mb-2"',
    'className="text-2xl md:text-5xl font-bold mb-1 md:mb-2"',
    c
)

with open('src/app/page.tsx', 'w') as f:
    f.write(c)
