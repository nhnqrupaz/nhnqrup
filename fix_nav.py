with open('src/components/Header.tsx', 'r') as f:
    c = f.read()

# Restore absolute centering for Desktop Nav so it looks perfect on large screens
old_nav = 'className="hidden lg:flex items-center gap-6 text-[16px] font-medium text-[#131312]"'
new_nav = 'className="hidden lg:flex items-center gap-5 xl:gap-6 text-[15px] xl:text-[16px] font-medium text-[#131312] absolute left-1/2 -translate-x-1/2"'

c = c.replace(old_nav, new_nav)

with open('src/components/Header.tsx', 'w') as f:
    f.write(c)
