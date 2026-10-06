import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# Add use client and motion
if '"use client"' not in content:
    content = '"use client";\n\n' + content
    content = content.replace('import Reveal from "@/components/Reveal";', 'import Reveal from "@/components/Reveal";\nimport { motion } from "framer-motion";')

# 1. Header Sticky & Scroll to top
# Header is currently: <header className="absolute top-0 w-full z-50 flex justify-center p-6">
content = content.replace(
    '<header className="absolute top-0 w-full z-50 flex justify-center p-6">',
    '<header className="fixed top-0 w-full z-50 flex justify-center p-6 transition-all duration-300">'
)

# Replace logo link to scroll to top
content = content.replace(
    '<div className="flex items-center gap-3">',
    '<a href="#top" className="flex items-center gap-3 cursor-pointer hover:opacity-80 transition-opacity">'
)
content = content.replace(
    '<span className="font-black text-2xl md:text-3xl tracking-tight bg-gradient-to-r from-[#ff4f14] to-[#131312] text-transparent bg-clip-text">NHN Qrup</span>\n          </div>',
    '<span className="font-black text-2xl md:text-3xl tracking-tight text-[#131312]">NHN Qrup</span>\n          </a>'
)

# 2. Header Links & CTA
content = content.replace(
    '<Link href="#">Vakansiyalar</Link>\n          </nav>\n          <button className="bg-[#ff4f14] text-white px-6 py-3 rounded-full font-semibold hover:bg-[#e64612] transition-colors whitespace-nowrap">\n            CV Göndər\n          </button>',
    '<Link href="#">Vakansiyalar</Link>\n            <Link href="#">CV Göndər</Link>\n          </nav>\n          <a href="#contact" className="bg-[#ff4f14] text-white px-6 py-3 rounded-full font-semibold hover:bg-[#e64612] transition-colors whitespace-nowrap">\n            ƏLAQƏ\n          </a>'
)

# Ana Sahife link to top
content = content.replace(
    '<Link href="#">Ana Səhifə</Link>',
    '<Link href="#top">Ana Səhifə</Link>'
)

# 3. Footer Links & Thickness
# Footer tag
content = content.replace(
    '<footer className="bg-[#131312] text-white pt-20 pb-10 px-6 lg:px-20">',
    '<footer id="contact" className="bg-[#131312] text-white pt-10 pb-6 px-6 lg:px-20">'
)
content = content.replace(
    '<div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 mb-16">',
    '<div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">'
)

# Footer links list
old_footer_links = """            <ul className="space-y-4 text-white/70">
              <li><Link href="#about" className="hover:text-white transition-colors">Haqqımızda</Link></li>
              <li><Link href="#contact" className="hover:text-white transition-colors">Əlaqə</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">Məxfilik siyasəti</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>
            </ul>"""

new_footer_links = """            <ul className="grid grid-cols-2 gap-4 text-white/70">
              <li><Link href="#top" className="hover:text-white transition-colors">Ana Səhifə</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">Məhsullar</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">Xidmətlər</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">Kurslar</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">Vakansiyalar</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">CV Göndər</Link></li>
              <li><Link href="#contact" className="hover:text-white transition-colors">Əlaqə</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>
            </ul>"""
content = content.replace(old_footer_links, new_footer_links)

# 4. Page wide animation and Top Anchor
# Wrap the return div with motion.div
content = content.replace(
    'return (\n    <div className="flex flex-col min-h-screen bg-[#f8f9f8]">',
    'return (\n    <motion.div \n      initial={{ opacity: 0 }}\n      animate={{ opacity: 1 }}\n      transition={{ duration: 1.2 }}\n      className="flex flex-col min-h-screen bg-[#f8f9f8]"\n    >\n      <div id="top" className="absolute top-0 w-full h-1" />'
)

# Close the motion div at the end
content = content.replace(
    '    </div>\n  );\n}',
    '    </motion.div>\n  );\n}'
)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

