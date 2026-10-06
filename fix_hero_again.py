import re
with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Pattern to remove the Kurslara Yazıl button completely
# <button className="bg-[#ff4f14] text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-[#e64612] transition-colors">
#   Kurslara Yazıl
# </button>
pattern = r'<button className="bg-\[#ff4f14\].*?Kurslara Yazıl\s*</button>'
c = re.sub(pattern, '', c, flags=re.DOTALL)

# And wrap the Bizə Zəng Edin button with Link to /contact
c = c.replace('<button className="bg-white text-[#131312] px-8 py-4 rounded-full font-semibold text-lg flex items-center gap-2 hover:bg-gray-100 transition-colors">\n              <Phone size={20} />\n              Bizə Zəng Edin\n            </button>', '<Link href="/contact" className="bg-[#ff4f14] text-white px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-[#e64612] transition-colors">\n              <Phone size={20} />\n              Bizə Zəng Edin\n            </Link>')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

