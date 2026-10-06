with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Pull entire text block up on mobile
c = c.replace('<div className="relative z-10 max-w-3xl text-white">', '<div className="relative z-10 max-w-3xl text-white -mt-16 md:mt-0">')

# Push button down relative to text on mobile by increasing the p margin
c = c.replace('className="text-base md:text-lg text-white/80 mb-8 max-w-xl leading-relaxed"', 'className="text-base md:text-lg text-white/80 mb-14 md:mb-8 max-w-xl leading-relaxed"')

# Make button smaller on mobile
c = c.replace('className="bg-[#ff4f14] text-white px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-[#e64612] transition-colors"', 'className="bg-[#ff4f14] text-white px-6 py-3 md:px-8 md:py-4 rounded-full font-bold text-base md:text-lg inline-flex items-center gap-2 hover:bg-[#e64612] transition-colors mt-4 md:mt-0"')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)
