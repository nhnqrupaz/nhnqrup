'use client';
import Reveal from "@/components/Reveal";

export default function PrivacyPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24 px-6 lg:px-20">
      <div className="max-w-4xl mx-auto bg-white rounded-3xl p-8 md:p-16 shadow-sm border border-gray-100">
        <Reveal direction="up" delay={0.1}>
          <h1 className="text-4xl md:text-5xl font-bold mb-8 text-[#131312]">
            Məxfilik <span className="text-[#ff4f14]">Siyasəti</span>
          </h1>
          <div className="space-y-6 text-gray-700 leading-relaxed">
            <p><strong>NHN QRUP ("Biz", "Şirkət")</strong> müştərilərinin, tələbələrinin və sayt ziyarətçilərinin fərdi məlumatlarının qorunmasına böyük əhəmiyyət verir. Bu Məxfilik Siyasəti, https://nhnqrup.az/ saytından istifadə zamanı şəxsi məlumatlarınızın necə toplandığını, istifadə olunduğunu və qorunduğunu izah edir.</p>
            
            <h2 className="text-2xl font-bold text-[#131312] mt-8">1. Hansı məlumatları toplayırıq?</h2>
            <p>Kurslara və ya xidmətlərə müraciət edərkən (Əlaqə və ya CV Göndər formu vasitəsilə) adınız, soyadınız, telefon nömrəniz, e-poçt ünvanınız və bizə təqdim etdiyiniz CV sənədləri sistemimizdə toplanır. Abunəlik formu vasitəsilə isə sadəcə e-poçt ünvanınız toplanır.</p>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">2. Məlumatlardan necə istifadə edirik?</h2>
            <ul className="list-disc pl-5 space-y-2">
              <li>Sizə müvafiq xidmət və kurslar haqqında məlumat vermək üçün.</li>
              <li>Müraciətlərinizi və CV-lərinizi dəyərləndirmək və sizinlə əlaqə saxlamaq üçün.</li>
              <li>Saytımızın fəaliyyətini və xidmət keyfiyyətimizi artırmaq üçün.</li>
              <li>Yeni kurslar, kampaniyalar və yeniliklər barədə sizə (abunə olmusunuzsa) məlumat göndərmək üçün.</li>
            </ul>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">3. Məlumatların Qorunması və Paylaşılması</h2>
            <p>Şəxsi məlumatlarınız üçüncü tərəflərə satılmır və ya icarəyə verilmir. Məlumatlarınız qanunla tələb olunmayan hallar istisna olmaqla, mütləq şəkildə konfidensial saxlanılır və yalnız NHN QRUP komandası tərəfindən müvafiq məqsədlər üçün istifadə olunur.</p>

            <h2 className="text-2xl font-bold text-[#131312] mt-8">4. Əlaqə</h2>
            <p>Məxfilik siyasəti ilə bağlı suallarınız olarsa, bizimlə aşağıdakı vasitələrlə əlaqə saxlaya bilərsiniz:</p>
            <ul className="list-disc pl-5 space-y-2 mt-4 font-medium">
              <li>E-poçt: info@nhnqrup.az</li>
              <li>Telefon: +994 77 333 44 66</li>
              <li>Ünvan: Nizami küçəsi 94</li>
            </ul>
            <p className="mt-8 text-sm text-gray-500">Son yenilənmə tarixi: 2024-cü il.</p>
          </div>
        </Reveal>
      </div>
    </div>
  );
}
