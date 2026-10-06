with open('src/components/Header.tsx', 'r') as f:
    c = f.read()

# Make the outer and inner padding thicker for mobile
c = c.replace('p-3 md:p-6', 'p-4 md:p-6')
c = c.replace('px-4 md:px-6 py-3 md:py-4', 'px-5 py-4')

# Fix the Logo text
old_logo = """<a href="/" onClick={handleHomeClick} className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity z-50">
          <img src="/LogoPNG.png" alt="NHN Qrup Logo" className="h-8 md:h-10 w-auto object-contain" />
          <span className="font-black text-lg md:text-2xl tracking-tight text-[#131312] hidden sm:block">NHN Qrup</span>
        </a>"""
new_logo = """<a href="/" onClick={handleHomeClick} className="flex items-center gap-2 cursor-pointer hover:opacity-80 transition-opacity z-50">
          <img src="/LogoPNG.png" alt="NHN Qrup Logo" className="h-8 md:h-10 w-auto object-contain" />
          <span className="font-black text-xl md:text-2xl tracking-tight text-[#131312]">NHN Qrup</span>
        </a>"""
c = c.replace(old_logo, new_logo)

# Remove the text from the mobile buttons
old_buttons = """{/* Mobile Buttons */}
        <div className="flex items-center gap-2 lg:hidden z-50 ml-auto">
          <span className="font-black text-lg tracking-tight text-[#131312] sm:hidden mr-2">NHN Qrup</span>
          <Link href="/contact" className="bg-[#ff4f14] text-white px-4 py-1.5 rounded-full text-xs font-bold hover:bg-[#e64612] transition-colors flex items-center gap-1 shadow-sm">
            <Phone size={12} />
            ƏLAQƏ
          </Link>
          <button 
            className="p-1 text-[#131312] ml-1" 
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X size={26} /> : <Menu size={26} />}
          </button>
        </div>"""
new_buttons = """{/* Mobile Buttons */}
        <div className="flex items-center gap-3 lg:hidden z-50 ml-auto">
          <Link href="/contact" className="bg-[#ff4f14] text-white px-4 py-2 rounded-full text-xs font-bold hover:bg-[#e64612] transition-colors flex items-center gap-1 shadow-sm">
            <Phone size={14} />
            ƏLAQƏ
          </Link>
          <button 
            className="p-1 text-[#131312]" 
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>"""
c = c.replace(old_buttons, new_buttons)

with open('src/components/Header.tsx', 'w') as f:
    f.write(c)
