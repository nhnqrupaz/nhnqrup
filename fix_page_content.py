import re

with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# 1. Top bar
c = c.replace('Available 24/7 Every Day - Fast, Reliable Plumbing Service.', '7/24 Peşəkar Elektrik və Generator Servisi - NHN QRUP.')
c = c.replace('Available 24/7 Every Day -Fast, NHN QRUP (NHN GROUP) Service and Training.', '7/24 Peşəkar Elektrik və Generator Servisi - NHN QRUP.')
c = c.replace('py-2 px-6', 'py-1.5 px-6')

# 2. Remove 4.9+ Reviews
reviews_pattern = r'<div className="bg-white/80 backdrop-blur-md rounded-full px-4 py-2 flex items-center gap-2 mb-6">.*?</div>'
c = re.sub(reviews_pattern, '', c, flags=re.DOTALL)

# 3. Subtitle
c = c.replace(
    'From emergency repairs to complete plumbing installations, our licensed \n            professionals deliver quality workmanship with transparent pricing and \n            same-day service.',
    'Elektrik, Elektrik mühəndisliyi, Zəif axın sistemləri, PLC, SCADA, Ağıllı ev sistemləri üzrə ixtisaslaşmış peşəkar komanda.'
)
c = c.replace(
    'From emergency repairs to complete plumbing installations, our licensed professionals deliver quality workmanship with transparent pricing and same-day service.',
    'Elektrik, Elektrik mühəndisliyi, Zəif axın sistemləri, PLC, SCADA, Ağıllı ev sistemləri üzrə ixtisaslaşmış peşəkar komanda.'
)

# 4. Niyə Bizi Seçməlisiniz
c = c.replace('Why Homeowners Trust Our <span className="text-[#ff4f14]">Plumbing Experts</span>', 'Niyə Məhz <span className="text-[#ff4f14]">NHN QRUP?</span>')
c = c.replace('We combine expert craftsmanship, quality materials, and exceptional customer care to deliver plumbing services you can trust.', 'Təcrübə, keyfiyyət və peşəkarlığı bir araya gətirərək mükəmməl xidmət göstəririk.')

c = c.replace('Licensed & Insured', 'Rəsmi və Zəmanətli')
c = c.replace('Fully licensed and insured plumbers delivering safe, reliable workmanship with complete peace of mind for every service visit.', 'Bütün servis və təlimlərimiz rəsmi zəmanətlə və yüksək keyfiyyət standartlarına uyğun aparılır.')

c = c.replace('Fast & Reliable Service', 'Operativ Texniki Servis')
c = c.replace('We value your time, arriving promptly and working efficiently to solve your plumbing issues without unnecessary delays or disruptions.', 'Nasazlıqların anında və yerində diaqnostikası, sürətli təmir və 7/24 xidmət.')

c = c.replace('Quality Workmanship', 'Peşəkar Təlimçilər')
c = c.replace('We use premium materials and proven techniques to deliver durable plumbing solutions built to perform reliably for years ahead.', 'Tədrisimiz çoxillik təcrübəyə malik, real istehsalat sahələrində çalışan mütəxəssislər tərəfindən aparılır.')

c = c.replace('24/7 Support', 'Sonda Rəsmi Sertifikat')
c = c.replace('Our dedicated team is available around the clock to handle emergencies, ensuring you receive rapid assistance whenever needed.', 'Təlimləri uğurla başa vuran hər kəsə rəsmi sertifikat təqdim olunur və işlə təminata dəstək göstərilir.')

c = c.replace('alt="Plumbing Expert"', 'alt="NHN QRUP Eksperti"')

# 5. Video Block (remove play button)
play_button_pattern = r'<div className="absolute inset-0 bg-black/30 flex items-center justify-center">.*?</div>\n          </div>'
c = re.sub(play_button_pattern, '</div>', c, flags=re.DOTALL)
c = c.replace('alt="Plumbing Work Video"', 'alt="Praktiki Dərslər"')

# 6. TƏCİLİ button to Link
emergency_button = """<button className="bg-white text-[#ff4f14] px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-gray-100 transition-colors">
              ZƏNG ET
              <ArrowRight size={20} />
            </button>"""
emergency_link = """<Link href="/contact" className="bg-white text-[#ff4f14] px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-gray-100 transition-colors">
              ZƏNG ET
              <ArrowRight size={20} />
            </Link>"""
c = c.replace(emergency_button, emergency_link)

# 7. Partnyorlarımız section (4 empty images side by side instead of 3 large ones)
old_partners = """<div className="grid md:grid-cols-3 gap-6">
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="rounded-3xl overflow-hidden h-80 group relative">
              <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=800&auto=format&fit=crop" alt="Partnyor Şirkət" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
            </div>
            </Reveal>
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="rounded-3xl overflow-hidden h-80 group relative">
              <img src="https://images.unsplash.com/photo-1620626011761-996317b8d101?q=80&w=800&auto=format&fit=crop" alt="Partnyor Şirkət" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
            </div>
            </Reveal>
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="rounded-3xl overflow-hidden h-80 group relative">
              <img src="https://images.unsplash.com/photo-1607472586893-edb57cb5b3b1?q=80&w=800&auto=format&fit=crop" alt="Partnyor Şirkət" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
            </div>
            </Reveal>
          </div>"""

new_partners = """<div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((i) => (
              <Reveal key={i} direction="up" delay={0.2 + (i * 0.1)} className="h-full">
                <div className="rounded-2xl overflow-hidden h-40 bg-gray-100 flex items-center justify-center border border-gray-200 hover:shadow-md transition-shadow">
                  {/* Empty placeholder for partner logo */}
                  <span className="text-gray-400 font-medium">Partnyor Logo</span>
                </div>
              </Reveal>
            ))}
          </div>"""
c = c.replace(old_partners, new_partners)

# Fix Header max-w in Header.tsx (Task 3)
with open('src/components/Header.tsx', 'r') as fh:
    ch = fh.read()
ch = ch.replace('max-w-4xl', 'max-w-5xl')
with open('src/components/Header.tsx', 'w') as fh:
    fh.write(ch)


with open('src/app/page.tsx', 'w') as f:
    f.write(c)

