with open('src/app/services/page.tsx', 'r') as f:
    c = f.read()

# Add Link import if missing (it might be missing)
if 'import Link' not in c:
    c = c.replace('import Reveal', 'import Link from "next/link";\nimport Reveal')

# Wrap the buttons with Link
c = c.replace('<button className="bg-[#131312] text-white px-8 py-4 rounded-full font-bold w-fit hover:bg-[#ff4f14] transition-colors flex items-center gap-2">\n                Kurslara Bax <ArrowRight size={20} />\n              </button>', '<Link href="/courses" className="bg-[#131312] text-white px-8 py-4 rounded-full font-bold w-fit hover:bg-[#ff4f14] transition-colors flex items-center gap-2">\n                Kurslara Bax <ArrowRight size={20} />\n              </Link>')

c = c.replace('<button className="bg-[#131312] text-white px-8 py-4 rounded-full font-bold w-fit hover:bg-[#ff4f14] transition-colors flex items-center gap-2">\n                Müraciət Et <ArrowRight size={20} />\n              </button>', '<Link href="/contact" className="bg-[#131312] text-white px-8 py-4 rounded-full font-bold w-fit hover:bg-[#ff4f14] transition-colors flex items-center gap-2">\n                Müraciət Et <ArrowRight size={20} />\n              </Link>')

with open('src/app/services/page.tsx', 'w') as f:
    f.write(c)

