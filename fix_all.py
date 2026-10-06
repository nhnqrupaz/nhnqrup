with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Task 1: "Servis və Təlimlər" white text on orange bg
c = c.replace(
    'NHN QRUP<br /><span className="text-[#ff4f14]">Servis və Təlimlər</span>',
    'NHN QRUP<br /><span className="bg-[#ff4f14] text-white px-3 py-1 rounded-xl inline-block mt-2">Servis və Təlimlər</span>'
)

# Task 3: Separate and shrink stats bar on mobile
old_stats_section = '<section className="bg-[#ff4f14] py-8 md:py-16 px-6 lg:px-20 text-white">'
new_stats_section = '<section className="bg-[#ff4f14] py-6 md:py-16 px-4 md:px-6 lg:px-20 text-white rounded-3xl md:rounded-none mx-4 md:mx-0 mt-[-20px] md:mt-0 relative z-20 shadow-xl">'
c = c.replace(old_stats_section, new_stats_section)

# Shrink text in stats
c = c.replace('className="text-4xl md:text-5xl font-bold mb-2"', 'className="text-2xl md:text-5xl font-bold mb-1 md:mb-2"')
c = c.replace('className="text-white/90"', 'className="text-xs md:text-base text-white/90"')
c = c.replace('gap-8 divide-x', 'gap-4 md:gap-8 divide-x')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)


# Task 4: Footer Thickness
with open('src/components/Footer.tsx', 'r') as f:
    c = f.read()

c = c.replace('pt-16 pb-6 px-6 lg:px-20', 'pt-10 md:pt-16 pb-6 px-6 lg:px-20')
c = c.replace('gap-12 mb-12', 'gap-8 md:gap-12 mb-8 md:mb-12')
c = c.replace('mb-6', 'mb-4 md:mb-6')

with open('src/components/Footer.tsx', 'w') as f:
    f.write(c)


# Task 2: Horizontal Scroll lock
with open('src/app/globals.css', 'r') as f:
    c = f.read()

# Add standard mobile overflow lock
lock_css = """
html, body {
  max-width: 100vw;
  overflow-x: hidden;
}
"""
if 'overflow-x: hidden' not in c:
    c += lock_css
    with open('src/app/globals.css', 'w') as f:
        f.write(c)

