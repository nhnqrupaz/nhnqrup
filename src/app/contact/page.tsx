'use client';
import Reveal from "@/components/Reveal";
import { Phone, Mail, MapPin } from "lucide-react";

export default function ContactPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Əlaqə</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Bizimlə <span className="text-[#ff4f14]">Əlaqə Saxlayın</span>
          </h1>
          <p className="text-lg text-gray-600">
            Kurslara yazılmaq, xidmətlərimizdən faydalanmaq və ya hər hansı sualınız üçün bizə yaza və ya zəng edə bilərsiniz.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-5xl mx-auto w-full">
        <div className="grid md:grid-cols-3 gap-6 mb-12">
          <Reveal direction="up" delay={0.2}>
            <div className="bg-white p-8 rounded-3xl text-center flex flex-col items-center shadow-sm h-full border border-gray-100">
              <div className="w-16 h-16 bg-[#fff0ec] text-[#ff4f14] rounded-full flex items-center justify-center mb-4">
                <Phone size={28} />
              </div>
              <h3 className="font-bold text-lg mb-2">Telefon</h3>
              <a href="https://wa.me/994773334466" target="_blank" rel="noopener noreferrer" className="text-gray-600 hover:text-[#ff4f14] transition-colors font-medium">+994 77 333 44 66</a>
            </div>
          </Reveal>
          <Reveal direction="up" delay={0.3}>
            <div className="bg-white p-8 rounded-3xl text-center flex flex-col items-center shadow-sm h-full border border-gray-100">
              <div className="w-16 h-16 bg-[#fff0ec] text-[#ff4f14] rounded-full flex items-center justify-center mb-4">
                <Mail size={28} />
              </div>
              <h3 className="font-bold text-lg mb-2">E-poçt</h3>
              <a href="mailto:info@nhnqrup.az" className="text-gray-600 hover:text-[#ff4f14] transition-colors font-medium">info@nhnqrup.az</a>
            </div>
          </Reveal>
          <Reveal direction="up" delay={0.4}>
            <div className="bg-white p-8 rounded-3xl text-center flex flex-col items-center shadow-sm h-full border border-gray-100">
              <div className="w-16 h-16 bg-[#fff0ec] text-[#ff4f14] rounded-full flex items-center justify-center mb-4">
                <MapPin size={28} />
              </div>
              <h3 className="font-bold text-lg mb-2">Ünvan</h3>
              <p className="text-gray-600">Nizami küçəsi 94</p>
            </div>
          </Reveal>
        </div>

        <Reveal direction="up" delay={0.5}>
          <div className="bg-white p-8 md:p-12 rounded-[2rem] shadow-sm border border-gray-100 max-w-3xl mx-auto">
            <h3 className="text-2xl font-bold mb-6 text-center">Bizə Yazın</h3>
            <form className="space-y-6">
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Ad və Soyad</label>
                  <input type="text" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="Adınızı daxil edin" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">Telefon</label>
                  <input type="text" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="+994 -- --- -- --" />
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Maraqlandığınız sahə</label>
                <select className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]">
                  <option>Kurslara yazılmaq</option>
                  <option>Servis xidməti sifariş etmək</option>
                  <option>Digər</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Mesajınız</label>
                <textarea rows={4} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="Bizə nə demək istəyirsiniz?"></textarea>
              </div>
              <button type="button" className="w-full bg-[#ff4f14] text-white py-4 rounded-xl font-bold hover:bg-[#e64612] transition-colors">
                Göndər
              </button>
            </form>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
