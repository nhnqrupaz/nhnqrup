import Link from "next/link";
import Reveal from "@/components/Reveal";
import { ArrowRight, Briefcase, MapPin, DollarSign } from "lucide-react";
import { supabase } from "@/lib/supabase";

const fallbackVacancies = [
  {
    title: "Elektrik köməkçisi",
    salary: "800 ₼",
    type: "Tam iş günü",
    location: "Bakı, Azərbaycan",
    desc: "Elektrik montaj işlərində usta köməkçisi tələb olunur.",
    reqs: ["Sahə üzrə ilkin biliklər", "Fiziki sağlamlıq", "Kollektivdə işləmək bacarığı"]
  }
];

export default async function VacanciesPage() {
  const { data } = await supabase.from('vacancies').select('*').order('created_at', { ascending: false });
  const vacancies = data && data.length > 0 ? data : fallbackVacancies;

  return (
    <div className="flex flex-col min-h-screen bg-[#f8f9f8] pt-32 pb-24">
      <section className="px-6 lg:px-20 mb-16 text-center max-w-4xl mx-auto">
        <Reveal direction="up" delay={0.1}>
          <p className="text-[#ff4f14] font-semibold tracking-wider uppercase mb-4">Karyera İmkanları</p>
          <h1 className="text-5xl md:text-6xl font-bold tracking-tight text-[#131312] mb-6">
            Açıq <span className="text-[#ff4f14]">Vakansiyalar</span>
          </h1>
          <p className="text-lg text-gray-600">
            Peşəkar komandamıza qoşulun və inkişaf edən şirkətimizdə karyeranızı qurun.
          </p>
        </Reveal>
      </section>

      <section className="px-6 lg:px-20 max-w-4xl mx-auto w-full space-y-6">
        {vacancies.map((job: any, idx: number) => (
          <Reveal key={idx} direction="up" delay={0.2 + (idx * 0.1)}>
            <div className="bg-white rounded-3xl p-8 shadow-sm hover:shadow-lg transition-shadow border border-gray-100 flex flex-col md:flex-row gap-8 justify-between">
              <div className="flex-1">
                <div className="flex flex-wrap items-center gap-3 mb-4">
                  <span className="bg-[#ffece6] text-[#ff4f14] px-4 py-1.5 rounded-full text-sm font-bold">
                    {job.type || 'Tam iş günü'}
                  </span>
                  <span className="flex items-center gap-1 text-gray-500 text-sm font-medium">
                    <MapPin size={16} /> {job.location || 'Bakı'}
                  </span>
                  <span className="flex items-center gap-1 text-gray-500 text-sm font-medium">
                    <DollarSign size={16} /> {job.salary}
                  </span>
                </div>
                
                <h3 className="text-2xl font-bold mb-3 text-[#131312]">{job.title}</h3>
                <p className="text-gray-600 mb-6">{job.description || job.desc}</p>
                
                {(job.requirements || job.reqs) && (
                  <div className="mb-6">
                    <h4 className="font-bold text-gray-900 mb-3 flex items-center gap-2">
                      <Briefcase size={18} className="text-[#ff4f14]" /> Tələblər:
                    </h4>
                    <ul className="space-y-2">
                      {String(job.requirements || job.reqs).split(',').map((req: string, i: number) => (
                        <li key={i} className="flex items-start gap-2 text-gray-600">
                          <span className="text-[#ff4f14] mt-1">•</span>
                          <span>{req.trim()}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
              
              <div className="flex items-center md:items-end justify-center">
                <Link href={`/cv?job=${encodeURIComponent(job.title)}`} className="w-full md:w-auto bg-[#ff4f14] text-white px-8 py-4 rounded-xl font-bold hover:bg-[#e64612] transition-colors flex items-center justify-center gap-2">
                  CV Göndər
                  <ArrowRight size={20} />
                </Link>
              </div>
            </div>
          </Reveal>
        ))}
      </section>
    </div>
  );
}
