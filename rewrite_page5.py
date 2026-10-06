import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

content = content.replace('import Link from "next/link";', 'import Link from "next/link";\nimport Reveal from "@/components/Reveal";')

# Find all <section> tags and replace their immediate contents with Reveal
# E.g. <section className="xyz"> \n <div...> -> <section className="xyz"> \n <Reveal> \n <div...>
# We can just look for </section> and add </Reveal> before it!

# 1. Hero: specific replacement
content = content.replace(
    '<div className="relative z-10 max-w-3xl text-white">', 
    '<Reveal direction="up" delay={0.2}>\n        <div className="relative z-10 max-w-3xl text-white">'
)
# Match the first section's closing tag
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 2. Stats
content = content.replace(
    '<div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">',
    '<Reveal direction="up" delay={0.2} className="w-full">\n        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">'
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 3. Services
content = content.replace(
    '<div className="max-w-7xl mx-auto">',
    '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto">',
    1 # Only the first occurrence
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 4. Why Choose Us
content = content.replace(
    '<div className="max-w-7xl mx-auto flex flex-col items-center text-center">',
    '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto flex flex-col items-center text-center">'
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 5. Video Block
content = content.replace(
    '<div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">',
    '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">'
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 6. How it works
content = content.replace(
    '<div className="max-w-7xl mx-auto text-center">',
    '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto text-center">'
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 7. Emergency CTA
content = content.replace(
    '<div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">',
    '<Reveal direction="up" delay={0.2} className="w-full">\n        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">'
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

# 8. Featured Projects
content = content.replace(
    '<div className="max-w-7xl mx-auto">',
    '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto">',
    1 # Only the second occurrence since the first is replaced above
)
content = content.replace(
    '      </section>',
    '        </Reveal>\n      </section>', 
    1
)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

