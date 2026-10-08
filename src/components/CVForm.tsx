'use client';

import { Upload, CheckCircle2 } from "lucide-react";
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
  const success = searchParams.get('success');
  const [job, setJob] = useState(initialJob);
  const [fileName, setFileName] = useState('');

  // Auto-set the job if it changes in URL
  useEffect(() => {
    if (initialJob && !job) {
      setJob(initialJob);
    }
  }, [initialJob]);

  if (success) {
    return (
      <div className="text-center py-12">
        <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <CheckCircle2 size={40} className="text-green-600" />
        </div>
        <h2 className="text-3xl font-bold mb-4">Müraciətiniz Uğurla Göndərildi!</h2>
        <p className="text-gray-600 mb-8">Tezliklə sizinlə əlaqə saxlayacağıq. İnamınız üçün təşəkkürlər.</p>
        <button onClick={() => window.location.href='/cv'} className="bg-[#131312] text-white px-8 py-3 rounded-xl font-bold hover:bg-[#ff4f14] transition-colors">
          Yeni Müraciət Et
        </button>
      </div>
    );
  }

  return (
    <form 
      className="space-y-6" 
      action="https://formsubmit.co/info@nhnqrup.az" 
      method="POST" 
      encType="multipart/form-data"
    >
      {/* FormSubmit Configuration */}
      <input type="hidden" name="_subject" value={job ? `Yeni Müraciət: ${job}` : "Yeni CV Müraciəti (Saytdan)"} />
      <input type="hidden" name="_captcha" value="false" />
      <input type="hidden" name="_template" value="table" />
      {/* We assume the site is deployed to https://www.nhnqrup.az. We use dynamic origin if possible, but formsubmit requires absolute URL. */}
      <input type="hidden" name="_next" value="https://nhnqrup.az/cv?success=true" />

      <div className="grid md:grid-cols-2 gap-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Ad və Soyad</label>
          <input required type="text" name="Ad_Soyad" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="Adınızı daxil edin" />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Telefon</label>
          <input required type="text" name="Telefon" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="+994 -- --- -- --" />
        </div>
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">E-poçt (istəyə bağlı)</label>
        <input type="email" name="Email" className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]" placeholder="E-poçt ünvanınız" />
      </div>
      
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">Müraciət etdiyiniz sahə</label>
        <select required name="Secilen_Vezife_ve_ya_Kurs" value={job} onChange={e => setJob(e.target.value)} className="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 focus:outline-none focus:border-[#ff4f14]">
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
          <input 
            required 
            type="file" 
            name="attachment" 
            accept=".pdf,.doc,.docx"
            className="absolute inset-0 w-full h-full opacity-0 cursor-pointer" 
            title="Fayl seçin" 
            onChange={(e) => setFileName(e.target.files?.[0]?.name || '')}
          />
          <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center shadow-sm mb-3 group-hover:scale-110 transition-transform">
            <Upload size={20} className={fileName ? "text-green-500" : "text-[#ff4f14]"} />
          </div>
          <span className="text-gray-700 font-medium text-center px-4">
            {fileName ? (
              <span className="text-green-600 font-bold">Fayl Seçildi: {fileName}</span>
            ) : (
              "CV faylınızı (PDF, DOC) bura yükləyin"
            )}
          </span>
        </div>
      </div>
      
      <button type="submit" className="w-full bg-[#131312] text-white py-4 rounded-xl font-bold hover:bg-[#ff4f14] transition-colors">
        Müraciəti Göndər
      </button>
      
      
    </form>
  );
}
