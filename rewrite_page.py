import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Add import for Reveal
if 'import Reveal' not in content:
    content = content.replace('import Link from "next/link";', 'import Link from "next/link";\nimport Reveal from "@/components/Reveal";')

# Replace sections with Reveal wrappers
# Section 1: Hero content
content = content.replace('<div className="relative z-10 max-w-3xl text-white">', '<Reveal delay={0.2} direction="up">\n        <div className="relative z-10 max-w-3xl text-white">')
content = content.replace('</div>\n      </section>\n\n      {/* Stats Section */}', '</div>\n        </Reveal>\n      </section>\n\n      {/* Stats Section */}')

# Replace section inner content for others
# Stats
content = content.replace('<div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">', '<Reveal delay={0.1} direction="up" className="w-full">\n        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">')
content = content.replace('</div>\n      </section>\n\n      {/* Services Section */}', '</div>\n        </Reveal>\n      </section>\n\n      {/* Services Section */}')

# Services header and cards
content = content.replace('<div className="mb-16 max-w-2xl">', '<Reveal direction="up" delay={0.1}>\n          <div className="mb-16 max-w-2xl">')
content = content.replace('</p>\n          </div>\n\n          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">', '</p>\n          </div>\n          </Reveal>\n\n          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">')

for i in range(1, 7):
    # Wrap each card
    content = content.replace(f'{{/* Card {i} */}}\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group">', f'{{/* Card {i} */}}\n            <Reveal direction="up" delay={{0.{i} + 0.1}}>\n            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col h-full group">')
    
# After the last card (Emergency Plumbing)
content = content.replace('</a>\n            </div>\n          </div>', '</a>\n            </div>\n            </Reveal>\n          </div>')
# Fix other cards closing tags
content = content.replace('</a>\n            </div>\n\n            {/* Card', '</a>\n            </div>\n            </Reveal>\n\n            {/* Card')

# Why choose us
content = content.replace('<div className="mb-16 max-w-3xl">', '<Reveal direction="up">\n          <div className="mb-16 max-w-3xl">')
content = content.replace('</p>\n          </div>\n\n          <div className="grid lg:grid-cols-3 gap-6 w-full">', '</p>\n          </div>\n          </Reveal>\n\n          <Reveal direction="up" delay={0.2}>\n          <div className="grid lg:grid-cols-3 gap-6 w-full">')
content = content.replace('</div>\n        </div>\n      </section>\n\n      {/* Video Block */}', '</div>\n          </Reveal>\n        </div>\n      </section>\n\n      {/* Video Block */}')

# Video Block
content = content.replace('<div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">', '<Reveal direction="up" delay={0.1}>\n        <div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">')
content = content.replace('</div>\n      </section>\n\n      {/* How It Works Section */}', '</div>\n        </Reveal>\n      </section>\n\n      {/* How It Works Section */}')

# How it works
content = content.replace('<div className="mb-16">', '<Reveal direction="up">\n          <div className="mb-16">')
content = content.replace('</p>\n          </div>\n\n          <div className="grid md:grid-cols-4 gap-8 relative">', '</p>\n          </div>\n          </Reveal>\n\n          <Reveal direction="up" delay={0.2}>\n          <div className="grid md:grid-cols-4 gap-8 relative">')
content = content.replace('</div>\n        </div>\n      </section>\n\n      {/* Emergency CTA */}', '</div>\n          </Reveal>\n        </div>\n      </section>\n\n      {/* Emergency CTA */}')

# Emergency CTA
content = content.replace('<div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">', '<Reveal direction="up" className="w-full">\n        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">')
content = content.replace('</div>\n      </section>\n\n      {/* Featured Projects Section */}', '</div>\n        </Reveal>\n      </section>\n\n      {/* Featured Projects Section */}')

# Featured Projects
content = content.replace('<div className="mb-16 max-w-2xl">', '<Reveal direction="up">\n          <div className="mb-16 max-w-2xl">')
content = content.replace('</p>\n          </div>\n          \n          <div className="grid md:grid-cols-3 gap-6">', '</p>\n          </div>\n          </Reveal>\n          \n          <Reveal direction="up" delay={0.2}>\n          <div className="grid md:grid-cols-3 gap-6">')
content = content.replace('</div>\n        </div>\n      </section>\n\n      {/* Footer */}', '</div>\n          </Reveal>\n        </div>\n      </section>\n\n      {/* Footer */}')


with open('src/app/page.tsx', 'w') as f:
    f.write(content)

