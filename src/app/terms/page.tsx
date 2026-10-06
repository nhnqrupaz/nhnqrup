'use client';
import Reveal from "@/components/Reveal";

export default function TermsPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24 px-6 lg:px-20">
      <div className="max-w-4xl mx-auto bg-white rounded-3xl p-8 md:p-16 shadow-sm border border-gray-100">
        <Reveal direction="up" delay={0.1}>
          <h1 className="text-4xl md:text-5xl font-bold mb-8 text-[#131312]">
            İstifadə <span className="text-[#ff4f14]">Qaydaları</span>
          </h1>
          <div className="space-y-6 text-gray-700 leading-relaxed">
            <p>Zəhmət olmasa, <strong>https://nhnqrup.az/</strong> veb-saytından istifadə etməzdən əvvəl bu İstifadə Qaydalarını diqqətlə oxuyun. Sayta daxil olmaqla və xidmətlərimizdən istifadə etməklə bu qaydalarla tam razılaşmış olursunuz.</p>
            
            <h2 className="text-2xl font-bold text-[#131312] mt-8">1. Xidmətlərin Mahiyyəti</h2>
            <p>NHN QRUP müştərilərinə həm peşəkar mühəndislik (Elektrik, Generator, Ağıllı Ev və s.) servisi, həm də qeyd olunan sahələr üzrə tədris (kurslar) xidməti təklif edir. Saytda yer alan məlumatlar, qiymətlər və kurs detalları şirkətin qərarı ilə xəbərdarlıq edilmədən dəyişdirilə bilər.</p>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">2. Qeydiyyat və Müraciət</h2>
            <p>Kurslara, vakansiyalara və ya xidmətlərə müraciət edərkən verdiyiniz məlumatların doğruluğuna tam cavabdehsiniz. Yanlış məlumat verilməsi müraciətin ləğv olunmasına səbəb ola bilər.</p>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">3. Əqli Mülkiyyət</h2>
            <p>Saytda yerləşdirilmiş bütün dizayn, mətnlər, qrafiklər və logolar NHN QRUP şirkətinə və ya lisenziya sahibinə (KhanButaGroup) məxsusdur. Bunların hər hansı bir formada iznsiz kopyalanması və ya istifadəsi qadağandır.</p>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">4. Sertifikatlaşdırma</h2>
            <p>Kursları bitirən tələbələrə verilən sertifikatlar NHN QRUP daxili qiymətləndirməsinə əsaslanır. Sertifikatın alınması üçün dərslərdə iştirak və yekun imtahandan keçmək mütləqdir.</p>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">5. Dəyişikliklər</h2>
            <p>NHN QRUP bu istifadə qaydalarına istənilən vaxt dəyişiklik etmək hüququnu özündə saxlayır. Dəyişikliklər saytda yayımlandığı andan etibarən qüvvəyə minir.</p>

            <p className="mt-8 text-sm text-gray-500">Son yenilənmə tarixi: 2024-cü il.</p>
          </div>
        </Reveal>
      </div>
    </div>
  );
}
