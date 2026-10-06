with open('src/app/page.tsx', 'r') as f:
    c = f.read()

old_text = "Elektrik, Elektrik mühəndisliyi, Zəif axın sistemləri, PLC, SCADA, Ağıllı ev sistemləri üzrə ixtisaslaşmış peşəkar komanda."
new_text = "Elektrik, Zəif Axın və Ağıllı Ev sistemləri üzrə ixtisaslaşmış peşəkar komanda."

c = c.replace(old_text, new_text)

# Change text size: <p className="text-lg md:text-xl text-white/90 mb-10 max-w-2xl leading-relaxed">
# to <p className="text-base md:text-lg text-white/80 mb-8 max-w-2xl leading-relaxed">
c = c.replace('className="text-lg md:text-xl text-white/90 mb-10 max-w-2xl leading-relaxed"', 'className="text-base md:text-lg text-white/80 mb-8 max-w-xl leading-relaxed"')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)
