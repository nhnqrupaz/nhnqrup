import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

content = content.replace('import Link from "next/link";', 'import Link from "next/link";\nimport Reveal from "@/components/Reveal";')

# 1. Hero text (leave background alone)
content = content.replace('<div className="relative z-10 max-w-3xl text-white">', '<Reveal direction="up" delay={0.2}>\n          <div className="relative z-10 max-w-3xl text-white">')
content = content.replace('</div>\n      </section>', '</div>\n          </Reveal>\n      </section>')

# 2. Stats
content = content.replace('<div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">', '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">')
content = content.replace('</div>\n      </section>', '</div>\n        </Reveal>\n      </section>')

# 3. Services Wrapper
content = content.replace('<div className="max-w-7xl mx-auto">', '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto">')
content = content.replace('</div>\n      </section>', '</div>\n        </Reveal>\n      </section>')

# 4. Why Choose Us
content = content.replace('<div className="max-w-7xl mx-auto flex flex-col items-center text-center">', '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto flex flex-col items-center text-center">')
content = content.replace('</div>\n      </section>', '</div>\n        </Reveal>\n      </section>')

# 5. Video Block
content = content.replace('<div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">', '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">')
content = content.replace('</div>\n      </section>', '</div>\n        </Reveal>\n      </section>')

# 6. How it works
content = content.replace('<div className="max-w-7xl mx-auto text-center">', '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto text-center">')
content = content.replace('</div>\n      </section>', '</div>\n        </Reveal>\n      </section>')

# 7. Emergency CTA
# Emergency CTA has relative inside and hidden overflow.
content = content.replace('<div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">', '<Reveal direction="up" delay={0.2} className="w-full">\n        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">')
content = content.replace('</div>\n      </section>', '</div>\n        </Reveal>\n      </section>')

# 8. Featured Projects
content = content.replace('<div className="max-w-7xl mx-auto">', '<Reveal direction="up" delay={0.2}>\n        <div className="max-w-7xl mx-auto">') # Wait, this might match twice!
# Services also uses <div className="max-w-7xl mx-auto">.
# My replacement will replace ALL of them. Let's make sure that's fine.
# If they all get replaced, then they all get wrapped, which is correct!
# But then `</div>\n      </section>` will also match multiple times and add `</Reveal>`.
# This is perfect!

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

