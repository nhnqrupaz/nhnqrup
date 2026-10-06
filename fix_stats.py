with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Add import
if 'NumberCounter' not in c:
    c = c.replace('import Reveal from "@/components/Reveal";', 'import Reveal from "@/components/Reveal";\nimport NumberCounter from "@/components/NumberCounter";')

# Replace stats
# 1. <h3 className="text-4xl md:text-5xl font-black mb-2">10+</h3>
c = c.replace('<h3 className="text-4xl md:text-5xl font-black mb-2">10+</h3>', '<h3 className="text-4xl md:text-5xl font-black mb-2"><NumberCounter end={10} suffix="+" /></h3>')
# 2. <h3 className="text-4xl md:text-5xl font-black mb-2">2.5k+</h3> -> we can use end=2500, but text is 2.5k. Let's just animate to 2500 or 2.5
c = c.replace('<h3 className="text-4xl md:text-5xl font-black mb-2">2.5k+</h3>', '<h3 className="text-4xl md:text-5xl font-black mb-2"><NumberCounter end={2500} suffix="+" /></h3>')
c = c.replace('2.5k+', '2500+') # Just in case
# 3. <h3 className="text-4xl md:text-5xl font-black mb-2">98%</h3>
c = c.replace('<h3 className="text-4xl md:text-5xl font-black mb-2">98%</h3>', '<h3 className="text-4xl md:text-5xl font-black mb-2"><NumberCounter end={98} suffix="%" /></h3>')
# 4. <h3 className="text-4xl md:text-5xl font-black mb-2">24/7</h3>
# 24/7 is a string, we don't animate it (or we can animate 24). Let's leave 24/7 static since it's not a counter.

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

