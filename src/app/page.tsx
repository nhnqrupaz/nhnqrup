"use client";

import Image from "next/image";
import { 
  Zap, Home as HomeIcon, Monitor, Activity, Cpu, Lightbulb, 
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
import { motion } from "framer-motion";
import { FaInstagram } from "react-icons/fa";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8]">
            {/* Navigation */}
      
      {/* Hero Section */}
      <section className="relative pt-40 pb-32 px-6 lg:px-20 min-h-[90vh] flex items-center">
        {/* Background Image (Using placeholder) */}
        <div className="absolute inset-0 z-0">
          <img 
            src="https://images.unsplash.com/photo-1585704032915-c3400ca199e7?q=80&w=3270&auto=format&fit=crop" 
            alt="Hero Plumbing" 
            className="w-full h-full object-cover"
          />
          {/* Light overlay to match design text readability on left side */}
          <div className="absolute inset-0 bg-gradient-to-r from-black/60 to-transparent"></div>
        </div>

        <div className="relative z-10 max-w-3xl text-white">
          <div className="inline-flex items-center gap-2 border border-white/30 rounded-full px-4 py-1.5 mb-6 backdrop-blur-sm">
            <span className="text-sm font-medium">Available 24/7 Every Day</span>
          </div>
          
          <Reveal direction="up" delay={0.1}>
          <h1 className="text-5xl md:text-7xl font-bold leading-[1.1] mb-6">
            Fast, NHN QRUP (NHN GROUP)<br />Service and Training
          </h1>
          </Reveal>
          
          <Reveal direction="up" delay={0.2}>
          <p className="text-lg md:text-xl text-white/90 mb-10 max-w-2xl leading-relaxed">
            From emergency repairs to complete plumbing installations, our licensed 
            professionals deliver quality workmanship with transparent pricing and 
            same-day service.
          </p>
          </Reveal>
          
          <div className="flex flex-wrap items-center gap-4 mb-12">
            <button className="bg-[#ff4f14] text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-[#e64612] transition-colors">
              Get Your Free Quote
            </button>
            <button className="bg-white text-[#131312] px-8 py-4 rounded-full font-semibold text-lg flex items-center gap-2 hover:bg-gray-100 transition-colors">
              <Phone size={20} />
              Call Now
            </button>
          </div>

          <div className="flex items-center gap-4">
            <div className="flex -space-x-3">
              {[1, 2, 3, 4].map((i) => (
                <img 
                  key={i}
                  src={`https://i.pravatar.cc/100?img=${i + 10}`} 
                  alt="Reviewer" 
                  className="w-12 h-12 rounded-full border-2 border-white object-cover"
                />
              ))}
            </div>
            <div>
              <div className="flex gap-1 text-white mb-1">
                {[1, 2, 3, 4, 5].map((i) => (
                  <Star key={i} size={16} fill="currentColor" />
                ))}
              </div>
              <p className="text-sm font-medium text-white/90">4.9+ Reviews</p>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="bg-[#ff4f14] py-16 px-6 lg:px-20 text-white">
        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 divide-x divide-white/20 text-center">
          <Reveal direction="up" delay={0.1}>
          <div>
            <div className="text-5xl font-bold mb-2">10+</div>
            <div className="text-white/90">Years of Experience</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.2}>
          <div>
            <div className="text-5xl font-bold mb-2">2.5k+</div>
            <div className="text-white/90">Projects Completed</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.3}>
          <div>
            <div className="text-5xl font-bold mb-2">98%</div>
            <div className="text-white/90">Customer Satisfaction</div>
          </div>
          </Reveal>
          <Reveal direction="up" delay={0.4}>
          <div>
            <div className="text-5xl font-bold mb-2">24/7</div>
            <div className="text-white/90">Texniki Dəstək</div>
          </div>
          </Reveal>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-16 max-w-2xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Bizim Xidmətlərimiz</p>
            <h2 className="text-5xl font-bold mb-6 text-[#131312]">
              Plumbing Solutions Built <span className="text-[#ff4f14]">Around You</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed">
              From quick fixes to full installations, our expert plumbers deliver reliable, 
              high-quality solutions for your home or business.
            </p>
          </div>
          </Reveal>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {/* Card 1 */}
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">
              <div className="rounded-2xl overflow-hidden mb-6 relative h-64">
                <img src="https://images.unsplash.com/photo-1607472586893-edb57cb5b3b1?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="Elektrik Kursları" />
                <div className="absolute bottom-4 left-4 bg-white w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg">
                  <Search className="text-[#ff4f14]" size={28} />
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">Elektrik Kursları</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                We detect hidden leaks quickly to protect your home, prevent costly water damage, and restore peace of mind with confidence.
              </p>
              <a href="#" className="flex items-center justify-between text-[#ff4f14] font-semibold group-hover:text-[#e64612]">
                Get a Quote
                <span className="bg-[#ff4f14] text-white w-10 h-10 rounded-full flex items-center justify-center group-hover:bg-[#e64612]">
                  <ArrowRight size={20} />
                </span>
              </a>
            </div>
            </Reveal>

            {/* Card 2 */}
            <Reveal direction="up" delay={0.3} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">
              <div className="rounded-2xl overflow-hidden mb-6 relative h-64">
                <img src="https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="Ağıllı Ev (Smart Home)" />
                <div className="absolute bottom-4 left-4 bg-white w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg">
                  <Droplets className="text-[#ff4f14]" size={28} />
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">Ağıllı Ev (Smart Home)</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                We clear stubborn clogs and buildup to keep your drains flowing efficiently and prevent future plumbing problems year after year.
              </p>
              <a href="#" className="flex items-center justify-between text-[#ff4f14] font-semibold group-hover:text-[#e64612]">
                Get a Quote
                <span className="bg-[#ff4f14] text-white w-10 h-10 rounded-full flex items-center justify-center group-hover:bg-[#e64612]">
                  <ArrowRight size={20} />
                </span>
              </a>
            </div>
            </Reveal>

            {/* Card 3 */}
            <Reveal direction="up" delay={0.4} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">
              <div className="rounded-2xl overflow-hidden mb-6 relative h-64">
                <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="Water Heater Repair" />
                <div className="absolute bottom-4 left-4 bg-white w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg">
                  <Wrench className="text-[#ff4f14]" size={28} />
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">Water Heater Repair</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Enjoy fast reliable water heater repairs that restore consistent hot water for your home with lasting performance and comfort daily.
              </p>
              <a href="#" className="flex items-center justify-between text-[#ff4f14] font-semibold group-hover:text-[#e64612]">
                Get a Quote
                <span className="bg-[#ff4f14] text-white w-10 h-10 rounded-full flex items-center justify-center group-hover:bg-[#e64612]">
                  <ArrowRight size={20} />
                </span>
              </a>
            </div>
            </Reveal>

            {/* Card 4 */}
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">
              <div className="rounded-2xl overflow-hidden mb-6 relative h-64">
                <img src="https://images.unsplash.com/photo-1505798577917-a65157d3320a?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="Pipe Installation" />
                <div className="absolute bottom-4 left-4 bg-white w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg">
                  <Wrench className="text-[#ff4f14]" size={28} />
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">Pipe Installation</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Professional pipe installation for durable plumbing systems that improve water flow and provide reliable performance for years ahead always.
              </p>
              <a href="#" className="flex items-center justify-between text-[#ff4f14] font-semibold group-hover:text-[#e64612]">
                Get a Quote
                <span className="bg-[#ff4f14] text-white w-10 h-10 rounded-full flex items-center justify-center group-hover:bg-[#e64612]">
                  <ArrowRight size={20} />
                </span>
              </a>
            </div>
            </Reveal>

            {/* Card 5 */}
            <Reveal direction="up" delay={0.3} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">
              <div className="rounded-2xl overflow-hidden mb-6 relative h-64">
                <img src="https://images.unsplash.com/photo-1620626011761-996317b8d101?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="Bathroom Plumbing" />
                <div className="absolute bottom-4 left-4 bg-white w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg">
                  <Droplets className="text-[#ff4f14]" size={28} />
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">Bathroom Plumbing</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Complete bathroom plumbing services for renovations, repairs, and fixture upgrades that enhance comfort and functionality.
              </p>
              <a href="#" className="flex items-center justify-between text-[#ff4f14] font-semibold group-hover:text-[#e64612]">
                Get a Quote
                <span className="bg-[#ff4f14] text-white w-10 h-10 rounded-full flex items-center justify-center group-hover:bg-[#e64612]">
                  <ArrowRight size={20} />
                </span>
              </a>
            </div>
            </Reveal>

            {/* Card 6 */}
            <Reveal direction="up" delay={0.4} className="h-full">
            <div className="bg-[#f8f9f8] rounded-3xl p-6 flex flex-col group h-full">
              <div className="rounded-2xl overflow-hidden mb-6 relative h-64">
                <img src="https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=1000&auto=format&fit=crop" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="Mühəndislik Həlləri" />
                <div className="absolute bottom-4 left-4 bg-white w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg">
                  <Siren className="text-[#ff4f14]" size={28} />
                </div>
              </div>
              <h3 className="text-2xl font-bold mb-3">Mühəndislik Həlləri</h3>
              <p className="text-gray-600 mb-8 flex-grow">
                Fast 24/7 emergency plumbing services for urgent repairs, minimizing damage and restoring your home's safety with rapid expert support anytime.
              </p>
              <a href="#" className="flex items-center justify-between text-[#ff4f14] font-semibold group-hover:text-[#e64612]">
                Get a Quote
                <span className="bg-[#ff4f14] text-white w-10 h-10 rounded-full flex items-center justify-center group-hover:bg-[#e64612]">
                  <ArrowRight size={20} />
                </span>
              </a>
            </div>
            </Reveal>
          </div>
        </div>
      </section>
      {/* Niyə Bizi Seçməlisiniz Section */}
      <section id="about" className="py-24 px-6 lg:px-20 bg-[#f8f9f8]">
        <div className="max-w-7xl mx-auto flex flex-col items-center text-center">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-16 max-w-3xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Niyə Bizi Seçməlisiniz</p>
            <h2 className="text-5xl font-bold mb-6 text-[#131312]">
              Why Homeowners Trust Our <span className="text-[#ff4f14]">Plumbing Experts</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed max-w-2xl mx-auto">
              We combine expert craftsmanship, quality materials, and exceptional customer care to deliver plumbing services you can trust.
            </p>
          </div>
          </Reveal>

          <div className="grid lg:grid-cols-3 gap-6 w-full">
            {/* Left Cards */}
            <Reveal direction="left" delay={0.2}>
            <div className="flex flex-col gap-6 h-full">
              <div className="bg-[#ff4f14] text-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-white/20 w-16 h-16 rounded-2xl flex items-center justify-center mb-6">
                  <ShieldCheck size={32} className="text-white" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Licensed & Insured</h3>
                <p className="text-white/90 leading-relaxed">
                  Fully licensed and insured plumbers delivering safe, reliable workmanship with complete peace of mind for every service visit.
                </p>
              </div>
              <div className="bg-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-[#f8f9f8] w-16 h-16 rounded-2xl flex items-center justify-center mb-6">
                  <Clock size={32} className="text-[#ff4f14]" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Fast & Reliable Service</h3>
                <p className="text-gray-600 leading-relaxed">
                  We value your time, arriving promptly and working efficiently to solve your plumbing issues without unnecessary delays or disruptions.
                </p>
              </div>
            </div>
            </Reveal>

            {/* Middle Image */}
            <Reveal direction="up" delay={0.3}>
            <div className="rounded-3xl overflow-hidden h-[600px] lg:h-auto relative">
              <img 
                src="https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=800&auto=format&fit=crop" 
                alt="Plumbing Expert" 
                className="w-full h-full object-cover"
              />
            </div>
            </Reveal>

            {/* Right Cards */}
            <Reveal direction="right" delay={0.4}>
            <div className="flex flex-col gap-6 h-full">
              <div className="bg-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-[#f8f9f8] w-16 h-16 rounded-2xl flex items-center justify-center mb-6">
                  <Award size={32} className="text-[#ff4f14]" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Quality Workmanship</h3>
                <p className="text-gray-600 leading-relaxed">
                  We use premium materials and proven techniques to deliver durable plumbing solutions built to perform reliably for years ahead.
                </p>
              </div>
              <div className="bg-white rounded-3xl p-8 flex-1 text-left flex flex-col justify-center">
                <div className="bg-[#f8f9f8] w-16 h-16 rounded-2xl flex items-center justify-center mb-6">
                  <Headphones size={32} className="text-[#ff4f14]" />
                </div>
                <h3 className="text-2xl font-bold mb-4">24/7 Support</h3>
                <p className="text-gray-600 leading-relaxed">
                  Our dedicated team is available around the clock to handle emergencies, ensuring you receive rapid assistance whenever needed.
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
            alt="Plumbing Work Video" 
            className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
          />
          <div className="absolute inset-0 bg-black/30 flex items-center justify-center">
            <div className="bg-white w-24 h-24 rounded-full flex items-center justify-center pl-2 shadow-2xl transition-transform duration-300 group-hover:scale-110">
              <Play size={40} className="text-[#ff4f14]" />
            </div>
          </div>
        </div>
        </Reveal>
      </section>

      {/* Necə İşləyirik? Section */}
      <section className="py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto text-center">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-16">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Necə İşləyirik?</p>
            <h2 className="text-5xl font-bold mb-6 text-[#131312]">
              From Your Call to <span className="text-[#ff4f14]">Problem Solved</span>
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
              <div className="w-24 h-24 bg-white rounded-full border-[6px] border-[#f8f9f8] flex items-center justify-center shadow-lg mb-6">
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
              <div className="w-24 h-24 bg-[#ff4f14] text-white rounded-full border-[6px] border-[#ffece6] flex items-center justify-center shadow-lg mb-6">
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
              <div className="w-24 h-24 bg-white rounded-full border-[6px] border-[#f8f9f8] flex items-center justify-center shadow-lg mb-6">
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
              <div className="w-24 h-24 bg-white rounded-full border-[6px] border-[#f8f9f8] flex items-center justify-center shadow-lg mb-6">
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
      <section className="bg-[#ff4f14] py-16 px-6 lg:px-20 text-white overflow-hidden relative">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between relative z-10">
          <Reveal direction="left" delay={0.2}>
          <div className="max-w-2xl mb-8 md:mb-0">
            <div className="inline-flex items-center gap-2 bg-white/20 rounded-full px-4 py-2 mb-6">
              <Siren size={20} />
              <span className="font-semibold tracking-wide">TƏCİLİ</span>
            </div>
            <h2 className="text-4xl md:text-5xl font-bold mb-4">
              Təcili Generator və ya Elektrik Servisi Lazımdır?
            </h2>
            <div className="flex items-center gap-3 text-xl text-white/90 mb-8">
              <Clock size={24} />
              <span>7/24 Operativ Texniki Dəstək Xidməti</span>
            </div>
            <button className="bg-white text-[#ff4f14] px-8 py-4 rounded-full font-bold text-lg inline-flex items-center gap-2 hover:bg-gray-100 transition-colors">
              ZƏNG ET
              <ArrowRight size={20} />
            </button>
          </div>
          </Reveal>
          
          <Reveal direction="right" delay={0.4}>
          <div className="relative w-72 h-72 hidden md:block">
            <div className="absolute inset-0 bg-white/10 rounded-full scale-110"></div>
            <img 
              src="https://images.unsplash.com/photo-1574739782594-db4ead022697?q=80&w=600&auto=format&fit=crop" 
              alt="Emergency Plumber" 
              className="w-full h-full object-cover rounded-full border-8 border-[#ff4f14]"
            />
          </div>
          </Reveal>
        </div>
      </section>

      {/* Partnyorlarımız Section */}
      <section className="py-24 px-6 lg:px-20 bg-white">
        <div className="max-w-7xl mx-auto">
          <Reveal direction="up" delay={0.1}>
          <div className="mb-16 max-w-2xl">
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Partnyorlarımız</p>
            <h2 className="text-5xl font-bold mb-6 text-[#131312]">
              Bizə Güvənən <span className="text-[#ff4f14]">Şirkətlər</span>
            </h2>
            <p className="text-lg text-gray-600 leading-relaxed">
              Azərbaycanda və regionda bir çox tanınmış şirkətlərlə rəsmi əməkdaşlıq edirik.
            </p>
          </div>
          </Reveal>
          
          <div className="grid md:grid-cols-3 gap-6">
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="rounded-3xl overflow-hidden h-80 group relative">
              <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?q=80&w=800&auto=format&fit=crop" alt="Project 1" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
            </div>
            </Reveal>
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="rounded-3xl overflow-hidden h-80 group relative">
              <img src="https://images.unsplash.com/photo-1620626011761-996317b8d101?q=80&w=800&auto=format&fit=crop" alt="Project 2" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
            </div>
            </Reveal>
            <Reveal direction="up" delay={0.2} className="h-full">
            <div className="rounded-3xl overflow-hidden h-80 group relative">
              <img src="https://images.unsplash.com/photo-1607472586893-edb57cb5b3b1?q=80&w=800&auto=format&fit=crop" alt="Project 3" className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
            </div>
            </Reveal>
          </div>
        </div>
      </section>

    </div>
  );
}
