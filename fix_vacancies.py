with open('src/app/vacancies/page.tsx', 'r') as f:
    c = f.read()

if 'import Link' not in c:
    c = c.replace('import Reveal', 'import Link from "next/link";\nimport Reveal')

c = c.replace('<button className="shrink-0 bg-[#f8f9f8] text-[#131312] px-8 py-4 rounded-full font-bold group-hover:bg-[#ff4f14] group-hover:text-white transition-colors flex items-center justify-center gap-2">\n                  CV Göndər\n                  <ArrowRight size={20} />\n                </button>', '<Link href="/cv" className="shrink-0 bg-[#f8f9f8] text-[#131312] px-8 py-4 rounded-full font-bold group-hover:bg-[#ff4f14] group-hover:text-white transition-colors flex items-center justify-center gap-2">\n                  CV Göndər\n                  <ArrowRight size={20} />\n                </Link>')

with open('src/app/vacancies/page.tsx', 'w') as f:
    f.write(c)

