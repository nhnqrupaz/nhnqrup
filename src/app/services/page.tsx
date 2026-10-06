'use client';
import Reveal from "@/components/Reveal";
import { ArrowRight, CheckCircle2 } from "lucide-react";

export default function ServicesPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Xidmətlərimiz</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Sizin Üçün <span className="text-[#ff4f14]">Peşəkar Həllər</span>
          </h1>
          <p className="text-lg text-gray-600">
            Həm mütəxəssis yetişdirmək, həm də mürəkkəb mühəndislik problemlərini həll etmək üçün buradayıq.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-7xl mx-auto w-full flex flex-col gap-12">
        {/* Service 1 */}
        <Reveal direction="up" delay={0.2}>
          <div className="bg-white rounded-[2rem] overflow-hidden shadow-sm flex flex-col lg:flex-row group border border-gray-100">
            <div className="lg:w-1/2 h-80 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1581092160562-40aa08e78837?q=80&w=1000&auto=format&fit=crop" alt="Kurslar" className="w-full h-full object-cover" />
            </div>
            <div className="lg:w-1/2 p-8 md:p-12 flex flex-col justify-center">
              <h3 className="text-3xl font-bold mb-4">Təlimlər və Kurslar</h3>
              <p className="text-gray-600 mb-8 text-lg">5 müxtəlif istiqamətdə peşəkar mühəndislik dərsləri.</p>
              <ul className="space-y-4 mb-8">
                <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff4f14]" /> <span>Peşəkar təlimçilər və real avadanlıqlar</span></li>
                <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff4f14]" /> <span>Sonda rəsmi sertifikat</span></li>
                <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff4f14]" /> <span>Uyğun iş yerlərinə yönləndirmə</span></li>
              </ul>
              <button className="bg-[#131312] text-white px-8 py-4 rounded-full font-bold w-fit hover:bg-[#ff4f14] transition-colors flex items-center gap-2">
                Kurslara Bax <ArrowRight size={20} />
              </button>
            </div>
          </div>
        </Reveal>

        {/* Service 2 */}
        <Reveal direction="up" delay={0.3}>
          <div className="bg-white rounded-[2rem] overflow-hidden shadow-sm flex flex-col lg:flex-row-reverse group border border-gray-100">
            <div className="lg:w-1/2 h-80 lg:h-auto relative">
              <img src="https://images.unsplash.com/photo-1621905252507-b35492cc74b4?q=80&w=1000&auto=format&fit=crop" alt="Servis" className="w-full h-full object-cover" />
            </div>
            <div className="lg:w-1/2 p-8 md:p-12 flex flex-col justify-center">
              <h3 className="text-3xl font-bold mb-4">Generator və Elektrik Servisi</h3>
              <p className="text-gray-600 mb-8 text-lg">Müəssisəniz və ya eviniz üçün 24/7 operativ texniki baxış.</p>
              <ul className="space-y-4 mb-8">
                <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff4f14]" /> <span>Planlı texniki baxış və profilaktika</span></li>
                <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff4f14]" /> <span>Nasazlıqların diaqnostikası və təmir</span></li>
                <li className="flex items-center gap-3"><CheckCircle2 className="text-[#ff4f14]" /> <span>Təcili yerində operativ servis</span></li>
              </ul>
              <button className="bg-[#131312] text-white px-8 py-4 rounded-full font-bold w-fit hover:bg-[#ff4f14] transition-colors flex items-center gap-2">
                Müraciət Et <ArrowRight size={20} />
              </button>
            </div>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
