import re

with open('src/app/page.tsx', 'r') as f:
    content = f.read()

footer_replacement = """      {/* Footer */}
      <footer className="bg-[#131312] text-white pt-20 pb-10 px-6 lg:px-20">
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 mb-16">
          <div className="col-span-1 flex flex-col justify-center">
            <div className="flex items-center gap-4 mb-6">
              <img src="/Logo.png" alt="NHN Qrup" className="w-16 h-16 rounded-full object-cover bg-white p-1" />
              <span className="font-bold text-3xl tracking-tight italic">NHN Qrup</span>
            </div>
            <p className="text-white/70 mb-6 italic max-w-sm">
              Peşəkar xidmətlər, innovativ həllər və gələcəyə inamlı addım. Hər zaman sizinlə.
            </p>
          </div>
          
          <div className="col-span-1 md:justify-self-end flex flex-col">
            <h4 className="font-bold text-lg mb-6">Keçidlər</h4>
            <ul className="space-y-4 text-white/70">
              <li><Link href="#about" className="hover:text-white transition-colors">Haqqımızda</Link></li>
              <li><Link href="#contact" className="hover:text-white transition-colors">Əlaqə</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">Məxfilik siyasəti</Link></li>
              <li><Link href="#" className="hover:text-white transition-colors">İstifadə qaydaları</Link></li>
            </ul>
            <div className="flex items-center gap-6 mt-8 text-white/50">
              <a href="#" className="hover:text-[#ff4f14] transition-colors"><Instagram size={24} /></a>
              <a href="#" className="hover:text-[#ff4f14] transition-colors"><Facebook size={24} /></a>
              <a href="#" className="hover:text-[#ff4f14] transition-colors"><Linkedin size={24} /></a>
            </div>
          </div>
        </div>
        <div className="max-w-7xl mx-auto pt-8 border-t border-white/10 flex flex-col md:flex-row items-center justify-between text-white/50 text-sm">
          <p>© 2024 NHN Qrup. Bütün hüquqlar qorunur.</p>
        </div>
      </footer>"""

# The footer starts at {/* Footer */} and goes until </footer>.
# We will use regex to replace it.
new_content = re.sub(r'      {/\* Footer \*/}.*?</footer>', footer_replacement, content, flags=re.DOTALL)

with open('src/app/page.tsx', 'w') as f:
    f.write(new_content)

