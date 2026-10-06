'use client';
import Reveal from "@/components/Reveal";

const partners = [
  "Elsmart", "KATV1", "Məlumat Mərkəzi", "Rahat Telekom", "Qoç Ət", 
  "Azərişıq", "Santral", "NHN QRUP", "Generator Servis", "Azərenerji", 
  "Additional Business Company", "Socar", "Khanbutagroup", "Sea Breeze"
];

export default function AboutPage() {
  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-12">
        <div className="md:w-1/2">
          <Reveal direction="up" delay={0.1}>
            <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Haqqımızda</p>
            <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
              Bizimlə <span className="text-[#ff4f14]">Gələcəyə Addım Atın</span>
            </h1>
            <p className="text-lg text-gray-600 mb-6 leading-relaxed">
              NHN QRUP (Service and Training) olaraq məqsədimiz mühəndislik sahəsində həm yüksək keyfiyyətli servis göstərmək, həm də gələcəyin peşəkarlarını yetişdirməkdir.
            </p>
            <p className="text-lg text-gray-600 leading-relaxed">
              <strong>Əsas fəaliyyət istiqamətlərimiz:</strong> Elektrik mühəndisliyi, Zəif axın sistemləri, PLC və SCADA, həmçinin Ağıllı Ev (Smart Home) sistemlərinin quraşdırılması və tədrisidir.
            </p>
          </Reveal>
        </div>
        <div className="md:w-1/2">
          <Reveal direction="left" delay={0.3}>
            <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=800&auto=format&fit=crop" alt="Haqqımızda" className="rounded-[2rem] w-full h-96 object-cover shadow-lg" />
          </Reveal>
        </div>
      </section>

      <section className="px-6 lg:px-20 mt-20 max-w-7xl mx-auto">
        <Reveal direction="up" delay={0.2}>
          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold">Bizə Güvənən Partnyorlarımız</h2>
          </div>
          <div className="flex flex-wrap justify-center gap-4">
            {partners.map((partner, idx) => (
              <div key={idx} className="bg-white px-6 py-3 rounded-full shadow-sm font-medium text-gray-700 border border-gray-100 hover:border-[#ff4f14] hover:text-[#ff4f14] transition-colors cursor-default">
                {partner}
              </div>
            ))}
          </div>
        </Reveal>
      </section>
    </div>
  );
}
