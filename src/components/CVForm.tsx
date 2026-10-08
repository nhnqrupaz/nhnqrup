'use client';

import { Upload } from "lucide-react";
import { useSearchParams } from "next/navigation";
import { useState, useEffect } from "react";

export default function CVForm({ 
  courses = [], 
  vacancies = [] 
}: { 
  courses: any[], 
  vacancies: any[] 
}) {
  const searchParams = useSearchParams();
  const initialJob = searchParams.get('job') || '';
  const [job, setJob] = useState(initialJob);
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [email, setEmail] = useState('');

  // Auto-set the job if it changes in URL
  useEffect(() => {
    if (initialJob && !job) {
      setJob(initialJob);
    }
  }, [initialJob]);

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
          {vacancies.length > 0 && (
            <optgroup label="Vakansiyalar">
              {vacancies.map((v: any) => (
                <option key={v.id} value={v.title}>{v.title}</option>
              ))}
            </optgroup>
          )}
          {courses.length > 0 && (
            <optgroup label="Kurslar">
              {courses.map((c: any) => (
                <option key={c.id} value={c.title}>{c.title}</option>
              ))}
            </optgroup>
          )}
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
