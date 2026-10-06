import re

with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Fix alt tags
c = c.replace('alt="Emergency Plumber"', 'alt="Təcili Servis"')
c = c.replace('alt="Project 1"', 'alt="Partnyor Şirkət"')
c = c.replace('alt="Project 2"', 'alt="Partnyor Şirkət"')
c = c.replace('alt="Project 3"', 'alt="Partnyor Şirkət"')

# The Services section starts at:
# <section className="py-24 px-6 lg:px-20 bg-white">
#           <div className="mb-16 max-w-2xl">
#             <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Bizim Xidmətlərimiz</p>
# ...
# And ends before:
#       {/* Niyə Bizi Seçməlisiniz Section */}

new_services_section = """      {/* Ana Səhifə Bölmələri (Kurslar, Servis, Vakansiyalar) */}
      <section className="py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-16 max-w-2xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Fəaliyyət Sahələrimiz</p>
            <h2 className="text-5xl font-bold mb-6 text-[#131312]">
              Professional <span className="text-[#ff4f14]">Təlimlər və Servis</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed">
              NHN QRUP olaraq ən müasir texnologiyalarla həm peşəkar kurslar, həm mühəndislik servisləri, həm də karyera imkanları təklif edirik.
            </p>
          </div>
          </Reveal>

          <div className="grid md:grid-cols-3 gap-8">
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-8 flex flex-col group h-full border border-gray-100 hover:shadow-lg transition-all">
              <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                <Lightbulb size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-2xl font-bold mb-4">Peşəkar Kurslar</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Elektrik, Ağıllı Ev, PLC və Zəif Axın sistemləri üzrə praktiki dərslər və rəsmi sertifikatlar.
              </p>
              <Link href="/courses" className="inline-flex items-center gap-2 font-bold hover:text-[#ff4f14] transition-colors">
                Kurslara Bax <ArrowRight size={20} />
              </Link>
            </div>
            </Reveal>

            <Reveal direction="up" delay={0.3} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-8 flex flex-col group h-full border border-gray-100 hover:shadow-lg transition-all">
              <div className="w-16 h-16 bg-[#ff4f14] text-white rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                <Wrench size={32} />
              </div>
              <h3 className="text-2xl font-bold mb-4">Mühəndislik Servisi</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Generatorlar və elektrik sistemləri üçün 7/24 operativ diaqnostika, təmir və texniki baxış.
              </p>
              <Link href="/services" className="inline-flex items-center gap-2 font-bold hover:text-[#ff4f14] transition-colors">
                Servisə Bax <ArrowRight size={20} />
              </Link>
            </div>
            </Reveal>

            <Reveal direction="up" delay={0.4} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-8 flex flex-col group h-full border border-gray-100 hover:shadow-lg transition-all">
              <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mb-6 shadow-sm">
                <Briefcase size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-2xl font-bold mb-4">Aktiv Vakansiyalar</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Komandamıza qoşulmaq, karyeranızı bizimlə qurmaq və inkişaf etmək üçün açıq iş yerləri.
              </p>
              <Link href="/vacancies" className="inline-flex items-center gap-2 font-bold hover:text-[#ff4f14] transition-colors">
                Müraciət Et <ArrowRight size={20} />
              </Link>
            </div>
            </Reveal>
          </div>
        </div>
      </section>

"""

# We need to replace everything from `      {/* Services Section */}` down to `      {/* Niyə Bizi Seçməlisiniz Section */}`
pattern = re.compile(r'      {/\* Services Section \*/}.*?      {/\* Niyə Bizi Seçməlisiniz Section \*/}', re.DOTALL)
c = pattern.sub(new_services_section + '      {/* Niyə Bizi Seçməlisiniz Section */}', c)

# Add Briefcase icon if not present
if 'Briefcase' not in c:
    c = c.replace('Lightbulb, \n  Phone,', 'Lightbulb, Briefcase, \n  Phone,')

with open('src/app/page.tsx', 'w') as f:
    f.write(c)

