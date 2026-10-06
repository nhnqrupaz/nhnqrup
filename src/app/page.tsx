"use client";

import Image from "next/image";
import { 
  Zap, Home as HomeIcon, Monitor, Activity, Cpu, Lightbulb, Briefcase, 
  Phone, 
  Search, 
  Droplets, 
  ShieldCheck, 
  Clock, 
  Award, 
  Headphones,
  Wrench,
  Calendar,
  Siren,
  Play,
  ArrowRight,
  Star,
  MapPin,
  CheckCircle2
} from "lucide-react";
import Link from "next/link";
import Reveal from "@/components/Reveal";
import NumberCounter from "@/components/NumberCounter";
import { motion } from "framer-motion";
import { FaInstagram } from "react-icons/fa";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8]">
            {/* Navigation */}
      
      {/* Hero Section */}
      <section className="relative pt-32 pb-24 md:pt-40 md:pb-32 px-6 lg:px-20 min-h-[90vh] flex items-center">
        {/* Background Image (Using placeholder) */}
        <div className="absolute inset-0 z-0">
          <img 
            src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=3270&auto=format&fit=crop" 
            alt="Hero Background" 
            className="w-full h-full object-cover"
          />
          {/* Light overlay to match design text readability on left side */}
          <div className="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent"></div>
        </div>

        <div className="relative z-10 max-w-3xl text-white">
          <div className="inline-flex items-center gap-2 border border-[#ff4f14] bg-[#ff4f14]/80 rounded-full px-3 md:px-5 py-0.5 md:py-1 mb-4 md:mb-6 backdrop-blur-sm">
            <span className="text-xs md:text-sm font-medium">7/24 Peşəkar Elektrik və Generator Servisi</span>
          </div>
          
          <Reveal direction="up" delay={0.1}>
          <h1 className="text-3xl md:text-6xl font-bold leading-[1.1] mb-4 md:mb-6">
            NHN QRUP<br /><span className="text-[#ff4f14]">Servis və Təlimlər</span>
          </h1>
          </Reveal>
          
          <Reveal direction="up" delay={0.2}>
          <p className="text-base md:text-lg text-white/80 mb-8 max-w-xl leading-relaxed">
            Elektrik, Zəif Axın və Ağıllı Ev sistemləri üzrə ixtisaslaşmış peşəkar komanda.
          </p>
          </Reveal>
          
          <div className="flex flex-wrap items-center gap-4 mb-12">
            <Link href="/contact" className="bg-[#ff4f14] text-white px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-[#e64612] transition-colors">
              <Phone size={20} />
              Bizə Zəng Edin
            </Link>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="bg-[#ff4f14] py-8 md:py-12 md:py-16 px-6 lg:px-20 text-white">
        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">
          <Reveal direction="up" delay={0.1}>
          <div>
            <div className="text-4xl md:text-3xl md:text-5xl font-bold mb-2"><NumberCounter end={10} suffix="+" /></div>
            <div className="text-white/90">İllik Təcrübə</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.2}>
          <div>
            <div className="text-4xl md:text-3xl md:text-5xl font-bold mb-2"><NumberCounter end={500} suffix="+" /></div>
            <div className="text-white/90">Məzun və Tələbə</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.3}>
          <div>
            <div className="text-4xl md:text-3xl md:text-5xl font-bold mb-2"><NumberCounter end={98} suffix="%" /></div>
            <div className="text-white/90">Müştəri Məmnuniyyəti</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.4}>
          <div>
            <div className="text-4xl md:text-3xl md:text-5xl font-bold mb-2">24/7</div>
            <div className="text-white/90">Texniki Dəstək</div>
          </div>
          </Reveal>
        </div>
      </section>

      {/* Ana Səhifə Bölmələri (Kurslar, Servis, Vakansiyalar) */}
      <section className="py-16 md:py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-10 md:mb-16 max-w-2xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Fəaliyyət Sahələrimiz</p>
            <h2 className="text-3xl md:text-5xl font-bold mb-4 md:mb-6 text-[#131312]">
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
              <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mb-4 md:mb-6 shadow-sm">
                <Lightbulb size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-2xl font-bold mb-4">Peşəkar Kurslar</h3>
              <p className="text-gray-600 mb-4 md:mb-6 md:mb-8 flex-grow">
                Elektrik, Ağıllı Ev, PLC və Zəif Axın sistemləri üzrə praktiki dərslər və rəsmi sertifikatlar.
              </p>
              <Link href="/courses" className="inline-flex items-center gap-2 font-bold hover:text-[#ff4f14] transition-colors">
                Kurslara Bax <ArrowRight size={20} />
              </Link>
            </div>
            </Reveal>

            <Reveal direction="up" delay={0.3} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-8 flex flex-col group h-full border border-gray-100 hover:shadow-lg transition-all">
              <div className="w-16 h-16 bg-[#ff4f14] text-white rounded-2xl flex items-center justify-center mb-4 md:mb-6 shadow-sm">
                <Wrench size={32} />
              </div>
              <h3 className="text-2xl font-bold mb-4">Mühəndislik Servisi</h3>
              <p className="text-gray-600 mb-4 md:mb-6 md:mb-8 flex-grow">
                Generatorlar və elektrik sistemləri üçün 7/24 operativ diaqnostika, təmir və texniki baxış.
              </p>
              <Link href="/services" className="inline-flex items-center gap-2 font-bold hover:text-[#ff4f14] transition-colors">
                Servisə Bax <ArrowRight size={20} />
              </Link>
            </div>
            </Reveal>

            <Reveal direction="up" delay={0.4} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-8 flex flex-col group h-full border border-gray-100 hover:shadow-lg transition-all">
              <div className="w-16 h-16 bg-white rounded-2xl flex items-center justify-center mb-4 md:mb-6 shadow-sm">
                <Briefcase size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-2xl font-bold mb-4">Aktiv Vakansiyalar</h3>
              <p className="text-gray-600 mb-4 md:mb-6 md:mb-8 flex-grow">
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

      {/* Niyə Bizi Seçməlisiniz Section */}
      <section id="about" className="py-16 md:py-24 px-6 lg:px-20 bg-[#f8f9f8]">
        <div className="max-w-7xl mx-auto flex flex-col items-center text-center">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-10 md:mb-16 max-w-3xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Niyə Bizi Seçməlisiniz</p>
            <h2 className="text-3xl md:text-5xl font-bold mb-4 md:mb-6 text-[#131312]">
              Niyə Məhz <span className="text-[#ff4f14]">NHN QRUP?</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed max-w-2xl mx-auto">
              Təcrübə, keyfiyyət və peşəkarlığı bir araya gətirərək mükəmməl xidmət göstəririk.
            </p>
          </div>
          </Reveal>

          <div className="grid lg:grid-cols-3 gap-6 w-full">
            {/* Left Cards */}
            <Reveal direction="left" delay={0.2}>
            <div className="flex flex-col gap-6 h-full">
              <div className="bg-[#ff4f14] text-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-white/20 w-16 h-16 rounded-2xl flex items-center justify-center mb-4 md:mb-6">
                  <ShieldCheck size={32} className="text-white" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Rəsmi və Zəmanətli</h3>
                <p className="text-white/90 leading-relaxed">
                  Bütün servis və təlimlərimiz rəsmi zəmanətlə və yüksək keyfiyyət standartlarına uyğun aparılır.
                </p>
              </div>
              <div className="bg-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-[#f8f9f8] w-16 h-16 rounded-2xl flex items-center justify-center mb-4 md:mb-6">
                  <Clock size={32} className="text-[#ff4f14]" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Operativ Texniki Servis</h3>
                <p className="text-gray-600 leading-relaxed">
                  Nasazlıqların anında və yerində diaqnostikası, sürətli təmir və 7/24 xidmət.
                </p>
              </div>
            </div>
            </Reveal>

            {/* Middle Image */}
            <Reveal direction="up" delay={0.3}>
            <div className="rounded-3xl overflow-hidden h-[600px] lg:h-auto relative">
              <img 
                src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800&auto=format&fit=crop" 
                alt="NHN QRUP Eksperti" 
                className="w-full h-full object-cover"
              />
            </div>
            </Reveal>

            {/* Right Cards */}
            <Reveal direction="right" delay={0.4}>
            <div className="flex flex-col gap-6 h-full">
              <div className="bg-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-[#f8f9f8] w-16 h-16 rounded-2xl flex items-center justify-center mb-4 md:mb-6">
                  <Award size={32} className="text-[#ff4f14]" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Peşəkar Təlimçilər</h3>
                <p className="text-gray-600 leading-relaxed">
                  Tədrisimiz çoxillik təcrübəyə malik, real istehsalat sahələrində çalışan mütəxəssislər tərəfindən aparılır.
                </p>
              </div>
              <div className="bg-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-[#f8f9f8] w-16 h-16 rounded-2xl flex items-center justify-center mb-4 md:mb-6">
                  <Headphones size={32} className="text-[#ff4f14]" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Sonda Rəsmi Sertifikat</h3>
                <p className="text-gray-600 leading-relaxed">
                  Təlimləri uğurla başa vuran hər kəsə rəsmi sertifikat təqdim olunur və işlə təminata dəstək göstərilir.
                </p>
              </div>
            </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Video Block */}
      <section className="px-6 lg:px-20 pb-24 bg-[#f8f9f8]">
        <Reveal direction="up" delay={0.2}>
        <div className="max-w-7xl mx-auto rounded-[2rem] overflow-hidden relative h-[500px] md:h-[600px] group cursor-pointer">
          <img 
            src="https://images.unsplash.com/photo-1542013936693-884638332954?q=80&w=1600&auto=format&fit=crop" 
            alt="Praktiki Dərslər" 
            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          />
        </div>
        </Reveal>
      </section>

      {/* Necə İşləyirik? Section */}
      <section className="py-16 md:py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto text-center">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-10 md:mb-16">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Necə İşləyirik?</p>
            <h2 className="text-3xl md:text-5xl font-bold mb-4 md:mb-6 text-[#131312]">
              Peşəkar <span className="text-[#ff4f14]">Həll Yolları</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed max-w-2xl mx-auto">
              Servis və təlimlərə qoşulmaq çox sadə və şəffafdır.
            </p>
          </div>
          </Reveal>

          <div className="grid md:grid-cols-4 gap-8 relative">
            {/* Connecting Line */}
            <div className="hidden md:block absolute top-12 left-[10%] right-[10%] h-0.5 bg-gray-200 z-0"></div>

            {/* Step 1 */}
            <Reveal direction="up" delay={0.2}>
            <div className="relative z-10 flex flex-col items-center">
              <div className="w-24 h-24 bg-white rounded-full border-[6px] border-[#f8f9f8] flex items-center justify-center shadow-lg mb-4 md:mb-6">
                <Calendar size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-xl font-bold mb-3">Müraciət</h3>
              <p className="text-gray-600 text-center">
                Bizimlə əlaqə saxlayın və ya onlayn qeydiyyatdan keçin.
              </p>
            </div>
            </Reveal>

            {/* Step 2 */}
            <Reveal direction="up" delay={0.3}>
            <div className="relative z-10 flex flex-col items-center">
              <div className="w-24 h-24 bg-[#ff4f14] text-white rounded-full border-[6px] border-[#ffece6] flex items-center justify-center shadow-lg mb-4 md:mb-6">
                <Search size={32} />
              </div>
              <h3 className="text-xl font-bold mb-3">Diaqnostika / Baxış</h3>
              <p className="text-gray-600 text-center">
                Tələblərinizi və ya probleminizi peşəkarlarla birlikdə təhlil edirik.
              </p>
            </div>
            </Reveal>

            {/* Step 3 */}
            <Reveal direction="up" delay={0.4}>
            <div className="relative z-10 flex flex-col items-center">
              <div className="w-24 h-24 bg-white rounded-full border-[6px] border-[#f8f9f8] flex items-center justify-center shadow-lg mb-4 md:mb-6">
                <Wrench size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-xl font-bold mb-3">Praktika və Həll</h3>
              <p className="text-gray-600 text-center">
                Təlimlərdə real avadanlıqlarla işləyir, servisdə isə problemi yerində həll edirik.
              </p>
            </div>
            </Reveal>

            {/* Step 4 */}
            <Reveal direction="up" delay={0.5}>
            <div className="relative z-10 flex flex-col items-center">
              <div className="w-24 h-24 bg-white rounded-full border-[6px] border-[#f8f9f8] flex items-center justify-center shadow-lg mb-4 md:mb-6">
                <ShieldCheck size={32} className="text-[#ff4f14]" />
              </div>
              <h3 className="text-xl font-bold mb-3">Təminat və Nəticə</h3>
              <p className="text-gray-600 text-center">
                Rəsmi sertifikat və ya zəmanətli xidmət əldə edərək işinizdən zövq alın.
              </p>
            </div>
            </Reveal>
          </div>
        </div>
      </section>

      {/* Emergency CTA */}
      <section className="bg-[#ff4f14] py-12 md:py-16 px-6 lg:px-20 text-white overflow-hidden relative">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">
          <Reveal direction="left" delay={0.2}>
          <div className="max-w-2xl mb-4 md:mb-6 md:mb-8 md:mb-0">
            <div className="inline-flex items-center gap-2 bg-white/20 rounded-full px-4 py-2 mb-4 md:mb-6">
              <Siren size={20} />
              <span className="font-semibold tracking-wide">TƏCİLİ</span>
            </div>
            <h2 className="text-4xl md:text-3xl md:text-5xl font-bold mb-4">
              Təcili Generator və ya Elektrik Servisi Lazımdır?
            </h2>
            <div className="flex items-center gap-3 text-xl text-white/90 mb-4 md:mb-6 md:mb-8">
              <Clock size={24} />
              <span>7/24 Operativ Texniki Dəstək Xidməti</span>
            </div>
            <Link href="/contact" className="bg-white text-[#ff4f14] px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-gray-100 transition-colors">
              ZƏNG ET
              <ArrowRight size={20} />
            </Link>
          </div>
          </Reveal>
          
          <Reveal direction="right" delay={0.4}>
          <div className="relative w-72 h-72 hidden md:block">
            <div className="absolute inset-0 bg-white/10 rounded-full scale-110"></div>
            <img 
              src="https://images.unsplash.com/photo-1574739782594-db4ead022697?q=80&w=600&auto=format&fit=crop" 
              alt="Təcili Servis" 
              className="w-full h-full object-cover rounded-full border-8 border-[#ff4f14]"
            />
          </div>
          </Reveal>
        </div>
      </section>

      {/* Partnyorlarımız Section */}
      <section className="py-16 md:py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-10 md:mb-16 max-w-2xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Partnyorlarımız</p>
            <h2 className="text-3xl md:text-5xl font-bold mb-4 md:mb-6 text-[#131312]">
              Bizə Güvənən <span className="text-[#ff4f14]">Şirkətlər</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed">
              Azərbaycanda və regionda bir çox tanınmış şirkətlərlə rəsmi əməkdaşlıq edirik.
            </p>
          </div>
          </Reveal>
          
          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((i) => (
              <Reveal key={i} direction="up" delay={0.2 + (i * 0.1)} className="h-full">
                <div className="rounded-2xl overflow-hidden h-40 bg-gray-100 flex items-center justify-center border border-gray-200 hover:shadow-md transition-shadow">
                  {/* Empty placeholder for partner logo */}
                  <span className="text-gray-400 font-medium">Partnyor Logo</span>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </section>

    </div>
  );
}
