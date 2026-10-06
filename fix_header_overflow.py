with open('src/components/Header.tsx', 'r') as f:
    c = f.read()

# Make sure logo text doesn't wrap and uses text-lg on mobile
c = c.replace('<span className="font-black text-xl md:text-2xl tracking-tight text-[#131312]">NHN Qrup</span>', '<span className="font-black text-lg md:text-2xl tracking-tight text-[#131312] whitespace-nowrap shrink-0">NHN Qrup</span>')

# Make sure the container handles shrinking gracefully
c = c.replace('className="bg-white rounded-full px-5 py-4 flex items-center justify-between w-full max-w-5xl shadow-sm relative"', 'className="bg-white rounded-full px-4 md:px-5 py-3 md:py-4 flex items-center justify-between w-full max-w-5xl shadow-sm relative gap-2"')

# Make sure Contact button text on mobile doesn't wrap
c = c.replace('className="bg-[#ff4f14] text-white px-4 py-2 rounded-full text-xs font-bold hover:bg-[#e64612] transition-colors flex items-center gap-1 shadow-sm"', 'className="bg-[#ff4f14] text-white px-3 md:px-4 py-2 rounded-full text-xs font-bold hover:bg-[#e64612] transition-colors flex items-center gap-1 shadow-sm whitespace-nowrap shrink-0"')

with open('src/components/Header.tsx', 'w') as f:
    f.write(c)
