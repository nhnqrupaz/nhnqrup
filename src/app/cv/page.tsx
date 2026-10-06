'use client';
import Reveal from "@/components/Reveal";
import { Upload } from "lucide-react";
import { useSearchParams } from "next/navigation";
import { Suspense, useState } from "react";

function CVForm() {
  const searchParams = useSearchParams();
  const initialJob = searchParams.get('job') || '';
  const [job, setJob] = useState(initialJob);
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Construct the email body
    const subject = encodeURIComponent(`Yeni Müraciət: ${job}`);
    const body = encodeURIComponent(
      `Ad və Soyad: ${name}\n` +
      `Telefon: ${phone}\n` +
      `E-poçt: ${email}\n` +
      `Müraciət edilən sahə: ${job}\n\n` +
      `Zəhmət olmasa CV faylınızı bu e-poçta əlavə edərək göndərin.`
    );
    
    // Open email client
    window.location.href = `mailto:info@nhnqrup.az?subject=${subject}&body=${body}`;
  };

  return (
    <form className="space-y-6" onSubmit={handleSubmit}>
      <div className="grid md:grid-cols-2 gap-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Ad və Soyad</label>
          <input required type="text" value={name} onChange={e => setName(e.target.value)} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="Adınızı daxil edin" />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Telefon</label>
          <input required type="text" value={phone} onChange={e => setPhone(e.target.value)} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="+994 -- --- -- --" />
        </div>
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">E-poçt (istəyə bağlı)</label>
        <input type="email" value={email} onChange={e => setEmail(e.target.value)} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="E-poçt ünvanınız" />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Müraciət etdiyiniz sahə</label>
        <select required value={job} onChange={e => setJob(e.target.value)} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]">
          <option value="">-- Seçin --</option>
          <optgroup label="Vakansiyalar">
            <option value="Elektrik">Elektrik</option>
            <option value="Elektrik köməkçisi">Elektrik köməkçisi</option>
            <option value="Elektromexanik">Elektromexanik</option>
          </optgroup>
          <optgroup label="Kurslar">
            <option value="Elektrik Kursu">Elektrik Kursu</option>
            <option value="Ağıllı Ev (Smart Home)">Ağıllı Ev (Smart Home)</option>
            <option value="Zəif Axın Sistemləri">Zəif Axın Sistemləri</option>
            <option value="PLC Proqramlaşdırma">PLC Proqramlaşdırma</option>
          </optgroup>
          <optgroup label="Digər">
            <option value="Digər">Digər</option>
          </optgroup>
        </select>
      </div>

      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">CV Yüklə (Məcburidir)</label>
        <div className="border-2 border-dashed border-gray-300 rounded-xl p-8 flex flex-col items-center justify-center bg-gray-50 hover:bg-gray-100 transition-colors cursor-pointer group relative">
          <input type="file" className="absolute inset-0 w-full h-full opacity-0 cursor-pointer" title="Fayl seçin" />
          <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm mb-3 group-hover:scale-110 transition-transform">
            <Upload size={20} className="text-[#ff4f14]" />
          </div>
          <span className="text-gray-500 font-medium text-center px-4">CV faylınızı bura yükləyin<br/><span className="text-sm">(Sistem email ünvanına göndərməyi tələb edəcək)</span></span>
        </div>
      </div>
      
      <button type="submit" className="w-full bg-[#131312] text-white py-4 rounded-xl font-bold hover:bg-[#ff4f14] transition-colors">
        Müraciəti Tamamla
      </button>
    </form>
  );
}

export default function CVPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Müraciət</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Bizə <span className="text-[#ff4f14]">Müraciət Edin</span>
          </h1>
          <p className="text-lg text-gray-600">
            NHN QRUP komandasına qoşulmaq və ya peşəkar kurslarımıza qeydiyyatdan keçmək üçün formu doldurun. Form göndərildikdə sistem məlumatlarınızı birbaşa info@nhnqrup.az ünvanına e-poçt olaraq hazırlayacaq.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-3xl mx-auto w-full">
        <Reveal direction="up" delay={0.2}>
          <div className="bg-white p-8 md:p-12 rounded-[2rem] shadow-sm border border-gray-100">
            <Suspense fallback={<p className="text-center text-gray-500">Yüklənir...</p>}>
              <CVForm />
            </Suspense>
          </div>
        </Reveal>
      </section>
    </div>
  );
}
