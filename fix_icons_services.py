with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Add imports
c = c.replace('import { \n  Phone,', 'import { \n  Zap, Home as HomeIcon, Monitor, Activity, Cpu, Lightbulb, \n  Phone,')

# Replace icons in Services section (which are Droplets, Search, etc.)
# I need to match the specific cards.
# Card 1: Elektrik Kursları
c = c.replace('<Search size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Elektrik Kursları</h3>', '<Zap size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Elektrik Kursları</h3>')

# Card 2: Ağıllı Ev
c = c.replace('<Droplets size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Ağıllı Ev (Smart Home)</h3>', '<HomeIcon size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Ağıllı Ev (Smart Home)</h3>')

# Card 3: PLC və SCADA
c = c.replace('<ShieldCheck size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">PLC və SCADA</h3>', '<Monitor size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">PLC və SCADA</h3>')

# Card 4: Generator Servisi
c = c.replace('<Wrench size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Generator Servisi</h3>', '<Activity size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Generator Servisi</h3>')

# Card 5: Zəif Axın Sistemləri
c = c.replace('<Clock size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Zəif Axın Sistemləri</h3>', '<Cpu size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Zəif Axın Sistemləri</h3>')

# Card 6: Mühəndislik Həlləri
c = c.replace('<Award size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Mühəndislik Həlləri</h3>', '<Lightbulb size={32} className="text-[#ff4f14]" />\n              </div>\n              <h3 className="text-xl font-bold mb-3">Mühəndislik Həlləri</h3>')


with open('src/app/page.tsx', 'w') as f:
    f.write(c)
