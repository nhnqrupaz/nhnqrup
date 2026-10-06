'use client';
import Reveal from "@/components/Reveal";
import { Upload } from "lucide-react";

export default function CVPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Müraciət</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            CV <span className="text-[#ff4f14]">Göndər</span>
          </h1>
          <p className="text-lg text-gray-600">
            NHN QRUP komandasına qoşulmaq üçün öz CV-nizi bizə göndərin. Uyğun vakansiya yarandıqda sizinlə əlaqə saxlayacağıq.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-3xl mx-auto w-full">
        <Reveal direction="up" delay={0.2}>
          <div className="bg-white p-8 md:p-12 rounded-[2rem] shadow-sm border border-gray-100">
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
                <label className="block text-sm font-medium text-gray-700 mb-2">E-poçt (istəyə bağlı)</label>
                <input type="email" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="E-poçt ünvanınız" />
              </div>
              
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Müraciət etdiyiniz vəzifə</label>
                <select className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]">
                  <option>Elektrik</option>
                  <option>Elektrik köməkçisi</option>
                  <option>Elektromexanik</option>
                  <option>Digər</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">CV Yüklə (PDF, DOCX)</label>
                <div className="border-2 border-dashed border-gray-300 rounded-xl p-8 flex flex-col items-center justify-center bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer group">
                  <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm mb-3 group-hover:scale-110 transition-transform">
                    <Upload size={20} className="text-[#ff4f14]" />
                  </div>
                  <span className="text-gray-500 font-medium">Faylı seçmək üçün bura vurun</span>
                </div>
              </div>
              
              <button type="button" className="w-full bg-[#131312] text-white py-4 rounded-xl font-bold hover:bg-[#ff4f14] transition-colors">
                Müraciəti Tamamla
              </button>
            </form>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
