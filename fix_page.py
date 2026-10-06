with open('src/app/page.tsx', 'r') as f:
    content = f.read()

# 1. Header: NHN -> NHN Qrup
content = content.replace(
    '<span className="font-bold text-2xl tracking-tight">NHN</span>',
    '<span className="font-black text-2xl md:text-3xl tracking-tight bg-gradient-to-r from-[#ff4f14] to-[#131312] text-transparent bg-clip-text">NHN Qrup</span>'
)

# 2. Footer: Keep only Instagram
content = content.replace(
    '<a href="#" className="hover:text-[#ff4f14] transition-colors"><FaFacebook size={24} /></a>\n              <a href="#" className="hover:text-[#ff4f14] transition-colors"><FaLinkedin size={24} /></a>',
    ''
)
content = content.replace(
    'import { FaInstagram, FaFacebook, FaLinkedin } from "react-icons/fa";',
    'import { FaInstagram } from "react-icons/fa";'
)

# 3. Footer bottom right: Add NHN QRUP MMC
# Currently it is empty on the right because we removed it in the last rewrite?
# Let's check what's currently in the footer bottom.
# From the previous python script:
# <div className="max-w-7xl mx-auto pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-white/50 text-sm">
#   <p>© 2024 NHN Qrup. Bütün hüquqlar qorunur.</p>
# </div>
content = content.replace(
    '<div className="max-w-7xl mx-auto pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-white/50 text-sm">\n          <p>© 2024 NHN Qrup. Bütün hüquqlar qorunur.</p>\n        </div>',
    '<div className="max-w-7xl mx-auto pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-white/50 text-sm">\n          <p>© 2024 NHN Qrup. Bütün hüquqlar qorunur.</p>\n          <p className="mt-4 md:mt-0 font-medium tracking-wider">NHN QRUP MMC</p>\n        </div>'
)

with open('src/app/page.tsx', 'w') as f:
    f.write(content)

