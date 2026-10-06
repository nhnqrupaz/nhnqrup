with open('src/components/Header.tsx', 'r') as f:
    c = f.read()

# Remove the absolute positioning that causes overlap
c = c.replace('className="hidden lg:flex gap-5 text-[16px] font-medium text-[#131312] absolute left-1/2 -translate-x-1/2"', 'className="hidden lg:flex items-center gap-6 text-[16px] font-medium text-[#131312]"')

with open('src/components/Header.tsx', 'w') as f:
    f.write(c)
