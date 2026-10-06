with open('src/app/page.tsx', 'r') as f:
    c = f.read()

# 1. Hero
c = c.replace('Reliable Plumbing', 'NHN QRUP (NHN GROUP)')
c = c.replace('Solutions You Can Trust', 'Service and Training')
c = c.replace('From minor leaks to full installations, we provide fast, professional plumbing services. Available 24/7 for emergencies with guaranteed same-day service.', 'Elektrik, Elektrik mühəndisliyi, Zəif axın sistemləri, PLC, SCADA, Ağıllı ev sistemləri üzrə ixtisaslaşmış peşəkar komanda.')
c = c.replace('Get a Free Quote', 'Kurslara yazıl')
c = c.replace('Our Services', 'Servis xidməti')

# 2. Stats
c = c.replace('Years Experience', 'İllik Təcrübə')
c = c.replace('Projects Done', 'Tələbələr')
c = c.replace('Happy Clients', 'Məmnuniyyət')
c = c.replace('Emergency Support', 'Texniki Dəstək')

# 3. Services (Bizim Xidmətlərimiz)
# Wait, "Our Services" was replaced above, but let's check if the second one got replaced.
# In the hero it was "Our Services" button. In the section it was "Our Services" uppercase text.
# Let's fix that.
c = c.replace('Servis xidməti</p>', 'Bizim Xidmətlərimiz</p>') # If it replaced the label.
# Actually, the button had "Our Services". The label had "Our Services". Let's do exact match.
c = c.replace('<p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Servis xidməti</p>', '<p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Bizim Xidmətlərimiz</p>')
c = c.replace('<p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Our Services</p>', '<p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Bizim Xidmətlərimiz</p>')

c = c.replace('Comprehensive Plumbing Solutions', 'Professional Təlimlər və Servis')
c = c.replace('We offer a full range of plumbing services for residential and commercial properties, ensuring everything flows smoothly in your home or business.', 'NHN QRUP olaraq ən müasir texnologiyalarla həm peşəkar kurslar, həm də mühəndislik servisləri təklif edirik.')

# Cards
c = c.replace('Leak Detection', 'Elektrik Kursları')
c = c.replace('We use advanced technology to find and fix hidden leaks before they cause major damage.', 'Praktiki biliklər və real avadanlıqlar üzərində peşəkar elektrik təlimləri.')

c = c.replace('Drain Cleaning', 'Ağıllı Ev (Smart Home)')
c = c.replace('Fast and effective clearing of stubborn clogs to restore proper flow in your pipes.', 'Müasir texnologiyalarla evlərinizin tam avtomatlaşdırılması tədrisi.')

c = c.replace('Water Heater Services', 'PLC və SCADA')
c = c.replace('Installation, repair, and maintenance for traditional and tankless water heaters.', 'Sənaye avtomatlaşdırması və proqramlaşdırma üzrə dərslər.')

c = c.replace('Pipe Repair & Replacement', 'Generator Servisi')
c = c.replace('Expert solutions for broken, corroded, or burst pipes using minimally invasive methods.', 'Nasazlıqların diaqnostikası, təmir, quraşdırma və planlı texniki baxış.')

c = c.replace('Fixture Installation', 'Zəif Axın Sistemləri')
c = c.replace('Professional installation of faucets, toilets, sinks, and showers with guaranteed workmanship.', 'Təhlükəsizlik və zəif axın sistemlərinin tam quraşdırılması qaydaları.')

c = c.replace('Emergency Plumbing', 'Mühəndislik Həlləri')
c = c.replace('Round-the-clock emergency services for urgent plumbing issues that cannot wait.', 'Fiziki şəxslər və müəssisələr üçün kompleks mühəndislik və servis həlləri.')


# 4. Why Choose Us
c = c.replace('Why Choose Us', 'Niyə Bizi Seçməlisiniz')
c = c.replace('Built on Trust, Delivered with Precision', 'Təcrübə, Keyfiyyət və Güvən')
c = c.replace('When you choose Plumbzo, you\'re choosing a team dedicated to excellence. We pride ourselves on delivering top-notch plumbing services that are reliable, transparent, and hassle-free.', 'İstər tədris, istərsə də texniki servis sahəsində hər zaman ən yüksək keyfiyyət standartlarını təmin edirik.')

c = c.replace('Transparent Pricing', 'Peşəkar Təlimçilər')
c = c.replace('No hidden fees. You get a clear, upfront estimate before any work begins, so you know exactly what to expect.', 'Tədrisimiz çoxillik təcrübəyə malik mütəxəssislər tərəfindən aparılır.')

c = c.replace('Licensed Experts', 'Sonda Sertifikat')
c = c.replace('Our team consists of fully licensed, insured, and highly trained professionals who treat your property with respect.', 'Təlimləri uğurla başa vuran hər kəsə rəsmi sertifikat təqdim olunur.')

c = c.replace('Fast Response', 'İşlə Təminat')
c = c.replace('We understand plumbing emergencies can\'t wait. Our local technicians arrive promptly to minimize damage and delays or disruptions.', 'Məzunlarımıza karyera qurmaqda və uyğun iş tapmaqda birbaşa dəstək oluruq.')

c = c.replace('Guaranteed Quality', 'Operativ Servis')
c = c.replace('We stand behind our work with a 100% satisfaction guarantee. We\'re not done until the job is done right and you have assistance whenever needed.', 'Generator və elektrik problemlərinə yerində və anında peşəkar müdaxilə edirik.')

# 5. Video block
c = c.replace('See Our Team In Action', 'Praktiki Dərslərimiz')

# 6. How it works
c = c.replace('How It Works', 'Necə İşləyirik?')
c = c.replace('From Your Call to Problem Solved', 'Müraciətdən Nəticəyə Doğru')
c = c.replace('From the first call to the final fix - our process is designed to be easy, transparent, and hassle-free.', 'Servis və təlimlərə qoşulmaq çox sadə və şəffafdır.')

c = c.replace('Schedule Service', 'Müraciət')
c = c.replace('Book an appointment online or give us a call.', 'Bizimlə əlaqə saxlayın və ya onlayn qeydiyyatdan keçin.')

c = c.replace('Inspect the Issue', 'Diaqnostika / Baxış')
c = c.replace('Our licensed plumber identifies the problem and explains the solution.', 'Tələblərinizi və ya probleminizi peşəkarlarla birlikdə təhlil edirik.')

c = c.replace('Repair & Install', 'Praktika və Həll')
c = c.replace('We complete the work using quality materials and proven techniques.', 'Təlimlərdə real avadanlıqlarla işləyir, servisdə isə problemi yerində həll edirik.')

c = c.replace('Enjoy Peace of Mind', 'Təminat və Nəticə')
c = c.replace('Your plumbing is working properly, backed by reliable service.', 'Rəsmi sertifikat və ya zəmanətli xidmət əldə edərək işinizdən zövq alın.')

# 7. Emergency CTA
c = c.replace('EMERGENCY', 'TƏCİLİ')
c = c.replace('Need Emergency Plumbing Help?', 'Təcili Generator və ya Elektrik Servisi Lazımdır?')
c = c.replace('Available 24 Hours Every Day', '7/24 Operativ Texniki Dəstək Xidməti')
c = c.replace('CALL NOW', 'ZƏNG ET')

# 8. Featured Projects
c = c.replace('Featured Projects', 'Partnyorlarımız')
c = c.replace('See Our Recent <span className="text-[#ff4f14]">Projects</span>', 'Bizə Güvənən <span className="text-[#ff4f14]">Şirkətlər</span>')
c = c.replace('Take a look at the plumbing solutions we\'ve completed, from everyday repairs to full installations, all delivered with care and precision.', 'Azərbaycanda və regionda bir çox tanınmış şirkətlərlə rəsmi əməkdaşlıq edirik.')


with open('src/app/page.tsx', 'w') as f:
    f.write(c)

