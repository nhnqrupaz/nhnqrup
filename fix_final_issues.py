with open('src/components/Header.tsx', 'r') as f:
    ch = f.read()

# Fix desktop nav: remove absolute, use flex-1 to distribute, add whitespace-nowrap
old_nav = 'className="hidden lg:flex items-center gap-5 xl:gap-6 text-[15px] xl:text-[16px] font-medium text-[#131312] absolute left-1/2 -translate-x-1/2"'
new_nav = 'className="hidden lg:flex items-center justify-center gap-4 xl:gap-6 text-[14px] xl:text-[16px] font-medium text-[#131312] flex-1 px-4 whitespace-nowrap"'
ch = ch.replace(old_nav, new_nav)

# Make sure the logo and contact button don't shrink too much
ch = ch.replace('className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity z-50"', 'className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity z-50 shrink-0"')
ch = ch.replace('className="hidden lg:block z-50"', 'className="hidden lg:block z-50 shrink-0"')

with open('src/components/Header.tsx', 'w') as f:
    f.write(ch)


with open('src/app/page.tsx', 'r') as f:
    cp = f.read()

# Mobile hero: increase text sizes and push button down
# H1: text-3xl -> text-4xl
cp = cp.replace('className="text-3xl md:text-6xl font-bold leading-[1.1] mb-4 md:mb-6"', 'className="text-4xl md:text-6xl font-bold leading-[1.1] mb-5 md:mb-6"')

# P: text-base -> text-lg, mb-14 -> mb-20
cp = cp.replace('className="text-base md:text-lg text-white/80 mb-14 md:mb-8 max-w-xl leading-relaxed"', 'className="text-lg text-white/80 mb-20 md:mb-8 max-w-xl leading-relaxed"')

# Pull up a bit less to balance the button push: -mt-16 -> -mt-12
cp = cp.replace('className="relative z-10 max-w-3xl text-white -mt-16 md:mt-0"', 'className="relative z-10 max-w-3xl text-white -mt-12 md:mt-0"')

with open('src/app/page.tsx', 'w') as f:
    f.write(cp)
