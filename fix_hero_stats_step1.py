with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# 1. Translate Service and Training
c = c.replace('Service and Training', 'Servis və Təlimlər')

# 2. Hero Image
c = c.replace('https://images.unsplash.com/photo-1585704032915-c3400ca199e7?q=80&w=3270&auto=format&fit=crop', 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=3270&auto=format&fit=crop')

# 3. Stats section padding for mobile and 2500 -> 500
c = c.replace('<section className="bg-[#ff4f14] py-16 px-6 lg:px-20 text-white">', '<section className="bg-[#ff4f14] py-8 md:py-16 px-6 lg:px-20 text-white">')
c = c.replace('<NumberCounter end={2500} suffix="+" />', '<NumberCounter end={500} suffix="+" />')

# Just in case they meant the top bar (bg-[#ff4f14]/80 rounded-full px-5 py-1 mb-6):
c = c.replace('className="inline-flex items-center gap-2 border border-[#ff4f14] bg-[#ff4f14]/80 rounded-full px-5 py-1 mb-6 backdrop-blur-sm"', 'className="inline-flex items-center gap-2 border border-[#ff4f14] bg-[#ff4f14]/80 rounded-full px-3 md:px-5 py-0.5 md:py-1 mb-6 backdrop-blur-sm"')
c = c.replace('className="text-sm font-medium"', 'className="text-xs md:text-sm font-medium"')


with open('src/app/page.tsx', 'w') as f:
    f.write(c)

