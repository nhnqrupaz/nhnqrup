import re

with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# Replace Hero Section block entirely
old_hero = re.search(r'\{/\* Hero Section \*/\}.*?</section>', c, re.DOTALL).group(0)
new_hero = """{/* Hero Section */}
      <section className="relative pt-40 pb-32 px-6 lg:px-20 min-h-[90vh] flex items-center">
        {/* Background Image (Using placeholder) */}
        <div className="absolute inset-0 z-0">
          <img 
            src="https://images.unsplash.com/photo-1585704032915-c3400ca199e7?q=80&w=3270&auto=format&fit=crop" 
            alt="Hero Background" 
            className="w-full h-full object-cover"
          />
          {/* Light overlay to match design text readability on left side */}
          <div className="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent"></div>
        </div>

        <div className="relative z-10 max-w-3xl text-white">
          <div className="inline-flex items-center gap-2 border border-[#ff4f14] bg-[#ff4f14]/80 rounded-full px-5 py-1 mb-6 backdrop-blur-sm">
            <span className="text-sm font-medium">7/24 Peşəkar Elektrik və Generator Servisi</span>
          </div>
          
          <Reveal direction="up" delay={0.1}>
          <h1 className="text-4xl md:text-6xl font-bold leading-[1.1] mb-6">
            NHN QRUP<br /><span className="text-[#ff4f14]">Service and Training</span>
          </h1>
          </Reveal>
          
          <Reveal direction="up" delay={0.2}>
          <p className="text-lg md:text-xl text-white/90 mb-10 max-w-2xl leading-relaxed">
            Elektrik, Elektrik mühəndisliyi, Zəif axın sistemləri, PLC, SCADA, Ağıllı ev sistemləri üzrə ixtisaslaşmış peşəkar komanda.
          </p>
          </Reveal>
          
          <div className="flex flex-wrap items-center gap-4 mb-12">
            <Link href="/contact" className="bg-[#ff4f14] text-white px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-[#e64612] transition-colors">
              <Phone size={20} />
              Bizə Zəng Edin
            </Link>
          </div>
        </div>
      </section>"""
c = c.replace(old_hero, new_hero)

# Replace Stats Section entirely
old_stats = re.search(r'\{/\* Stats Section \*/\}.*?</section>', c, re.DOTALL).group(0)
new_stats = """{/* Stats Section */}
      <section className="bg-[#ff4f14] py-16 px-6 lg:px-20 text-white">
        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">
          <Reveal direction="up" delay={0.1}>
          <div>
            <div className="text-4xl md:text-5xl font-bold mb-2"><NumberCounter end={10} suffix="+" /></div>
            <div className="text-white/90">İllik Təcrübə</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.2}>
          <div>
            <div className="text-4xl md:text-5xl font-bold mb-2"><NumberCounter end={2500} suffix="+" /></div>
            <div className="text-white/90">Məzun və Tələbə</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.3}>
          <div>
            <div className="text-4xl md:text-5xl font-bold mb-2"><NumberCounter end={98} suffix="%" /></div>
            <div className="text-white/90">Müştəri Məmnuniyyəti</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.4}>
          <div>
            <div className="text-4xl md:text-5xl font-bold mb-2">24/7</div>
            <div className="text-white/90">Texniki Dəstək</div>
          </div>
          </Reveal>
        </div>
      </section>"""
c = c.replace(old_stats, new_stats)

with open('src/app/page.tsx', 'w') as f:
    f.write(c)
