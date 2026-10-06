with open('src/app/courses/page.tsx', 'r') as f:
    c = f.read()

if 'import Link' not in c:
    c = c.replace('import Reveal', 'import Link from "next/link";\nimport Reveal')

old_button = """<button className="w-full bg-[#131312] text-white py-4 rounded-full font-bold hover:bg-[#ff4f14] transition-colors flex items-center justify-center gap-2">
                    Müraciət Et
                    <ArrowRight size={20} />
                  </button>"""

new_button = """<Link href={`/cv?job=${encodeURIComponent(course.title)}`} className="w-full bg-[#131312] text-white py-4 rounded-full font-bold hover:bg-[#ff4f14] transition-colors flex items-center justify-center gap-2">
                    Müraciət Et
                    <ArrowRight size={20} />
                  </Link>"""

c = c.replace(old_button, new_button)

with open('src/app/courses/page.tsx', 'w') as f:
    f.write(c)

