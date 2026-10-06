import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Fix header spacing (gap-8 to gap-5) and links
# <nav className="hidden lg:flex gap-8 text-[15px] font-medium text-[#131312]">
content = content.replace(
    '<nav className="hidden lg:flex gap-8 text-[15px] font-medium text-[#131312]">',
    '<nav className="hidden lg:flex gap-5 text-[15px] font-medium text-[#131312]">'
)
# Max width of header background
content = content.replace(
    '<div className="bg-white rounded-full px-6 py-4 flex items-center justify-between w-full max-w-7xl shadow-sm">',
    '<div className="bg-white rounded-full px-6 py-4 flex items-center justify-between w-full max-w-5xl shadow-sm">'
)

# Header smooth scroll
content = content.replace(
    '<a href="#top" className="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity">',
    '<button onClick={() => window.scrollTo({ top: 0, behavior: \'smooth\' })} className="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity">'
)
content = content.replace(
    '<span className="font-black text-2xl md:text-3xl tracking-tight text-[#131312]">NHN Qrup</span>\n          </a>',
    '<span className="font-black text-2xl md:text-3xl tracking-tight text-[#131312]">NHN Qrup</span>\n          </button>'
)

# Ana Sahife smooth scroll
content = content.replace(
    '<Link href="#top">Ana Səhifə</Link>',
    '<button onClick={() => window.scrollTo({ top: 0, behavior: \'smooth\' })} className="hover:text-[#ff4f14] transition-colors">Ana Səhifə</button>'
)

# Update other links in header
content = content.replace('<Link href="#">Məhsullar</Link>', '<Link href="/products" className="hover:text-[#ff4f14] transition-colors">Məhsullar</Link>')
content = content.replace('<Link href="#">Xidmətlər</Link>', '<Link href="/services" className="hover:text-[#ff4f14] transition-colors">Xidmətlər</Link>')
content = content.replace('<Link href="#">Kurslar</Link>', '<Link href="/courses" className="hover:text-[#ff4f14] transition-colors">Kurslar</Link>')
content = content.replace('<Link href="#">Vakansiyalar</Link>', '<Link href="/vacancies" className="hover:text-[#ff4f14] transition-colors">Vakansiyalar</Link>')
content = content.replace('<Link href="#">CV Göndər</Link>', '<Link href="/cv" className="hover:text-[#ff4f14] transition-colors">CV Göndər</Link>')
content = content.replace('<a href="#contact" className="bg-[#ff4f14] text-white px-6 py-3 rounded-full font-semibold hover:bg-[#e64612] transition-colors whitespace-nowrap">\n            ƏLAQƏ\n          </a>', '<Link href="/contact" className="bg-[#ff4f14] text-white px-6 py-3 rounded-full font-semibold hover:bg-[#e64612] transition-colors whitespace-nowrap">\n            ƏLAQƏ\n          </Link>')

# Footer updates
# Move Instagram to left (under description)
# Old left footer:
# Peşəkar xidmətlər, innovativ həllər və gələcəyə inamlı addım. Hər zaman sizinlə.
#             </p>
#           </div>
new_left = """Peşəkar xidmətlər, innovativ həllər və gələcəyə inamlı addım. Hər zaman sizinlə.
            </p>
            <div className="flex items-center gap-4 text-white/50">
              <a href="#" className="hover:text-[#ff4f14] transition-colors"><FaInstagram size={28} /></a>
            </div>
          </div>"""
content = content.replace('Peşəkar xidmətlər, innovativ həllər və gələcəyə inamlı addım. Hər zaman sizinlə.\n            </p>\n          </div>', new_left)

# Remove Instagram from right
content = content.replace('<div className="flex items-center gap-6 mt-8 text-white/50">\n              <a href="#" className="hover:text-[#ff4f14] transition-colors"><FaInstagram size={24} /></a>\n            </div>', '')

# Update footer links to actual paths
content = content.replace('<Link href="#about" className="hover:text-white transition-colors">Haqqımızda</Link>', '<Link href="/about" className="hover:text-white transition-colors">Haqqımızda</Link>')
content = content.replace('<Link href="#contact" className="hover:text-white transition-colors">Əlaqə</Link>', '<Link href="/contact" className="hover:text-white transition-colors">Əlaqə</Link>')


with open('src/app/page.tsx', 'w') as f:
    f.write(content)

